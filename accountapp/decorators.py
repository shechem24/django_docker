from django.contrib.auth.models import User
from django.http import HttpResponseForbidden


def account_ownership_required(func):
    """
    요청한 유저와 db변경 대상 유자가 같은지 확인
    """
    def decorated(request, *args, **kwargs):
        user = User.objects.get(pk=kwargs['pk'])
        if not user == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)
    return decorated