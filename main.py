from scanner.port_scanner import scan_ports
from scanner.web_info import get_web_info
from utils.banner import banner

banner()

target = input("Enter target (domain/IP): ")

print("\n[1] Port Scan")
print("[2] Web Info Scan")

choice = input("Choose option: ")

if choice == "1":
    start = int(input("Start port: "))
    end = int(input("End port: "))
    scan_ports(target, start, end)

elif choice == "2":
    get_web_info(target)

else:
    print("Invalid choice")