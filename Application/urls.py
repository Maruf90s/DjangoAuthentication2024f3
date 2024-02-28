from django.urls import path
from . import views
urlpatterns = [
    path("",views.index,name="index"),
    path('signup',views.signup,name="signupp"),
    path("login",views.LOGIN_PRO,name="login"),
    path('success',views.success,name="SUC")
]