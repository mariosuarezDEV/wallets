from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class PerfilView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'
