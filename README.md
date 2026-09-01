# CodeAlpha Network Sniffer 🕵️‍♂️

A basic Python-based network packet sniffer built using **Scapy**, developed as part of the CodeAlpha Cybersecurity Internship (Task 1).

## 📌 Features
- Captures live network packets in real-time
- Supports both IPv4 and IPv6 traffic
- Identifies source IP, destination IP, and protocol (TCP/UDP)
- Displays payload data (first 50 bytes) when available
- Saves all captured packet details to a log file (`captured_packets.txt`)

## 🛠 Tech Stack
- Python 3.14
- [Scapy](https://scapy.net/) — packet manipulation library

## ⚙️ How to Run

1. Clone this repository
```bash
git clone https://github.com/xarsalan-sudo/CodeAlpha_NetworkSniffer.git
cd CodeAlpha_NetworkSniffer
```

2. Create and activate a virtual environment
```bash
python -m venv myenv
myenv\Scripts\activate      # Windows
source myenv/bin/activate   # Mac/Linux
```

3. Install dependencies
```bash
pip install scapy
```

4. Run the sniffer **as Administrator/root** (required for raw packet capture)
```bash
python sniffer.py
```

## 📖 What I Learned
- How packets flow through a network (Ethernet, IP, TCP/UDP layers)
- The difference between IPv4 and IPv6 addressing
- Why raw packet sniffing requires elevated (admin/root) permissions
- How TLS/HTTPS encrypts payload data for security
- Practical use of Python for network analysis and cybersecurity fundamentals

## ⚠️ Disclaimer
This tool is built strictly for educational purposes as part of the CodeAlpha internship. It should only be used on networks you own or have explicit permission to monitor.

## 👤 Author
**Arsalan Ashraf**
CodeAlpha Cybersecurity Intern