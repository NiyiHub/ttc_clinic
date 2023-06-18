from django.db import models
from django.utils import timezone


class Appointment(models.Model):
    time_choices = (
        ('morning', "Morning"),
        ('evening', "Evening")
    )
    name = models.CharField(max_length=120)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    date = models.DateField(default=timezone.now)
    time = models.CharField(choices=time_choices, max_length=10)
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name}-{self.doctor.name}"


class Blog(models.Model):
	title						= models.CharField(max_length=255)
	pub_date					= models.DateTimeField(auto_now_add=True)
	body						= models.TextField()
	image						= models.ImageField(upload_to='Images/')

	def __str__(self):
		return self.title

	def summary(self):
		return self.body[:100]

	def pub_date_cut(self):
		return self.pub_date.strftime('%b %e %Y')


class Faq(models.Model):
    question = models.CharField(max_length=120)
    answer = models.TextField()

    def __str__(self):
        return self.question