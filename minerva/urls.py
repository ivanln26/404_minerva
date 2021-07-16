from django.contrib.auth.views import LogoutView
from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.ProductListView.as_view(), name='product_list'),
    path('product/create', views.ProductCreateView.as_view(), name='product_create'),
    path('product/delete/<int:id>', views.ProductDeleteView.as_view(), name='product_delete'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
