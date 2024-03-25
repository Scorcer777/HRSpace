from django.db import models

from apps.industries.models import Industry


class Profession(models.Model):
    """Профессия."""

    title = models.CharField(max_length=100, unique=True)
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Skill(models.Model):
    """Навык."""

    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title


class ProfessionSkill(models.Model):
    """Ключевой навык, относящийся к определенной профессии."""

    profession = models.ForeignKey(Profession, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('profession', 'skill')

    def __str__(self) -> str:
        return self.skill.title
