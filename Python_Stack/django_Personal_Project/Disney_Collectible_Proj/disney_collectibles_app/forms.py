from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your forms here.

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    First_Name = forms.CharField(max_length=255)
    Last_Name = forms.CharField(max_length=255)

    class Meta:
        model = User
        fields = ("First_Name", "Last_Name", "username",
                  "email", "password1", "password2")

        def save(self, commit=True):
            user = super(NewUserForm, self).save(commit=False)
            user.First_Name = self.cleaned_data['First_Name']
            user.Last_Name = self.cleanded_data['Last_Name']
            user.email = self.cleaned_data['email']
            if commit:
                user.save()
            return user
