---
title: "CosmosDB: Hello Stored Procedures (sproc)" # Title of the blog post.
date: 2020-04-26T21:45:20-04:00 # Date of post creation.
description: "A tutorial showing how a CosmosBD Stored procedures (sprocs) can be deployed, updated and tested from code." # Description used for search engine.
categories:
- Azure
tags:
- CosmosDB
---

# CosmosDB Stored Procedures

## Why stored procedures?

Stored Procedures (*sprocs*) are functions that run on the server-side of a database.  In particular, we will be talking about sprocs in _CosmosDB_.

The main reasons for using CosmosDB [Sprocs][1] are atomic transactions and performance. All database operations completed in a single sproc call will be atomic. Since the Sproc runs on the server the network latency for loading and saving documents will be considerably less than running the same operations from a remote server or laptop.

I assume you already have a cosmos DB account and the write token to complete this example.

## The Code

For this example, we will create a simple "Hello World" sproc that returns "Hello World" when called.

### Create the Sproc

To define a sproc in code, create an object with an 'id' and a body that is the function itself. The 'id' will be the name of the Sproc and will be used for execution calls.

Once a sproc is in production, I recommend versioning it, by naming the next one something like id: "helloWorld_2", if you are concerned with breaking existing applications.

```js
const helloWorldStoredProc = {
    id: "helloWorld",
    body: function () {
        console.log("logging message from the sproc")
        var context = getContext();
        var response = context.getResponse();
        response.setBody("Hello, World");
    }
}
```

This is a very simple sproc, it just gets the response object from the context and sets the body. When called we expect to see 'Hello, World" as the return.

Every stored procedure is a javascript object with an ID and a body, where the body is the function to exectue.


### Setup `hello_world_sproc.js`
```bash
# if you prefix the export command with a space
# it usually will not save the secret key to your history file
 export cosmos_key="<<INSERT KEY HERE>>"
npm i -s @azure/cosmos
```

### Load Cosmos client
```js
const { CosmosClient } = require('@azure/cosmos')

const endpoint = 'https://******.documents.azure.com:443/'
const key = process.env.cosmos_key
const client = new CosmosClient({ endpoint, key })

//get a reference to the container we want to work with
const container = client.database('cart').container('coupons')
```

### Create Sproc in the container

write a function to push the Sproc up

```js
async function createSproc(sproc) {
    return container.scripts.storedProcedures.create(sproc)
}
```

In order to work with sprocs, you need to access the [Scripts class](https://docs.microsoft.com/en-us/javascript/api/@azure/cosmos/scripts?view=azure-node-latest) from the container. This class gets you access to both sprocs as well as User Defined Functions. We will use the create method of the storedProcedure object for now.

### Execute the Sproc

```js
async function runSproc(sprocname, partition_id, args) {
    const result = await container
            .scripts
            .storedProcedure(sprocname)
            .execute(partition_id, args, 
                { enableScriptLogging: true }
                )

    console.log("Sproc Log: ", decodeURIComponent(result.headers['x-ms-documentdb-script-log-results']))
    console.log("Sproc RU cost: ", result.headers['x-ms-request-charge'])
    return result.resource
}
```

Again use the scripts object to access the sprocs. `container.scripts.storedProcedure(sprocname)` will give you access to the [stored Procedure object](https://docs.microsoft.com/en-us/javascript/api/@azure/cosmos/storedprocedure?view=azure-node-latest), which you can then use to access the [execute method](https://docs.microsoft.com/en-us/javascript/api/@azure/cosmos/storedprocedure?view=azure-node-latest#execute-any--any----requestoptions-).

`execute` takes a few positional arguments.
```ts
function execute<T>(partitionKey: any, params?: any[], options?: RequestOptions)
```
The first is a partition key (string works for simple keys), the second are the arguments to pass into the Sproc, and the third is a [RequestOptions](https://docs.microsoft.com/en-us/javascript/api/@azure/cosmos/requestoptions?view=azure-node-latest) configuration object that we will use to capture logs. If you do not specifically request logs, you will not see them returned.

### Get it working
Add a small async main function and get this code working!

```js
async function runHello() {
  console.log("\n*****\n* Starting simple case\n")
  const sproc = helloWorldStoredProc
  await createSproc(sproc)
  const res = await runSproc(sproc.id, "")
  console.log(res)
}

runHello()
```

### Create or Update??
Once this works, it should fail the second time, because you cannot create a sproc that already exists. You must update it.

Let's modify createSproc to be a createOrModify function. Since we will more likely be updating than creating, let's optimize it that way.

```js
async function createOrUpdateSproc(sproc) {
  try {
    await container.scripts.storedProcedure(sproc.id).replace(sproc)
  } catch (e) {
    if (e.code === 404) { //same error code for 'not found'
      console.log('REPLACE failed, try to add ', sproc.id)
      await container.scripts.storedProcedures.create(sproc)
    } else {
      throw(e) // don't swallow unexpected errors!
    }
  }
}
```

update your code and now you should have a simple little test harness to quickly test how to write basic stored procedures.

For a general introduction to interacting with CosmosDB using nodejs see: https://docs.microsoft.com/en-us/learn/modules/build-node-cosmos-app-vscode/

<!---
## Other Articles in this series

1. [Create / Update sproc via code](hello-sproc#why-stored-procedure "This page") (You are here)
2. [Query for multiple documents and return them merged](cosmos-merge-sproc "query sproc")
3. [Apply an atomic update to a single doc](cosmos-update-sproc)
--->

## Completed Script
```js {linenos=table, hl_lines=["8-16"]}
const assert = require('assert')
const { CosmosClient } = require('@azure/cosmos')

const endpoint = 'https://********.documents.azure.com:443/'
const key = "process.env.cosmos_key"
const client = new CosmosClient({ endpoint, key });

const container = client.database('cart').container('coupons')

const helloWorldStoredProc = {
    id: "helloWorld2",
    body: function () {
        var context = getContext();
        var response = context.getResponse();
        console.log("logging message from the sproc")
        response.setBody("Hello, World");
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

async function runHello() {
  console.log("\n*****\n* Starting simple case\n")
  const sproc = helloWorldStoredProc
  await createOrUpdateSproc(sproc)
  const res = await runSproc(sproc.id, "")
  assert.strictEqual(res, "Hello, World")
  console.log("\n*Assertions passed")
  return res
}

runHello().then(console.log).catch(console.error)
```


[1]: https://docs.microsoft.com/en-us/azure/cosmos-db/stored-procedures-triggers-udfs "Azure Stored Procedure Overview"
