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
                cowsay_text=data['text_input'])

            out_put = subprocess.check_output(['cowsay', str(data['text_input'])]).decode('utf-8')


            form = AddTextForm()
            return render(req, 'index.html', {'form': form, 'out_put': out_put })

    form = AddTextForm()
    return render(req, 'index.html', {'form': form})



