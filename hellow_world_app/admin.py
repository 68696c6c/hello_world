from django.contrib import admin

# import model
from hellow_world_app.models import Rock


# set up automated slug creation
class RockAdmin(admin.ModelAdmin):
    model = Rock
    list_display = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}


# Register your models here.
admin.site.register(Rock, RockAdmin)
