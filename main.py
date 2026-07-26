import argparse
import socket

def scan_target(target):
    print(f"\n[+] Starting scan on: {target}\n")

    try:
        target_ip = socket.gethostbyname(target)
        print(f"[+] Resolved IP: {target_ip}\n")
    except socket.gaierror:
        print("[-] Invalid target")
        return

    ports = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 8080]

    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        result = sock.connect_ex((target_ip, port))

        if result == 0:
            print(f"[OPEN] Port {port}")

        sock.close()

    print("\n[+] Scan finished.\n")


def main():
    parser = argparse.ArgumentParser(description="Port Scanner")

    parser.add_argument(
        "--target",
        type=str,
        required=True,
        help="Target domain or IP (example: google.com)"
    )

    args = parser.parse_args()

    scan_target(args.target)


if __name__ == "__main__":
    main()