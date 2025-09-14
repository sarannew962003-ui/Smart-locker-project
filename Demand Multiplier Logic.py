def get_demand_multiplier():
    now = timezone.now()
    if now.hour in range(18, 22):  # Evening peak
        return 1.5
    elif now.weekday() in [5, 6]:  # Weekend
        return 1.2
    return 1.0
