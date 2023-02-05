# server.py
import mysql.connector
import socket
import json
from dotenv import load_dotenv
import os

# Load the values from the .env file
load_dotenv()

# Get the values from the environment variables
hostname = os.getenv("DB_HOST")
username = os.getenv("DB_USER")
password = os.getenv("DB_PASS")
database = os.getenv("DB_NAME")
server_address = os.getenv("SERVER_ADDRESS")
port = int(os.getenv("SERVER_PORT"))

# Function to receive data from the client
def receive_data(client_socket):
    data = b""
    while True:
        # Receive data in chunks and append it to the data variable
        chunk = client_socket.recv(4096)
        if not chunk:
            break
        data += chunk
    return data

# Function to save the received data to the MariaDB database
def save_to_database(data):
    # Connect to the MariaDB database
    connection = mysql.connector.connect(
        host=hostname,
        user=username,
        password=password,
        database=database
    )
    cursor = connection.cursor()
    # Convert the received data from bytes to a dictionary
    data = json.loads(data.decode())
    # Insert the data into the MariaDB database
    sql = "INSERT INTO client_data (hostname, ip_address, operating_system, current_user, other_users, processes) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (data["hostname"], data["ip_address"], data["operating_system"], data["current_user"], data["other_users"], data["processes"])
    cursor.execute(sql, values)
    connection.commit()
    # Close the cursor and connection to the MariaDB database
    cursor.close()
    connection.close()

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to a specific address and port
server_address = (server_address, port)
server_socket.bind(server_address)
# Listen for incoming connections
server_socket.listen(1)
print("Server is listening for incoming connections...")
while True:
    # Wait for a connection from a client
    client_socket, client_address = server_socket.accept()
    print("Accepted connection from", client_address)
    # Receive data from the client
    data = receive_data(client_socket)
    # Save the received data to the MariaDB database
    save_to_database(data)
    # Close the connection to the client
    client_socket.close()
