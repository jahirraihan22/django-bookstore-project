from django import forms
from books.models import Review


class ReviewForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control', 'placeholder': 'Write a review here...', 'cols': '30', 'rows': '5'}))
    image = forms.ImageField(required=False)

    class Meta:
        model = Review
        fields = ['body', 'image']
        # widgets = {
        #     'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write a review here...', 'cols': '30', 'rows': '5'})
        # }
