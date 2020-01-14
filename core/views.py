from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView, UpdateView
from .models import Asset
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
import os
from pymediainfo import MediaInfo
from django.conf import settings


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

def delete_asset(request,pk):
    if request.method == 'POST':
        asset = Asset.objects.get(pk=pk)
        asset.delete()
    return redirect('asset_list')

class MainPageView(TemplateView):
    template_name = 'main.html'

class UploadAssetView(CreateView):
    model = Asset
    fields = ('filename', 'file', 'data')
    # form_class= AssetForm
    success_url = reverse_lazy('asset_list')
    template_name = 'create_asset.html'

    def parse_mediainfo(self, file):
        mediadir = os.path.join(settings.BASE_DIR, 'core\\assets\\')
        mediainfo = MediaInfo.parse(str(mediadir)+str(file))
        # print(mediainfo.to_json())
        media_json = mediainfo.to_json()
        return media_json

    def form_valid(self, form):
        base = str(form.instance.file)
        base_wo_ext = os.path.splitext(base)[0]
        form.instance.filename = base_wo_ext

        # call super in order to avaoid runtime error (file noot fully sent ?)
        super(UploadAssetView, self).form_valid(form)
        json_data = self.parse_mediainfo(form.instance.file)
        form.instance.data = json_data
        response = super(UploadAssetView, self).form_valid(form)
        return response


class AssetListView(ListView):
    model = Asset
    template_name = 'asset_list.html'
    context_object_name = 'assets'


class AssetUpdateView(UpdateView):
    model = Asset
    fields = ('filename', 'file', 'data')
    template_name = 'update_asset.html'
    success_url = reverse_lazy('asset_list')


        

