from django.contrib import admin
from .models import Restaurant, Review,Feedback,Order,Menu
# Register your models here.
admin.site.register(Restaurant)
admin.site.register(Review)
admin.site.register(Feedback)
admin.site.register(Order)
admin.site.register(Menu)