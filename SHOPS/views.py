from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request, 'SHOPS/basic.html')


def About(request):
    return render(request, 'SHOPS/About.html')


def Contact(request):
    return render(request, 'SHOPS/Contact.html')


def login(request):
    return render(request, 'SHOPS/login.html')


def Signup(request):
    return render(request, 'SHOPS/SignUp.html')


def TrackOrder(request):
    return render(request, 'SHOPS/TrackOrder.html')


def Addtocart(request):
    return render(request, 'SHOPS/Addtocart.html')


def Authorization(request):
    agent = True
    paramerter={'value1': agent}
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['Finame']
        lname = request.POST['lasname']
        email = request.POST['Email']
        pass1 = request.POST['Pass1']
        pass2 = request.POST['Pass2']

        if '@' not in username:
            agent =False
            
            return redirect("signup", paramerter)
        if pass1 != pass2:
            raise ValueError("Password do matched.")
        myuser = User.objects.create_user(username, email, pass1)
        myuser = User.first_name = fname
        myuser = User.last_name = lname
        myuser.save()

        return redirect("Home")
    else:
        return HttpResponse("404 Error")


def handeLogin(request):
    if request.method == "POST":
        # Get the post parameters
        loginusername = request.POST['username']
        loginpassword = request.POST['pass1']

        user = authenticate(username=loginusername, password=loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("home")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("home")

    return HttpResponse("login")


def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('home')
