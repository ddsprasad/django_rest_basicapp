
from django.urls import path
from .views import article_list, article_detail, ArticleAPIView

urlpatterns = [
    # path('article/', article_list),
    path('article/', ArticleAPIView.as_view()),
    path('details/<int:id>/', article_detail)
]