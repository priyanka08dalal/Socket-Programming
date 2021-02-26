import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

# Create a UDP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Bind the socket to the port
server_address = (HOST, PORT)
s.bind(server_address)
print("Do Ctrl+c to exit the program !!")

try:
    while True:
        send_data = ""
        print("Server is listening on port : {0}".format(PORT))
        data, address = s.recvfrom(4096)

        if data:
            try:
                data_numeric = float(data.decode('utf-8'))
                print("\nServer received: ", data.decode('utf-8'), "\n")
                send_data = data_numeric * data_numeric
            except ValueError as ex:
                send_data = "error: input must be a number"
            s.sendto(str(send_data).encode('utf-8'), address)
            print("Server sent : ", send_data, "\n")
except KeyboardInterrupt:
    print("exiting client...")
