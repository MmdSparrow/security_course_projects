import pyshark

def capture_tls_packets():
    capture = pyshark.LiveCapture(interface='any', bpf_filter='tcp port 8585')
    print("Capturing packets...")

    for packet in capture.sniff_continuously(packet_count=10):
        if 'TLS' in packet:
            print("TLS Packet Detected:")
            print(f"Version: {packet.tls.record_version}")
            print(f"Cipher: {packet.tls.record_cipher_suites}")
            print(f"Length: {packet.tls.record_length}")
        else:
            print("Non-TLS Packet Detected:", packet)

capture_tls_packets()
