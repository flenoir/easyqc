from django.urls import path

from .views import MainPageView, AssetListView, UploadAssetView, AssetUpdateView
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('main', MainPageView.as_view(), name="main"),
    # path('upload/', views.upload, name='upload'),
    path('assets/', AssetListView.as_view(), name='asset_list'),
    path('assets/create/', UploadAssetView.as_view(), name='create_asset'),
    path('assets/update/<uuid:pk>', AssetUpdateView.as_view(), name='update_asset'),
    path('assets/<uuid:pk>', views.delete_asset, name='delete_asset'),

]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)