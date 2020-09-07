from django.contrib import admin
from reminderlist import models

# Register your models here.
admin.site.register([
    models.Post,
    models.Like,
    models.Comment,
])