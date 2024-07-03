from django.contrib import admin
from . import models
admin.site.register(models.Classes)
admin.site.register(models.Books)
admin.site.register(models.Chapter)
admin.site.register(models.SingleClass)
admin.site.register(models.BookPdf)
