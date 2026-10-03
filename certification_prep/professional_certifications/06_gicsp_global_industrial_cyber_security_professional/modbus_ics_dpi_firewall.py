#!/usr/bin/env python3
"""
GICSP Deep Packet Inspection (DPI) SCADA Firewall Engine
Inspects Modbus TCP packets and blocks unauthorized coil write operations in OT environments.
"""

class ModbusDPIFirewall:
    def __init__(self, allowed_read_only: bool = True):
        self.allowed_read_only = allowed_read_only
        self.READ_FUNCTIONS = {0x01, 0x02, 0x03, 0x04}
        self.WRITE_FUNCTIONS = {0x05, 0x06, 0x0F, 0x10}

    def inspect_packet(self, unit_id: int, function_code: int, address: int) -> bool:
        if self.allowed_read_only and function_code in self.WRITE_FUNCTIONS:
            return False  # DROP: Unauthorized write command to PLC
        return True  # PASS

if __name__ == "__main__":
    firewall = ModbusDPIFirewall(allowed_read_only=True)
    packets = [
        {"desc": "Read Holding Registers (0x03)", "unit_id": 1, "fn": 0x03, "addr": 100},
        {"desc": "Force Single Coil Trip (0x05)", "unit_id": 1, "fn": 0x05, "addr": 10},
    ]
    print("[*] GICSP Modbus DPI Firewall Event Log:")
    for p in packets:
        allowed = firewall.inspect_packet(p["unit_id"], p["fn"], p["addr"])
        status = "PASSED" if allowed else "BLOCKED (Unauthorized Write Attempt)"
        print(f"  Packet: {p['desc']:<35} -> Action: {status}")
