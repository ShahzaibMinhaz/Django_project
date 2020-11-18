from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import profile,invoiceheader,itemdetails


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

class Invoice(forms.ModelForm):
	class Meta:
		model = invoiceheader
		fields = ("Name","Total_Price")

class Invoice_details(forms.ModelForm):
	Item_Name = forms.CharField(widget=forms.TextInput(attrs={'id': 'item_name', 'placeholder':'Shirt'}))
	Item_quentity = forms.IntegerField(widget=forms.TextInput(attrs={'id': 'item_quantity', 'placeholder':'quantity'}))	
	Item_Price = forms.IntegerField(widget=forms.TextInput(attrs={'id': 'item_price', 'placeholder':'price'}))

	class Meta:
		model = itemdetails
		fields = ("Item_Name","Item_quentity","Item_Price")
