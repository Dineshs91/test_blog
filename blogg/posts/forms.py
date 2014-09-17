from django import forms
from posts.models import UserPosts
from django.core.exceptions import ValidationError

def validate_input(value):
    if len(value.strip()) == 0:
        raise ValidationError('field empty')

class UserPostForm(forms.ModelForm):
	post_title = forms.CharField(
        max_length=100,
        help_text="Please enter the title",
        validators=[validate_input],
        error_messages={'required':'Post title is required', 'invalid':'Enter a valid post title'}
        )
	post_content = forms.CharField(
        widget=forms.Textarea, 
        validators=[validate_input],
        error_messages={'required':'Post content is required', 'invalid':'Add some content'}
        )

	class Meta:
		model = UserPosts
		fields=('post_title','post_content')
