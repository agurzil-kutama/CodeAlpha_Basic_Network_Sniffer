#!/usr/bin/env python3
"""
CodeAlpha Cybersecurity Internship - Task 1
Basic Network Sniffer
Author: Adel Boutaghane
"""

import argparse
from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw

def process_packet(packet):
    """Processes and displays information from captured packets."""
    
    # Check if the packet has an IP layer
    if IP in packet:
        ip_layer = packet[IP]
        protocol_name = "Unknown"
        
        # Determine the protocol
        if TCP in packet:
            protocol_name = "TCP"
        elif UDP in packet:
            protocol_name = "UDP"
        elif ICMP in packet:
            protocol_name = "ICMP"

        print(f"\n[+] New Packet Captured:")
        print(f"    Source IP:      {ip_layer.src}")
        print(f"    Destination IP: {ip_layer.dst}")
        print(f"    Protocol:       {protocol_name}")

        # Extract and display payload if it exists
        if packet.haslayer(Raw):
            payload = packet[Raw].load
            try:
                # Try to decode payload as UTF-8 text
                decoded_payload = payload.decode('utf-8', errors='ignore')
                print(f"    Payload:        {decoded_payload[:100]}...") # Truncate for readability
            except Exception:
                print(f"    Payload:        [Binary Data]")
        print("-" * 50)

def main():
    parser = argparse.ArgumentParser(description="Basic Network Sniffer using Scapy")
    parser.add_argument("-i", "--interface", help="Network interface to sniff on (e.g., eth0, Wi-Fi)", default=None)
    parser.add_argument("-c", "--count", help="Number of packets to capture (0 for infinite)", type=int, default=0)
    
    args = parser.parse_args()

    print(f"[*] Starting Network Sniffer...")
    if args.interface:
        print(f"[*] Listening on interface: {args.interface}")
    else:
        print(f"[*] Listening on default interface...")
    print(f"[*] Capture limit: {'Infinite' if args.count == 0 else args.count} packets")
    print(f"[*] Press Ctrl+C to stop.\n")

    try:
        # Start sniffing. store=False keeps memory clean.
        sniff(iface=args.interface, prn=process_packet, store=False, count=args.count)
    except PermissionError:
        print("\n[!] Error: Permission denied. Please run this script as root/administrator.")
    except KeyboardInterrupt:
        print("\n[*] Sniffer stopped by user. Exiting.")

if __name__ == "__main__":
    main()
