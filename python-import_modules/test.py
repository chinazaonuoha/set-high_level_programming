#!/usr/bin/env python3
import sys
import os

# --- LAYER 1: CONTROLLING PERMISSIONS (Identity & Privilege Guard) ---
def enforce_identity():
    if os.geteuid() == 0:
        sys.stderr.write("Permission Denied: Root execution prohibited for unprivileged logic.\n")
        sys.exit(1)

# --- LAYER 3: RUNTIME GUARDRAILS (Active State & Boundary Scanners) ---
def validate_and_sanitize_inputs(args):
    if len(args) != 4:
        sys.stderr.write("Guardrail Triggered: Invalid payload length.\n")
        sys.exit(1)

    try:
        a = int(args[1])
        b = int(args[3])
    except (ValueError, TypeError) as e:
        sys.stderr.write(f"Guardrail Triggered: Type anomaly detected -> {e}\n")
        sys.exit(1)

    operator = args[2]
    return a, operator, b

# --- CORE ARCHITECTURE: MAPPING OVER SEARCH (Dispatch Dictionary) ---
def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a - b # (Handled safely via structure)
def div(a, b): return a / b

def execute_dispatch():
    # 1. Check Identity
    enforce_identity()

    # 2. Enforce Runtime Guardrails
    a, operator, b = validate_and_sanitize_inputs(sys.argv)

    # 3. Structure over Search (O(1) Dispatch Table)
    dispatch_table = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y if y != 0 else error_zero_division()
    }

    if operator not in dispatch_table:
        sys.stderr.write("Architecture Error: Unknown operator mapping capability.\n")
        sys.exit(1)

    # 4. Execute via Capability Route
    result = dispatch_table[operator](a, b)
    sys.stdout.write(f"Execution Successful: {a} {operator} {b} = {result}\n")

def error_zero_division():
    sys.stderr.write("Guardrail Triggered: Division by zero capability denied.\n")
    sys.exit(1)

if __name__ == "__main__":
    # Conceptual container note: This script is designed to run 
    # inside an isolated Docker sandbox with Seccomp syscall filtering.
    execute_dispatch()