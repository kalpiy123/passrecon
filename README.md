🔍 PASSRECON

This is my very first project and its kind of a mixture of multiple different tools and its pretty powerful Linux-based passive reconnaissance tool designed to extract critical open-source intelligence (OSINT) from domains and IPs — without ever touching the target directly.

# Features
    -WHOIS lookup
    -DNS record enumeration
    -IP Geolocation, ASN, ISP Detection
    -Subdomain Discovery via Certificate Transperency 
    -Reverse DNS lookup
    -TOR Exit Node check

# Installation
	- git clone https://github.com/kalpiy123/passrecon.git
	- cd passrecon
	- pip install -r requirements.txt
	
# Usage 
	-python3 passrecon.py --target example.com --output result.txt

    
