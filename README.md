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