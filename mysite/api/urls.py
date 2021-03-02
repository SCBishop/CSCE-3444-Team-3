from django.urls import path
from . import views

urlpatterns = [
	path('', views.apiOverview, name="api-overview"),
    path('show-menu/', views.showMenu, name="show-menu"),

]