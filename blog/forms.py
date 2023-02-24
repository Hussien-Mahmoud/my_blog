from django import forms


class CommentForm(forms.Form):
    name = forms.CharField(max_length=200, label='Your Name')
    email = forms.EmailField(required=True, label='Your Email')
    comment = forms.CharField(widget=forms.Textarea,required=True, label='Comment')
