from django.contrib import admin
from django.urls import path,include
from olcha import views 
from rest_framework.routers import DefaultRouter



app_name = 'olcha'

router = DefaultRouter()
router.register('categoriesModelviewset', views.CategoryModelViewSet, basename='category')
router.register('products_model_view_set', views.ProductModelViewSet, basename='product')


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
   path('categoriesModelviewset/', include(router.urls)),
   
   #Product CRUD
   path('products/', views.ProductList.as_view(), name='product-list'),
   path('products/create/', views.ProductListGeneric.as_view(), name='product-create'),
   path('products/<int:pk>/', views.ProductDetail.as_view(), name='product-detail'),
   path('products/<int:pk>/update/', views.ProductDetailUpdate.as_view(), name='product-update'),
   path('products/<int:pk>/delete/', views.ProductDetailDelete.as_view(), name='product-delete'),
   path('products_model_view_set/', include(router.urls)),
   
   #Login, registr, logout
   path('register/', views.RegisterAPI.as_view(), name='register'),
   path('login/', views.LoginView.as_view(), name='login'),
   path('logout/', views.LogoutView.as_view(), name='logout'),
   
   
]
