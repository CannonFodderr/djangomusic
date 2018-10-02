from django.shortcuts import render, get_object_or_404
from .models import Album, Song

# Create your views here.
def index(request):
    all_albums = Album.objects.all()
    return render(request, 'music/index.html', {'albums':all_albums})

def details(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    return render(request, 'music/details.html', {'album':album})

def favorite(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    try:
        print(request.POST)
        selected_song = album.song_set.get(id=request.POST['song'])
    except (KeyError, Song.DoesNotExist):
        return render(request, 'music/details.html', {'album': album, 'error_message': 'You did not select a song!'})
    else:
        if selected_song.is_favorite:
            selected_song.is_favorite = False
        else:
            selected_song.is_favorite = True
        selected_song.save()
        return render(request, 'music/details.html', {'album':album})