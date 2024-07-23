from django.contrib import admin
from django.urls import path,include
from olcha import views 
from rest_framework.routers import DefaultRouter



app_name = 'olcha'

router = DefaultRouter()
router.register('categories', views.CategoryModelViewSet, basename='category')
router.register('products', views.ProductViewSet, basename='product')


urlpatterns = [
   path('categories/',views.CategoryListView.as_view(), name='category_list'),
   path('groups/',views.GroupListApiView.as_view(),name='group_list'),
   path('images/',views.ImageListApiView.as_view(), name='image_list'),
   path('products/',views.ProductListApiView.as_view(),name='products'),
   
   #Category CRUD
   path('category-list-generic-api-view/', views.CategoryList.as_view(), name='category_list_generic'),
   path('category-detail-generic-api-view/<int:pk>', views.CategoryDetail.as_view(),name='category_detail'),
   path('category-add-generic-api-view/', views.CategoryAdd.as_view(), name='category_add'),
   path('category-change-generic-api-view/<int:pk>', views.CategoryChange.as_view(),name='category_change'),
   path('category-delete-generic-api-view/<int:pk>', views.CategoryDelete.as_view(),name='category_delete'),
   path('modelviewset/', include(router.urls)),
   
   #Product CRUD
   path('products/', views.ProductListView.as_view(), name='product-list'),
   path('products/create/', views.ProductCreateView.as_view(), name='product-create'),
   path('products/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
   path('products/<int:pk>/update/', views.ProductUpdateView.as_view(), name='product-update'),
   path('products/<int:pk>/delete/', views.ProductDeleteView.as_view(), name='product-delete'),
]
