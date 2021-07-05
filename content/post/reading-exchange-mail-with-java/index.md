---
title: "Reading Exchange Mail with Java"
date: "2013-07-14"
categories: 
  - "code"
---

Many times I've had to sweep an inbox and do something with the email. Typically the easiest way is to use IMAP, but our corporate email server has IMAP disabled.

Fortunately 2007 Microsoft Exchange has had a rich web service interface so I wanted to give that a try.

One of the main patterns used is to read an email and then move it to something like an 'archive' or 'error' directory. Exchange supports arbitrary message properties such as 'category' and even custom properties, so adding a category tag of "processed" seems like a good idea. I wanted to experiment a bit.

Some googling turned up a java API and seems 'lightly' supported. I had little luck finding any examples for just reading email. [http://archive.msdn.microsoft.com/ewsjavaapi](http://archive.msdn.microsoft.com/ewsjavaapi)

I decided to check out the .NET library to see if that would shed some light on how to use the Java API - and it did. [http://msdn.microsoft.com/en-us/library/dd633710(v=exchg.80).aspx](http://msdn.microsoft.com/en-us/library/dd633710(v=exchg.80).aspx)

and found the 2 APIs are very similar. By writing some samples in c# I was able to quickly port them into Java and something like this should work for you.

\[gist id="5995611"\]

You do have to download the Microsoft .jar and a few dependencies to get this working. I'm posting this because I could not find this type of simple example.

tip: If you are unsure of the API domain endpoint look for the wsdl at https://EXCHANGE\_API\_DOMAIN/EWS/Services.wsdl
