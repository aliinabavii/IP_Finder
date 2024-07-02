import socket
import sys

def get_ip_address():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address

if __name__ == "__main__":
    try:
        while True:
            ip_address = get_ip_address()
            print(f"IP Address of the system: {ip_address}")
            user_input = input("Press 'q' to quit: ")
            if user_input.lower() == 'q':
                break
    except KeyboardInterrupt:
        sys.exit(0)
