# farkli websitelerin yollar
from django.urls import path

from . import views

urlpatterns = [
    # siteye ilk girdiğimiz zaman direk olarak index.html sayfasına gitmesi için emir vermiş olduk.
    path("<int:id>", views.index, name="index"),
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("create/", views.create, name="create"),
    path("view/", views.view, name="view"),
    #path("events/", views.all_events, name="list-events"),
    path("about/", views.about, name="about"),
]
