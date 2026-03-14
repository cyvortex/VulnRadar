# VulnRadar

VulnRadar is an automated web reconnaissance and vulnerability scanning framework.

Developed by CyVortex.

## Features

- Port scanning
- Full port scanning
- Subdomain discovery (20k+ wordlist)
- Directory brute forcing
- Technology detection
- Security header analysis
- SQL injection testing
- XSS vulnerability testing
- HTML vulnerability reports
- Recon mode

## Installation

git clone https://github.com/cyvortex/VulnRadar.git

cd VulnRadar

pip install -r requirements.txt

sudo cp vulnradar.py /usr/local/bin/vulnradar

## Usage

Recon scan

vulnradar -t example.com --recon

Full vulnerability scan

vulnradar -t example.com --fullscan

Full scan with HTML report

vulnradar -t example.com --fullscan --html-report
