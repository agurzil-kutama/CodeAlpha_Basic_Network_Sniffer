# CodeAlpha_Basic_Network_Sniffer

## 📌 Project Overview
This project was developed as part of the **CodeAlpha Cyber Security Internship** (November 2026). It is a Python-based network sniffer built using the `scapy` library. The tool captures live network traffic on a specified interface and extracts critical information such as Source IP, Destination IP, Protocol (TCP/UDP/ICMP), and raw payload data.

## 🚀 Features
- **Live Packet Capture:** Listens to network traffic on a specified interface.
- **Protocol Analysis:** Identifies TCP, UDP, and ICMP protocols.
- **Payload Extraction:** Captures and displays the raw payload of the packets.
- **Command Line Interface (CLI):** Uses `argparse` to allow the user to specify the network interface and the number of packets to capture.

## 🛠️ Prerequisites
- Python 3.x
- `scapy` library

## 📦 Installation
1. Clone the repository:
   git clone https://github.com/YOUR_USERNAME/CodeAlpha_Basic_Network_Sniffer.git
   cd CodeAlpha_Basic_Network_Sniffer

2. Install the required library (Kali Linux users can use `sudo apt install python3-scapy`):
   pip install -r requirements.txt

## 💻 Usage
**Note:** Capturing network traffic requires root/administrator privileges.

Run the script using `sudo` and specify the network interface (`-i`) and packet count (`-c`):
sudo python3 network_sniffer.py -i eth0 -c 10

*To capture traffic on your own machine for testing, use the loopback interface (`-i lo`).*

## 🖼️ Proof of Concept
![Sniffer Output](screenshots/sniffer_output.png)
![Ping Traffic](screenshots/ping_traffic.png)

## ⚠️ Disclaimer
This tool is created for **educational purposes only** as part of an internship program. Do not use this tool on networks you do not own or have explicit permission to test.

---
**Author:** Adel Boutaghane  
**Internship:** CodeAlpha Cyber Security Intern
