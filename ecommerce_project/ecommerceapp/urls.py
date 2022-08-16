from . import views
from django.urls import path
from .import views
app_name='shop'
urlpatterns = [

    path('',views.allprod_cat, name ='allprod_cat'),
    path('<slug:c_slug>/',views.allprod_cat,name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.prodetail, name='product_detail'),

]















'''
urlpatterns = [
    
    path('',views.index,name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
  
    ]
      '''

