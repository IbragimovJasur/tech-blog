from django.urls import path
from .views import MessageCreateView

urlpatterns= [
    path('contact/', MessageCreateView.as_view(), name='contact'),
]