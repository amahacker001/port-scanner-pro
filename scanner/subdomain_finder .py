import requests
from utils.file_writer import save_result

def find_subdomains(domain):
    print("\nFinding subdomains...\n")

    with open("wordlists/subdomains.txt") as f:
        subs = f.read().splitlines()

    for sub in subs:
        url = f"http://{sub}.{domain}"
        try:
            requests.get(url, timeout=2)
            print(f"[FOUND] {url}")
            save_result(url)
        except:
            pass