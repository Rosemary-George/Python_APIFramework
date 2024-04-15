from django.urls import path
from . import views
from .views import ProductListCreate, ProductRetrieveUpdateDestroy

urlpatterns = [
    path('products/', ProductListCreate.as_view(), name='product-list-create'),
    path('product/<int:pk>/', ProductRetrieveUpdateDestroy.as_view(), name='product-detail'),
    path('ProductDetails',views.Productdetails),
    path('ProductEdit',views.Productedit),
    path('ProductUpdate',views.Productupdate),
    path('ProductDelete',views.delete),
]

