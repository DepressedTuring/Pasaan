from django.shortcuts import render

# Create your views here.
def index(request):
    context = {}
    return render(request, "pages/index.html", context)


def about(request):
    context = {}
    return render(request, "pages/about.html", context)


def contact(request):
    context = {}
    return render(request, "pages/contact.html", context)


def water(request):
    context = {}
    return render(request, "pages/water.html", context)


def soil(request):
    context = {}
    return render(request, "pages/soil.html", context)


def technical(request):
    context = {}
    return render(request, "pages/technical.html", context)


def microbiology(request):
    context = {}
    return render(request, "pages/microbiology.html", context)


def services(request):
    context = {}
    return render(request, "pages/services.html", context)


def industrialwaste(request):
    context = {}
    return render(request, "pages/industrialwaste.html", context)