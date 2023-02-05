# client.py
import socket
import json
import os
import subprocess
import platform
import psutil
from dotenv import load_dotenv

# Load the values from the .env file
load_dotenv()

# Get the values from the environment variables
server_address = os.getenv("SERVER_ADDRESS")
port = int(os.getenv("SERVER_PORT"))

def get_current_user():
    # Get the current user using the 'whoami' command
    result = subprocess.run(['whoami'], stdout=subprocess.PIPE)
    current_user = result.stdout.decode().strip()
    return current_user

def get_other_users():
    # Get a list of all users logged in to the computer using the 'w' command
    result = subprocess.run(['w'], stdout=subprocess.PIPE)
    output = result.stdout.decode().strip().split('\n')
    users = [line.split()[0] for line in output[2:]]
    return users

def get_processes():
    # Get a list of all processes running on the computer using the 'ps -e' command
    result = subprocess.run(['ps', '-e'], stdout=subprocess.PIPE)
    output = result.stdout.decode().strip().split('\n')
    processes = [line.split()[0] for line in output[1:]]
    return processes

# Get the hostname and IP address of the computer
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

# Get the operating system name
operating_system = platform.system()

# Get the current user
current_user = get_current_user()

# Get other users on the computer
other_users = get_other_users()

# Get all the processes running on the computer
processes = get_processes()

# Create a dictionary to store the information
data = {
    "hostname": hostname,
    "ip_address": ip_address,
    "operating_system": operating_system,
    "current_user": current_user,
    "other_users": other_users,
    "processes": processes
}

# Convert the dictionary to a JSON string
data = json.dumps(data).encode()

# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the server
server_address = (server_address, port)
client_socket.connect(server_address)

# Send the data to the server
client_socket.sendall(data)

# Close the socket
client_socket.close()
