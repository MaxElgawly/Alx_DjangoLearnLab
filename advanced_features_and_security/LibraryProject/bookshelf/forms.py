from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description']

    # Extra validation example
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if any(char in title for char in [';', '--', "'"]):
            raise forms.ValidationError("Invalid characters in title.")
        return title
