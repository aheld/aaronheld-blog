---
title: "Create a sproc to atomically update a document" # Title of the blog post.
date: 2020-05-12 #
description: "A example of a CosmosBD Stored procedures (sprocs) that will do an atomic update."
featured: true # Sets if post is a featured post, making appear on the home page side bar.
draft: false # Sets whether to render this page. Draft of true will not be rendered.
toc: true # Controls if a table of contents should be generated for first-level links automatically.
featureImage: "/post/cosmosdb-stored-procedure/cosmosdb.png" # Sets featured image on blog post.
thumbnail: "/post/cosmosdb-stored-procedure/cosmosdb.png" # Sets thumbnail image appearing inside card on homepage.
shareImage: "/post/cosmosdb-stored-procedure/cosmosdb.png" # Designate a separate image for social media sharing.
codeMaxLines: 10 # Override global value for how many lines within a code block before auto-collapsing.
codeLineNumbers: true # Override global value for showing of line numbers within code block.
figurePositionShow: true # Override global value for showing the figure label.
categories:
  - Azure
tags:
  - CosmosDB
---

## Why stored procedure?

The Cosmos SQL is very flexable, but the client cannot easily guarantee an atomic update.  It is possible to get a similar effect using the newer .Update method in the SDK along with a conditional header using the doc._etag.  But sometimes a stored procedure makes more sense. 

## Use Case

Imagine we have documents with a counter field and we want to incement it by one every time it is called.  If we download the document, add 1, then post it back we run the risk of missing an update.

## The Code

We will building on the [previous](../merge-sproc/) but start to use Promises to simplify the sproc code.


### Lets start with out test runner

```js
async function run() {
  console.log("\n*****\n* Starting test case\n")
  await createOrUpdateSproc(updateSproc)

  const fixtures = getFixtures(guid())

  //write a doc to cosmos for the sproc to edit  
  const doc = await createDoc(fixtures.userDoc)

  //user_id is the partition key for this particular collection
  const docId = doc.id
  const partitionKey = doc.user_id

  // runSproc(sproc name, partition key, document id to )
  const sprocRes = await runSproc(updateSproc.id, partitionKey, docId)
  // console.log("sprocRes :", sprocRes)

  const newDoc = await getDoc(dId, partitionKey)
  assert.strictEqual(newDoc.touched, 1, "touched should equal 1")
  await deleteDoc(fixtures.userDoc)

  console.log("\n*Assertions passed")
  return newDoc
}

run()
  .then(console.log)
  .catch(console.error)
```

### Fixture generator

We only need a single document for this test.


```js
function guid() {
  return ([1e7] + -1e3 + -4e3 + -8e3 + -1e11).replace(/[018]/g, (a) =>
    (a ^ ((Math.random() * 16) >> (a / 4))).toString(16)
  );
}

function getFixtures(guid) {
  return {
    userDoc: {
      id: "user-" + guid,
      user_id: "test-user",
      coupon_name: "sproc_testing",
      user_details: "I am the user doc",
      detail: "child detail"
    }
  }
}
```

### the stored procedure

Since the sprocs use callbacks we would have to triple nest this.  
1. Get the document
2. update the document
3. replace the document

To make this javascipt a bit more clear, lets use promises and frame out someething like this.

```js
const updateSproc = {
    id: "updateSproc_001",
    body: function (docId) {
      console.log("Sproc called with " + docId)

    getDocument(__.getAltLink() + '/docs/' + docId)
        .then(updateDoc)
        .then(replace)
        .then(setResponse)
        .catch(setResponse)
```

in order to get there lets start simply with a sproc that just retrieves the document.  It does not make the update.

```js
const updateSproc = {
    id: "updateSproc_001",
    body: function (docId) {
      console.log("Sproc called with " + docId)

    getDocument(__.getAltLink() + '/docs/' + docId)
        .then(setResponse)
        .catch(setResponse)

      function getDocument(documentLink) {
        return new Promise( (resolve, reject) =>{
          var isAccepted = __.readDocument(documentLink, {}, function (err, feed, options) { 
            console.log("feed ", feed, err, "]")
                if (err) reject(err)
                resolve(feed)
            })
            if (!isAccepted) reject('The query was not accepted by the server.')
          })
        }

      function setResponse(body) {
        getContext().getResponse().setBody(body)
      }
    }
}
```

At this point you may have a failing test (because doc.touched will be undefined).  Take some time to make this stable so that you can start iterating on the stored prod.

#### readDocument
```js
var isAccepted = __.readDocument(documentLink, {}, function (err, feed, options) { 
  console.log("feed ", feed, err, "]")
  if (err) reject(err)
  resolve(feed)
})
```

`__` is a [shorthand](http://azure.github.io/azure-cosmosdb-js-server/-__object.html) for getContext().getCollection()

[readDocument](http://azure.github.io/azure-cosmosdb-js-server/Collection.html#readDocument) takes a documentLink, request options and a callback.

The documentLink is a _name based link_.  In the early days of Comsos links to the collection and documents were based on IDs such as `dbs/6kJfAA==/colls/6kJfAOyb9Zw=/docs/6kJfAOyb9ZwyAQAAAAAAAA==/`
In the current version the links are human readable based on the collection and database names such as `dbs/goCart/colls/user_coupons/docs/user-46f28052-d2f4-4269-ac11-0fd736481662`
the new version is much more clear, but is condered the 'alternative link'.  The `__self` and `getSelfLink()` return the legacy link.

### Finish the code

At this point you should have simple script that represents a failing test.  It should be fast and you can iterate to explore how the sproc works.

[Full Working Script](https://github.com/gopuff/snippets/blob/master/cosmosScripts/cosmso-update-sproc.js)

#### Working sproc

```js
const updateSproc = {
    id: "updateSproc_001",
    body: function (docId) {
      console.log("Sproc called with " + docId)

    getDocument(__.getAltLink() + '/docs/' + docId)
        .then(updateDoc)
        .then(replace)
        .then(setResponse)
        .catch(setResponse)

      function updateDoc(doc) {
          doc.touched = (doc.touched || 0) + 1
          return doc
      }  

      function replace(doc) { 
        const documentLink = __.getAltLink() + '/docs/' + doc.id
        return  new Promise( (resolve,reject) => {
                __.replaceDocument(documentLink, doc, function(err, feed){
                if (err) reject(err)
                resolve(doc)
              })
          })
      }

      function getDocument(documentLink) {
        return new Promise( (resolve, reject) =>{
          var isAccepted = __.readDocument(documentLink, {}, function (err, feed, options) { 
            console.log("feed ", feed, err, "]")
                if (err) reject(err)
                resolve(feed)
            })
            if (!isAccepted) reject('The query was not accepted by the server.')
          })
        }

      function setResponse(body) {
        getContext().getResponse().setBody(body)
      }
    }
}
```
