from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1> hello world</h1>")

def login(request):
    return HttpResponse ("<h1> login </h1>")

def registration(request):
    return HttpResponse("<h1> Welcome to registration </h1>")