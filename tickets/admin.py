from django.contrib import admin
from .models import Cinema, Session
# Register your models here.

# Добавляю информацию о моделях в админку
@admin.register(Cinema)
class ObjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')
    search_fields = ('name',)

@admin.register(Session)
class ObjectAdmin(admin.ModelAdmin):
    list_display = ('cinema', 'title', 'date_time', 'total_seats', 'booked_seats')
    search_fields = ('name',)
