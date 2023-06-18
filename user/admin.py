from django.contrib import admin
from .models import TtcUser  


class TtcUserAdmin(admin.ModelAdmin):
	list_display = ('email', 'first_name', 'last_name')


admin.site.register(TtcUser,TtcUserAdmin)