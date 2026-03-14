import requests
from concurrent.futures import ThreadPoolExecutor

def check_directory(target, directory):

    url = "http://" + target + "/" + directory

    try:
        response = requests.get(url, timeout=3)

        if response.status_code == 200:
            print("Found:", url)

    except:
        pass


def directory_scan(target):

    print("\n[+] Starting Directory Brute Force (Multi-threaded)...")

    try:
        with open("wordlists/directories.txt") as f:
            directories = f.read().splitlines()

        with ThreadPoolExecutor(max_workers=10) as executor:
            for directory in directories:
                executor.submit(check_directory, target, directory)

    except:
        print("Wordlist not found")
