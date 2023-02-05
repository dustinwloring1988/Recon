import unittest
import socket
import subprocess
import time

class TestClientServerCommunication(unittest.TestCase):
    def test_client_server_communication(self):
        # Start the server script on the server machine
        server = subprocess.Popen(["python", "server.py"])

        # Wait for the server to start up
        time.sleep(2)

        # Start the client script on the client machine
        client = subprocess.Popen(["python", "client.py"])

        # Wait for the client to send its message to the server
        time.sleep(2)

        # Check if the client's message was received by the server
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("127.0.0.1", 8000))
        received = s.recv(1024).decode("utf-8")
        self.assertTrue("client message" in received)

        # Clean up the subprocesses
        client.terminate()
        server.terminate()

if __name__ == '__main__':
    unittest.main()
