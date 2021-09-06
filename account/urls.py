from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import SignUpView, LogoutConfirm

urlpatterns= [
    path('signup/', SignUpView.as_view(), name= 'signup'),
    path('login/', LoginView.as_view(template_name='account/login.html'), name='login'),
    path('logout/confirm/', LogoutConfirm.as_view(), name='logoutconfirm'),
    path('logout/', LogoutView.as_view(), name='logout'),
]