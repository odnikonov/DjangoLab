from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=200, unique=True, verbose_name='заголовок')
    author = models.ForeignKey(User,
                               null=True,
                               on_delete=models.CASCADE, verbose_name='автор')
    text = models.TextField(null=True, verbose_name='текст')
    created_date = models.DateField(auto_now_add=True,
                                    null=True, verbose_name='дата')

    def __str__(self):
        arr = ['Автор', 'Заголовок']
        if self.author:
            if self.author.username:
                arr[0] = self.author.username
            if self.title:
                arr[1] = self.title
        return "%s: %s" % (arr[0], arr[1])

    def get_excerpt(self):
        return self.text[:140] + "..." if len(self.text) > 140 else self.text

    def get_absolute_url(self):
        if self.pk:
            return reverse('archive:get_article', kwargs={'pk': self.pk})


    class Meta:
        verbose_name = 'статья'
