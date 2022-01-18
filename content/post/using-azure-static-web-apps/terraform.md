---
title: "Azure Static Web Apps with Terraform" 
date: 2021-08-27T08:33:08-04:00 # Date of post creation.
description: "Example of how to setup an Azure Static Web App Using Terraform"
featured: false 
draft: false
ShowToc: true
TocOpen: true
# menu: main
featureImage: "/post/using-azure-static-web-apps/terraform_logo.png" # Sets featured image on blog post.
thumbnail: "/post/using-azure-static-web-apps/terraform_logo.png" # Sets thumbnail image appearing inside card on homepage.
shareImage: "/post/using-azure-static-web-apps/terraform_logo.png" # Designate a separate image for social media sharing.
codeMaxLines: 300 # Override global value for how many lines within a code block before auto-collapsing.
codeLineNumbers: true # Override global value for showing of line numbers within code block.
figurePositionShow: true # Override global value for showing the figure label.
categories:
  - Azure
tags:
  - Tutorial
  - Terraform
  - hosting
---

Devops is many different things to many different people, but nearly all practitioners agree that infrastructure as code is a critical part.  So rather then use the Azure portal UI to create our desired resources we are going to script it in code.  We will have confidence that we can create, destroy and eventually scale resources as needed. 

In this post we will create a Azure static using terraform, step by step.

[Terraform](https://www.terraform.io/) is a great tool for scripting your infrastructure.  It has first class Azure providers and the security model integrates with the `az` command line. 


## Setup

In order to follow this example you will need
1. An [Azure](https://azure.microsoft.com/en-us/free/search/) account
2. [Terraform installed](https://learn.hashicorp.com/tutorials/terraform/install-cli?in=terraform/azure-get-started)
3. [az cli](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli) installed

This exercise can be done in the free plan.  We will create and destroy the infrastructure.  If you neglect to destroy the resources you may wind up with charges. 

### Logging in to Azure

Once the az cli is installed, run `az login` and follow the instructions. On some operating systems your browser will automatically open with a login page, Once you have logged in, return to the terminal.

I'm running linux [System76 Lemur Pro w/ PopOS (ubuntu)](https://system76.com/laptops/lemur) and I've given my subscription the name *personal*.  If you run this on a new free account you may see something like "Pay as you go" for the name. 


```bash
⚡  uname
Linux

⚡  az login
The default web browser has been opened at https://login.microsoftonline.com/common/oauth2/authorize. Please continue the login in the web browser. If no web browser is available or if the web browser fails to open, use device code flow with `az login --use-device-code`.

# The above command opens a browser window and you need to login to it.

You have logged in. Now let us find all the subscriptions to which you have access...
[
  {
    "cloudName": "AzureCloud",
    "homeTenantId": "XXXXX-XXXX-",
    "id": "XXXXX-XXXX-",
    "isDefault": true,
    "managedByTenants": [],
    "name": "personal",
    "state": "Enabled",
    "tenantId": "XXXXX-XXXX-"
    "user": {
      "name": "myemail@live.com",
      "type": "user"
    }
  }
]
```

## Use Terraform to create the infrastructure

### Base setup and Resource Group

Let's start with a minimal terraform file that just sets up a new _Resource Group_.

You need to tell Terraform that you will be using the Azure provider and then add the code for a basic resource group.

```tf
# file: blog.tf
terraform {
  required_providers {
    azurerm = {
      source = "hashicorp/azurerm"
      version = "~>2.0"
    }
  }
}

resource "azurerm_resource_group" "rg" {
  name = "test-resource-group"
  location = eastus
}
```

Run `terraform init` and then `terraform plan` to ensure we have the syntax right.  If that was successful then you will now see a `.terraform` directory has been created.

Whenever you change the providers block you will need to rerun `terraform init`. For other changes you can just re-run the plan command.

My run looked something like this

```bash
⚡  terraform init

Initializing the backend...

Initializing provider plugins...
- Finding hashicorp/azurerm versions matching "~> 2.0"...
- Installing hashicorp/azurerm v2.74.0...
- Installed hashicorp/azurerm v2.74.0 (signed by HashiCorp)

Terraform has created a lock file .terraform.lock.hcl to record the provider
selections it made above. Include this file in your version control repository
so that Terraform can guarantee to make the same selections by default when
you run "terraform init" in the future.

Terraform has been successfully initialized!
# note: I trimmed the output, you will see more

⚡ terraform plan

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated
with the following symbols:
  + create

Terraform will perform the following actions:

  # azurerm_resource_group.rg will be created
  + resource "azurerm_resource_group" "rg" {
      + id       = (known after apply)
      + location = "eastus"
      + name     = "test-resource-group"
    }

Plan: 1 to add, 0 to change, 0 to destroy.
# note: I trimmed the output, you will see more
```

If everything looks good, lets create that resource group using `terraform apply`.  Note that you will prompted to confirm the creation of resources.  Eventually this will cost money, so please pay attention to what you create. 

```bash
⚡ terraform apply

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated
with the following symbols:
  + create

Terraform will perform the following actions:

  # azurerm_resource_group.rg will be created
  + resource "azurerm_resource_group" "rg" {
      + id       = (known after apply)
      + location = "eastus"
      + name     = "test-resource-group"
    }

Plan: 1 to add, 0 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

azurerm_resource_group.rg: Creating...
azurerm_resource_group.rg: Creation complete after 1s [id=/subscriptions/7c4de52a-a467-40ad-b304-219534ba76e3/resourceGroups/test-resource-group]

Apply complete! Resources: 1 added, 0 changed, 0 destroyed.
```

After a few seconds you should see your new resource group in the [Azure Portal](https://portal.azure.com/#blade/HubsExtension/BrowseResourceGroups)

![Resource Groups listing in Azure Portal](../azure-portal-resource-group-list.png)

or use the command line
```bash
⚡  az group show --name test-resource-group --query 'properties.provisioningState' --out tsv
Succeeded
```

Before we move onto then next step, lets destroy the resource group using `terraform destroy` and you can check it with the cli or portal.

### Add Static Web App

Now that we have a resource group, lets put a static web app into it.  The terraform looks like this

```tf
# add to blog.tf
resource "azurerm_static_site" "web" {
  name = "web-myblog-prod-eastus"
  resource_group_name = azurerm_resource_group.rg.name
  location = "eastus"
}
```

and run it

```bash
⚡  terraform plan 
  ...
Plan: 2 to add, 0 to change, 0 to destroy.
```

looks good, lets apply it

```bash
⚡  terraform apply

Terraform used ....

...

azurerm_static_site.web: Creating...
╷
│ Error: failed creating Static Site: (Name "web-myblog-prod-eastus" / Resource Group "rg-myblog-prod-eastus"): web.StaticSitesClient#CreateOrUpdateStaticSite: Failure sending request: StatusCode=0 -- Original Error: Code="LocationNotAvailableForResourceType" Message="The provided location 'eastus' is not available for resource type 'Microsoft.Web/staticSites'. List of available regions for the resource type is 'westus2,centralus,eastus2,westeurope,eastasia'."
│ 
│   with azurerm_static_site.web,
│   on blog.tf line 30, in resource "azurerm_static_site" "web":
│   30: resource "azurerm_static_site" "web" {
```

From the helpful error message, it looks like Azure Static websites aren't rolled out into every region.  Azure is growing and routinely rolls out new services by region.  Keep this in mind when you plan out your infrastructure.  It caused me some pain because this resulted in some of my services split across regions.

### Terraform Variables

Now we have 2 resources to edit the location, both the resource group and web app need to be updated to used useast2.

Run a `terraform destroy` and refactor the terraform file to use variables as opposed to hardcoded values.

I like using the Azure convention where resource names should be in the form `{resourceType}-{name}-{tier/environment}-{region}` so we will do that as well.

Adding some local variables to terraform looks like 
```tf
# file: blog.tf
locals {
  name = "myblog"
  location = "eastus2"
}
```

and use them like so:

```tf
# file: blog.tf
resource "azurerm_resource_group" "rg" {
  name = "rg-${local.name}-prod-${local.location}"
  location = local.location
  tags = local.common_tags
}

resource "azurerm_static_site" "web" {
  name = "web-${local.name}-prod-${local.location}"
  resource_group_name = azurerm_resource_group.rg.name
  location = local.location
}
```

Running `terraform plan` will check the syntax and display the interpolated strings

```bash
# azurerm_resource_group.rg will be created
  + resource "azurerm_resource_group" "rg" {
      + id       = (known after apply)
      + location = "eastus2"
      + name     = "rg-myblog-prod-eastus"
```

While we are at it, lets add some tags to our variables. Tags are indispensible to help understand and organize as your grow your cloud.

I usually add a `common_tags` to the locals. so now our terraform file looks like this;

```tf
locals {
  name = "myblog"
  location = "eastus2"
  common_tags = {
      created_by = "youremail@...."
      tier = "production"
      inspiration = "https://aaronheld.com"
  }
}

terraform {
  required_providers {
    azurerm = {
      source = "hashicorp/azurerm"
      version = "~>2.0"
    }
  }
}

provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "rg" {
  name = "rg-${local.name}-prod-${local.location}"
  location = local.location
  tags = local.common_tags
}

resource "azurerm_static_site" "web" {
  name = "web-${local.name}-prod-${local.location}"
  resource_group_name = azurerm_resource_group.rg.name
  location = local.location
  tags = local.common_tags
}
```

Run this using `terraform apply` and check your work

```bash
⚡  az group show -n rg-myblog-prod-eastus2

{
  "id": "/subscriptions/XXXXXXXXXX/resourceGroups/rg-myblog-prod-eastus2",
  "location": "eastus2",
  "managedBy": null,
  "name": "rg-myblog-prod-eastus2",
  "properties": {
    "provisioningState": "Succeeded"
  },
  "tags": {
    "created_by": "youremail@....",
    "inspiration": "https://aaronheld.com",
    "tier": "production"
  },
  "type": "Microsoft.Resources/resourceGroups"
}
```


see if the static web app deployed 
```bash
⚡  az staticwebapp show web-myblog-prod-eastus2
```

if you want to get the default hostname
```bash
⚡  az staticwebapp show -n web-myblog-prod-eastus2 --query defaultHostname --out tsv

# open in a browser
# osx
⚡  open http://`az staticwebapp show -n web-myblog-prod-eastus2 --query defaultHostname -o tsv --only-show-errors`
# linux
⚡  firefox http://`az staticwebapp show -n web-myblog-prod-eastus2 --query defaultHostname -o tsv --only-show-errors`
```

finally, lets destroy the resources and move onto deploying a static app from github.

```bash
⚡  terraform destroy
```

## Summary

In this article we used Terraform to script the creation of an Azure Static web app.  We introduced variables and some scripting that will be the foundation of our infrastructure code as we progress.

The next step is to get some content to our website.
