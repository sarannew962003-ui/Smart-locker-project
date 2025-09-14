class Locker(models.Model):
    SIZE_CHOICES = [('S', 'Small'), ('M', 'Medium'), ('L', 'Large')]
    size = models.CharField(max_length=1, choices=SIZE_CHOICES)
    location = models.CharField(max_length=255)
    base_price = models.DecimalField(max_digits=6, decimal_places=2)
    is_occupied = models.BooleanField(default=False)

class Reservation(models.Model):
    STATUS_CHOICES = [('pending', 'Pending'), ('confirmed', 'Confirmed'), ('cancelled', 'Cancelled')]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    locker = models.ForeignKey(Locker, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    total_cost = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firebase_token = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15, blank=True, null=True)