from modules.report import report_data
import os
from datetime import datetime


def generate_html_report():

    os.makedirs("reports", exist_ok=True)

    target = report_data.get("target", "Unknown")
    findings = report_data.get("findings", [])

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    html_content = f"""
<html>
<head>
<title>VulnRadar Security Report</title>

<style>
body {{
    font-family: Arial, sans-serif;
    background: #f4f6f8;
    padding: 30px;
}}

h1 {{
    color: #1f2937;
}}

table {{
    width: 100%;
    border-collapse: collapse;
    margin-top: 20px;
}}

th, td {{
    padding: 12px;
    border: 1px solid #ccc;
}}

th {{
    background: #111827;
    color: white;
}}

.high {{ color: red; font-weight: bold; }}
.medium {{ color: orange; font-weight: bold; }}
.low {{ color: green; font-weight: bold; }}
.info {{ color: blue; font-weight: bold; }}
</style>

</head>

<body>

<h1>VulnRadar Security Report</h1>

<p><b>Target:</b> {target}</p>
<p><b>Generated:</b> {now}</p>

<h2>Findings</h2>

<table>
<tr>
<th>Issue</th>
<th>Severity</th>
</tr>
"""

    for finding in findings:

        severity = finding["severity"].lower()

        html_content += f"""
<tr>
<td>{finding['issue']}</td>
<td class="{severity}">{finding['severity']}</td>
</tr>
"""

    html_content += """
</table>

</body>
</html>
"""

    with open("reports/report.html", "w") as f:
        f.write(html_content)

    print("\n[+] HTML report generated: reports/report.html")
