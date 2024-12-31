from django.db import models
from django.utils import timezone


class TextTransformation(models.Model):
    original_text = models.TextField()
    transformed_text = models.TextField(blank=True)
    fonction = models.TextField()
    date = models.DateField(default=timezone.now)
    def __str__(self):
        return self.original_text

    def title(self):
        return f'{self.original_text[:10]} - {self.date}'