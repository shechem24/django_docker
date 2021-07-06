from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from accountapp.views import AccountCreateView, AccountDetailView, AccountUpdateView, AccountDeleteView

app_name = 'accountapp'

urlpatterns = [
    # 장고 기본 제공하는 login/logout view 바로 사용 가능
    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('create/', AccountCreateView.as_view(), name='create'),   # 클래스 베이스 형 → 이름 뒤에 .as_view() 붙여야함
    path('detail/<int:pk>', AccountDetailView.as_view(), name='detail'),    # primary key로 받음
    path('update/<int:pk>', AccountUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', AccountDeleteView.as_view(), name='delete'),
]