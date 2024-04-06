from django.shortcuts import render
from django.views.generic import TemplateView


class MainView(TemplateView):
    template_name = 'shop/index.html'


class AboutView(TemplateView):
    template_name = 'shop/about.html'
