from django import forms
from webapp.models import UserData

class CollectData(forms.ModelForm):
    class Meta:
        model = UserData
        fields = '__all__' # renders all the field 
        widgets = {
        'Gender': forms.Select(attrs={'class': 'form-control'})
        }