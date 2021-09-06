from django.urls import path, include
from .views import CommentDeleteView, CategoryListView, PostCommentView, PostListView

urlpatterns= [
    path('', PostListView.as_view(), name='home'),
    path('categories/<str:post_category>/', CategoryListView.as_view(), name='category'),
    path('<str:category>/<slug:post_slug>/', PostCommentView.as_view(), name='post_detail'),
    path('<str:category>/<slug:post_slug>/<uuid:commentpk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),   
]