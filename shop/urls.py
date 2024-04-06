from django.urls import path

from shop.views import MainView, AboutView

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('about/', AboutView.as_view(), name='about'),
]
