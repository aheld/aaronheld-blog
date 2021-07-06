install `az` cli
    https://docs.microsoft.com/en-us/cli/azure/install-azure-cli-linux?pivots=apt
az login
az account show
az account list --query "[].{name:name, subscriptionId:id}"
az account set --subscription="<subscription_id>"
az account show --query "name" --output tsv 



terraform init after changing resources
