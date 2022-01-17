---
title: "CosmosDB: A Stored Procedure to merge documents on read"
date: "2020-04-28"
#T08:14:45-04:00" #
description: "An example of an Azure cosmosDB stored Procedure to retrieve multiple documents and return a merged payload."
draft: false # Sets whether to render this page. Draft of true will not be rendered.
toc: true # Controls if a table of contents should be generated for first-level links automatically.
featureImage: "/post/cosmosdb-stored-procedure/cosmosdb.png" # Sets featured image on blog post.
thumbnail: "/post/cosmosdb-stored-procedure/cosmosdb.png" # Sets thumbnail image appearing inside card on homepage.
shareImage: "/post/cosmosdb-stored-procedure/cosmosdb.png" # Designate a separate image for social media sharing.
codeMaxLines: 10 # Override global value for how many lines within a code block before auto-collapsing.
codeLineNumbers: true # Override global value for showing of line numbers within code block.
summary: The CosmosDB SQL API is very flexible in returning objects and view projections, but it cannot merge documents via its SQL dialect.
categories:
- Azure
tags:
- CosmosDB
markup:
  tableOfContents:
    endLevel: 3
    ordered: true
    startLevel: 2
---

## Why stored procedures?

The Cosmos SQL is very flexible in returning objects and view projections, but it cannot merge documents via its SQL dialect.

   {{< callout title="Note:" note="This could be done with a User Defined Function (UDF) as well." >}}

## Use Case

Imagine we have documents in a collection that need to be 'joined'. In a simple case, we may have a template that is a master record and a user-level record with more details. We need a query that will load both objects and then merge them into one combined document.

## The Code

We will build on the [previous](../hello-sproc/) but add some simple assertion testing.

To set up our test, we will need 2 new functions, one to add a document and one to remove it.

```js
async function createDoc(doc) {
  const result = await container.items.create(doc);
  return result.resource;
}

async function deleteDoc(doc) {
  await container.item(doc.id, doc.user_id).delete();
}
```

and for a fixture, let us generate a simplistic guid for an id

```js
function guid() {
  return ([1e7] + -1e3 + -4e3 + -8e3 + -1e11).replace(/[018]/g, (a) =>
    (a ^ ((Math.random() * 16) >> (a / 4))).toString(16)
  );
}
```

and a little generator

```js
function getFixtures(guid) {
  return {
    template:{
      id: "template-" + guid,
      coupon_name: "sproc_testing",
      master_details: "I am the template",
      detail: "master detail"
    },
    userDoc: {
      id: "user-" + guid,
      user_id: "test-user",
      coupon_name: "sproc_testing",
      user_details: "I am the child",
      detail: "child detail"
    },
    expected: {
      user_id: "test-user",
      coupon_name: "sproc_testing",
      master_details: "I am the template",
      user_details: "I am the child",
      detail: "child detail"
    }
  }
}
```

And then modify our primary function to result in a failing test that you can run over and over as we develop our merge sproc.
This will fail because we have not uploaded the sproc to Azure yet.

```js
async function run() {
  console.log("\n*****\n* Starting test case\n")
  const sproc = mergeSproc
  await createOrUpdateSproc(sproc)

  // begin test
  const id = 'test' //guid()
  const fixtures = getFixtures(id)

  await createDoc(fixtures.template)
  await createDoc(fixtures.userDoc)

  //user_id is the partition key for this particular collection
  const partitionKey = fixtures.userDoc.user_id
  const res = await runSproc(sproc.id, partitionKey, id)

  await deleteDoc(fixtures.template)
  await deleteDoc(fixtures.userDoc)

  assert.strictEqual(res.detail, fixtures.expected.detail, "detail does not match")
  assert.strictEqual(res.master_details, fixtures.expected.master_details, "master details don't match")
  console.log("\n*Assertions passed")
  return res
}

run().then(console.log).catch(console.error)
```

All you need now is the stored procedure to do the merge.

```js
const mergeSproc = {
    id: "mergeSproc_001",
    body: function (guid) {
      var collection = getContext().getCollection()
      console.log("Sproc called with " + guid)
      var filterQuery = 
      {     
          'query' :  'SELECT * FROM root r where r.id = @id1 or r.id = @id2',
          'parameters' : [{'name':'@id1', 'value':'template-' + guid},
                          {'name':'@id2', 'value':'user-' + guid}]
      }
      var isAccepted = collection.queryDocuments(
          collection.getSelfLink(), 
          filterQuery,
          {}, 
          function (err, feed, options) { if (err) throw err
            if (!feed || !feed.length) {
              var response = getContext().getResponse()
              response.setBody('no docs found....!.')
            }
            else {
              // Do the merge!
              var body = {merged: "yes"}
              var response = getContext().getResponse()
              response.setBody(body)
          }
      })
      if (!isAccepted) throw new Error('The query was not accepted by the server.')
  }
}
```

let us break this down:
### SQL injection is bad, so lets use parameter substituions:

```js
  var filterQuery = 
  {     
      'query' :  'SELECT * FROM root r where r.id = @id1 or r.id = @id2',
      'parameters' : [{'name':'@id1', 'value':'template-' + guid},
                      {'name':'@id2', 'value':'user-' + guid}]
  }
```
This is not a model for proper NoSQL Schema, I wanted to keep the SQL simple, for now, to focus on the sproc and get a specific set of documents back.

This object complies with the well documented [SqlQuerySpec Interface](https://docs.microsoft.com/en-us/javascript/api/@azure/cosmos/sqlqueryspec?view=azure-node-latest) and will handle the proper formatting of strings vs numbers. The type of the 'value' is any JSONValue. `boolean | number | string | null | JSONArray | JSONObject`, but it doesn't always do the right thing for complex types.

### Start the async query
```js
      var collection = getContext().getCollection()
      var isAccepted = collection.queryDocuments(
          collection.getSelfLink(), 
          filterQuery,
          {}, 
          function (err, feed, options) { if (err) throw err
```
1. Get the current collection object from the content
2. Call queryDocuments, passing in the collection link, SQL, [feed options](http://azure.github.io/azure-cosmosdb-js-server/Collection.html#.FeedOptions) and a [callback](http://azure.github.io/azure-cosmosdb-js-server/Collection.html#.FeedCallback).
3. The queryDocuments will return False if the server rejects it. if you enter bad SQL it may also be accepted and then throw an error later.
4. throw errors result in proper HTTP codes being returned to the caller

Since you are already running in a partition, you don't need to reference the partition key in the filter query or request options.

:::tip pro tip
This seems to be similar to the [V1 DocumentDB Syntax](https://github.com/Azure/azure-cosmosdb-node#readme) but you should read the [current documentation](http://azure.github.io/azure-cosmosdb-js-server/Collection.html)
:::

### The callback
```js
          function (err, feed, responseOptions) { if (err) throw err
            if (!feed || !feed.length) {
              var response = getContext().getResponse()
              response.setBody('no docs found....!.')
            }
            else {
              // Do the merge!
              var body = {merged: "yes"}
              var response = getContext().getResponse()
              response.setBody(body)
          }
```
1. First check for an error and early return
2. feed will be the array of results from the queue
3. responseOptions will contain a continuation token if the query needs to be called again to gather more records
4. if you have no error, and you have records, so something interesting and set the body of the response appropriately.

### Finish the code

At this point you should have simple script that represents a failing test. It should be fast and you can iterate on until yet get the merge right.

You can extend the example to join records based on coupon_name by passing in just user_id.

## Completed Script

```js {linenos=table}
const assert = require('assert')

const { CosmosClient } = require('@azure/cosmos')

const endpoint = 'https://xxxxxxxxxxxxxx.documents.azure.com:443/'
const key = process.env.cosmos_key
const client = new CosmosClient({ endpoint, key });

const container = client.database('dbname').container('coupons')

const mergeSproc = {
    id: "mergeSproc_001",
    body: function (guid) {
      var collection = getContext().getCollection()
      console.log("Sproc called with " + guid)
      var filterQuery = 
      {     
          'query' :  'SELECT * FROM root r where r.id = @id1 or r.id = @id2',
          'parameters' : [{'name':'@id1', 'value':'template-' + guid},
                          {'name':'@id2', 'value':'user-' + guid}]
      }
      var isAccepted = collection.queryDocuments(
          collection.getSelfLink(), 
          filterQuery,
          {}, 
          function (err, feed, options) { if (err) throw err
            if (!feed || !feed.length) {
              var response = getContext().getResponse()
              response.setBody('no docs found....!.')
            }
            else {
              var master = {}
              var child = {}
              feed.forEach(doc => {
                if (doc.master_details) master = doc
                else child = doc
              })
              var body = Object.assign({}, master, child)
              var response = getContext().getResponse()
              response.setBody(body)
          }
      })
      if (!isAccepted) throw new Error('The query was not accepted by the server.')
  }
}

async function createDoc(doc) {
  const result = await container.items.create(doc);
  return result.resource;
}

async function deleteDoc(doc) {
  await container.item(doc.id, doc.user_id).delete();
}

function guid() {
  return ([1e7] + -1e3 + -4e3 + -8e3 + -1e11).replace(/[018]/g, (a) =>
    (a ^ ((Math.random() * 16) >> (a / 4))).toString(16)
  );
}

function getFixtures(guid) {
  return {
    template:{
      id: "template-" + guid,
      user_id: "test-user",
      coupon_name: "sproc_testing",
      master_details: "I am the template",
      detail: "master detail"
    },
    userDoc: {
      id: "user-" + guid,
      user_id: "test-user",
      coupon_name: "sproc_testing",
      user_details: "I am the child",
      detail: "child detail"
    },
    expected: {
      user_id: "test-user",
      coupon_name: "sproc_testing",
      master_details: "I am the template",
      user_details: "I am the child",
      detail: "child detail"
    }
  }
}
async function createOrUpdateSproc(sproc) {
  try {
    await container.scripts.storedProcedure(sproc.id).replace(sproc)
  } catch (e) {
    if (e.code === 404) {
      console.log('REPLACE failed, try to add ', sproc.id)
      await container.scripts.storedProcedures.create(sproc)
    } else {
      throw(e)
    }
  }
}

async function runSproc(sprocname, partition_id, args) {
    const result = await container
                            .scripts
                            .storedProcedure(sprocname)
                            .execute(partition_id, args, { enableScriptLogging: true })
    console.log("Sproc Log: ", decodeURIComponent(result.headers['x-ms-documentdb-script-log-results']))
    console.log("Sproc RU cost: ", result.headers['x-ms-request-charge'])
    return result.resource
}

async function run() {
  console.log("\n*****\n* Starting test case\n")
  const sproc = mergeSproc
  await createOrUpdateSproc(sproc)

  // setup test
  const id = guid()
  const fixtures = getFixtures(id)

  await createDoc(fixtures.template)
  await createDoc(fixtures.userDoc)

  // execute test
  // user_id is the partition key for this particular collection
  const partitionKey = fixtures.userDoc.user_id
  const res = await runSproc(sproc.id, partitionKey, id)

  // cleanup test
  await deleteDoc(fixtures.template)
  await deleteDoc(fixtures.userDoc)

  // assert satisfaction
  assert.strictEqual(res.detail, fixtures.expected.detail, "detail does not match")
  assert.strictEqual(res.master_details, fixtures.expected.master_details, "master details don't match")
  console.log("\n*Assertions passed")
  return res
}

run().then(console.log).catch(console.error)
```
