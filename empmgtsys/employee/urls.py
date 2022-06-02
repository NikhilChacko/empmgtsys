from django.urls import path
from employee import views
urlpatterns = [

    path('index', views.Indexview.as_view()),     #**
    path("login", views.Loginview.as_view()),	#**
    path("signup",views.Signupview.as_view())	#**
]