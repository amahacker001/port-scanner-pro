import requests
from utils.file_writer import save_result

def scan_directories(domain):
    print("\nScanning directories...\n")

    with open("wordlists/dirs.txt") as f:
        dirs = f.read().splitlines()

    for d in dirs:
        url = f"http://{domain}/{d}"
        try:
            r = requests.get(url, timeout=2)
            if r.status_code == 200:
                print(f"[FOUND] {url}")
                save_result(url)
        except:
            pass