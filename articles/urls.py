from django.urls import path
from .views import (ArticleAddComment, ArticleListView,
                    ArticleUpdateView,
                    ArticleDetailView,
                    ArticleDeleteView,
                    ArticleCreateView,
                    )
urlpatterns = [
    path('<int:pk>/edit/',
         ArticleUpdateView.as_view(), name='article_edit'),
    path('<int:pk>/',
         ArticleDetailView.as_view(), name='article_detail'),
    path('<int:pk>/delete/',
         ArticleDeleteView.as_view(), name='article_delete'),
    path('new/', ArticleCreateView.as_view(), name='article_new'),
    path('new/<int:pk>/comment', ArticleAddComment.as_view(), name='article_comment'),
    path('', ArticleListView.as_view(), name='article_list'),
]
