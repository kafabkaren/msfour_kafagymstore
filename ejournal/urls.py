from django.urls import path
from .views import view_article

from . import views

urlpatterns = [
    path('', view_article.as_view(), name='view_article'),
]