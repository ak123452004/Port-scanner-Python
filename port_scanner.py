import socket
import argparse
from datetime import datetime


def scan_port(target, port, timeout=0.5):
    """
    Check whether a specific TCP port is open.
    Returns True if the port is open, otherwise False.
    """

    try:
        # Create a TCP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Set the maximum time to wait for a connection
        sock.settimeout(timeout)

        # Try to connect to the target and port
        # connect_ex() returns 0 when the connection is successful
        result = sock.connect_ex((target, port))

        # Close the socket after checking the port
        sock.close()

        # Return True if the port is open
        return result == 0

    except socket.error:
        # Return False if a socket/network error occurs
        return False


def port_scanner(target, start_port, end_port):
    """
    Scan a range of TCP ports on the target system.
    """

    # Display the program heading
    print("\n" + "=" * 50)
    print("        PYTHON PORT SCANNER")
    print("=" * 50)

    # Try to convert the hostname into an IP address
    try:
        ip_address = socket.gethostbyname(target)

    except socket.gaierror:
        # Display an error if the hostname cannot be resolved
        print(f"\n[ERROR] Could not resolve hostname: {target}")
        return

    # Display scan information
    print(f"Target   : {target}")
    print(f"IP       : {ip_address}")
    print(f"Port     : {start_port} - {end_port}")
    print(f"Started  : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 50)

    # Create an empty list to store open ports
    open_ports = []

    # Loop through every port in the selected range
    for port in range(start_port, end_port + 1):

        # Show the current port being scanned
        print(f"Scanning port {port}...", end="\r")

        # Check whether the current port is open
        if scan_port(ip_address, port):

            # Add the open port to the list
            open_ports.append(port)

    # Clear the scanning message from the terminal
    print(" " * 50, end="\r")

    # Check if any open ports were found
    if open_ports:

        print("\nOpen Ports:")

        # Display every open port
        for port in open_ports:

            # Try to find the common service name for the port
            try:
                service = socket.getservbyport(port, "tcp")

            except OSError:
                # If the service is not known, display Unknown
                service = "Unknown"

            # Display the port and its service
            print(f"  Port {port:<5} -> {service}")

    else:
        # Display this message if no open ports were found
        print("\nNo open ports found in the selected range.")

    # Display scan completion information
    print("\n" + "-" * 50)
    print(f"Scan completed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 50)


def main():
    """
    Main function of the program.
    Handles command-line arguments.
    """

    # Create an argument parser
    parser = argparse.ArgumentParser(
        description="Beginner-friendly TCP Port Scanner"
    )

    # Add the target argument
    parser.add_argument(
        "target",
        help="Target hostname or IP address"
    )

    # Add the starting port argument
    # Default value is port 1
    parser.add_argument(
        "-s",
        "--start",
        type=int,
        default=1,
        help="Starting port (default: 1)"
    )

    # Add the ending port argument
    # Default value is port 1024
    parser.add_argument(
        "-e",
        "--end",
        type=int,
        default=1024,
        help="Ending port (default: 1024)"
    )

    # Read the arguments entered by the user
    args = parser.parse_args()

    # Check whether the starting port is valid
    if not (1 <= args.start <= 65535):
        print("[ERROR] Start port must be between 1 and 65535.")
        return

    # Check whether the ending port is valid
    if not (1 <= args.end <= 65535):
        print("[ERROR] End port must be between 1 and 65535.")
        return

    # Make sure the starting port is not greater than the ending port
    if args.start > args.end:
        print("[ERROR] Start port cannot be greater than end port.")
        return

    # Start the port scanning process
    port_scanner(args.target, args.start, args.end)


# This condition makes sure main() runs only when
# this file is executed directly.
if __name__ == "__main__":
    main()
