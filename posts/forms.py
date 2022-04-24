from django import forms
from .models import Post


# creating a form
class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        
        exclude = ['user','slug'] 

        # fields = '__all__'
        
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'content': forms.Textarea(attrs={'class':'form-control'}),
            'category':forms.Select(attrs={'class':'form-control'}),
            'user':forms.Select(attrs={'class':'form-control'}),
        }