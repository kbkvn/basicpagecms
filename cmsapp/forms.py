from django import forms
from .models import PageData

class PageDataForm(forms.ModelForm):
    class Meta:
        model =PageData
        fields = ['title', 'message']
        widgets = {
            "title": forms.TextInput(attrs={'class':'form-control', 'style': 'background-color: #fcfbff; border-radius: 0px; margin-bottom: 10px; margin-left: 10px; !important; min-width: 385px; max-width: 400px; margin-left: 25% !important; font-size: 14px;', 'placeholder':'Enter the title for the page'}),
            "message": forms.TextInput(attrs={'class':'form-control', 'style': 'background-color: #fcfbff; border-radius: 0px; margin-bottom: 10px; margin-left: 10px; !important; min-width: 385px; max-width: 400px; margin-left: 25% !important; font-size: 14px;', 'placeholder':'Enter any updates or messages'}),
        }
        labels = {
            "title": "Title",
            "message": "Message",
        }
