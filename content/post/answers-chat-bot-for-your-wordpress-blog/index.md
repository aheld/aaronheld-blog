---
title: "Answers Chat bot for your WordPress blog"
date: 2017-04-15
description: "Chat based interfaces, backed by powerful AI (Artificial Intelligence), are effective ways to connect with your customers."
---

## Introduction

Chat based interfaces, backed by powerful AI (Artificial Intelligence), are effective ways to connect with your customers. For decades thousands of [brilliant and dedicated scientists](http://technav.ieee.org/tag/1215/natural-language-processing) have collaborated to create [AI](http://spectrum.ieee.org/view-from-the-valley/robotics/industrial-robots/sri-shakey-robot-honored-as-ieee-milestone) and Language Processing to construct automated systems for the betterment of humanity. More recently Microsoft wrapped this magic in tooling that makes it accessible to the less sophisticated masses (and .net developers)

When blogging became popular a number of companies sought to ‘commoditize’ the complexity of setting up a server and running custom website software. Wordpress is the undisputed winner of ‘personal blog software’. What Wordpress has done for websites and content management Microsoft is doing for AI. The haven’t won yet, Amazon, IBM and others are all in this together. I’m working on an Amazon bot in parallel to this so that I can compare and contrast the services.

In order for a chatbot to be useful, it needs data to provide. Microsoft has created a ‘Question and Answer’ service that provides for the common use cases. In many cities navigating the Office of Property Management is daunting task, so lets build a chatbot to help users get answers to the [Philadelphia OPM FAQ![](/assets/posts/images/MS-bot-intro-OPM.png)](http://www.phila.gov/OPA/Pages/FAQ.aspx)

Once we have created the service, we will develop a [quick wordpress plugin](https://github.com/aheld/wp_chatbot) in order to connect the service to your blog.

## Create a Microsoft Question and Answer Service

Login to MS cognitive services and create your QandA service

[https://qnamaker.ai/](https://qnamaker.ai/)

From the top menu click ‘create new service’. You will be promoted to login using an existing Microsoft account, or to create a new one.

Give your bot a friendly name and paste in a URL of a FAQ page for the service to scrape. You can also upload a data file or questions and answers, and there are API calls to add or refresh content from existing URLs.

[![](/assets/posts/images/MS-bot-create-1024x726.png)](http://www.aaronheld.com/wp-content/uploads/2017/04/MS-bot-create.png) [ ](http://www.aaronheld.com/wp-content/uploads/2017/04/MS-bot-edit-kb.png)[](http://www.aaronheld.com/wp-content/uploads/2017/04/MS-bot-settings.png) 

Once the service has completed scraping the provided URL you will see a list of the questions and answers![](/assets/posts/images/MS-bot-edit-kb-1024x686.png)

on this screen you can edit and update questions and answers. Click the ’test’ option on the left to test out the chatbot and train it.

![](/assets/posts/images/MS-bot-training-1024x668.png)

When you are satisfied with the results, click ’Save and Train’ and then ‘Publish’.

Before we can build the Wordpress plugin, lets try a simple PHP script to ensure we have connectivity. In order to access the API, you will need 2 variables. The GUID of your knowledgebase and your subscriber key. The simplest way to get them is by clicking the ’settings’ tab and looking at the code sample provided:![](/assets/posts/images/MS-bot-settings-1024x259.png)

test our a simple PHP script to connect to the service. Replace the `{Knowledgebase ID}` and `{Subscription-Key`} with the variables from your service.

\[gist id="aheld/1e4d8a5df0d13385c50018ca67d693dc" \]

### You should now be able to test your bot using a web browser

[http://Your Web Server/bot.php?question=how%20do%20I%20get%20a%20permit](http://Your Web Server/bot.php?question=how%20do%20I%20get%20a%20permit)

Congratulations. You can now add Natural Language Processing, Machine Learning and AI to your resume ;)

In our next post we will create a simple [Wordpress plugin](https://github.com/aheld/wp_chatbot) to easily access your new service.
