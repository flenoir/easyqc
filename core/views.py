from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
from .models import Asset

# Create your views here.

def upload(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        print(uploaded_file.name)
        print(uploaded_file.size)
    return render(request, 'upload.html')

class MainPageView(TemplateView):
    template_name = 'main.html'

class CreateAssetView(CreateView):
    model = Asset
    fields = ('uuid', 'filename', 'file')
    success_url = 'asset_list'
    template_name = 'create_asset.html'


class AssetListView(ListView):
    model = Asset
    template_name = 'asset_list.html'
    context_object_name = 'assets'

