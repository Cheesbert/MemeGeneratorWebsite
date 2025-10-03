from django.urls import path
from . import views

urlpatterns = [
    path("", views.mg_app, name="mg_home"),
    path("", views.mg_app, name="create_meme")
]