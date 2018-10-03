from django.views import generic
from .models import Album

class indexView(generic.ListView):
    template_name="music/index.html"

    def get_queryset(self):
        return Album.objects.all()

class detailsView(generic.DetailView):
    model = Album
    template_name = "music/details.html"
