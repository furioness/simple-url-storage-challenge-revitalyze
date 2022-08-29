from django.urls import path

from . import views

app_name = 'storage'

urlpatterns = [
    path('', views.ListURLsView.as_view(), name='list'),
    path('add', views.AddURLView.as_view(), name='add'),
]