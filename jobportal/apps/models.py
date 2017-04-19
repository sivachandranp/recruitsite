from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.

class ApplicationForm(models.Model):
	TITLE_CHOICES = (('Mr', 'Mr'), ('Mrs', 'Mrs'), ('Ms', 'Ms'), ('Miss', 'Miss'),)
	POSITIONS = (('Development','Development'), ('Testing', 'Testing'), ('Admin', 'Admin'))

	title = models.CharField(max_length=10,blank = True, null = True, choices=TITLE_CHOICES, default = 'Mr')
	first_name = models.CharField(max_length=250, verbose_name='Name')
	address = models.TextField()
	mobile_number = models.CharField(max_length=60, verbose_name = 'Mobile Number')
	email = models.EmailField()
	position_sought = models.CharField(max_length=100, choices= POSITIONS, default='Development')
	posted_date = models.DateTimeField(default=timezone.now)
	status = models.CharField(max_length=100,blank = True, null = True, default='Apply')
	
	class Meta:
		db_table = 'application_form'

	def __str__(self):
		return self.first_name







