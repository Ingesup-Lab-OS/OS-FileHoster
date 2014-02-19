from django.shortcuts import get_object_or_404, render
from frontos.libs.utils import KeystoneHelper
from frontos.libs.utils import SwiftHelper
import json
from django.http import HttpResponse

kshelper = KeystoneHelper()
swifthelper = SwiftHelper()

def index(request):
    ksadmin = kshelper.getKsadmin()
    users = ksadmin.users.list()
    user_list = []
    for user in users:
        # print user._info
        user = {
            "id": user.id,
            "username": user.username,
            "name": user.name,
            "email": user.email,
            "enabled": user.enabled
        }
        user_list.append(user)

    return HttpResponse(json.dumps(user_list), content_type="application/json")

def user_login(request):
    data = {}
    post = json.loads(request.body)
    username = post['username']
    password = post['password']
    ksadmin = kshelper.getKsadminFromCredentials(username, password)
    if ksadmin:
        request.session['authenticated'] = True
        data['authenticated'] = True
        data['auth_token'] = ksadmin.auth_token
    return HttpResponse(json.dumps(data), content_type="application/json")

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

def file_new(request):
    if request.method == 'POST':
        print request.FILES
        # c.http_connection = self.fake_http_connection(200)
        # args = ('http://www.test.com', 'asdf', 'asdf', 'asdf', 'asdf')
        # value = c.put_object(*args)
    return HttpResponse(json.dumps([{"done": True}]), content_type="application/json")
