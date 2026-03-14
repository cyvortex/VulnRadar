import dns.resolver
from concurrent.futures import ThreadPoolExecutor
from modules.report import add_finding


resolver = dns.resolver.Resolver()
resolver.timeout = 3
resolver.lifetime = 3


def check_subdomain(target, sub):

    domain = f"{sub}.{target}"

    try:
        dns.resolver.resolve(domain, "A")

        print("Found:", domain)

        add_finding(f"Discovered subdomain {domain}", "Info")

    except:
        pass


def subdomain_scan(target):

    print("\n[+] Starting Wordlist Subdomain Discovery...\n")

    try:
        with open("wordlists/subdomains.txt") as f:
            subs = f.read().splitlines()

    except:
        print("Subdomain wordlist not found")
        return


    with ThreadPoolExecutor(max_workers=80) as executor:

        for sub in subs:
            executor.submit(check_subdomain, target, sub)
