from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name="home"),

    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),

    path('dashboard/', views.dashboardPage, name="dashboard"),
    path('settings/', views.settingsPage, name="settings"),
]
