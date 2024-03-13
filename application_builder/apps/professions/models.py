from django.db import models


class Profession(models.Model):
    """Профессия."""

    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
