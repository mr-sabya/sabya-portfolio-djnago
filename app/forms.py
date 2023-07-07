from django import forms

from .models import Comment, Order

class NewCommentForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = Comment
        fields = ('name', 'email', 'comment')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'placeholder': 'Full Name*', 'class': 'form-control', 'required': ''})
        self.fields['email'].widget.attrs.update({'placeholder': 'Email*', 'class': 'form-control', 'required': ''})
        self.fields['comment'].widget.attrs.update({'placeholder': 'Comment*', 'class': 'form-control', 'required': '', 'cols': 10, 'rows': 5})


    

class NewOrderForm(forms.ModelForm):
    email = forms.EmailField()
    
    class Meta:
        model = Order
        fields = ('subject', 'name', 'email', 'phone', 'details', 'budget')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'placeholder': 'Full Name*', 'class': 'form-control', 'required': ''})