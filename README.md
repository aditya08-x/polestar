# Polestar
This repo is for all the Polstar Api service

# Installation

Install a **python 3.7** environment and create a virtual environment using 

`python -m venv env-name`

Install all requirements by Running.

`pip install --no-cache-dir -r requirements.txt`

# Prerequisite

Start a postgres instance at **5433** Port

# Environment variables

**POSTGRES_USER**      : postgres User Name
**POSTGRES_PASSWORD**  : postgres password for the user
**POSTGRES_HOST**      : postgres host by default its **localhost**
**POSTGRES_PORT**      : postgres port by default its **5433**
**POSTGRES_DB**        : postgres database name
**APP_HOST**           : host for application to run by default its **127.0.0.1**
**APP_PORT**           : port for application by default its **5001**


# Loading the data

You can call upload_data.py file to create tables and load all the data in the database using bellow command.

`python3 upload_data.py`


# Running tests

You can run **test_database.py** file to run all tests


# How to Run

Activate the Virtual environment 

`source venv/bin/activate`

To start application you can call main.py file by running bellow command

`python3 main.py`

# Accessing the SWAGGER

http://127.0.0.1:5000/api/polestar/swagger


