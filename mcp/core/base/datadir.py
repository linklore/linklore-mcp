"""Marks the data directory as non-code for scans and file anchors."""
DATA_DIR_NAME = ".linklore"
DATA_DIR_NAMES: tuple[str, ...] = (DATA_DIR_NAME,)
DATA_DIR_PREFIXES: tuple[str, ...] = tuple(f"{d}/" for d in DATA_DIR_NAMES)
