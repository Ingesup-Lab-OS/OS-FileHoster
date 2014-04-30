from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from os_file_hoster.utils.os_helper import KeystoneHelper
from django.contrib.auth.decorators import login_required
from os_file_hoster.decorator import admin_required

kshelper = KeystoneHelper()

@login_required
@admin_required
def user_list(request):
    users = kshelper.get_ksclient().users.list(tenant_id = "6ca0f39be8bc4b208abb4dbd1f9eb1e2")
    user_list = {}
    for user in users:
        user_item = {
            "id": user.id,
            "username": user.username,
            "name": user.name,
            "enabled": user.enabled
        }
        dicto = {user.id: user_item}
        user_list.update(dicto)
    return render(request, 'user/list.html', {'users' : user_list})

@login_required
@admin_required
def user_new(request):
    if request.method == 'POST':
        user = request.POST.get('username', '')
        password = request.POST.get('password', '')
        email = request.POST.get('email', '')
        kshelper.create_ksuser(user, password, email)
        return HttpResponseRedirect(reverse('user_list'))
    else:
        return render(request, 'user/new.html')

@login_required
@admin_required
def user_delete(request, id):
    kshelper.delete_ksuser(id)
    return HttpResponseRedirect(reverse('user_list'))

@login_required
def set_role(request):
    roles = request.user.roles
    if any(role['name'] == 'admin' for role in roles):
        request.session['is_admin'] = True
    else:
        request.session['is_admin'] = False
    return HttpResponseRedirect('/')
