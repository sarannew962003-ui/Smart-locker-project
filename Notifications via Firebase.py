def notify_users(locker):
    interested_users = UserProfile.objects.filter(...)  # filter by price interest
    for user in interested_users:
        push_service.notify_single_device(
            registration_id=user.firebase_token,
            message_title="Price Drop Alert!",
            message_body=f"Locker at {locker.location} is now ₹{get_dynamic_price(locker.id)}"
        )
