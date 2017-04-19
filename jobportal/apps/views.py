from django.shortcuts import render
from django.views.generic import View
from forms import FormApplication

class ApplicationView(View):
	form_class = FormApplication
	template_name = 'application.html'

	def get(self, request, *args, **kwargs):
		"""
		This method executes on form load
		"""

		form = self.form_class()
		return render(request, self.template_name, {'form': form})

	def post(self, request, *args, **kwargs):
		"""
		This method executes when form is submitted. Once the form is validated successfully, 
		values are saved into table.
		"""
		
		form = self.form_class(request.POST)
		if form.is_valid():
			model = form.save(commit=False)
			model.status = 'Apply'
			model.save()
			return render(request, self.template_name, {'form': self.form_class(), 'success': True})
		else:
			return render(request, self.template_name, {'form': form})



