from rest_framework import serializers

from apps.industries.models import Industry


class IndustrySerializer(serializers.ModelSerializer):
    """Сериализация модели - отрасль."""
    class Meta:
        fields = '__all__'
        model = Industry
