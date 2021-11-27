from django.contrib import admin
from .models import Worker, Shift, WorkPlanner
# Register your models here.

admin.site.register([Worker, Shift, WorkPlanner])
