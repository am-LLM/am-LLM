# GICSP ICS/SCADA Security Architecture & Industrial Protocols
**Author**: Ali Malik (`@am-LLM`)  
**Scope**: GIAC GICSP, Purdue Model (ISA-95/IEC 62443), Modbus TCP, DNP3, and Safety Instrumented Systems (SIS).

---

## 1. The Purdue Enterprise Reference Architecture (ISA-95)

* **Level 0 (Physical Process)**: Sensors, actuators, pumps, transformers.
* **Level 1 (Direct Control)**: PLCs, RTUs, IEDs, drive controllers.
* **Level 2 (Plant Supervisory Control)**: HMI, Engineering Workstations, SCADA software.
* **Level 3 (Manufacturing Operations)**: Historians, domain controllers, patch management.
* **Industrial DMZ (IDMZ - Level 3.5)**: Jumphosts, data diodes, dual-homed historians separating IT and OT.
* **Level 4/5 (Enterprise IT)**: ERP, Corporate LAN, Internet access.

---

## 2. Modbus TCP Protocol Security Anomalies

Modbus TCP (Port 502) has no built-in encryption or authentication. Critical attacks include unauthorized Function Code `0x05` (Write Single Coil) or `0x10` (Write Multiple Registers).
