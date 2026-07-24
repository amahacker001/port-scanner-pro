import socket
from queue import Queue
import threading

def scan_ports(target, start, end):
    print(f"\nScanning ports {start}-{end} on {target}\n")

    queue = Queue()
    open_ports = []

    def scan(port):
        try:
            sock = socket.socket()
            sock.settimeout(0.5)
            if sock.connect_ex((target, port)) == 0:
                print(f"[OPEN] {port}")
                open_ports.append(port)
            sock.close()
        except:
            pass

    def worker():
        while not queue.empty():
            port = queue.get()
            scan(port)
            queue.task_done()

    for port in range(start, end+1):
        queue.put(port)

    for _ in range(100):
        t = threading.Thread(target=worker)
        t.start()

    queue.join()

    with open("output/results.txt", "w") as f:
        for p in open_ports:
            f.write(str(p) + "\n")

    print("\nDone. Results saved.")