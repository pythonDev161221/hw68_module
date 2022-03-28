from django.urls import path, include

from api_v2.views import ArticleListView, ArticleSingleObjectView

app_name = "v2"

# urlpatterns = [
#     path("articles/", ArticleListView.as_view(), name="articles"),
# ]
articles_urlpatterns = [
    path("", ArticleListView.as_view(), name="articles"),
    path("<int:pk>/", ArticleSingleObjectView.as_view(), name="article-single-object"),
]


urlpatterns = [
    path("articles/", include(articles_urlpatterns)),
]
