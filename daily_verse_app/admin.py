from django.contrib import admin

# Register your models here.
from .models import Verse, ShownVerse

@admin.register(Verse)
class VerseAdmin(admin.ModelAdmin):
    list_display = ("reference", "translation", "book")
    search_fields = ("reference", "text", "book", "translation")

@admin.register(ShownVerse)
class ShownVerseAdmin(admin.ModelAdmin):
    list_display = ("verse", "date_shown", "translation", "book")
    list_filter = ("date_shown", "translation", "book")
