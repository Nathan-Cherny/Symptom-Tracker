from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("report/", views.report, name="report"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("callback/", views.callback, name="callback"),
]
