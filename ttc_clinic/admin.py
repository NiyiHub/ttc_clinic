from django.contrib import admin
from .models import Appointment, Blog, Faq


class AppointmentAdmin(admin.ModelAdmin):
	list_display = ('name', 'phone', 'email', 'date', 'time', 'note')


class BlogAdmin(admin.ModelAdmin):
	list_display = ('title', 'pub_date', 'body', 'image')


class FaqAdmin(admin.ModelAdmin):
	list_display = ('question', 'answer')


admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Faq, FaqAdmin)


