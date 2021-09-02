from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *


class TaskEditForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        exclude = ['user']

class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username']