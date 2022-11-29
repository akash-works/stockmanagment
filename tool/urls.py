from django.urls import path,include
from tool.views import *

urlpatterns = [
    path("",home,name="home"),
    path("add_company/",add_company,name="add_company"),
    path("add_product/",add_product,name="add_product"),
    path("detail/<pk>/",product_detail,name="product_detail"),
    path("delete/<pk>/",product_delete,name="product_delete"),
    path("update/<pk>/",product_update,name="product_update"),

]