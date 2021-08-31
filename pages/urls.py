from django.urls import path

from .views import HomePageView, AboutPageView

app_name = "pages"

urlpatterns = [
    path("about/", AboutPageView.as_view(), name="about"),
    path("", HomePageView.as_view(), name="home"),
]