from django.contrib import admin
from .models import Restaurant

class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('nom', 'rue', 'code_postal', 'ville')
    search_fields = ['ville']


# Register your models here.
admin.site.register(Restaurant, RestaurantAdmin)
