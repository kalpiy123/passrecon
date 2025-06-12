import requests

def run(domain):
    lines = []
    try:
        resp = requests.get(f"https://crt.sh/?q=%25.{domain}&output=json", timeout=10)
        resp.raise_for_status()
        subs = {entry["name_value"].strip() for entry in resp.json()}
        lines.append(f"[+] Found {len(subs)} subdomains:")
        for s in sorted(subs):
            lines.append(f"    - {s}")
    except Exception as e:
        lines = [f"[!] crt.sh lookup error: {e}"]
    for l in lines:
        print(l)
    return "\n".join(lines)
