from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.review

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    imageUrl = models.CharField(max_length=500)
    dataAlign=models.CharField(max_length=100)
    reviews = models.ManyToManyField(Review, blank=True)
    def __str__(self):
        return self.name

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.text

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.TextField(default="hhh")
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.order

class Menu(models.Model):
    dataAlign=models.CharField(max_length=100)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    imageUrl = models.CharField(max_length=500)
    def __str__(self):
        return self.name
    