from django.db import models


class Citizenship(models.Model):
    """Гражданство."""

    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
