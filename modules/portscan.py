import nmap
from modules.report import add_finding


def port_scan(target, full=False):

    scanner = nmap.PortScanner()

    if full:
        ports = "1-65535"
        print("\n[+] Starting Full Port Scan (1-65535)...")
    else:
        ports = "1-1000"
        print("\n[+] Starting Quick Port Scan (1-1000)...")

    try:

        scanner.scan(target, ports, arguments="-sV -T4")

        print("\nOpen Ports:")

        for host in scanner.all_hosts():
            for proto in scanner[host].all_protocols():

                ports = scanner[host][proto].keys()

                for port in ports:

                    service = scanner[host][proto][port]["name"]

                    print(f"{port}/tcp - {service}")

                    add_finding(
                        f"Open port {port} running {service}",
                        "Info"
                    )

    except Exception as e:

        print("Port scan failed:", e)
