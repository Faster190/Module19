from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.


def platform(request):
    return render(request, "fourth_task/platform.html")


def games(request):
    all_games = Game.objects.all()
    context = {
        "all_games": all_games
    }
    return render(request, "fourth_task/games.html", context)


def cart(request):
    return render(request, "fourth_task/cart.html")


def registration(request):
    users = Buyer.objects.all()
    context = {}
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        repeat_password = request.POST.get("repeat_password")
        age = request.POST.get("age")
        if password != repeat_password:
            context["error"] = "Пароли не совпадают"
        if int(age) < 18:
            context["error"] = "Вы должны быть старше 18"
        for user in users:
            if username == user.name:
                context["error"] = "Пользователь уже существует"
                break
        if not context:
            Buyer.objects.create(name=username, balance=0, age=age)
            return HttpResponse(f"Приветствуем, {username}!")
    return render(request, "fourth_task/registration_page.html", context)
