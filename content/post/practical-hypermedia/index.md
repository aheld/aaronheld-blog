---
title: "Practical Hypermedia for our post ORM world"
date: "2012-09-29"
categories: 
  - "code"
  - "professional"
tags: 
  - "architecture"
  - "barcamp"
  - "hypermedia"
---

This post is for people who have started learning about hypermedia and feel that it over complicates the elegance of REST. When I started hearing about hypermedia I felt it was adding architecture acrobatics for the sake of buzzword enhancement. After having applied these techniques in a few places not only have a drunk the cool aid, I've setup a stand beside my desk. I look back and try to understand where my initial negative reaction came from. I realized that many of the examples were trivial and did not demonstrate the reality of what hypermedia brings to the table.

The main epiphany I'd like to share is that REST has proven itself as the best way to take an ORM focused approach to an API and Hypermedia is proving itself as the best way to take a business process approach to an API.

A key aspect of Hypermedia that I don’t see used often enough is the notion of a template. The template portion of the spec calls for the API to send down to the client the parameters necessary to call the API itself. This notion is akin to how you load a web page with a blank form and then submit the form directly. You don’t post to twitter by typing a bunch of stuff into the url, you load twitter first and then fill in a textarea.

Essentially in my early experiments I was writing XML api payloads where the template portion was basically an HTML form that the client could decompose and render. The problem that I felt was that I was basically writing a full old school web application that happened to send XML rather than HTML back to the client. Then my client had extra complexity in parsing the XML and implementing all the UX rules to get the client looking and feeling right. I also had to build 2 webapps that both were basically doing the same thing, view, validation and calling a service.

Now lets take a look at doing this for real using AngularJS, JSON and a deadline.

The business case: Our sales team has access to a report of customer service change activity. Current use cases include a simple sales report to show and total the usage of a sales rep's customers on a monthly basis.

An initial implementation focusing around the orm simply used Linq against Entity Framework to retrieve the data from a MSSQL database.

Before we can generate the report we need to present an input form to the user. The design calls for a "Sales Rep" drop down list which will allow us to report on activity by sales rep. In an ORM world generating this drop down is easy enough, throw up a few classes against the employees table, query based on role, and render that to HTML on the server.

In our razor/asp/whatever template there is some code along the lines of:

```
<select name="salesrep">
    <% foreach rep in salesreps %><option value="<%= rep.id %>"><%end%>
</select>
```
Easy!

Next iteration we are asked to restrict reports such that a rep can only see their own customers, but the sales manager can see all customers.

Now the code looks something like:

```
<select name="salesrep">
    <% if User.hasRole(Roles.SALESMGR) %>
       <% foreach rep in salesreps %><option value="<%= rep.id %>"><%end%>
    <% else %>
        <option value="<%=User.id%>">User.Name</option>
```
Ok so this could be refactored along the lines of

```
<select name="salesrep">
   <% foreach rep in salesreps\_Based\_on\_Role %><option value="<%= rep.id %>"><%end%>
```
The relevant point here is that the salesrep list restrictions must be handled in the view based on this use case.

Once that work is done we need to generate the report data itself. Building a restful endpoint for this sounds like a good idea and is an incremental effort for a reusable data source. Most people (including myself) would build out that restful endpoint and use it to generate the data. Maybe put some logic in the server side controller that will parse the HTML submission form, apply security, and they make the restful call.

This restful approach could be a generic "SalesRep’ list endpoint and move the filtering logic there. Since we also need a list of sales reps for things like "forwarding a customer’ that new end point would need to know how it is going to be used before it is called. So the CONTEXT of how the API is called matters. Unfortunately in a stateless world the API call does not have the context unless it is given a hint by the client.

Additionally we need to implement this logic against the report generation as well, otherwise anyone could modify the http request and generate a report for a salesrep against our business requirements. The linq query (psudocode) could look like:

```
//find all the records 
IEnumerable<ServiceChanges> servicechanges =
 from records in recordsORM
     select record where SalesRep = {0};
// and filter based on role
if !User.rolein(Roles.SALESMGR) {
     servicechanges = servicechanges.Where(records.salesrep.id = {0},User.id);
}
```

In our orm world, even if we we create restful services such as "/api/servicechanges/’ and "/api/salesrep/’ we still have two bits of unrelated code that need to be kept in sync. The view is ultimately coupled to the api call.

The ORM layer has now served to couple the database directly to the view. dropdowns are created against the salesreps\_Based\_on\_Role object which is coupled to the employee tables and sprikled with business logic for every view it may be called for. Not a very reusable pattern simply because it is called by the client WITHOUT THE CONTEXT of how it will be used.

Older developers will remember the good old stateful days of foxbase and objectpal where these use cases would be trivial. Just implement row level security into the table and your salesrep list is a view such as:

reportview = select \* from serivceactivity join salesrep.id in ALLOWED\_IDS\_BASED\_ON\_ROLE

then you bind a drop-down list to "select distinct salesrep.id from reportview"

this antiquated approach has the benefit of both the form construction as well as the report generation being based off the sames business rules - row level restrictions. Sometimes I miss the stateful, context rich, execution environment of an old school desktop application.

### Hypermedia approach

How does hypermedia lend itself to a cleaner solution?

It brings context back to the conversation by preserving the state at the API level.

This is what HATEOS http://en.wikipedia.org/wiki/HATEOAS , Hypermedia As an Engine Of State, means.

A key tenet of hypermedia is that the client does not need any prior knowledge in order to make the api call. This is where common sense needs to balance reality. I don’t expect to build a magic client that can do anything, but within the scope of a particular problem domain we can limit the need of the client to make multiple calls in order to "setup’ the parameters necessary.

In the example of the sales rep situation, our client still need to make a call to the server before calling the api. In this case however it calls the /salesrep/ service itself and retrieves the hypermedia template. (yes this is akin to WSDL, if WSDL was easier to understand and extensible). When the server side code is calling for the list of salesreps for the client to render it has the context of how the data will be called, as well as the knowing the user/role based security model to operate under.

Our hypermedia design is based on a combination of JSON+collection media type as published by Mike Amundsen [http://www.amundsen.com/media-types/collection/](http://www.amundsen.com/media-types/collection/) blended with what we have experienced using the indispensable JIRA api [http://docs.atlassian.com/jira/REST/latest/](http://docs.atlassian.com/jira/REST/latest/).

JSON+collection calls for a query template. This query template is where the api will describe to the client how to make a query or find data.

In my case it looks something like:

```
"queries" : \[{
     "href" : "/api/saleslog/search",
     "rel" : "search",
     "data" :  \[
       {"name" : "startDate","type":"date", "prompt":"Start date for report"},
       {"name" : "endDate", "type":"date", "prompt":"End date for report"},
       {"name" : "salesrep", 
        "type":"select", 
        "required": true, 
        "options":\[
          {"name":"B. Hartnell", value:1},
          {"name":"J. Pertwee", value:3},
          {"name":"P Troughton", value:2},
          {"name":"T Baker", value:4},
          {"name":"D Tennant", value:10}
                  \]
        }
     \]
 }\]
```
 

To render that into a form using angular was remarkably easy:

[http://fiddle.jshell.net/aaronheld/kQ8K3/](http://fiddle.jshell.net/aaronheld/kQ8K3/ "Fiddle this")

[Angularjs](http://angularjs.org/) allows me to bind the client side state to the API and handles keeping the DOM and view in sync with the model.  More on that later (hint: synergy!)

The fun part being that the client does not have to know anything about the security concerns around "salesRep’. The way that the drop down is rendered is something along the lines of

```
 <select ng:switch-when="select" ng:model="field.value" >
     <option ng:repeat="option in field.options" value="{{option.value}}">{{option.name}}</option>
 </select>
```

You can google for some robust form builder implementations but with a good template representation they do not seem necessary for my needs. http://007design.com/formular/index.html was the inspiration for this approach.

the final step is almost anticlimactic, for the client to render the drop down with security all that has to happen is that the API sends back a salesRep list with one option.

From here I feel that we have an agile design. With suitable testing we have a confident implementation. So far all of the iterative updates have felt easy. Yesterday we were discussing changing the UX so that if there is one option we don’t render a select box (since there is no selection). In that case we simply change the angular form logic in the browser, where UX view logic belongs. Security changes and additional query logic is based in the server/API where it belongs.

Next I’ll write up how we return the row items of the report and leverage hypermedia links to allow the client to perform operations on items based on business rules.

This will all lead up to demonstrating how this an API first approach (rather then object model based design) will allow me to replace all of the search/list/operate work queues in my enterprise with a consistent pattern and greatly simplified software stack.

If you are in Philly this November I'm thinking about a code walkthough at [http://2012.barcampphilly.org/](http://2012.barcampphilly.org/) See you there!
