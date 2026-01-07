#!/usr/bin/env python3

import argparse
import sys
from geoip2.database import Reader
from geoip2.errors import AddressNotFoundError


def lookup_ip(ip: str, db_path: str) -> None:
    try:
        with Reader(db_path) as reader:
            response = reader.city(ip)

            result = {
                "IP Address": ip,
                "Country": response.country.name,
                "Country Code": response.country.iso_code,
                "City": response.city.name,
                "Region": response.subdivisions.most_specific.name,
                "Postal Code": response.postal.code,
                "Latitude": response.location.latitude,
                "Longitude": response.location.longitude,
                "Time Zone": response.location.time_zone,
            }

            print("\n[+] GeoIP Lookup Result\n" + "-" * 30)
            for key, value in result.items():
                print(f"{key:<15}: {value}")

    except AddressNotFoundError:
        print(f"[-] No geolocation data found for {ip}")
    except FileNotFoundError:
        print(f"[-] Database not found: {db_path}")
    except Exception as e:
        print(f"[!] Error: {e}")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description="Professional GeoIP lookup using MaxMind GeoLite2"
    )
    parser.add_argument("ip", help="Target IP address")
    parser.add_argument(
        "-d",
        "--database",
        default="GeoLite2-City.mmdb",
        help="Path to GeoLite2-City.mmdb",
    )

    args = parser.parse_args()
    lookup_ip(args.ip, args.database)


if __name__ == "__main__":
    main()
