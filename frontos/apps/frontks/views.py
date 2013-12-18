from django.shortcuts import get_object_or_404, render
from frontos.libs.utils import KeystoneHelper

kshelper = KeystoneHelper()

def index(request):
    return render(request, 'frontks/index.html')

def user_show(request):
    ksadmin = kshelper.getKsadmin()
    userlist = ksadmin.users.list
    return render(request, 'frontks/user.html', {'userlist':userlist})

def user_create(request):
    ksadmin = kshelper.getKsadmin()
    if request.method == "GET":
        return render(request, 'frontks/user_new.html', {'ksadmin':ksadmin})
    elif request.method == "POST":
        user = request.POST.get('username', '')
        password = request.POST.get('password', '')
        email = request.POST.get('email', '')
        tenants = ksadmin.tenants.list()
        tenant = [x for x in tenants if x.name=='demo'][0]
        
        kshelper.createKsuser(user, password, email, tenant)
        return HttpResponseRedirect(reverse('frontks:user'))

"""
def user_edit(request):
    if request.method == "GET":
        return render(request, 'frontks/user_new.html')
    elif request.method == "POST":
        return HttpResponseRedirect(reverse('frontks:user'))
"""

def user_delete(request):
    ksadmin = kshelper.getKsadmin()
    if request.method == "GET":
        return render(request, 'frontks/user_remove.html')
    elif request.method == "POST":
        username = request.POST.get('username', '')
        users = ksadmin.users.list()
        user = [x for x in users if x.name==username][0]
        
        kshelper.deleteKsuser(user)
        return HttpResponseRedirect(reverse('frontks:user'))