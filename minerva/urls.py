from django.contrib.auth.views import LogoutView
from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about_us', views.aboutUs, name='about_us'),
    path('categories/', views.CategoryListView.as_view(), name='category_list'),
    path('category/create', views.CategoryCreateView.as_view(), name='category_create'),
    path('category/delete/<int:id>', views.CategoryDeleteView.as_view(), name='category_delete'),
    path('category/edit/<int:id>', views.CategoryEditView.as_view(), name='category_edit'),
    path('client/create', views.ClientCreateView.as_view(), name='client_create'),
    path('client/edit/<int:id>', views.ClientEditView.as_view(), name='client_edit'),
    path('clients/', views.ClientListView.as_view(), name='client_list'),
    path('product/create', views.ProductCreateView.as_view(), name='product_create'),
    path('product/delete/<int:id>', views.ProductDeleteView.as_view(), name='product_delete'),
    path('product/detail/<int:id>', views.ProductDetailView.as_view(), name='product_detail'),
    path('product/edit/<int:id>', views.ProductEditView.as_view(), name='product_edit'),
    path('products/', views.ProductListView.as_view(), name='product_list'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
