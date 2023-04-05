from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('<int:id>', views.design_detail, name='design_detail'),
    path('search', views.search, name='search'),
]