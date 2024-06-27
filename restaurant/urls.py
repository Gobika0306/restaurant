from django.urls import path
from . import views
from .views import home, menu_view
from .views import add_to_order

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', menu_view, name='menu'),
    path('add_to_order/', add_to_order, name='add_to_order'),
]



