from django.urls import path

from .views import MainPageView, AssetListView, CreateAssetView
from . import views

urlpatterns = [
    path('main', MainPageView.as_view(), name="main"),
    path('upload/', views.upload, name='upload'),
    path('assets/', AssetListView.as_view(), name='asset_list'),
    path('assets/create/', CreateAssetView.as_view(), name='create_asset'),

]