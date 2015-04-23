from django.db import models

class BHK(models.Model):
	bhk=models.IntegerField(unique=True)
	def __str__(self):
		return self.bhk

class Company(models.Model):
	name=models.CharField(unique=True,null=False,max_length=50)
	def __str__(self):
		return self.name

class City(models.Model):
	name=models.CharField(unique=True,null=False,max_length=50)
	def __str__(self):
		return self.name

class Flat(models.Model):
	url=models.URLField(unique=True,null=False)
	title=models.CharField(max_length=100)
	price=models.CharField(max_length=10)
	bhk=models.ForeignKey(BHK)
	location=models.CharField(max_length=100)
	area=models.CharField(max_length=20)
	pic_url=models.URLField()
	def __str__(self):
		return self.url

class CompanyFlat(models.Model):
	company=models.ForeignKey(Company)
	flat=models.ForeignKey(Flat)
	city=models.ForeignKey(City)

	

