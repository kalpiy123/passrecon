#!/usr/bin/env python3

import argparse
from modules import whois_lookup, dns_lookup, ip_lookup, crtsh_lookup, reverse_dns, tor_exit_check
from modules.utils import print_section

def banner():
    print(r"""
   ____   __   ____  _____ ____   ____   ____   _____
  / ___| / _| |  _ \| ____|  _ \ / ___| / ___| | ____|
 | |    | |_  | |_) |  _| | |_) | |     \___ \ |  _|
 | |___ |  _| |  __/| |___|  _ <| |___   ___) || |___
  \____||_|   |_|   |_____|_| \_\\____| |____/ |_____|

      Passive Recon CLI Tool v1.0
""")

def main():
    banner()
    parser = argparse.ArgumentParser(description="PASSRECON: passive recon tool")
    parser.add_argument("--target", required=True, help="Target domain (e.g. example.com)")
    parser.add_argument("--output", help="Save full report to file")
    args = parser.parse_args()

    domain = args.target.strip()
    report = []

    # WHOIS
    print_section("WHOIS LOOKUP")
    whois_text = whois_lookup.run(domain)
    report.append(whois_text)

    # DNS
    print_section("DNS LOOKUP")
    dns_text = dns_lookup.run(domain)
    report.append(dns_text)

    # IP Lookup
    print_section("IP LOOKUP")
    ip_text, ip = ip_lookup.run(domain)
    report.append(ip_text)

    # CRT.sh subdomains
    print_section("CRT.SH SUBDOMAINS")
    crt_text = crtsh_lookup.run(domain)
    report.append(crt_text)

    # Reverse DNS
    if ip:
        print_section("REVERSE DNS")
        rd_text = reverse_dns.run(ip)
        report.append(rd_text)

        # TOR exit check
        print_section("TOR EXIT CHECK")
        tor_text = tor_exit_check.run(ip)
        report.append(tor_text)

    print("\n[+] Recon complete.")

    if args.output:
        with open(args.output, "w") as f:
            f.write("\n\n".join(report))
        print(f"[+] Full report saved to {args.output}")

if __name__ == "__main__":
    main()
