from django.contrib import admin
from messaging.models import *
# Register your models here.

admin.site.register(Nachricht)

admin.site.register(Direktnachricht)

admin.site.register(Kreis)
admin.site.register(Thema)