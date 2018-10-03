from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Album

class indexView(generic.ListView):
    template_name="music/index.html"
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.all()

class detailsView(generic.DetailView):
    model = Album
    template_name = "music/details.html"

class AlbumCreate(CreateView):
    model = Album
    fields = ['title', 'artist', 'year', 'image']