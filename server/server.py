import socket

# Server configuration
server_ip = "localhost"
server_port = 8002
format = "utf-8"

# Create a socket object
SS = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the server IP address and port
SS.bind((server_ip, server_port))

# Listen for incoming connections
SS.listen(5)

# Accept a client connection
sl, addr = SS.accept()

# Receive the file name from the client
file_name = sl.recv(1024).decode(format)
print(file_name)

# Open the file in write mode
file = open(file_name, "w")

# Send a response to the client
response = "File data received"
sl.send(response.encode(format))

# Receive the file data from the client
data = sl.recv(1024).decode(format)
print("File received")

# Write the file data to the file
file.write(data)

# Close the file
file.close()

# Close the client socket
sl.close()

# Close the server socket
SS.close()

# import socket

# # Server configuration
# server_ip = "localhost"
# server_port = 8002
# format = "utf-8"

# # Create a socket object
# SS = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# # Bind the socket to the server IP address and port
# SS.bind((server_ip, server_port))

# # Listen for incoming connections
# SS.listen(5)

# # Accept a client connection
# sl, addr = SS.accept()

# # Receive the file name from the client
# file_name = sl.recv(1024).decode(format)
# print(file_name)

# # Open the file in write mode
# file = open(file_name, "w")

# # Send a response to the client
# response = "File data received"
# sl.send(response.encode(format))

# # Receive the file data from the client
# data = sl.recv(1024).decode(format)
# print("File received")

# # Write the file data to the file
# file.write(data)

# # Close the file
# file.close()

# # Close the client socket
# sl.close()

# # Close the server socket
# SS.close()
