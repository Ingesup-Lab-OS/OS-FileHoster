from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm
from os_file_hoster.utils.os_helper import SwiftHelper
from os_file_hoster.utils.os_helper import KeystoneHelper
from django.contrib.auth.decorators import login_required

swifthelper = SwiftHelper()
kshelper = KeystoneHelper()

@login_required
def file_upload(request):
    container = request.POST.get('container', '')
    ksadmin = kshelper.get_ksadmin(request)
    if request.method == 'POST':
        for filename, file in request.FILES.iteritems():
            swifthelper.put_file(ksadmin.token.id, container, request.FILES[filename].name, request.FILES[filename].read())
        return HttpResponseRedirect(reverse('file_list', args=[container]))
    else:
        return HttpResponseRedirect(reverse('file_list'))

@login_required
def file_list(request, container = None):
    if not container:
        container = request.session.get('user_id')
    ksadmin = kshelper.get_ksadmin(request)
    files = swifthelper.get_files(ksadmin.token.id, container)
    new_files = []
    for cur_file in files[1]:
        cur_file['url'] = swifthelper.gen_url_for_file(container, cur_file['name'])
        new_files.append(cur_file)
    form = UploadFileForm()
    return render(request, 'file/list.html',  {'files' : new_files, 'form' : form, 'container': container })

@login_required
def file_delete(request, name, container):
    if not container:
        container = request.session.get('user_id')
    ksadmin = kshelper.get_ksadmin(request)
    files = swifthelper.delete_file(ksadmin.token.id, container, name)
    return HttpResponseRedirect(reverse('file_list', args=[container]))
