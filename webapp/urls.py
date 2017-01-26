from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views.auth import LoginView, LogoutView
from .views.carnival import HomeView

urlpatterns = [
    url(r'^home/', login_required(HomeView.as_view(), login_url='webapp:login'), name='home'),
    url(r'^login/', LoginView.as_view(), name='login'),
    url(r'^logout/', LogoutView.as_view(), name='logout')
]
