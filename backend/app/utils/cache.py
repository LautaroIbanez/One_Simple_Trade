import time
from typing import Any, Dict, Tuple


class InMemoryTTLCache:
    def __init__(self) -> None:
        self._store: Dict[str, Tuple[float, Any]] = {}

    def get(self, key: str) -> Any | None:
        now = time.time()
        entry = self._store.get(key)
        if not entry:
            return None
        expires_at, value = entry
        if now >= expires_at:
            self._store.pop(key, None)
            return None
        return value

    def set(self, key: str, value: Any, ttl_seconds: int) -> None:
        self._store[key] = (time.time() + ttl_seconds, value)

    def clear(self) -> None:
        self._store.clear()


cache = InMemoryTTLCache()


