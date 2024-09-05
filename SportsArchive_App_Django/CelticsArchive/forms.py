from django import forms
from .models import LegendaryMoment

class LegendaryMomentForm(forms.ModelForm):
    class Meta:
        model = LegendaryMoment
        fields = ['title', 'description', 'date', 'video_url', 'boxscore_url']
        labels = {
            'title': 'Moment Title',
            'description': 'Moment Description',
            'date': 'Date of Moment',
            'video_url': 'Video URL (optional)',
            'boxscore_url': 'Boxscore URL (optional)',

        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Give the Moment a Name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Describe the Moment and what made it Legendary.', 'rows': 5}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'Date'}),
            'video_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Must provide YouTube *Embed* URL. (https://www.youtube.com/embed/YOURVIDEOID)', 'style': 'width: 96%;'}),
            'boxscore_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Provide BasketballReference.com URL', 'style': 'width: 96%;'}),

        }