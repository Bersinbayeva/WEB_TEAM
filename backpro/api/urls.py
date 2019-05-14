from django.conf import settings
from django.urls import path
from . import views


urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('login/', views.login),
    path('logout/', views.logout),
    path('categories/', views.CategoryList.as_view()),
    path('categories/<int:pk>/', views.CategoryDetail.as_view()),
    path('categories/<int:pk>/sections/', views.sections_list),
    path('categories/<int:pk>/sections/<int:pk2>/', views.sections_detail),
    path('categories/<int:pk>/sections/<int:pk2>/product/', views.product_list),
    path('categories/<int:pk>/sections/<int:pk2>/product/<int:pk3>/', views.product_detail),
    # path('basket/', views.BasketList.as_view()),
]
