from django.contrib import admin
from django.urls import path, include
# from . import views 
from .views import HomeView, PostDetailView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView, CategoryView, CategoryListView
from .views import redirect_view

urlpatterns = [    
    path('', redirect_view, name="home"),
    path('post', HomeView.as_view(), name="post"),    
    path('post/<int:pk>', PostDetailView.as_view(), name="post-detail"),
    path('add_post/', AddPostView.as_view(), name="add_post"),
    path('post/update/<int:pk>', UpdatePostView.as_view(), name="update_post"),
    path('post/<int:pk>/delete', DeletePostView.as_view(), name="delete_post"),
    path('add_category/', AddCategoryView.as_view(), name="add_category"),
    path('category/<str:cats>/', CategoryView, name="category"),
    path('category_list/', CategoryListView, name="category_list"),
]