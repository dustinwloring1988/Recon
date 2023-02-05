# Python Remote Access Client: The Informant

Have you ever wanted to know what your computer is up to while you're away? Say hello to our little informant, the Python Remote Access Client! This script will collect all the juicy details about your computer and send it straight to the boss (aka the server). The project uses a `.env` file to store sensitive information such as database credentials. Because we don't want any hackers (or your boss) to know your secrets.

## Requirements
- Python 3.9 or higher: Because we only work with the best.
- MariaDB: Because databases are like diaries, they keep all your secrets safe.

## Usage
- Run the `server.py` script on the server machine to collect information from the client like a spy.
- Run the `client.py` script on the client machine to report information to the server like a spy with a code. 

## Docker Deployment
The project includes a `docker-compose.yml` file for deploying the server and MariaDB services using Docker. So, even if the CIA (or your boss) tries to spy on you, they'll have a tough time cracking into your Docker containers. 

## How Dose This Work
The server.py script acts as a server that collects information from multiple clients running the client.py script. The client.py script gathers information about the computer it is running on, such as the current IP address, the current user, and the list of other users on the computer.

The server.py script then receives this information from each client and stores it in a MariaDB database. The database stores information about the computer, the current user, and the list of other users. The server also provides an API for querying this information.

The client.py script uses the subprocess module to gather information about the computer it is running on. This information is then sent to the server using the requests library, which makes an HTTP request to the server's API.

By using a combination of the client.py and server.py scripts, you can gather information about multiple computers in one centralized location. The use of the MariaDB database and the API provided by the server makes it easy to query and analyze this information.

The docker-compose file provides a way to easily set up and run the MariaDB database and the server.py script in a Docker container. The use of a Docker container ensures that the environment is consistent and reproducible, no matter where the container is run. Additionally, the use of a .env file makes it easy to configure the database connection details and other parameters.

## Git Ignore
The project includes a `.gitignore` file to ignore common files and directories generated during development. Because sometimes, we all have a bad hair day and we don't want anyone to see it (or in this case, our generated files).

## Contributing
Feel free to contribute to this project by submitting pull requests or reporting issues. Together, we can create the most informative and humorous Python Remote Access Client in the world!
