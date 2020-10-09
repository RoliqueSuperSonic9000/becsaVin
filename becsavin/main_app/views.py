from django.shortcuts import render

# from django.http import HttpResponse

# Create your views here.


# def index(request):
#   return HttpResponse("Hello! c'est la page d'index de cette main_app.")


def index(request):
    return render(request, "main_app/index.html")


def carousel(request):
    return render(request, "main_app/carousel.html")


def plan(request):
    return render(request, "main_app/plan.html")


def caviste(request):
    return render(request, "main_app/caviste.html")


def commentaires(request):
    return render(request, "main_app/commentaires.html")


def bistrot(request):
    return render(request, "main_app/bistrot.html")


def baravin(request):
    return render(request, "main_app/baravin.html")


def partenaires(request):
    return render(request, "main_app/partenaires.html")


def propos(request):
    return render(request, "main_app/propos.html")