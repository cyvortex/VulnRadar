import dns.resolver
from core.utils import SUBDOMAIN_WORDLIST, file_exists


def subdomain_scan(target):

    print("\n[+] Starting Wordlist Subdomain Discovery...")

    if not file_exists(SUBDOMAIN_WORDLIST):
        print("Subdomain wordlist not found")
        return

    try:
        with open(SUBDOMAIN_WORDLIST, "r") as f:
            subdomains = f.read().splitlines()
    except:
        print("Failed to load wordlist")
        return

    found = []

    for sub in subdomains:
        domain = f"{sub}.{target}"

        try:
            dns.resolver.resolve(domain, "A")
            print(f"Found: {domain}")
            found.append(domain)

        except:
            pass

    return found
