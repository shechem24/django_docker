from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView
from django.utils.decorators import method_decorator

from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile
from profileapp.decorators import profile_ownership_required

class ProfileCreateView(CreateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    # success_url = reverse_lazy('accountapp:detail') # <int:pk> 때문에 바로 사용 불가 → 내부 메소드 수정 필요
    template_name = 'profileapp/create.html'

    def form_valid(self, form):
        temp_profile = form.save(commit=False)  # 지정한 폼(ProfileCreationForm)을 통해 받은 데이터를 임시로 저장(commit=False)
        temp_profile.user = self.request.user   # request 한 유저 정보 추가
        temp_profile.save()                     # 데이터 저장
        return super().form_valid(form)
    
    def get_success_url(self):                  # 기본 success_url은 단순 정적으로 랜더링 함
        return reverse('accountapp:detail', kwargs={ 'pk': self.object.user.pk })     # self.object = profile → .user.pk 추가해서 pk를 같이 날리게 함


@method_decorator(profile_ownership_required, 'get')
@method_decorator(profile_ownership_required, 'post')
class ProfileUpdateView(UpdateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    # success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'profileapp/update.html'
    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={ 'pk': self.object.user.pk })