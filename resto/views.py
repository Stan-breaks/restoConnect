from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Restaurant, Review, Feedback,Order,Menu
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as auth_login
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/login')
def index(request):
    return render(request, 'resto/index.html', {
        'restaurants': Restaurant.objects.all()
    }) 

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        # Attempt to sign user in
        user = authenticate(request, username=username, password=password)
        # Check if authentication successful
        if user is not None:
            auth_login(request,user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "resto/login.html", {
                "message": "Invalid username and/or password."
            })
    return render(request, 'resto/login.html')

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirmation = request.POST["password2"]
        # Ensure password matches confirmation
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })
        try:
            User.objects.get(username=username)
            return render(request, "resto/register.html", {
                "message": "Username already taken."
            })
        except User.DoesNotExist:
            pass
        # Attempt to create new user
        user = User.objects.create_user(username, email, password)
        user.save()
        auth_login(request, user)
        return HttpResponseRedirect(reverse("index"))
    return render(request, 'resto/register.html')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))

def order(request,resturant_name,order_name):
    if request.method == "POST":
        resturant=Restaurant.objects.get(name=resturant_name)
        user=request.user
        order=Order.objects.create(user=user,restaurant=resturant,order=order_name)
        order.save()
        return JsonResponse({"message": "Order placed successfully."}, status=201)

def orderList(request):
    user=request.user
    orders=Order.objects.filter(user=user)
    return render(request, 'resto/orders.html', {
        'orders': orders,
        'user':user.username,
    })
    
def menu(request,resturant_name):
    resturant=Restaurant.objects.get(name=resturant_name)
    try:
        menu=Menu.objects.filter(restaurant=resturant)
    except Menu.DoesNotExist:
        menu=None
    return render(request, 'resto/menu.html', {
        'menu': menu, 
        'resturant':resturant_name,
    })

def feedback(request):
    if request.method == "POST":
        user=request.user
        text=request.POST["feedback"]
        feedback=Feedback.objects.create(user=user,text=text)
        feedback.save()
        return HttpResponseRedirect(reverse("index"))
    
def empty(request):
        return HttpResponseRedirect(reverse("login"))

def review(request,resturant_name):
    if request.method == "POST":
        user=request.user
        text=request.POST["review"]
        resturant=Restaurant.objects.get(name=resturant_name)
        review=Review.objects.create(user=user,review=text)
        review.save()
        resturant.reviews.add(review)
        return HttpResponseRedirect(reverse("index"))