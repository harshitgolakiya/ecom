
from django.urls import path
from . import views

urlpatterns = [
    path('', views.products, name='products'),
    path('login/',views.loginuser,name='login'),
    path('logout/',views.logoutuser,name='logout'),
    path('register/',views.register,name='register'),
    path('<int:product_id>', views.product_info, name='product_detail'),
    path('category/<str:category_name>/', views.product_category, name='product_category'),
]