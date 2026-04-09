"""Loyalty points calculation."""

def calculate_points(amount: float, tier: str = "Classic") -> int:
    multiplier = {"Classic": 1, "Silver": 1.5, "Gold": 2, "Platinum": 3}
    return int(amount * multiplier.get(tier, 1))
