from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import profile,currency


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class Userupdateform(forms.ModelForm):
	email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control'}),required=True,)
	username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','Placeholder':"Enter User Name"}),required=True)
	class Meta:
		model = User
		fields = ['username', 'email']

class Userupdateprofile(forms.ModelForm):
	class Meta:
		model = profile
		fields = ['image']

class Opps(forms.Form):
	CHOICES=[('+','Add'),
         ('-','Mutltiply')]

	Operation = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
	value1 = forms.IntegerField()
	value2 = forms.IntegerField()

class customformajax(forms.Form):
# 	FAVORITE_COLORS_CHOICES = [
#     ('blue', 'Blue'),
#     ('green', 'Green'),
#     ('black', 'Black'),
# ]
	Name = forms.CharField(widget=forms.TextInput(attrs={'id': 'name', 'placeholder':'Shahzaib'}))
	Email = forms.CharField(widget=forms.EmailInput(attrs={'id':'email','placeholder':'email'}))
	# choice_field = forms.ChoiceField(widget=forms.RadioSelect({'id':'radio','name':'radio'}), choices=FAVORITE_COLORS_CHOICES)