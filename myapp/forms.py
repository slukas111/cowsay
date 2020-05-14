from django import forms

class AddTextForm(forms.Form):
    text_input = forms.CharField(widget=forms.Textarea)
