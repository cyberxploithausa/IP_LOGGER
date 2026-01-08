#!/usr/bin/env python3

import argparse
import requests

APIS = [
    #requires an api key
    #("ipwho", "https://api.ipwho.org/ip/{ip}"),
    ("ip-api", "http://ip-api.com/json/{ip}"),
    ("reallyfreegeoip", "https://reallyfreegeoip.org/json/{ip}"),
    #Broke ah api end point response dont wanna fix it
    #("geojs", "https://get.geojs.io/v1/ip/geo.json?ip={ip}"),
    ("apip", "https://apip.cc/api-json/{ip}")
]


def geo_lookup(ip: str) -> None:
    print(f"\n[+] Running GeoIP lookup for {ip}")
    print("=" * 50)

    for name, url in APIS:
        print(f"\n[*] Querying {name}")
        print("-" * 40)

        try:
            r = requests.get(url.format(ip=ip), timeout=5)
            r.raise_for_status()

            data = r.json()

            if not isinstance(data, dict):
                print("[-] Unexpected response format")
                continue

            for k, v in data.items():
                print(f"{k:<15}: {v}")

        except requests.exceptions.RequestException as e:
            print(f"[-] Request failed: {e}")
        except ValueError:
            print("[-] Invalid JSON response")
        except Exception as e:
            print(f"[-] Error: {e}")


def main():
    parser = argparse.ArgumentParser(
        description="Run multiple no-key GeoIP APIs against a single IP"
    )
    parser.add_argument("ip", help="Target IP address")

    args = parser.parse_args()
    geo_lookup(args.ip)


if __name__ == "__main__":
    main()
