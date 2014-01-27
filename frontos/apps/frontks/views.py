from django.shortcuts import get_object_or_404, render
from frontos.libs.utils import KeystoneHelper
import json
from django.http import HttpResponse

kshelper = KeystoneHelper()
users = [
    {
        "id": "1",
        "username": "adrien",
        "email": "adrien.louis.r@gmail.com"
    },
    {
        "id": "2",
        "username": "arnaud",
        "email": "arnaud.cavat@y-nov.com"
    }
]

def index(request):
    return HttpResponse(json.dumps(users), content_type="application/json")

def user_show(request):
    user_id = int(request.GET.get('user_id', )) - 1
    return HttpResponse(json.dumps(users[user_id]), content_type="application/json")

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
