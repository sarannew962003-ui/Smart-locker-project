# Locking logic
redis_client.set(f"locker_lock:{locker_id}", user_id, ex=600)
