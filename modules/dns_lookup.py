import dns.resolver

def run(domain):
    lines = []
    for record in ("A", "MX", "TXT"):
        try:
            answers = dns.resolver.resolve(domain, record)
            lines.append(f"[+] {record} Records:")
            for r in answers:
                lines.append(f"    - {r.to_text()}")
        except Exception:
            lines.append(f"[!] No {record} records found or error.")
    for l in lines:
        print(l)
    return "\n".join(lines)
