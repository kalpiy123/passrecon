import whois

def run(domain):
    try:
        info = whois.whois(domain)
        lines = [
            f"[+] Registrar: {info.registrar}",
            f"[+] Creation Date: {info.creation_date}",
            f"[+] Expiration Date: {info.expiration_date}"
        ]
    except Exception as e:
        lines = [f"[!] WHOIS lookup error: {e}"]
    for l in lines:
        print(l)
    return "\n".join(lines)
