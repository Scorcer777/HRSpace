from django.db import models


class Profession(models.Model):
    """Профессия."""

    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Skill(models.Model):
    """Навык."""

    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class ProfessionSkill(models.Model):
    """Ключевой навык, относящийся к определенной профессии."""

    profession = models.ForeignKey(Profession, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('profession', 'skill')
