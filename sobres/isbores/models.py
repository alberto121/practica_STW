from django.db import models

# Create your models here.
class Donor(models.Model):
	name = models.CharField(max_length=40)

	def __unicode__(self):
		return self.name

class Sobre(models.Model):
	date = models.DateTimeField()
	amount = models.IntegerField()
	concept = models.TextField(max_length=100)
	return self.donor.name+" - "+self.concept
