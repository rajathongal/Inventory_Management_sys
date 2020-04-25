from django.contrib import admin
from . import models

# Register your models here.

admin.site.register([models.Desktop,models.Laptop,models.Mobile])
