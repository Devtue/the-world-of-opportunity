from django import forms
from django.utils.translation import gettext_lazy as _
from.import models
from .models import Comment
class CreateArticle(forms.ModelForm):
	class Meta:
		model=models.Article
		fields=['title','body','slug','thumb','url']

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['body']
		labels = {
		'body': _('Comment here')
		}
		widgets = {
            'body': forms.TextInput(attrs={'placeholder': 'Add a comment'}),
        }
