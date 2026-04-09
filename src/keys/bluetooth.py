"""Bluetooth digital key for room access."""

def generate_ble_key(room_id: str, guest_id: str, duration_hours: int = 24):
    """Generate a temporary BLE key for room access."""
    return {"key_id": "abc123", "expires_in": duration_hours * 3600}
