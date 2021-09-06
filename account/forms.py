from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
User= get_user_model()

class CustomUserCreateForm(UserCreationForm):
    class Meta:
        model= User
        fields= ['username', 'email', ]

    #removing the help text
    def __init__(self, *args, **kwargs):
        super(CustomUserCreateForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model= User
        fields= ['username', 'email', ]