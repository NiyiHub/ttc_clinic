from rest_framework import serializers
from .models import Appointment, Blog, Faq


class AppointmentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Appointment
		fields = ('id', 'name', 'phone', 'email', 'date', 'time', 'note')


class BlogSerializer(serializers.ModelSerializer):
	class Meta:
		model = Blog
		fields = ('id', 'title', 'pub_date', 'body', 'image')


class FaqSerializer(serializers.ModelSerializer):
	class Meta:
		model = Faq
		fields = ('id', 'question', 'answer')