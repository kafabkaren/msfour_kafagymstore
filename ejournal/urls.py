from django.urls import path
from .views import view_article, view_ejournal_article_details, view_add_article

urlpatterns = [
    path('', view_article.as_view(), name='article'),
    path('article/<int:pk>', view_ejournal_article_details.as_view(), name='ejournal_article_details'),
    path('add_article/', view_add_article.as_view(), name='add_article'),
    
]
