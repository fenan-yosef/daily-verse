
from django.db import models
from django.utils import timezone

class Verse(models.Model):
    reference = models.CharField(max_length=100)
    text = models.TextField()
    translation = models.CharField(max_length=20, default="kjv")
    book = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.reference} ({self.translation})"

class ShownVerse(models.Model):
    verse = models.ForeignKey(Verse, on_delete=models.CASCADE)
    date_shown = models.DateField(default=timezone.now)
    translation = models.CharField(max_length=20, default="kjv")
    book = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        unique_together = ("date_shown", "translation", "book")

    def __str__(self):
        return f"{self.verse.reference} shown on {self.date_shown} ({self.translation})"
