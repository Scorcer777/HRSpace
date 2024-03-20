from rest_framework import serializers

from apps.languages.models import Language


class LanguageSerializer(serializers.ModelSerializer):
    """Сериализация модели - язык."""
    class Meta:
        fields = '__all__'
        model = Language
