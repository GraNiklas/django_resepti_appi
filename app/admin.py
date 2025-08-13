from django.contrib import admin

# Register your models here.
from app.models import Resepti, Vaihe, ReseptiAines

@admin.register(Resepti)
class ReseptiAdmin(admin.ModelAdmin):
    pass

@admin.register(Vaihe)
class VaiheAdmin(admin.ModelAdmin):
    pass

@admin.register(ReseptiAines)
class ReseptiAinesAdmin(admin.ModelAdmin):
    pass