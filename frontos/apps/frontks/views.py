from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from .forms import UploadFileForm
from frontos.libs.utils import SwiftHelper
from django.template import RequestContext

swifthelper = SwiftHelper()

def upload_file(request):
    if request.method == 'POST':
        for filename, file in request.FILES.iteritems():
            print request.FILES[filename].name
            print request.FILES[filename].size
        return HttpResponseRedirect('/upload_file/')
    else:
        form = UploadFileForm()
        return render_to_response('file/upload.html',  {'form' : form }, context_instance=RequestContext(request))
