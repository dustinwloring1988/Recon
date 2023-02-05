Client-Server Information Reporting System

This repository contains a client-server system that reports information about a computer to a MariaDB database. The system consists of two main components: the client.py script, which runs on the computer and collects information, and the server.py script, which runs on a separate server and receives information from the client.
Requirements

    Python 3.8 or later
    pip
    A MariaDB database

Installation

    Clone this repository to your computer
    Create a virtual environment for the project: python -m venv env
    Activate the virtual environment: source env/bin/activate
    Install the dependencies: pip install -r requirements.txt
    Create a .env file and set the following environment variables:
        DB_HOST: The hostname or IP address of the MariaDB server
        DB_PORT: The port number of the MariaDB server
        DB_NAME: The name of the database to use
        DB_USER: The username for the MariaDB server
        DB_PASSWORD: The password for the MariaDB server

Usage

    Run the server.py script on the server: python server.py
    Run the client.py script on the computer: python client.py
    Check the MariaDB database to see if the information was successfully recorded.

Deployment with Docker Compose

The docker-compose.yml file in this repository can be used to set up a MariaDB database for use with this system. Simply run docker-compose up to start the database and connect to it. Note that you will need to set the DB_* environment variables in the .env file before starting the database.
Continuous Integration and Deployment (CI/CD)

This repository uses GitHub Actions to automate the CI/CD process. When changes are pushed to the main branch, the workflow defined in .github/workflows/cicd.yml will run the unit tests, and if they pass, deploy the code to production.
Testing

This repository includes unit tests to verify the functionality of the client and server scripts. To run the tests, simply run python -m unittest discover while in the virtual environment.