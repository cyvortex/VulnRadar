#!/usr/bin/env python3

import argparse
from colorama import Fore, Style, init

init()

# Import modules
from modules.portscan import port_scan
from modules.techdetect import detect_technology
from modules.dirscan import directory_scan
from modules.headercheck import check_headers
from modules.sqlscan import sql_scan
from modules.subdomain import subdomain_scan
from modules.xssscan import xss_scan
from modules.report import save_report, report_data
from modules.htmlreport import generate_html_report


print(Fore.CYAN + """
====================================
VulnRadar v1.8
Automated Web Pentesting Framework
Published by CyVortex
====================================
""" + Style.RESET_ALL)


parser = argparse.ArgumentParser(description="VulnRadar Web Security Scanner")

parser.add_argument("-t", "--target", help="Target website or IP")

parser.add_argument("--portscan", action="store_true", help="Quick port scan (1-1000)")
parser.add_argument("--fullports", action="store_true", help="Full port scan (1-65535)")

parser.add_argument("--tech", action="store_true", help="Detect technology")
parser.add_argument("--dirs", action="store_true", help="Directory scan")
parser.add_argument("--headers", action="store_true", help="Security header check")
parser.add_argument("--sql", action="store_true", help="SQL injection test")
parser.add_argument("--subdomains", action="store_true", help="Subdomain discovery")
parser.add_argument("--xss", action="store_true", help="XSS vulnerability test")

parser.add_argument("--fullscan", action="store_true", help="Run all scans")
parser.add_argument("--recon", action="store_true", help="Run reconnaissance scan")

parser.add_argument("--html-report", action="store_true", help="Generate HTML report")

args = parser.parse_args()

target = args.target

if not target:
    print("Please specify a target using -t")
    exit()

report_data["target"] = target


# Quick port scan
if args.portscan:
    port_scan(target)

# Full port scan
if args.fullports:
    port_scan(target, full=True)


# Recon Mode
if args.recon:

    print(Fore.YELLOW + "\n[+] Starting Recon Mode...\n" + Style.RESET_ALL)

    subdomain_scan(target)
    port_scan(target)
    directory_scan(target)
    detect_technology(target)


# Full Scan
if args.fullscan:

    port_scan(target)
    detect_technology(target)
    directory_scan(target)
    check_headers(target)
    sql_scan(target)
    subdomain_scan(target)
    xss_scan(target)


# Individual modules
if args.tech:
    detect_technology(target)

if args.dirs:
    directory_scan(target)

if args.headers:
    check_headers(target)

if args.sql:
    sql_scan(target)

if args.subdomains:
    subdomain_scan(target)

if args.xss:
    xss_scan(target)


# Save JSON report
save_report()


# Generate HTML report
if args.html_report:
    generate_html_report()
