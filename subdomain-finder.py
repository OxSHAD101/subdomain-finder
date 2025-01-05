import requests
import argparse
import re

def fetch_subdomains(domain):
    subdomains = set()
    try:
        # Example using a public subdomain enumeration API (replace with actual implementation)
        response = requests.get(f"https://crt.sh/?q=%25.{domain}&output=json")
        if response.status_code == 200:
            data = response.json()
            for entry in data:
                name = entry.get('name_value')
                if name:
                    subdomains.update(name.split('\n'))
        else:
            print(f"[!] Failed to fetch subdomains from crt.sh for {domain}.")
    except Exception as e:
        print(f"[!] Error fetching subdomains: {e}")
    return subdomains

def write_to_file(subdomains, output_file):
    try:
        with open(output_file, 'w') as f:
            for subdomain in sorted(subdomains):
                f.write(f"{subdomain}\n")
        print(f"[+] Subdomains saved to {output_file}")
    except Exception as e:
        print(f"[!] Error writing to file: {e}")

def main():
    parser = argparse.ArgumentParser(description="Simple Subdomain Finder Tool")
    parser.add_argument("-d", "--domain", required=True, help="Target domain to find subdomains for")
    parser.add_argument("-o", "--output", default="subdomains.txt", help="Output file to save subdomains")
    args = parser.parse_args()

    print(f"[+] Finding subdomains for {args.domain}...")
    subdomains = fetch_subdomains(args.domain)

    if subdomains:
        print(f"[+] Found {len(subdomains)} subdomains.")
        write_to_file(subdomains, args.output)
    else:
        print("[!] No subdomains found.")

if __name__ == "__main__":
    main()
