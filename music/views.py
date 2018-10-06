from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Album
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from .forms import UserForm, UserLogin

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

class AlbumUpdate(UpdateView):
    model = Album
    fields = ['title', 'artist', 'year', 'image']

class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')

class UserFormView(View):
    form_class = UserForm
    template_name = 'music/registration.html'

    # Display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form })
    
    # Process Form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            # cleaned normalized data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # Authenticate
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    print(f"{request.user.username} logged in")
                    return redirect('music:index')
        return render(request, self.template_name, {'form': form })

class Login(View):
    template_name = 'music/login.html'
    form_class = UserLogin

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form })

    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('music:index')
        return redirect('/login')

class Logout(View):
    def get(self, request):
        if request.user is not None:
            print(f" logging out {request.user.username}")
            logout(request)
        return redirect('music:index')