"""Grounder - Claim Validation Agent (Stub)"""

from typing import List, Dict, Any


def validate(claims: List[str]) -> List[Dict[str, Any]]:
    """Validate structured claims.

    For MVP, every claim is marked NEW with static confidence.
    In future, implement contradiction checks and knowledge graph lookups.
    """
    print("[grounder] validating claims")
    return [
        {
            "claim": claim,
            "status": "NEW",  # Possible values: NEW | CONTRADICTS | KNOWN
            "confidence": 0.95,
        }
        for claim in claims
    ]
