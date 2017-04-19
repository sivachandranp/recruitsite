from django import forms
from models import ApplicationForm

class FormApplication(forms.ModelForm):
	class Meta:
		model = ApplicationForm
		exclude = ['id', 'posted_date']
