from django.db import models


class Listing(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    price_per_night = models.DecimalField(max_digits=8, decimal_places=2)
    available = models.BooleanField(default=True)


class Booking(models.Model):
    listing = models.ForeignKey(
        Listing, related_name='bookings', on_delete=models.CASCADE)
    guest_name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()


class Review(models.Model):
    listing = models.ForeignKey(
        Listing, related_name='reviews', on_delete=models.CASCADE)
    reviewer_name = models.CharField(max_length=255)
    rating = models.PositiveIntegerField()
    comment = models.TextField()
