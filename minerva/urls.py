from django.contrib.auth.views import LogoutView
from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('client/create', views.ClientCreateView.as_view(), name='client_create'),
    path('clients/', views.ClientListView.as_view(), name='client_list'),
    path('product/create', views.ProductCreateView.as_view(), name='product_create'),
    path('product/delete/<int:id>', views.ProductDeleteView.as_view(), name='product_delete'),
    path('product/detail/<int:id>', views.ProductDetailView.as_view(), name='product_detail'),
    path('product/edit/<int:id>', views.ProductEditView.as_view(), name='product_edit'),
    path('products/', views.ProductListView.as_view(), name='product_list'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
