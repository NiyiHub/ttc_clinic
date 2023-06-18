from django.shortcuts import render
from rest_framework import viewsets
from .serializers import AppointmentSerializer, BlogSerializer, FaqSerializer
from .models import Appointment, Blog, Faq


class AppointmentView(viewsets.ModelViewSet):
	serializer_class = AppointmentSerializer
	queryset = Appointment.objects.all()


class BlogView(viewsets.ModelViewSet):
	serializer_class = BlogSerializer
	queryset = Blog.objects.all()


class FaqView(viewsets.ModelViewSet):
	serializer_class = FaqSerializer
	queryset = Faq.objects.all()
	