from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm
from os_file_hoster.utils.os_helper import SwiftHelper
from os_file_hoster.utils.os_helper import KeystoneHelper

swifthelper = SwiftHelper()
kshelper = KeystoneHelper()

def file_upload(request):
    ksadmin = kshelper.get_ksadmin(request)
    print request.session.get('user_id')
    if request.method == 'POST':
        for filename, file in request.FILES.iteritems():
            swifthelper.put_file(ksadmin.token.id, request.session.get('user_id'), request.FILES[filename].name, request.FILES[filename].read())
        return HttpResponseRedirect(reverse('file_upload'))
    else:
        form = UploadFileForm()
        return render(request, 'file/upload.html',  {'form' : form })

def file_list(request):
    ksadmin = kshelper.get_ksadmin(request)
    files = swifthelper.get_files(ksadmin.token.id, request.session.get('user_id'))
    return render(request, 'file/list.html',  {'files' : files[1] })

def file_delete(request, name):
    ksadmin = kshelper.get_ksadmin(request)
    files = swifthelper.delete_file(ksadmin.token.id, request.session.get('user_id'), name)
    return HttpResponseRedirect(reverse('file_list'))
