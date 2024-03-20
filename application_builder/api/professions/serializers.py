from rest_framework import serializers

from apps.professions.models import Profession


class ProfessionSerializer(serializers.ModelSerializer):
    """Сериализация модели - Профессия."""
    class Meta:
        fields = ('id', 'title')
        model = Profession
