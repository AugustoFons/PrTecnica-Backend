
from django.shortcuts import render, redirect, get_object_or_404
from .models import User, Movie
from django.db.models import Q
from .forms import UserForm, MovieForm

# Obtener todos los usuarios y películas favoritas
def all_users(request):
    users = User.objects.prefetch_related('favourite_movies').all()
    return render(request, 'base.html', {
        'users': users
    })

# Crear usuario
def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        # validar un max de 3 peliculas favoritas
        if form.is_valid():
            favourite_movies = form.cleaned_data.get('favourite_movies')
            if favourite_movies and len(favourite_movies) > 3:
                form.add_error('favourite_movies', 'You can select a maximum of 3 favourite movies.')
            else:
                user = form.save()
                return redirect('all_users')
    else:
        form = UserForm()
    
    return render(request, 'add.html', {'form': form})

# Crear pelicula
def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            new_movie_title = form.cleaned_data['new_movie_title']
            new_movie_genre = form.cleaned_data['new_movie_genre']
            Movie.objects.get_or_create(title=new_movie_title, genre=new_movie_genre)
            return redirect('add_user') 
    else:
        form = MovieForm()
    
    return render(request, 'add_movie.html', {'form': form})

# editar usuario
def edit_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('all_users')
    else:
        form = UserForm(instance=user)
    
    return render(request, 'edit_user.html', {'form': form, 'user': user})

# eliminar usuario
def delete_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    user.delete()
    return redirect('/')

# busquedas
def user_list(request):
    query = request.GET.get('q', '')  # Obtener el parámetro de búsqueda de la URL
    users = User.objects.all()
    
    if query:
        # busqueda por nombre + apellido
        if ' ' in query:
            first_name, last_name = query.split(' ', 1)
            users = users.filter(
                Q(first_name__icontains=first_name) & 
                Q(last_name__icontains=last_name)
            )
        else:
            # Buscar por nombre, apellido o ID
            users = users.filter(
                Q(first_name__icontains=query) |
                Q(last_name__icontains=query) |
                Q(id__icontains=query)
            )

    return render(request, 'base.html', {'users': users, 'query': query})