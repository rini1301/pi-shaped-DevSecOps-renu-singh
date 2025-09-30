from typing import Any

# This module contains a purposely insecure helper for the lab.
# Use of eval() is intentionally shown in the lab. For editor health,
# keep the function small and reachable.

def insecure_process(data: str) -> str:
    """
    Process the input string in an intentionally insecure way for demonstration.
    In production, DO NOT use eval on untrusted input.
    """
    if not data:
        return "no input"

    try:
        # Intentionally insecure: using eval
        return str(eval(data))
    except Exception:
        return "processing error"
