from django import forms

class CommentForm(forms.Form):
    author = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Your Name'}
        ),
    )
    context = forms.CharField(
        widget=forms.Textarea(
            attrs={'class': 'form-control', 'placeholder': 'Leave your comment!'}
        )
    )