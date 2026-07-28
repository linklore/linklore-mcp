"""Per-process session pin state."""
_PIN: str = ""


def set_pin(path: str) -> None:
    global _PIN
    _PIN = path


def get_pin() -> str:
    return _PIN


def clear_pin() -> None:
    global _PIN
    _PIN = ""
