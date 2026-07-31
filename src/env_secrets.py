import os


def get_secret(name: str) -> str | None:
    """Read NAME from env, or from the file at NAME_FILE if that's set (Docker secrets)."""
    file_path = os.getenv(f"{name}_FILE")
    if file_path:
        with open(file_path) as f:
            return f.read().strip()
    return os.getenv(name)
