from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin
)
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, TemplateView

from webapp.forms import ArticleForm, ArticleDeleteForm
from webapp.models import Article
from webapp.views.base import SearchView


class IndexView(SearchView):
    model = Article
    context_object_name = "articles"
    template_name = "articles/index.html"
    paginate_by = 10
    paginate_orphans = 1
    search_fields = ["title__icontains", "author__icontains"]
    ordering = ["-updated_at"]

    # def get(self, request, *args, **kwargs):
    #     print(request.user)
    #     return JsonResponse(
    #         {"key": "value", "key2": [1, 2, 3]}
    #     )


class ArticleCreateView(PermissionRequiredMixin, CreateView):
    model = Article
    form_class = ArticleForm
    template_name = "articles/create.html"
    permission_required = "webapp.add_article"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ArticleView(DetailView):
    template_name = 'articles/view.html'
    model = Article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comments = self.object.comments.order_by("-created_at")
        context['comments'] = comments
        return context


class ArticleUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = "webapp.change_article"
    form_class = ArticleForm
    template_name = "articles/update.html"
    model = Article

    def has_permission(self):
        return super().has_permission() or self.request.user == self.get_object().author


class ArticleDeleteView(PermissionRequiredMixin, DeleteView):
    model = Article
    template_name = "articles/delete.html"
    success_url = reverse_lazy('webapp:index')
    form_class = ArticleDeleteForm
    permission_required = "webapp.delete_article"

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.method == "POST":
            kwargs['instance'] = self.object
        return kwargs


class ArticleAddLike(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        article = Article.objects.get(pk=self.kwargs.get('pk'))
        article.users_liked.add(self.request.user)
        return JsonResponse({"like": f"{article.users_liked.count()}", 'article_id': article.pk})


class ArticleRemoveLike(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        article = Article.objects.get(pk=self.kwargs.get('pk'))
        article.users_liked.remove(self.request.user)
        return JsonResponse({"like": f"{article.users_liked.count()}", 'article_id': article.pk})

