# from scapy.all import sniff, TCP, IP
# import pyshark

# def analyze_packet(packet):
#     """
#     Analyzes SSL/TLS packets to identify handshake steps and other information.
#     """
#     try:
#         # Filter out SSL/TLS packets based on port (usually 443)
#         if packet.haslayer(TCP) and packet[TCP].dport == 443 or packet[TCP].sport == 443:
#             # Print basic packet information
#             print(f"Source IP: {packet[IP].src}")
#             print(f"Destination IP: {packet[IP].dst}")
#             print(f"Source Port: {packet[TCP].sport}")
#             print(f"Destination Port: {packet[TCP].dport}")

#             # Check if it's a handshake step based on the packet load
#             if packet.haslayer("Raw"):
#                 load = packet["Raw"].load
#                 if b"ClientHello" in load:
#                     print("Detected ClientHello")
#                 elif b"ServerHello" in load:
#                     print("Detected ServerHello")
#                 elif b"Certificate" in load:
#                     print("Detected Certificate Transmission")
#                 elif b"Finished" in load:
#                     print("Detected Finished Message")
#                 else:
#                     print("Detected Other TLS Packet")

#             print("-" * 50)

#     except Exception as e:
#         print(f"Error analyzing packet: {e}")

# def capture_packets():
#     """
#     Captures packets on a network interface, filtering for SSL/TLS (port 443).
#     """
#     print("Starting packet capture...")
#     sniff(filter="tcp port 443", prn=analyze_packet, store=0)

# def capture_with_pyshark():
#     """
#     Uses Pyshark to capture and analyze packets with TLS layers.
#     """
#     print("Starting capture with Pyshark...")
#     capture = pyshark.LiveCapture(interface='eth0', display_filter='tls')

#     for packet in capture.sniff_continuously():
#         try:
#             # Only analyze packets with TLS layers
#             if 'tls' in packet:
#                 print("TLS Packet Detected:")
#                 print(f"Packet Number: {packet.number}")
#                 print(f"Source IP: {packet.ip.src}")
#                 print(f"Destination IP: {packet.ip.dst}")
#                 print(f"TLS Layer Info: {packet.tls}")
#                 print("-" * 50)
#         except AttributeError:
#             continue

# if __name__ == "__main__":
#     # Uncomment one of these functions based on your choice of packet analysis tool
#     # capture_packets() # Use scapy for packet capture
#     # OR
#     capture_with_pyshark() # Use pyshark for advanced filtering


# from scapy.all import sniff, TLS

# def analyze_tls_packets(packet):
#     if packet.haslayer(TLS):
#         tls_layer = packet[TLS]
#         print("TLS Packet Summary:")
#         print(f"Version: {tls_layer.version}")
#         print(f"Cipher Suite: {tls_layer.cipher_suite}")

# sniff(filter="tcp port 8443", prn=analyze_tls_packets, count=10)

