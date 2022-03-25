from django.urls import path

from api_v2.views import ArticleListView

app_name = "v2"

urlpatterns = [
    path("articles/", ArticleListView.as_view(), name="articles"),
]
