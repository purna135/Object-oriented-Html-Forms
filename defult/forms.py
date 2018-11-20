from django import forms

class myForm(forms.Form):
	name = forms.CharField()
	password = forms.CharField()
	password3 = forms.CharField()