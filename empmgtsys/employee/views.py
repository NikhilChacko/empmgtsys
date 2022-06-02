from django.http import HttpResponse
from django.shortcuts import render

def index(request):

    return render(request,'index.html')
def login(request):
    print(',.,.,.,.,.,.,.,..',request.method) #show the method in terminal
    print(',.,.,.,.,.,.,.,..', request)  #shows the request in the terminal
    return render(request, 'login.html')

def registration(request):
    return render(request, 'register.html')