import json
from http import HTTPStatus

from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponse
from django.shortcuts import get_object_or_404
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView

from api_v2.serializers import ArticleSerializer
from webapp.models import Article


# class ArticleListView(View):
#     serializer_class = ArticleSerializer
#
#     def get(self, request, *args, **kwargs):
#         response_article_fields = ["pk", "title", "content", "author_id"]
#         articles = Article.objects.all()
#         serializer = self.serializer_class(articles, many=True)
#
#         return JsonResponse(serializer.data, safe=False)
#
#     def post(self, request, *args, **kwargs):
#         article_data = json.loads(request.body)
#
#         serializer = self.serializer_class(data=article_data)
#         if not serializer.is_valid():
#             return HttpResponse(status=HTTPStatus.BAD_REQUEST)
#
#         article = Article.objects.create(**article_data)
#
#         return JsonResponse(
#             serializer.data,
#             status=HTTPStatus.CREATED
#         )


class ArticleListView(APIView):
    serializer_class = ArticleSerializer

    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()
        serializer = self.serializer_class(articles, many=True)

        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        serializer.is_valid(raise_exception=True)
        article = serializer.save(author=request.user)

        return Response(
            self.serializer_class(article).data,
            status=HTTPStatus.CREATED
        )


class ArticleSingleObjectView(APIView):
    serializer_class = ArticleSerializer

    def put(self, request, *args, pk=None, **kwargs):
        article = get_object_or_404(Article, pk=pk)

        serializer = self.serializer_class(data=request.data, instance=article)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(data=serializer.data)
