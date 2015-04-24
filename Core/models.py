from django.db import models

class BHK(models.Model):
	bhk=models.FloatField(unique=True)
	def __str__(self):
		return str(self.bhk)

class Company(models.Model):
	name=models.CharField(unique=True,null=False,max_length=50)
	def __str__(self):
		return self.name

class City(models.Model):
	name=models.CharField(unique=True,null=False,max_length=50)
	def __str__(self):
		return self.name

class Location(models.Model):
	name=models.CharField(unique=True,null=False,max_length=50)
	def __str__(self):
		return self.name

class Flat(models.Model):
	url=models.URLField(unique=True,null=False)
	title=models.CharField(max_length=100)
	price=models.CharField(max_length=10)
	bhk=models.ForeignKey(BHK)
	address=models.CharField(max_length=300)
	location=models.ForeignKey(Location)
	area=models.CharField(max_length=20)
	pic_url=models.URLField()
	def __str__(self):
		return str(self.url)

class LocationCompanyCity(models.Model):
	location=models.ForeignKey(Location)
	company=models.ForeignKey(Company)
	city=models.ForeignKey(City)
	def __str__(self):
		return str(self.location) + ' : ' + str(self.company) 
	class Meta:
		unique_together=['location','company','city']



