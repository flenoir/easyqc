from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
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

class MainPageView(TemplateView):
    template_name = 'main.html'

class UploadAssetView(CreateView):
    model = Asset
    fields = ('filename', 'file')
    # form_class= AssetForm
    success_url = reverse_lazy('asset_list')
    template_name = 'create_asset.html'

    def parse_mediainfo(self, file):
        mediadir = os.path.join(settings.BASE_DIR, 'core\\assets\\')
        mediainfo = MediaInfo.parse(str(mediadir)+str(file))
        for track in mediainfo.tracks:
            print(track)

    def form_valid(self, form):
        # print(self.request.POST)
        base = str(form.instance.file)
        base_wo_ext = os.path.splitext(base)[0]
        form.instance.filename = base_wo_ext
        response = super(UploadAssetView, self).form_valid(form)
        self.parse_mediainfo(form.instance.file)
        return response


class AssetListView(ListView):
    model = Asset
    template_name = 'asset_list.html'
    context_object_name = 'assets'

