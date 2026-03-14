import requests
from core.utils import build_url
from modules.report import add_finding

headers = {
    "User-Agent": "Mozilla/5.0 (VulnRadar Security Scanner)"
}

def xss_scan(target):

    print("\n[+] Testing for Basic XSS...")

    payload = "<script>alert(1)</script>"

    base_url = build_url(target)

    test_url = base_url + "/?q=" + payload

    try:

        response = requests.get(test_url, headers=headers, timeout=10)

        if payload in response.text:

            print("Possible XSS vulnerability detected")
            add_finding("Possible XSS vulnerability", "High")

        else:

            print("No XSS indicators found")

    except Exception as e:

        print("XSS test failed:", e)
