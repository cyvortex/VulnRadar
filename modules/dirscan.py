import requests
import concurrent.futures
from core.utils import DIRECTORY_WORDLIST, file_exists


def directory_scan(target):

    print("\n[+] Starting Directory Brute Force (Multi-threaded)...")

    if not file_exists(DIRECTORY_WORDLIST):
        print("Wordlist not found")
        return

    try:
        with open(DIRECTORY_WORDLIST, "r") as f:
            directories = f.read().splitlines()
    except:
        print("Failed to load wordlist")
        return

    if not target.startswith("http"):
        target = "http://" + target

    def scan_dir(directory):
        url = f"{target}/{directory}"

        try:
            response = requests.get(url, timeout=3)

            if response.status_code == 200:
                print(f"Found: {url}")

        except:
            pass

    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        executor.map(scan_dir, directories)
