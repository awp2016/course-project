from django.http import HttpResponse


def index(request):
    return HttpResponse("<html><h1>HELLO WORLD</h1></html>")
