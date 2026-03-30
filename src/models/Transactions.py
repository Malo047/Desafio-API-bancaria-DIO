from datetime import datetime, timezone

class Transaction:
    def __init__(self, type: str, value: float):
        self.type = type
        self.value = value
        self.created_at = datetime.now(timezone.utc)
        