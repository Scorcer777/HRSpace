from django.db import models


class City(models.Model):
    """Город."""

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Citizenship(models.Model):
    """Гражданство."""

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
