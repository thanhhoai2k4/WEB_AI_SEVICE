from django.db import models
from django import forms

class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)


class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()








# form

class MusicianForm(forms.ModelForm):
    class Meta:
        model = Musician
        fields = ["first_name", "last_name", "instrument"]

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nhập tên'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nhập họ'}),
            'instrument': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nhập nhạc cụ'}),
        }