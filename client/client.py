# import socket

# # Server configuration
# server_ip = "localhost"
# server_port = 8002
# format = "utf-8"

# # Create a socket object
# CS = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# # Connect to the server
# CS.connect((server_ip, server_port))

# # Read the contents of the file
# with open("data/test.txt", "r") as file:
#     data = file.read()

# # Create a new file with a custom message
# new_file_name = "data_from_server.txt"
# new_file = open(new_file_name, "w")
# new_file.write("This data is from server.py\n")
# new_file.close()

# # Convert the string to bytes
# data_bytes = data.encode(format)

# # Send the bytes over the socket
# CS.send(data_bytes)

# # Close the client socket
# CS.close()

import socket

# Server configuration
Server_ip = "localhost"
Server_port = 8002
FORMAT = "utf-8"

# Create a socket object
CS = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
CS.connect((Server_ip, Server_port))

# Read the contents of the file
with open("data/test.txt", "r") as file:
   data = file.read()

# Convert the string to bytes
data_bytes = data.encode(FORMAT)

# Send the bytes over the socket
CS.send(data_bytes)

# Close the client socket
CS.close()
