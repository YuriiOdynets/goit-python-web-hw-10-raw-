from django import forms
from django .forms import ModelForm, CharField, TextInput, ModelChoiceField
from . models import Author, Quote

class AuthorForm(ModelForm):
    name = CharField(min_length=3, max_length=100, required=True, widget=TextInput())
    born_date = CharField(min_length=1, max_length=25, widget=TextInput())
    bio = CharField()
    user = CharField()

    class Meta:
        model = Author
        fields = ['name', 'born_date', 'bio', 'user']

class QuoteForm(ModelForm):
    text = CharField(widget=forms.Textarea)
    author = ModelChoiceField(queryset=Author.objects.all(), empty_label="Select Author")
    user = CharField()

    class Meta:
        model = Quote
        fields = ['text', 'author']