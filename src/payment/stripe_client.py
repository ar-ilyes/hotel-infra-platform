"""Stripe payment processing client."""

class StripeClient:
    def __init__(self, api_key: str):
        self.api_key = api_key

    def charge(self, amount: float, currency: str = "EUR"):
        return {"status": "success", "amount": amount}
