from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
from .models import Asset
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy


from .forms import AssetForm

# Create your views here.



# def upload(request):
#     if request.method == 'POST':
#         context = {}
#         uploaded_file = request.FILES['document']
#         print(uploaded_file.name)
#         print(uploaded_file.size)
#         fs= FileSystemStorage()
#         name = fs.save(uploaded_file.name, uploaded_file)
#         context['url'] = fs.url(name)
#         return render(request, 'upload.html', context)
#     return render(request, 'upload.html')

class MainPageView(TemplateView):
    template_name = 'main.html'

class UploadAssetView(CreateView):
    model = Asset
    fields = ('uuid', 'filename', 'file')
    # form_class= AssetForm
    success_url = reverse_lazy('asset_list')
    template_name = 'create_asset.html'


class AssetListView(ListView):
    model = Asset
    template_name = 'asset_list.html'
    context_object_name = 'assets'

