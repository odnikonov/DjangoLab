from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.models import User

def home(request):
    return render(request, 'flatpages/static_handler.html', {})
    # return HttpResponse(u'Привет, Мир!')
# , content_type="text/plain"


class register(CreateView):
    template_name = "user_add.html"
    model = User
    fields = ['food']
    success_url = reverse_lazy('formulahome')

    def form_valid(self, form):
        self.object = form.save(commit = False)
        self.object.maker = User.objects.get(pk=1)
        form.save()
        return reverse_lazy('formula home')
