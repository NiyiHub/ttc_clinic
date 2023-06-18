from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import AppointmentView, BlogView, FaqView

router = routers.DefaultRouter()
router.register(r'appointments', AppointmentView, 'appointment')
router.register(r'blogs', BlogView, 'blog')
router.register(r'faqs', FaqView, 'faq')


urlpatterns = [
	path('', include(router.urls)),
]