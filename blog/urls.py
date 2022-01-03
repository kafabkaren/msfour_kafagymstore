from django.urls import path
from .views import view_blog, view_article_details

urlpatterns = [
    path('', view_blog.as_view(), name='view_blog'),
    path(
        'article/<int:pk>', view_article_details.as_view(), name='article-details'),
]
