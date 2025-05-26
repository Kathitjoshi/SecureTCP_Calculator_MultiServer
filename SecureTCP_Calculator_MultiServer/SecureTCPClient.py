
import ssl
import socket

DEST_IP = input("Enter server IP (default 127.0.0.1): ") or "127.0.0.1"
DEST_PORT = int(input("Enter server port (default 8000): ") or 8000)
BUF_SIZE = 1024

context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

with socket.create_connection((DEST_IP, DEST_PORT)) as sock:
    with context.wrap_socket(sock, server_hostname=DEST_IP) as ssock:
        try:
            while True:
                data = input("Enter operation (e.g. + 2 3) or 'quit': ")
                ssock.sendall(data.encode())
                result = ssock.recv(BUF_SIZE).decode()
                print(f"Result: {result}")
                if data.lower() == 'quit':
                    break
        except KeyboardInterrupt:
            print("\nClient exited.")
