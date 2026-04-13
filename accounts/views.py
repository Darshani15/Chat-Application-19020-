from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


# ---------------- LOGIN ----------------
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        print("LOGIN ATTEMPT:", username, password)

        user = authenticate(request, username=username, password=password)

        print("AUTH RESULT:", user)

        if user is not None:
            login(request, user)
            return redirect("/chat/")
        else:
            return render(request, "login.html", {
                "error": "Invalid username or password"
            })

    return render(request, "login.html")


# ---------------- REGISTER ----------------
def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        print("REGISTER:", username)

        # check user exists
        if User.objects.filter(username=username).exists():
            return render(request, "register.html", {
                "error": "User already exists"
            })

        # create user properly (IMPORTANT FIX)
        user = User.objects.create_user(username=username)
        user.set_password(password)   # 🔥 FIX PASSWORD ENCRYPTION
        user.save()

        print("USER CREATED:", username)

        return redirect("/login/")

    return render(request, "register.html")


# ---------------- LOGOUT ----------------
def logout_view(request):
    logout(request)
    return redirect("/login/")