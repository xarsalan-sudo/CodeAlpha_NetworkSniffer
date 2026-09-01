from scapy.all import sniff, IP, IPv6, TCP, UDP, Raw

log_file = open("captured_packets.txt", "a")

def process_packet(packet):
    if packet.haslayer(IP) or packet.haslayer(IPv6):
        if packet.haslayer(IP):
            src_ip = packet[IP].src
            dst_ip = packet[IP].dst
            ip_version = "IPv4"
        else:
            src_ip = packet[IPv6].src
            dst_ip = packet[IPv6].dst
            ip_version = "IPv6"

        if packet.haslayer(TCP):
            proto_name = "TCP"
        elif packet.haslayer(UDP):
            proto_name = "UDP"
        else:
            proto_name = "Other"

        output = f"\n[+] {ip_version} Packet Captured\n"
        output += f"    Source IP      : {src_ip}\n"
        output += f"    Destination IP : {dst_ip}\n"
        output += f"    Protocol       : {proto_name}\n"

        if packet.haslayer(Raw):
            payload = packet[Raw].load
            output += f"    Payload (first 50 bytes): {payload[:50]}\n"

        print(output)
        log_file.write(output)

print("[*] Starting Network Sniffer")
print("[*] Capturing 20 packets — browse the web to generate traffic\n")

sniff(prn=process_packet, count=20, timeout=25)

log_file.close()
print("\n[*] Capture complete. Results saved to captured_packets.txt")