from django.views.generic import ListView
from .models import Blog


class HomeView(ListView):

    queryset = Blog.objects.published()
    template_name = 'blog/home.html'
    context_object_name = 'entries'
