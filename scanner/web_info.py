import requests

def get_web_info(target):
    try:
        url = f"http://{target}"
        response = requests.get(url)

        print("\n--- Web Info ---")
        print("Status Code:", response.status_code)
        print("Server:", response.headers.get("Server"))

        with open("output/results.txt", "w") as f:
            f.write(f"Status: {response.status_code}\n")
            f.write(f"Server: {response.headers.get('Server')}\n")

    except Exception as e:
        print("Error:", e)