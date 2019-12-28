from django.urls import path

from .views import HomePageView, MainPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('main', MainPageView.as_view(), name="main")
]