from django import forms
from rango.models import Page, Category

max_char = 128
max_url = 200


class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=max_char,
                           help_text="Please enter the category name.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Category
        fields = ('name',)


class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=max_char,
                            help_text="Please enter the title of the page.")
    url = forms.URLField(max_length=max_url,
                         help_text="Please enter the URL of the page.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Page
        exclude = ('category',)
