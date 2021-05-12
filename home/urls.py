from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index,name='home'),
    path('login', views.handlelogin,name='login'),
    path('logout', views.handlelogout,name='logout'),
    path('hosp_dash', views.hosp,name='hosp'),
    path('br_dash', views.branch,name='branch'),
    path('add_data', views.add_data,name='add'),
    path('show_data', views.show_data,name='show'),
    path('show_database', views.show_database,name='show_database'),

]
