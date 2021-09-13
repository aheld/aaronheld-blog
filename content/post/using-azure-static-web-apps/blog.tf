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