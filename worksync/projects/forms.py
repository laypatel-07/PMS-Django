from django import forms
from .models import Project, Task
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Form for Project
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project 
        fields = ['projectname','description', 'photo']

# Form for User Registration
class UserRegistrationForm(UserCreationForm):  
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class TaskForm(forms.ModelForm):
    due_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=False
    )
    
    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'priority', 'assigned_to', 'due_date']