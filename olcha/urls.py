from django.contrib import admin
from django.urls import path
from olcha import views 

app_name = 'olcha'

urlpatterns = [
   path('categories/',views.CategoryListView.as_view(), name='category_list'),
   path('category/<slug:slug>/',views.CategoryDetailView.as_view(), name='category_detail'),
   path('groups/',views.GroupListView.as_view(),name='groups_list'),
   path('group/<slug:slug>/',views.GroupDetailView.as_view(), name='group_detail'),
   
]
