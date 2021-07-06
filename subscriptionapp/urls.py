from subscriptionapp.views import SubscriptionListView, SubscriptionView
from django.urls import path

app_name = 'subscriptionapp'

urlpatterns = [   
    path('subscribe/', SubscriptionView.as_view(), name='subscribe'),
    path('list/', SubscriptionListView.as_view(), name='list'),
]