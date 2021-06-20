from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('test', views.get_documents_to_expire, name='index'),
    ]