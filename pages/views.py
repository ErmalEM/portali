from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'
    login_url = 'login'
