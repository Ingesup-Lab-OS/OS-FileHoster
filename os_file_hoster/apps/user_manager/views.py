from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from os_file_hoster.utils.os_helper import KeystoneHelper

kshelper = KeystoneHelper()

def user_list(request):
    users = kshelper.get_ksadmin(request).users.list(tenant_id = "6ca0f39be8bc4b208abb4dbd1f9eb1e2")
    user_list = []
    for user in users:
        # print user._info
        user = {
            "id": user.id,
            "username": user.username,
            "name": user.name,
            "enabled": user.enabled
        }
        user_list.append(user)

    return render(request, 'user/list.html', {'users' : user_list})

def user_new(request):
    if request.method == 'POST':
        kshelper.get_ksadmin(request)
        user = request.POST.get('username', '')
        password = request.POST.get('password', '')
        email = request.POST.get('email', '')

        kshelper.create_ksuser(user, password, email)
        return HttpResponseRedirect(reverse('user_list'))
    else:
        return render(request, 'user/new.html')

def user_delete(request, id):
    kshelper.delete_ksuser(id)
    return HttpResponseRedirect('/');
