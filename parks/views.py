from django.views.generic import DetailView


class ParkDetailView(DetailView):

    template_name = 'parks/details.html'
    context_object_name = 'park'



