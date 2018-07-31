from django.http import HttpResponse
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage


def home(request):
    return render(request, 'index.html')


def save_video(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['file']
        fs = FileSystemStorage()
        filename = fs.save(uploaded_file.name, uploaded_file)
        # TODO: THis url will be used in future to give user download link
        # url = fs.url(filename)
        return HttpResponse("Done")