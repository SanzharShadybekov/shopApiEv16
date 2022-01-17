from django.urls import path

from product import views

urlpatterns = [
    # path('products/', product_list, name='products_list'), фунции
    # path('products/create/', ProductListView.as_view()), класс APIView
    path('products/', views.ProductListCreateView.as_view()),
    path('products/<int:pk>/', views.ProductDetailView.as_view())
]

# locolhost:8000/api/v1/products/ - GET -> list of objects
#                                   POST -> create object
#
# locolhost:8000/api/v1/products/1/ - GET -> DETAIL object
#                                     PUT/PATCH -> Update object
#                                     DELETE -> Delete object

