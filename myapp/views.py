from django.shortcuts import render
from myapp.models import TextInput
from myapp.forms import AddTextForm
import subprocess
# Create your views here.

def index(req):
    if req.method == "POST":
        form = AddTextForm(req.POST)

        if form.is_valid():
            data = form.cleaned_data
            TextInput.objects.create(
                text_input=data['add_text'])
            


