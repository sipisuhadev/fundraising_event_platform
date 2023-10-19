from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('fundraiser/',views.fundraiser,name='fundraiser'),
    path('fundraiser/add/',views.add,name='add'),
    path('logout/',views.logout,name='logout'),
    path('login/',views.login,name="login"),
    path('login/signin/',views.signin,name="signin"),
    path('login/signup/',views.signup,name="signup"),
    path('login/signup/back/',views.back,name="back"),
    path('login/signup/createuser/',views.createuser,name="createuser"),


]