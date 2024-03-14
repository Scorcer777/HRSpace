from django.db import models


class Industry(models.Model):
    """Отрасль."""

    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title
