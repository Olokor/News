from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, UpdateView, DetailView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Article
# Create your views here.

class ArticleListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = 'article_list.html'


class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Article
    template_name = "article_detail.html"


class ArticleUpdateView(UserPassesTestMixin,LoginRequiredMixin, UpdateView):
    model = Article
    fields = ('title', 'body')
    template_name = 'article_update.html'

    def test_func(self):
        obj = self.get_object()
        return  obj.author == self.request.user

class ArticleDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):

    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')

    def test_func(self):
        obj = self.get_object()
        return  obj.author == self.request.user

class ArticleCreateView(LoginRequiredMixin, CreateView):

    model = Article
    template_name = "article_create.html"
    fields = ("title", "body")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)







