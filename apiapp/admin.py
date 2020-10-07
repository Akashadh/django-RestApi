from django.contrib import admin
from .models import Hero

# Register your models here.


class HeroAdmin(admin.ModelAdmin):
    list_display = ['name', 'age']
    search_fields = ['name', ]
    list_filter = ['age', ]


admin.site.register(Hero, HeroAdmin)
