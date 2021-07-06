from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, DetailView, ListView
from django.urls import reverse
from django.views.generic.list import MultipleObjectMixin

from projectapp.forms import ProjectCreationForm
from projectapp.models import Project

from articleapp.models import Article
from subscriptionapp.models import Subscription

@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectCreationForm
    template_name = 'projectapp/create.html'

    def get_success_url(self):
        return reverse('projectapp:detail', kwargs={ 'pk': self.object.pk })

class ProjectDetailView(DetailView, MultipleObjectMixin):
    model = Project
    context_object_name = 'target_project'
    template_name = 'projectapp/detail.html'

    paginate_by = 25

    # context_object_name 뿐 아니라 다른 context도 추가하고 싶을 때 사용
    def get_context_data(self, **kwargs):
        project = self.object
        user = self.request.user

        if user.is_authenticated:
            subscription = Subscription.objects.filter(user=user, project=project)
        else:
            subscription = None
        object_list = Article.objects.filter(project=self.get_object())
        # return super(ProjectDetailView, self).get_context_data(object_list=object_list, **kwargs)   # html에서 object_list 사용
        return super(ProjectDetailView, self).get_context_data(object_list=object_list, subscription=subscription, **kwargs)   # html에서 object_list 사용


class ProjectListView(ListView):
    model = Project
    context_object_name = 'project_list'
    template_name = 'projectapp/list.html'
    paginate_by = 25