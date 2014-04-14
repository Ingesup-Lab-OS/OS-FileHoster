from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from .forms import UploadFileForm
from os_file_hoster.libs.utils import SwiftHelper
from os_file_hoster.libs.utils import KeystoneHelper
from django.template import RequestContext

swifthelper = SwiftHelper()
kshelper = KeystoneHelper()

def file_upload(request):
    if request.method == 'POST':
        for filename, file in request.FILES.iteritems():
            print request.FILES[filename].name
            print request.user.id
            swifthelper.putFile(request.user.token.id, request.user.id, request.FILES[filename].name, request.FILES[filename].read())
        return HttpResponseRedirect('/file/upload/')
    else:
        form = UploadFileForm()
        return render_to_response('file/upload.html',  {'form' : form }, context_instance=RequestContext(request))
