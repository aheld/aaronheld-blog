install `az` cli
    https://docs.microsoft.com/en-us/cli/azure/install-azure-cli-linux?pivots=apt
az login
az account show
az account list --query "[].{name:name, subscriptionId:id}"
az account set --subscription="<subscription_id>"
az account show --query "name" --output tsv 



terraform init after changing resources

badfile=`printf '*[\\x01-\\x1f\\x7f]*'`

☁  aaronheld-blog [main] ⚡ echo $badfile
*[-]*
☁  aaronheld-blog [main] ⚡ find public -name "$badfile" -exec echo 1 \

Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   .github/workflows/azure-static-web-deploy.yml
        deleted:    "content/post/chef-ramsay-as-a-model\nmanager/image.jpg"


        https://dwheeler.com/essays/fixing-unix-linux-filenames.html