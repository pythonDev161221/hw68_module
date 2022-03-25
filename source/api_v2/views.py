import json
from http import HTTPStatus

from django.http import JsonResponse, HttpResponseNotAllowed

from api_v2.serializers import ArticleSerializer
from webapp.models import Article


def article_list_view(request):
    if request.method == "GET":
        response_article_fields = ["pk", "title", "content", "author_id"]
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)

        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        article_data = json.loads(request.body)
        print(article_data)
        article = Article.objects.create(**article_data)

        return JsonResponse(
            {
                "pk": article.pk,
                "title": article.title,
                "content": article.content,
            },
            status=HTTPStatus.CREATED
        )

    return HttpResponseNotAllowed(["GET", "POST"])
