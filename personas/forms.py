from django import forms
from .models import User, Movie

class UserForm(forms.ModelForm):
    # seleccionar películas favoritas existentes
    favourite_movies = forms.ModelMultipleChoiceField(
        queryset=Movie.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Favourite Movies"
    )

    birthdate = forms.DateField(
        label="Birthdate",
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'birthdate', 'has_insurance', 'favourite_movies']

#crear nuevas peliculas
class MovieForm(forms.Form):
    new_movie_title = forms.CharField(
        max_length=100,
        required=True,
        label="New Movie Title"
    )
    
    new_movie_genre = forms.CharField(
        max_length=100,
        required=True,
        label="New Movie Genre"
    )
