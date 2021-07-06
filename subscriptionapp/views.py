from articleapp.models import Article
from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView
from django.urls import reverse
from django.views.generic.list import ListView
from projectapp.models import Project
from subscriptionapp.models import Subscription

@method_decorator(login_required, 'get')
class SubscriptionView(RedirectView):
    
    def get_redirect_url(self, *args):
        return reverse('projectapp:detail', kwargs={ 'pk': self.request.GET.get('project_pk') })

    def get(self, request, *args, **kwagrs):

        # 해당 pk를 가지는 project를 찾음 → 없으면 404를 리턴
        project = get_object_or_404(Project, pk=self.request.GET.get('project_pk'))
        user = self.request.user
        subscription = Subscription.objects.filter(user=user, project=project)

        if subscription.exists():
            subscription.delete()
        else:
            Subscription(user=user, project=project).save()
        return super(SubscriptionView, self).get(request, *args, **kwagrs)


@method_decorator(login_required, 'get')
class SubscriptionListView(ListView):
    model = Article
    context_object_name = 'article_list'
    template_name = 'subscriptionapp/list.html'
    paginate_by = 5

    def get_queryset(self):
        projects = Subscription.objects.filter(user=self.request.user).values_list('project')   # project에 대해서 list화 함
        article_list = Article.objects.filter(project__in=projects)
        return article_list