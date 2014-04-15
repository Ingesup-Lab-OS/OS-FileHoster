from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

def admin_required(view_func):
    def _wrapped_view_func(request, *args, **kwargs):
        if request.session['is_admin']:
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('login'))
    return _wrapped_view_func
