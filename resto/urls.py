from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('index', views.index, name='index'),
    path('logout/', views.logout_view, name='logout'),
    path('order/<str:resturant_name>/<str:order_name>', views.order, name='order'),
    path('menu/<str:resturant_name>', views.menu, name='menu'),
    path('orderList', views.orderList, name='orderList'),
    path('feedback/', views.feedback, name='feedback'),
]