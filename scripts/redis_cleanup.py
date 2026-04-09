"""Cleanup orphaned Redis session keys."""
import redis

def cleanup_orphaned_sessions(host="localhost", port=6379):
    r = redis.Redis(host=host, port=port)
    for key in r.scan_iter("session:*"):
        if r.ttl(key) == -1:
            r.expire(key, 86400)
