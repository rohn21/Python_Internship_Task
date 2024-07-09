from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from webapp import views

app_name = 'webapp'

urlpatterns = [
    # path('',TemplateView.as_view(template_name='webapp/index.html'), name='index'), # using Class Based View's TemplateView
    path('', views.index, name='index'),
    path('user-form/', views.user_data, name='feedback'),
    path('user-data/', views.display_data, name='success'),
]
