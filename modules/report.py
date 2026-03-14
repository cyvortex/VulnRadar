import json
import os

report_data = {
    "target": "",
    "findings": []
}


def add_finding(issue, severity):

    report_data["findings"].append({
        "issue": issue,
        "severity": severity
    })


def save_report():

    os.makedirs("reports", exist_ok=True)

    with open("reports/scan_report.json", "w") as f:
        json.dump(report_data, f, indent=4)

    print("\n[+] Report saved to reports/scan_report.json")
