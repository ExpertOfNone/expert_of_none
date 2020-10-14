from django.views.generic import ListView

from blog.models import Blog


class HomeView(ListView):

    queryset = Blog.objects.published()
    template_name = 'blog/home.html'
    context_object_name = 'entries'

# TODO Add Date Detail View