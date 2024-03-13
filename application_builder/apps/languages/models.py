from django.db import models

from . import LEVEL_CHOICES


class Language(models.Model):
    """Язык."""

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class LanguageProficiency(models.Model):
    """Знание языков."""

    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    proficiency_level = models.CharField(max_length=20, choices=LEVEL_CHOICES)

    def __str__(self):
        return f'{self.language.name} - {self.proficiency_level}'
