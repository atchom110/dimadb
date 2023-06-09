from django.urls import path
from .import views
from user import views as user_view
from django.contrib.auth import views as auth_views

urlpatterns=[
    path('',views.index, name='dashb-index'),
    path('search/',views.search, name='dashb-search'),
    path('search_sport/', views.search_sport, name='dashb-search_sport'),
    path('search_p/',views.search_phone, name='dashb-search_phone'),
    path('search_prodA/', views.search_prodAd, name='dashb-search_prodAd'),
    path('search_pA/',views.search_phoneAd, name='dashb-search_phoneAd'),
    path('search_tA/',views.search_tabAd, name='dashb-search_tabAd'),
    path('search_lA/',views.search_laptopAd, name='dashb-search_laptopAd'),
    path('search_top/',views.search_laptop, name='dashb-search_laptop'),
    path('search_t/',views.search_tab, name='dashb-search_tab'),
    path('search_exit/',views.search_sortie, name='dashb-search_sortie'),
    path('dashb', views.index_admin, name='dashb-index_admin'),
    path('sortie', views.sortieMat_admin, name='dashb-sortieMat_admin'),
    path('sortie_index', views.sortieMat_index, name='dashb-sortieMat_index'),
    path('phone2', views.high_tech_phone, name='dashb-high_tech_phone'),
    path('tab2', views.high_tech_tab, name='dashb-high_tech_tab'),
    path('dashb2', views.high_tech_admin, name='dashb-high_tech_admin'),
    path('phoneAdmin', views.phone_admin, name='dashb-phone_admin'),
    path('tabAdmin', views.tab_admin, name='dashb-tab_admin'),
    path('laptop', views.laptop_index, name='dashb-laptop_index'),
    path('dashb3', views.laptop_admin, name='dashb-laptop_admin'),
    path('sport', views.sport, name='dashb-sport'),
    path('serveur', views.serveur, name='dashb-serveur'),
    path('transit', views.transit, name='dashb-transit'),
    path('kousseri', views.kousseri, name='dashb-kousseri'),
    path('aird', views.aird, name='dashb-aird'),
    path('product/update/<int:pk>/', views.product_update, name='dashb-product_update'),
    path('index/delete/<int:pk>/', views.index_delete, name='dashb-index_delete'),
    path('sortie/delete/<int:pk>/', views.sortieMat_delete, name='dashb-sortieMat_delete'),
    path('hightech/update/<int:pk>/', views.high_tech_update, name='dashb-high_tech_update'),
    path('phone2/update/<int:pk>/', views.phone_update, name='dashb-phone_update'),
    path('tab2/update/<int:pk>/', views.tab_update, name='dashb-tab_update'),
    path('laptop2/update/<int:pk>/', views.laptop_update, name='dashb-laptop_update'),
    path('mat2/update/<int:pk>/', views.sortieMat_update, name='dashb-sortieMat_update'),


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