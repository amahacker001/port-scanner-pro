import socket
from datetime import datetime
from utils import banner

banner()

target = input("Enter target (IP or domain): ")

print("-" * 50)
print(f"Scanning: {target}")
print(f"Started at: {datetime.now()}")
print("-" * 50)

open_ports = []

try:
    for port in range(1, 1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.3)

        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"[OPEN] Port {port}")
            open_ports.append(port)

        sock.close()

    print("\nScan complete!")
    print(f"Open ports: {open_ports}")

except KeyboardInterrupt:
    print("\n[!] Scan stopped")
except socket.gaierror:
    print("[!] Hostname could not be resolved")
except socket.error:
    print("[!] Server not responding")