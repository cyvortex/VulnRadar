import requests
from core.utils import build_url
from modules.report import add_finding

headers = {
    "User-Agent": "Mozilla/5.0 (VulnRadar Security Scanner)"
}

def check_headers(target):

    print("\n[+] Checking Security Headers...")

    url = build_url(target)

    try:

        response = requests.get(url, headers=headers, timeout=10)

        response_headers = response.headers

        if "X-Frame-Options" not in response_headers:
            print("Missing Header: X-Frame-Options")
            add_finding("Missing X-Frame-Options", "Medium")

        if "Content-Security-Policy" not in response_headers:
            print("Missing Header: Content-Security-Policy")
            add_finding("Missing Content-Security-Policy", "Medium")

        if "Strict-Transport-Security" not in response_headers:
            print("Missing Header: Strict-Transport-Security")
            add_finding("Missing Strict-Transport-Security", "Medium")

    except Exception as e:

        print("Header check failed:", e)
