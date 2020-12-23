from django.urls import path
from .views import Home,Single_product,category_product,About,Contact,SearchView,Faq_details

urlpatterns = [
    path('',Home,name='home'),
    path('about/',About,name='about'),
    path('contact/',Contact,name='contact'),
    path('single_product/<int:id>/',Single_product,name='single_product'),
    path('single_product/<int:id>/<slug:slug>/',category_product,name='category_product'),
    path('search/',SearchView,name='SearchView'),
    path('faq/',Faq_details,name='Faq_details'),
]