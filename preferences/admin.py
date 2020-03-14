from django.contrib import admin

# Register your models here.
from preferences.models import Preference

admin.site.register(Preference)