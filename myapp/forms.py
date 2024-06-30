from django import forms

from myapp.models import Movie


class MovieForm(forms.Form):

    title=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control border border-info"}))

    year=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control border border-info"}))

    director=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control border border-info"}))

    run_time=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control border border-info"}))

    language=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control border border-info"}))

    genre=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control border border-info"}))


class MovieModelForm(forms.ModelForm):

    class Meta:

        model=Movie
        # fields="__all__"
        # fields=["title","year",.......]
        exclude=("id",)

        widgets={
            "title":forms.TextInput(attrs={"class":"form-control border border-info"}),
            "year":forms.TextInput(attrs={"class":"form-control border border-info"}),
            "director":forms.TextInput(attrs={"class":"form-control border border-info"}),
            "run_time":forms.NumberInput(attrs={"class":"form-control border border-info"}),
            "language":forms.TextInput(attrs={"class":"form-control border border-info"}),
            "genre":forms.TextInput(attrs={"class":"form-control border border-info"})
        }
