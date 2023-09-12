from django.urls import path
from . import views

app_name="home"
urlpatterns = [
    path("",views.home),
    path("login-page",views.login_page, name="login"),
    path("thank-you",views.thank_you, name="thx"),
    path("kitchen",views.kitchen),
    path("washroom",views.washroom),
    path("bathroom",views.bathroom),
    path("elevation",views.elevation),
    path("livingroom",views.livingroom),
    path("bedroom",views.bedroom),
    path("pods",views.pod),
    path("washbasine",views.washbasine),
    path("parking",views.parking),
    path("commercial",views.commercial),
    path("home",views.home),
    path("premiumfloor",views.premiumfloor),
    path("premiumwall",views.premiumwall),
    path("GVT-tiles",views.GVT_tiles),
    path("vitrified-tiles",views.vitrified_tiles),
    path("premiumelevation",views.premiumelevation)
]