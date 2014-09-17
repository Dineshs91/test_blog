from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

def validate_input(value):
    if len(value.strip()) == 0:
        raise ValidationError('field empty')

class UserRegisterForm(forms.ModelForm):
    """
    User registration form. All fields are required.
    """
    first_name = forms.CharField(
        max_length=15, 
        help_text="Firstname",
        validators=[validate_input]
        )
    last_name = forms.CharField(
        max_length=15, 
        help_text="Lastname",
        validators=[validate_input]
        )
    email = forms.EmailField(help_text='Email ID')
    username = forms.CharField(
        help_text='Username', 
        max_length=15,
        validators=[validate_input]
        )
    password = forms.CharField(
        widget=forms.PasswordInput, 
        max_length=15, 
        help_text="Password",
        validators=[validate_input]
        )
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password')
        
    def save(self, commit=True):
        user = super(UserRegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user