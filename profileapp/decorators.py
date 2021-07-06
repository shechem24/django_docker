from django.http import HttpResponseForbidden
from profileapp.models import Profile

def profile_ownership_required(func):
    def decorated(request, *args, **kwargs):
        profile = Profile.objects.get(pk=kwargs['pk'])
        if not profile.user == request.user:            # Profile과 User는 OneToOne으로 묶어서 바로 접근 가능
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)
    return decorated