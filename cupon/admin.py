from django.contrib import admin
from cupon.models import Cupon

# Register your models here.

class CuponAdmin(admin.ModelAdmin):
    list_display = ('name', 'valid', 'expired', 'discount', 'available')


admin.site.register(Cupon, CuponAdmin)