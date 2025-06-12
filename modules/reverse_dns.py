import socket

def run(ip):
    try:
        host = socket.gethostbyaddr(ip)[0]
        line = f"[+] Reverse DNS: {host}"
    except Exception:
        line = "[!] No reverse DNS record found."
    print(line)
    return line
