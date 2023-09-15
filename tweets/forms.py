from django import forms
from .models import Tweet


class TweetModelForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = [
            'user',
            'content'
        ]

    def clean_content(self):
        data = self.cleaned_data.get('content')
        if data == 'abc':
            raise forms.ValidationError('Cannot be ABC')
        return data
