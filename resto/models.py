from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.TextField()
    def __str__(self):
        return self.review

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    imageUrl = models.CharField(max_length=100)
    dataAlign=models.CharField(max_length=100)
    reviews = models.ManyToManyField(Review, blank=True)
    def __str__(self):
        return self.name

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    def __str__(self):
        return self.text

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    def __str__(self):
        return self.order
