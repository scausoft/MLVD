from django import forms

from web.models import LightGBM

class ContractForm(forms.ModelForm):
    class Meta:
        model = LightGBM
        fields = "__all__"
