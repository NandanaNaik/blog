# from django import forms
# from .models import BlogPost, Comment

# class BlogPostForm(forms.ModelForm):
#     class Meta:
#         model = BlogPost
#         fields = ['title', 'content', 'categories']

# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ['content']


from django import forms
from .models import BlogPost, Comment

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'categories']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
