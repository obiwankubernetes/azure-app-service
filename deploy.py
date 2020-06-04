### Setup App

    # import packages

    # create app

    # create requirements.txt -> pip freeze > requirements.txt

    # install requirements.txt -> pip install -r requirements.txt

    # init flask app -> FLASK_APP=application.py

    # run app locally -> python -m flask run

    # check app locally -> go to localhost:5000

### Setup Deployment

    # login to azure thru cmd line -> az login

    # create resource group -> az group create --name [your name for a resource group] --location westus

    # create app service plan -> az appservice plan create --name [your name for an app service plan] --resource-group [you name for a resource group] --sku B1 --is-linux

    # create webapp -> az webapp create --resource-group [your name for a resource group] --plan [your name for a service plan] --name [your name for an app name] --runtime "PYTHON|3.7" --deployment-local-git

    # Configure a deployment user -> az webapp deployment user set --user-name <username> --password <password>

    # visit website -> go to public url (http://.azurewebsites.net)

### Push Code

    # align git with azure -> git remote add azure <deploymentLocalGitUrl-from-create-step>

    # push from git to azure -> git push azure master

    # visit public url again



