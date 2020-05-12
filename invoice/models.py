from django.db import models

# Create your models here.
class Form(models.Model):
	productType = models.CharField(max_length=255)
	contactID = models.CharField(max_length=255)
	date = models.DateTimeField()
	dueDate = models.DateTimeField()
	lineAmountTypes = models.CharField(max_length=255)
	description = models.TextField()
	quantity = models.IntegerField()
	unitAmount = models.IntegerField()
	accountCode = models.IntegerField()
	discountRate = models.IntegerField()
