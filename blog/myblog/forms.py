from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Comment


class SignUpForm(forms.Form):
    username = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "inputUsername",
                "placeholder": "Имя пользователя",
            }
        ),
    )

    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id": "inputPassword",
                "placeholder": "Пароль",
            }
        ),
    )
    repeat_password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id": "ReInputPassword",
                "placeholder": "Повторите пароль",
            }
        ),
    )

    def clean(self):
        password = self.cleaned_data["password"]
        confirm_password = self.cleaned_data["repeat_password"]

        if password != confirm_password:
            raise forms.ValidationError("Пароли не совпадают")

    def save(self):
        user = User.objects.create_user(
            username=self.cleaned_data["username"],
            password=self.cleaned_data["password"],
        )
        #user.save()
        auth = authenticate(**self.cleaned_data)
        return auth

class SignInForm(forms.Form):
    username = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "inputUsername",
                "placeholder": "Имя пользователя",
            }
        ),
    )

    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id": "inputPassword",
                "placeholder": "Пароль",
            }
        ),
    )
    
class FeedBackForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'name',
            'placeholder': 'Ваше имя'
        })
    )
    
    email = forms.CharField(
        max_length=100,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'id': 'email',
            'placeholder': 'Ваша почта'
        })
    )
    
    subject = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'subject',
            'placeholder': 'Тема сообщения'
        })    
    )
    message = forms.CharField(
        max_length=100,
        widget=forms.Textarea(attrs={
            'class': 'form-control md-textarea',
            'id': 'message',
            'placeholder': 'Ваше сообщение'
        })
    )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        widgets = {
            'text': forms.Textarea(attrs={
                'class':'form-control mb-3',
                'rows':3
            }),
        }
    
        