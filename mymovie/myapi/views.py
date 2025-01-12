from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

def home(request):
    allMovies = Movie.objects.all() #select * from Movies
    
    context = {
        'Movie': allMovies,
    }

    return render(request, 'myapi/index.html', context)
    
#details page
def detail(request, id):
    movie = get_object_or_404(Movie, id=id) #select * from Movies where id = id
    
    context = {
        'movie': movie,
    }

    return render(request, 'myapi/details.html', context)

#adding a movie
def add_movies(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            if request.method == 'POST':
                form = MovieForm(request.POST or None)
                 #check if the form is valid
                if form.is_valid():
                    data=form.save(commit= False)
                    data.save()
                    return redirect('myapi:home')
            else:
                form = MovieForm()
            return render(request, 'myapi/addmovies.html', {'form': form})
        else:
            return redirect('myapi:home')
    return redirect('accounts:login')

#editing movies
def edit_movies(request, id):
    if request.user.is_authenticated:
        if request.user.is_superuser:
             #get the movie with the respective id
             movie = Movie.objects.get(id=id)
             #check if the request is a POST request
             if request.method == 'POST':
                form = MovieForm(request.POST or None, instance=movie)
                 #check if the form is valid
                if form.is_valid():
                    data=form.save(commit= False)
                    data.save()
                    return redirect('myapi:detail', id)
             else:
                form = MovieForm(instance=movie)
             return render(request, 'myapi/addmovies.html', {'form': form})
        else:
             return redirect('myapi:home')
    return redirect('accounts:login')
def delete_movies(request, id):
    if request.user.is_authenticated:
         if request.user.is_superuser:
             movie = Movie.objects.get(id=id)
             movie.delete()
             return redirect('myapi:home')
         else:
             return redirect('myapi:home')
    return redirect('accounts:login')


#adding a review
