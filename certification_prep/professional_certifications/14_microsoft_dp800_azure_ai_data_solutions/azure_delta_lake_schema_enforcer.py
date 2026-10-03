#!/usr/bin/env python3
"""
Microsoft DP-800: Delta Lake Schema Enforcement & Medallion Pipeline Validator
"""

def validate_silver_record(record: dict, expected_schema: dict) -> bool:
    for field, expected_type in expected_schema.items():
        if field not in record:
            return False
        if not isinstance(record[field], expected_type):
            return False
    return True

if __name__ == "__main__":
    schema = {"id": int, "telemetry": float, "valid": bool}
    sample_bronze = {"id": 101, "telemetry": 42.5, "valid": True}
    is_valid = validate_silver_record(sample_bronze, schema)
    print(f"[*] Azure Delta Lake Schema Validation: {'PASSED (Promote to Silver)' if is_valid else 'FAILED'}")
