from django.contrib import admin
from .models import Plan
from .models import Detail

# Register your models here.

admin.site.register(Plan)
admin.site.register(Detail)