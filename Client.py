import socket
import sys

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

# Create socket for server
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# s.bind((HOST, PORT))
address = (HOST, PORT)
s.settimeout(5)

print("Do Ctrl+c to exit the program !!")

# Let's send data through UDP protocol
try:
    while True:
        send_data = input("Type some number to send =>")
        s.sendto(send_data.encode('utf-8'), address)
        print("\n Client Sent : ", send_data, "\n")
        data, address = s.recvfrom(4096)
        print("\n\n 2. Client received : ", data.decode('utf-8'), "\n\n")
        if socket.timeout == 5:
            sys.exit(0)
except KeyboardInterrupt:
    print("exiting server...")
