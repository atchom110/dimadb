from django.urls import path
from .import views
from user import views as user_view
from django.contrib.auth import views as auth_views

urlpatterns=[
    path('',views.index, name='dashb-index'),
    path('search/',views.search, name='dashb-search'),
    path('dashb', views.index_admin, name='dashb-index_admin'),
    path('phone2', views.high_tech_phone, name='dashb-high_tech_phone'),
    path('tab2', views.high_tech_tab, name='dashb-high_tech_tab'),
    path('dashb2', views.high_tech_admin, name='dashb-high_tech_admin'),
    path('laptop', views.laptop_index, name='dashb-laptop_index'),
    path('dashb3', views.laptop_admin, name='dashb-laptop_admin'),
    path('sport', views.sport, name='dashb-sport'),
    path('serveur', views.serveur, name='dashb-serveur'),
    path('transit', views.transit, name='dashb-transit'),
    path('kousseri', views.kousseri, name='dashb-kousseri'),
    path('aird', views.aird, name='dashb-aird'),
    path('product/update/<int:pk>/', views.product_update, name='dashb-product_update'),
    path('hightech/update/<int:pk>/', views.high_tech_update, name='dashb-high_tech_update'),
    path('laptop2/update/<int:pk>/', views.laptop_update, name='dashb-laptop_update'),


    path('register/', user_view.register, name='user-register'),
    path('login', auth_views.LoginView.as_view(template_name='user/login.html'), name='user-login'),
    path('logout', auth_views.LogoutView.as_view(template_name='user/logout.html'), name='user-logout'),
 #   path('serveur/', views.serveur, name='dashb-serveur'),

 #   path('transit/', views.transit, name='dashb-transit'),
  #  path('kousseri/', views.kousseri, name='dashb-kousseri'),
 #   path('phone/', views.phone, name='dashb-phone'),
 #   path('ordi/', views.sport, name='dashb-ordi'),
 #   path('tab/', views.tab, name='dashb-tab')

    ]