from .models import Movies
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, Select, FileInput, NumberInput


class MoviesForm(ModelForm):
    class Meta:
        model = Movies
        fields = ['title', 'original_lang_title', 'type_item', 'date', 'description',
                  'mdb_link','poster','year']
        
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'original_lang_title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Original Title'}),
            'type_item ': Select(attrs={'class': 'form-control', 'placeholder': 'Item Type'}),
            'date': DateTimeInput(attrs={'class': 'form-control', 'placeholder':'Date'}),
            'description': Textarea(attrs={'class': 'form-control', 'placeholder': 'description'}),
            'mdb_link': TextInput(attrs={'class': 'form-control', 'placeholder': 'link to movie db'}),
            'poster': FileInput(attrs={'class': 'form-control', 'placeholder': 'Poster'}),
            'year' : NumberInput(attrs={'class': 'form-control', 'placeholder': 'Year'})   
        }