import socket
import threading
from queue import Queue
from datetime import datetime
from utils import banner
from config import THREADS

banner()

target = input("Enter target (IP/domain): ")
start_port = int(input("Start port: "))
end_port = int(input("End port: "))

print(f"\nScanning {target} from port {start_port} to {end_port}")
print(f"Started at: {datetime.now()}\n")

queue = Queue()
open_ports = []

def scan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)

        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"[OPEN] Port {port}")
            open_ports.append(port)

        sock.close()
    except:
        pass

def worker():
    while not queue.empty():
        port = queue.get()
        scan(port)
        queue.task_done()

for port in range(start_port, end_port + 1):
    queue.put(port)

threads = []

for _ in range(THREADS):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)

for t in threads:
    t.join()

# Save results
with open("results.txt", "w") as f:
    for port in open_ports:
        f.write(f"{port}\n")

print("\nScan complete!")
print(f"Open ports: {open_ports}")
print("Results saved to results.txt")