from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from .forms import UploadFileForm
from frontos.libs.utils import SwiftHelper

swifthelper = SwiftHelper()

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/')
    else:
        form = UploadFileForm()
    return render_to_response('file/upload.html', {'form': form})
