import socket, requests

def run(domain):
    lines = []
    ip = None
    try:
        ip = socket.gethostbyname(domain)
        lines.append(f"[+] Resolved IP: {ip}")
        data = requests.get(f"https://ipinfo.io/{ip}/json", timeout=10).json()
        for key in ("org", "city", "region", "country", "asn"):
            if key in data:
                lines.append(f"[+] {key.upper()}: {data[key]}")
    except Exception as e:
        lines.append(f"[!] IP lookup error: {e}")
    for l in lines:
        print(l)
    return "\n".join(lines), ip
