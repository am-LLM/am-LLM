# Global Industrial Cyber Security Professional (GICSP) — ICS/SCADA Security

## 1. Purdue Model for Industrial Control Systems (ISA-95)

```
                            PURDUE MODEL HIERARCHY
 ┌────────────────────────────────────────────────────────────────────────┐
 │ Level 5: Enterprise Network (Corporate ERP, Billing, Internet Access)   │
 ├────────────────────────────────────────────────────────────────────────┤
 │ Level 4: Site Business Operations (Logistics, MES, Plant Management)   │
 ├────────────────────────────────────────────────────────────────────────┤
 │ === INDUSTRIAL DEMILITARIZED ZONE (IDMZ / Layer 3.5: Historians/Jump) ==│
 ├────────────────────────────────────────────────────────────────────────┤
 │ Level 3: Site Operations & Supervisory Control (SCADA HMI, Eng Station)│
 ├────────────────────────────────────────────────────────────────────────┤
 │ Level 2: Area Supervisory Control (Local HMIs, Operator Consoles)      │
 ├────────────────────────────────────────────────────────────────────────┤
 │ Level 1: Basic Process Control (PLCs, RTUs, DCS Controllers, IEDs)     │
 ├────────────────────────────────────────────────────────────────────────┤
 │ Level 0: Physical Process (Sensors, Actuators, Valves, Pumps, Motors)  │
 └────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Industrial Protocols & Deep Packet Inspection (DPI)

### Modbus TCP Architecture
* Modbus TCP operates on port **502**.
* Structure: `MBAP Header (7 bytes) + PDU (Function Code + Data)`.

| Function Code | Name | Operation Type | Risk Level |
|---|---|---|---|
| `0x01` / `0x02` | Read Coils / Discrete Inputs | Read Binary Status | Low |
| `0x03` / `0x04` | Read Holding / Input Registers | Read Analog Values | Low |
| `0x05` / `0x06` | Write Single Coil / Register | Modify Single Physical State | **HIGH** |
| `0x0F` / `0x10` | Write Multiple Coils / Registers | Bulk Process State Override | **CRITICAL** |

### ICS DPI Firewall Rule Requirements:
1. Block all write commands (`FC >= 0x05`) from non-Engineering Workstations.
2. Restrict coil write address ranges to prevent safety valve overrides.
3. Enforce strict Layer 3.5 IDMZ isolation with zero direct Level 4 to Level 2/1 routing.
