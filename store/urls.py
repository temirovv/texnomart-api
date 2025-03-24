from django.urls import path
from .views import PromotionView, CategoryView,\
      ProductListView, ProductDetailView, \
      SearchView


urlpatterns = [
    path('promotions/', PromotionView.as_view(), name='promotions'),
    path('categories/', CategoryView.as_view(), name='categories'),
    path('products/', ProductListView.as_view(), name='products'),
    path('product/detail/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('search/', SearchView.as_view(), name='search')
]
