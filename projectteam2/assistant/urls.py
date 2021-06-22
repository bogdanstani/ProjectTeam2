from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('sign-up', views.sign_up, name="sign-up"),
#    path('cars', views.get_cars, name="cars"),

    # path('', views.index, name='index'),
    path('checker', views.get_documents_to_expire, name='index'),
    ]