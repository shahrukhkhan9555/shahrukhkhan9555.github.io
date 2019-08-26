from django.db import models
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import uuid

#from django.contrib.auth.models import User
# Create your models here.
class feedback(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    feedback = models.CharField(max_length=500)
    def __str__(self):
        return self.first_name

class feedbackform(ModelForm):
    class Meta:
        model = feedback
        fields = ['first_name', 'last_name', 'feedback']

class Signupform(UserCreationForm):

    #username = models.CharField(max_length=20)
    #passw = models.CharField(max_length=20)
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password' )

class Profile(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=20)
    start_date = models.DateField()
    members = models.ManyToManyField(User)

class Profileform(ModelForm):
    class Meta:
        model = Profile
        fields = ('project_name', 'start_date', 'members')
    def __str__(self):
        return self.members

"""
class Signupform(ModelForm):
    class Meta:
        model = myUsers
        fields = ['first_name', 'last_name', 'username', 'passw', 'email']

class Loginform(ModelForm):
    class Meta:
        model = myUsers
        fields = ['username','passw']
        """