# hack-ksu-2019

The purpose of this repository is to store our notes and application for the 2019 KSU Hackathon.

## Requirements
python 3.6.8
git

## Environment Files
Do not add apikey or other sensitive data to this repo.

## Set up the environment
```
cd scripts
python3.6 -m venv .env
. .env/bin/activate
pip install wheel
pip install -r requirements.txt
```

## Run the application
```
. ./run.sh
```
Alternatively:
```
. .env/bin/activate
cd scripts
python app.py
```
## File Structure

## scripts
This directory holds our main api interface application. The application runs from `app.py`. The only package used for our application is `requests`. You can see the version of requests we used in the requirements.txt

### scripts/.config
This folder holds config for our application. It has a logs folder, where the logs are stored if the user wishes to log to file (see `utility/env.py`). It also has a json which has the base url for the api and the api key. Currently, this data is available to the developer for conveinence. However, this data is 'hidden' due to the fact that this repo is private, and likely by the time this repo is public, the base url is no longer available or the api key is invalid.

### scripts/connection
This folder holds the connection class, which is a class that utilizes the basic api endpoints to add additional functionality. It stores user and owner data and gives the user the data they have stored in the main database in with the api.

### scripts/context
This folder holds our Context class, in `context.py`. This class is not initialized as an object, but is used as a global storage class for variables such as the api key, and base url. This class handles pulling data from the config files (see `scripts/.config`). If this were production level code, then the developer would have to initialize their config file by running a script, and insert the base url and api they wish to use. For convenience, this config file is preinitialized and Context pulls the data from `config.json`.

### scripts/endpoints
This folder contains two folders, one for account api endpoints and the other for transaction api endpoints. There is also a class called Endpoints that is not initialized as an object, simliar to `Context`. It is used to reference the functions stored in the subdirectories in this folder.

Our scripts for the endpoints build the request url based off of the based url stored in `Context`. It will use the input parameters to the function to build the request along with the headers from the Context class. 

## scripts/utilty
This folder holds several scripts for general use. 

`const.py` holds constant string variables. These are useful because they can be used for dictionary keys, and make it easier to reference the key values across different scripts. 

`env.py` holds environmental variables. This is where the names of the variables used in `config.json` are stored. Also, the developer can change the logging level and log to file if they wish.

`tablemap.py` holds the Tablemap class, which is a base helper class that can be referenced as dictionary. Classes that extend Tablemap gain this functionality.

## notes
This directory holds notes, including pictures used for our alexa skill and our presentation. In addition, there are some images showing the functionality of the Alexa conversational skills from the Alexa Developer's Console

## lambda
This directory holds the scripts that are used on our lambda server application. The file structure is similar to the main directory but has a few tweaks. For example, the lambda server does not have access to the `requests` package, so it uses `botocore.vendored.requests` instead. The main entrypoint for the application is the `lambda_function.py.` This script handles the Alexa requests and looks to the `/intents` folder to generate the correct response to the intent.

The biggest difference from our api interface application in `./scripts` is the `/intents` folder. All of the intent response generation functions are stored here. Note that the scripts were copied from the AWS lamdba ide and have not been tested in this environments. There may be typos in the names of the files. 
