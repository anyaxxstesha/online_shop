from django.contrib.auth.forms import UserCreationForm
from django.forms import Form, EmailField, ValidationError
from catalog.forms import StyleFormMixin
from users.models import User


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class UserResetForm(StyleFormMixin, Form):
    email = EmailField()

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if not qs.exists():
            raise ValidationError('Пользователь с таким email не найден')
        self.user = qs.first()
        return email
