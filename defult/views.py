from django.shortcuts import render
from . import forms
import inspect
from multiprocessing import Process
# Create your views here.


def indexview(request):
    if request.method == "POST":
        data = request.POST['data']

        if request.POST['action'] == 'save':
            savedata(data)
            return render(request, 'index.html', {'formdata': data})
        elif request.POST['action'] == 'run':
            form = getobj()
            return render(request, 'index.html', {'form':form, 'formdata':data})
    else:
        return render(request, 'index.html')


def getobj():
    for name, obj in inspect.getmembers(forms):
        if inspect.isclass(obj):
            return obj
    return None

def savedata(data):
    with open('defult/forms.py', 'w', newline='') as f:
        f.write(data)