from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View

# def index(request):
#
#     return render(request,'index.html')
# def login(request):
#     print(',.,.,.,.,.,.,.,..',request.method) #show the method in terminal
#     print(',.,.,.,.,.,.,.,..', request)  #shows the request in the terminal
#     return render(request, 'login.html')
#
# def registration(request):
#     return render(request, 'register.html')

class Indexview(View):

    def get(self, request):
        return render(request, "index.html")
    def post(selfrequest):
        pass

class Loginview(View):

    def get(self, request):
        return render(request, "login.html")
    def post(selfrequest):
        pass


class Signupview(View):

    def get(self, request):
        return render(request, "register.html")

    def post(selfrequest):
        pass