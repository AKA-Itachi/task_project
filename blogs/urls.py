from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.blog_create, name='create'),
    path('blog/', views.BlogsListView.as_view(), name='blog'),
    path('blogs/<int:pk>', views.BlogsDetailView.as_view(), name='blogs-detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
    path('blogs/<int:pk>/comment', views.BlogCommentCreate.as_view(), name='comment'),
]
