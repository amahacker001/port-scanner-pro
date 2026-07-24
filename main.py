from utils.report import generate_html_report
from utils.banner import banner
from scanner.port_scanner import scan_ports
from scanner.web_info import get_web_info
from scanner.subdomain_finder import find_subdomains
from scanner.dir_scanner import scan_directories

banner()

target = input("Enter target (domain/IP): ")

print("""
[1] Port Scan
[2] Web Info
[3] Subdomain Finder
[4] Directory Scanner
""")

choice = input("Select option: ")

if choice == "1":
    start = int(input("Start port: "))
    end = int(input("End port: "))
    scan_ports(target, start, end)

elif choice == "2":
    get_web_info(target)

elif choice == "3":
    find_subdomains(target)

elif choice == "4":
    scan_directories(target)

else:
    print("Invalid choice")