from django import forms

from .models import Asset

class AssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = ('filename', 'file', 'data')
        # labels = {
        #     'filename': _('nom du fichier'),
        # }
        # help_texts = {
        #     'filename': _('Le nom du fichier'),
        # }
