"""Core Agent Safety Boundary Sentinel implementation."""
import re
from typing import Tuple

class SafetyVerdict:
    def __init__(self, is_safe: bool, category: str, message: str):
        self.is_safe = is_safe
        self.category = category
        self.message = message

class SafetyBoundarySentinel:
    DANGEROUS_INTENTS = [
        ("credential_theft", re.compile(r"(extract|dump|steal|leak)\s+(passwords?|credentials?|private\s+keys?|api\s+keys?)", re.IGNORECASE)),
        ("ddos_attack", re.compile(r"(ddos|flood|syn\s+flood|dos\s+attack)", re.IGNORECASE)),
        ("ransomware", re.compile(r"(encrypt\s+all\s+files|demand\s+ransom|lock\s+filesystem)", re.IGNORECASE))
    ]

    @classmethod
    def evaluate_prompt(cls, prompt: str) -> SafetyVerdict:
        clean = prompt.strip()
        for cat, pat in cls.DANGEROUS_INTENTS:
            if pat.search(clean):
                return SafetyVerdict(False, cat, f"Operation blocked under safety category: {cat}")

        return SafetyVerdict(True, "none", "Prompt cleared safety boundary")
