from django.contrib import admin

# Register your models here.
from .models import * #  * = means import all

admin.site.register(Task)