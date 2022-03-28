from django.urls import path, include

from api_v2.views import ArticleListView, ArticleSingleObjectView, ArticleDetailView, ArticleUpdateView, \
    ArticleDeleteView

app_name = "v2"

articles_urlpatterns = [
    path("", ArticleListView.as_view(), name="articles"),
    path("<int:pk>/", ArticleSingleObjectView.as_view(), name="article-single-object"),
    path("detail/<int:pk>/", ArticleDetailView.as_view(), name="article-detail-view"),
    path("update/<int:pk>/", ArticleUpdateView.as_view(), name="article-update-view"),
    path("delete/<int:pk>/", ArticleDeleteView.as_view(), name="article-delete-view"),
]


urlpatterns = [
    path("articles/", include(articles_urlpatterns)),
]
# urlpatterns = [
#     path("articles/", ArticleListView.as_view(), name="articles"),
# ]
