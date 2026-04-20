import time

CACHE = {
    "data": [],
    "timestamp": 0
}

CACHE_TTL = 300  # 5 min


def get_cache():
    if time.time() - CACHE["timestamp"] < CACHE_TTL:
        return CACHE["data"]
    return None


def set_cache(data):
    CACHE["data"] = data
    CACHE["timestamp"] = time.time()