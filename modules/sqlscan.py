import requests
from core.utils import build_url
from modules.report import add_finding

headers = {
    "User-Agent": "Mozilla/5.0 (VulnRadar Security Scanner)"
}

def sql_scan(target):

    print("\n[+] Testing for Basic SQL Injection...")

    payload = "'"

    base_url = build_url(target)

    test_url = base_url + "/?id=" + payload

    try:

        response = requests.get(test_url, headers=headers, timeout=10)

        errors = [
            "sql syntax",
            "mysql",
            "syntax error",
            "database error",
            "warning"
        ]

        for error in errors:

            if error in response.text.lower():

                print("Possible SQL Injection vulnerability detected")
                add_finding("Possible SQL Injection", "High")

                return

        print("No SQL Injection indicators found")

    except Exception as e:

        print("SQL test failed:", e)
