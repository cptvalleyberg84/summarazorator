from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('create/', views.create_post, name='create_post'),
    path('search/', views.search_posts, name='search'),
    path('<slug:post_slug>/', views.post_detail, name='post_detail'),
    path('<slug:post_slug>/edit_comment/<int:comment_id>', views.comment_edit, name='comment_edit'),
    path('<slug:post_slug>/delete_comment/<int:comment_id>', views.comment_delete, name='comment_delete'),
]