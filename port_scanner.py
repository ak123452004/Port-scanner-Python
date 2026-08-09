#!/usr/bin/env python3

"""
Simple TCP Port Scanner
Author: Ankit Kumar

A beginner-friendly port scanner built using Python's socket module.

Use this tool only on systems you own or have permission to scan.
"""

import socket
import argparse
from datetime import datetime


def scan_port(target, port, timeout=0.5):
    """
    Check whether a TCP port is open.

    Returns:
        True  -> Port is open
        False -> Port is closed
    """

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)

        result = sock.connect_ex((target, port))
        sock.close()

        return result == 0

    except socket.error:
        return False


def scan_ports(target, start_port, end_port):
    """Scan a range of TCP ports."""

    print("\n" + "=" * 50)
    print("          PYTHON PORT SCANNER")
    print("=" * 50)

    print(f"Target : {target}")
    print(f"Ports  : {start_port}-{end_port}")
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 50)

    open_ports = []

    for port in range(start_port, end_port + 1):

        print(f"Scanning port {port}...", end="\r")

        if scan_port(target, port):
            print(f"Port {port:<5} -> OPEN")
            open_ports.append(port)

    print("\n" + "-" * 50)

    if open_ports:
        print("Open Ports:")
        for port in open_ports:
            print(f"  [+] {port}")
    else:
        print("No open ports found.")

    print("-" * 50)
    print("Scan completed.")
    print("=" * 50)


def main():
    """Main program."""

    parser = argparse.ArgumentParser(
        description="Beginner-friendly TCP Port Scanner"
    )

    parser.add_argument(
        "target",
        help="Target hostname or IP address"
    )

    parser.add_argument(
        "-s",
        "--start",
        type=int,
        default=1,
        help="Starting port (default: 1)"
    )

    parser.add_argument(
        "-e",
        "--end",
        type=int,
        default=1024,
        help="Ending port (default: 1024)"
    )

    args = parser.parse_args()

    # Validate port numbers
    if args.start < 1 or args.end > 65535:
        print("Error: Port numbers must be between 1 and 65535.")
        return

    if args.start > args.end:
        print("Error: Starting port must be less than ending port.")
        return

    # Convert hostname to IP address
    try:
        target_ip = socket.gethostbyname(args.target)
    except socket.gaierror:
        print(f"Error: Could not resolve '{args.target}'.")
        return

    print(f"\nResolved {args.target} -> {target_ip}")

    scan_ports(target_ip, args.start, args.end)


if __name__ == "__main__":
    main()
