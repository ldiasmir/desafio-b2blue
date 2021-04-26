from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
	path('', views.tvshows_list_view, name='home_list'),
	path('details/<int:tv_id>/', views.tvshows_detail_view, name='show_details')
]