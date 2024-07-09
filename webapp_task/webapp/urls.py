from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from webapp import views
app_name = 'webapp'

urlpatterns = [
    # path('',TemplateView.as_view(template_name='webapp/index.html'), name='index'),
    path('', views.index, name='index'),
]
