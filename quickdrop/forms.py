from django import forms
from .models import TempNote

class NoteForm(forms.ModelForm):
    days = forms.IntegerField(min_value=0, initial=0, required=False, label="Days")
    hours = forms.IntegerField(min_value=0, initial=0, required=False, label="Hours")
    minutes = forms.IntegerField(min_value=0, initial=1, required=False, label="Minutes")

    class Meta:
        model = TempNote
        fields = ['title', 'content']