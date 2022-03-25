from django.urls import path

from api_v2.views import article_list_view

app_name = "v2"

urlpatterns = [
    path("articles/", article_list_view, name="articles"),
]
