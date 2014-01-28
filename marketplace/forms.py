from django import forms
#from django.core import validators
from django.core.exceptions import ValidationError

class SearchForm(forms.Form):
	q = forms.CharField(label='Search', required=False)
	
	def clean_q(self):
		q = self.cleaned_data['q']
		if len(q) < 1:
			raise ValidationError('Enter search query')
		return q

