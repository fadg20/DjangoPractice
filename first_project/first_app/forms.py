from django import forms
from .models import Post

class SearchForm(forms.Form):
    q = forms.CharField()

class TestForm(forms.Form):
    texto = forms.CharField(min_length=7, widget=forms.Textarea, required=False)
    boolean = forms.BooleanField()
    integer = forms.IntegerField()
    email = forms.EmailField()

    RADIO_CHOICES = [
        ('signin', 'Sign In'),
        ('signup', 'Sign Up'),
        ('forgotpassword', 'Forgot Password'),
    ]
    radio_choices = forms.CharField(min_length=7, widget=forms.RadioSelect(choices=RADIO_CHOICES))

class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['user', 'title', 'slug', 'image', 'content', 'draft', 'publish']
        exclude = []