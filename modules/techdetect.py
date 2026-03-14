import requests
from core.utils import build_url
from modules.report import report_data

def detect_technology(target):

    print("\n[+] Detecting Web Technology...")

    url = build_url(target)

    try:
        response = requests.get(url, timeout=5)

        headers = response.headers

        if "Server" in headers:
            server = headers["Server"]
            print("Server:", server)

            report_data["server"] = server

    except:
        print("Could not detect technology")
