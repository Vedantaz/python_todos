from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import UserProfile
from django import forms


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def form_valid(self, form):
        form.instance.user = self.request.user   #assign to the logged-in user
        return super().form_valid(form)

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label="Email / Username")

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'profile_picture', 'profession']