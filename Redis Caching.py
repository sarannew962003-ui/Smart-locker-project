import redis
r = redis.Redis()

def get_dynamic_price(locker_id, base_price):
    cached_price = r.get(f"locker_price:{locker_id}")
    if cached_price:
        return float(cached_price)
    multiplier = get_demand_multiplier()
    price = base_price * multiplier
    r.setex(f"locker_price:{locker_id}", 300, price)  # Cache for 5 mins
    return price
