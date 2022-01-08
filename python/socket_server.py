"""Socket server. Run this before socket client."""

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 9999))
s.listen()
print("Listening...")

while True:
    client, address=s.accept()
    print("Connected to {}".format(address))
    message = "Hello Client!"
    client.send(message.encode('ascii'))
    client.close()
