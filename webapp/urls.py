from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login, logout_then_login

from .views import HomeView

urlpatterns = [
    url(r'^$', login_required(HomeView.as_view(), login_url='webapp:login'), name='home'),
    url(r'^login', login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout', logout_then_login, name='logout'),
]
