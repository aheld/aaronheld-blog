locals {
  name = "blog"
  location = "eastus2"
  common_tags = {
      created_by = "aarondheld@gmail.com"
      tier = "production"
  }
  deploy_token_name = "AZURE_STATIC_WEB_TOKEN"
  repo_name = "aaronheld-blog"
}

terraform {
  required_providers {
    azurerm = {
      source = "hashicorp/azurerm"
      version = "~>2.0"
    }
    github = {
      source = "integrations/github"
      version = "4.12.1"
    }
  }
}
provider "azurerm" {
  features {}
}

output hostname {
  value = azurerm_static_site.web.default_host_name
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

resource "github_actions_secret" "web" {
  repository       = local.repo_name
  secret_name      = local.deploy_token_name
  plaintext_value  = azurerm_static_site.web.api_key
}

resource "github_actions_secret" "host_name" {
  repository       = local.repo_name
  secret_name      = "host_name"
  plaintext_value  = azurerm_static_site.web.default_host_name
}