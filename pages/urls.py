from django.urls import path

from .views import HomePageView, MainPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('initial_main', MainPageView.as_view(), name="initial_main")
]