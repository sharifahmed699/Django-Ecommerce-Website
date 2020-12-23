from django.urls import path
from OrderApp.views import Add_to_shoping_cart,Cart_details,cart_delete,OrderCart,order_show,order_product_show,user_order_details,user_order_product_details


urlpatterns = [
    path('addingcart/<int:id>/',Add_to_shoping_cart,name="add_to_shoping_cart"),
    path('cart_details/',Cart_details,name="cart_details"),
    path('cart_delete/<int:id>/',cart_delete,name="cart_delete"),
    path('order_cart/',OrderCart,name="ordercart"),
    path('orderlist/',order_show,name="order_show"),
    path('order_product_list/',order_product_show,name="order_product_show"),
    path('user_order_details/<int:id>/',user_order_details,name="user_order_details"),
    path('user_order_product_details/<int:id>/<int:oid>/',user_order_product_details,name="user_order_product_details"),
   
    
]