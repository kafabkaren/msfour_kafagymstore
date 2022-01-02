from django.urls import path
from .views import view_article, view_ejournal_article_details


urlpatterns = [
    path('', view_article.as_view(), name='view_article'),
    path('article/<int:pk>', view_ejournal_article_details.as_view(), name='ejournal_article_details')
]