import os

# Base directory of the VulnRadar project
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Wordlist directory
WORDLIST_DIR = os.path.join(BASE_DIR, "wordlists")

# Wordlist paths
DIRECTORY_WORDLIST = os.path.join(WORDLIST_DIR, "directories.txt")
SUBDOMAIN_WORDLIST = os.path.join(WORDLIST_DIR, "subdomains.txt")


def file_exists(path):
    return os.path.isfile(path)


def build_url(target):
    """
    Ensures the target has http:// or https://
    """
    if not target.startswith("http"):
        target = "http://" + target
    return target
