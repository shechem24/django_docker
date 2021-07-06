from django.shortcuts import render

# Create your views here.

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, TemplateView

from accountapp.forms import AccountUpdateForm
from accountapp.decorators import account_ownership_required
from articleapp.models import Article

# 여러 데코레이터 합침
has_ownership = [account_ownership_required, login_required]

# class 형 view
# django는 get, post 등이 하나의 함수에서 진행
# CreateView: 장고 기본 제공하는 가입 양식
class AccountCreateView(CreateView):
    """
    Account app: user create
    """
    model = User                                            # model: db table 매핑 형태
    form_class = UserCreationForm                           # form: 사용자로부터 정보를 수집하여 서버에 제출하는데 사용
    success_url = reverse_lazy('home')           # reverse는 class에서 사용할 수 없음(함수에서 사용). 해당주소로 렌더링
    template_name = 'accountapp/create.html'                # 사용 template

# Read
class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'                     # html에서 사용하는 변수 이름
    template_name = 'accountapp/detail.html'                #

    paginate_by = 25

    def get_context_data(self, **kwargs):
        object_list = Article.objects.filter(writer=self.get_object())
        return super(AccountDetailView, self).get_context_data(object_list=object_list, **kwargs)


@method_decorator(has_ownership, 'get')                     # name='dispatch' → 모든 메소드 적용
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountUpdateForm
    context_object_name = 'target_user'
    success_url = reverse_lazy('home')
    template_name = 'accountapp/update.html'


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('home')
    template_name = 'accountapp/delete.html'


class HomeView(TemplateView):
    template_name = 'base.html'
