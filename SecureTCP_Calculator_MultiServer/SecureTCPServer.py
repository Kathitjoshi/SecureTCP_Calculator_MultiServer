# cmd for ssl to be put in terminal ;opening same folder as both codes is:
# openssl req -new -x509 -days 365 -nodes -out server.crt -keyout server.key

import ssl
import socket
import threading
import logging
import sys

# Default values
DEFAULT_IP = '127.0.0.1'
DEFAULT_PORT = 8000
BUF_SIZE = 1024

CERTFILE = 'server.crt'
KEYFILE = 'server.key'

# Setup logging
logging.basicConfig(filename='server.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# === Core Operation Logic ===
def addNumbers(operator, num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '/':
        if num2 == 0:
            return "Error: Division by zero."
        return num1 / num2
    elif operator == '*':
        return num1 * num2
    elif operator == '%':
        return num1 % num2
    elif operator == '**':
        return num1 ** num2
    return "Error: Invalid operator."

def checkType(value1, value2):
    try:
        int(value1)
        int(value2)
        return True
    except ValueError:
        return False

def doOperations(operator, value1, value2):
    if operator == '+':
        if not checkType(value1, value2):
            return value1 + value2  # String concat
        return addNumbers(operator, value1, value2)
    elif checkType(value1, value2):
        return addNumbers(operator, value1, value2)
    return "Error: Non-numeric values provided."

# === Handle each client in its own thread ===
def handle_client(conn, addr):
    print(f"Connected by {addr}")
    logging.info(f"Connection established with {addr}")
    try:
        while True:
            data = conn.recv(BUF_SIZE)
            if not data:
                break
            message = data.decode().strip()
            if message.lower() == "quit":
                conn.send("Connection closed.".encode())
                break
            parts = message.split(" ")
            if len(parts) != 3:
                result = "Error: Use '<operator> <num1> <num2>'."
            else:
                operator, num1, num2 = parts
                result = doOperations(operator, num1, num2)
            logging.info(f"Operation from {addr}: {data} -> Result: {result}")
            conn.send(str(result).encode())
    except Exception as e:
        print(f"Error with client {addr}: {e}")
        logging.error(f"Error with client {addr}: {e}")
    finally:
        print(f"Connection closed for {addr}")
        logging.info(f"Connection closed for {addr}")
        conn.close()

# === Server Entry Point ===
def main():
    ip = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_IP
    port = int(sys.argv[2]) if len(sys.argv) > 2 else DEFAULT_PORT

    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile=CERTFILE, keyfile=KEYFILE)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        try:
            sock.bind((ip, port))
        except OSError as e:
            print(f"Bind failed on {ip}:{port}: {e}")
            logging.error("Bind failed.")
            return

        sock.listen(5)
        print(f"Server listening on {ip}:{port}")
        logging.info(f"Server started and listening on {ip}:{port}")
        while True:
            client_sock, addr = sock.accept()
            conn = context.wrap_socket(client_sock, server_side=True)
            threading.Thread(target=handle_client, args=(conn, addr), daemon=True).start()

if __name__ == "__main__":
    main()
