from django.shortcuts import render, HttpResponseRedirect
from .models import Article
from django.views.generic import DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

from .forms import ArticleCreateForm


# Create your views here.


context = {}


def archive(request):
    context['posts'] = Article.objects.all().select_related()
    return render(request, 'articles/archive.html', context)


class get_article(DetailView):
    model = Article
    context_object_name = 'article'
    template_name = 'articles/article.html'


class create_post(CreateView):
    model = Article
    fields = ['title', 'text', 'author', ]
    # form_class = ArticleCreateForm
    template_name = 'articles/article_form.html'
    # success_url = 'success'


    # def get(self, request, *args, **kwargs):
    #     context = {'form': ArticleCreateForm()}
    #     return render(request, 'articles/article.html', context)
    #
    # def post(self, request, *args, **kwargs):
    #     form = ArticleCreateForm(request.POST)
    #     if form.is_valid():
    #         article = form.save()
    #         article.save()
    #         return HttpResponseRedirect(reverse_lazy('archive:get_article', args=[article.pk]))
    #     return render(request, 'articles/article_form.html', {'form': form})

