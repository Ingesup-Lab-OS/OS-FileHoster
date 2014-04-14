from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from os_file_hoster.libs.utils import KeystoneHelper
from django.template import RequestContext

kshelper = KeystoneHelper()

def user_list(request):
    ksadmin = kshelper.get_ksadmin()
    users = ksadmin.users.list(tenant_id = "6ca0f39be8bc4b208abb4dbd1f9eb1e2")
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

    print user_list[0]
    return render_to_response('user/list.html', {'users' : user_list}, context_instance=RequestContext(request))

def user_new(request):
    print "here"
    if request.method == 'POST':
        ksclient = kshelper.get_ksadmin_fom_token_id(request.user.token.id)
        print ksclient
        user = request.POST.get('username', '')
        password = request.POST.get('password', '')
        email = request.POST.get('email', '')

        kshelper.create_ksuser(ksclient, user, password, email)
        return HttpResponseRedirect(reverse('UserManager:user_list'))
    else:
        return render_to_response('user/new.html', context_instance=RequestContext(request))
