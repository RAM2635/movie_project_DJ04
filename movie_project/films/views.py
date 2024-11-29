from django.shortcuts import render, redirect
from .forms import FilmForm
from .models import Film
from datetime import datetime

def add_film(request):
    if request.method == 'POST':
        form = FilmForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('film_list')
    else:
        form = FilmForm()
    return render(request, 'films/add_film.html', {'form': form, 'current_year': datetime.now().year})

def film_list(request):
    films = Film.objects.all()
    return render(request, 'films/film_list.html', {'films': films, 'current_year': datetime.now().year})

# Create your views here.
