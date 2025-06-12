import requests

def run(ip):
    try:
        r = requests.get("https://check.torproject.org/exit-addresses", timeout=10)
        ok = f"[+] TOR exit node: {ip}" if ip in r.text else f"[+] Not a TOR exit node: {ip}"
        print(ok)
        return ok
    except Exception as e:
        err = f"[!] TOR check error: {e}"
        print(err)
        return err
