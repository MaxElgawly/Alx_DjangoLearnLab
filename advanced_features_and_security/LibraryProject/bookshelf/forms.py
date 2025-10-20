from django import forms
from .models import Book

class ExampleForm(forms.ModelForm):
    """
    ExampleForm is used to securely handle Book data input.
    Includes validation to prevent malicious input (e.g., SQL injection or XSS).
    """
    class Meta:
        model = Book
        fields = ['title', 'author', 'description']

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if any(char in title for char in [';', '--', "'"]):
            raise forms.ValidationError("Invalid characters in title.")
        return title
