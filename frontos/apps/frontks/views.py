from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
import keystoneclient.v2_0.client as ksclient
from frontos.libs.utils import getAdminKeystone

def index(request):
  return render(request, 'admin/index.html')

def user_show(request):
  return render(request, 'admin/user.html', {'ksadmin':ksadmin})

def user_create(request):
  ksadmin = getAdminKeystone()
  if request.method == "GET":
    return render(request, 'admin/user_new.html')
  elif request.method == "POST":
    user = request.POST.get('username', '')
    password = request.POST.get('password', '')
    email = request.POST.get('email', '')
    tenants = ksadmin.tenants.list()
    tenant = [x for x in tenants if x.name=='share_project'][0]
    
    ksadmin.users.create(username=username,
                password=password,
                email=email, tenant_id=tenant.id)

    return HttpResponseRedirect(reverse('admin:user'))

"""
def user_edit(request):
  if request.method == "GET":
    return render(request, 'admin/user_new.html')
  elif request.method == "POST":
    return HttpResponseRedirect(reverse('admin:user'))
"""

def user_delete(request):
  ksadmin = getAdminKeystone()
  if request.method == "GET":
    return render(request, 'admin/user_remove.html')
  elif request.method == "POST":
    username = request.POST.get('username', '')

    users = ksadmin.users.list()
    user = [x for x in users if x.name==username][0]
    
    ksadmin.users.delete(user)

    return HttpResponseRedirect(reverse('admin:user'))