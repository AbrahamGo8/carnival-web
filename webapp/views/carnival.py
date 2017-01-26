from django.views.generic.base import TemplateView

__all__ = ['HomeView']


class HomeView(TemplateView):
    template_name = 'home.html'
