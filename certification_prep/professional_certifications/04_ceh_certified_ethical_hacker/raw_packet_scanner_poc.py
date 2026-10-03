#!/usr/bin/env python3
"""
CEH Module: Raw Socket TCP SYN Flag Analyzer
Demonstrates packet header crafting logic and TCP state transitions.
"""

def analyze_tcp_response(tcp_flags_hex: int):
    # Flag bits: FIN=0x01, SYN=0x02, RST=0x04, PSH=0x08, ACK=0x10, URG=0x20
    is_syn = bool(tcp_flags_hex & 0x02)
    is_rst = bool(tcp_flags_hex & 0x04)
    is_ack = bool(tcp_flags_hex & 0x10)

    if is_syn and is_ack:
        return "OPEN (Received SYN-ACK -> Port Listening)"
    elif is_rst:
        return "CLOSED (Received RST -> Port Closed)"
    else:
        return "FILTERED / UNKNOWN (Dropped by Firewall)"

if __name__ == "__main__":
    print("[*] TCP Flag Analysis Tests:")
    print(f"  Flags 0x12 (SYN/ACK): {analyze_tcp_response(0x12)}")
    print(f"  Flags 0x04 (RST):     {analyze_tcp_response(0x04)}")
    print(f"  Flags 0x00 (None):    {analyze_tcp_response(0x00)}")
