from rest_framework import serializers

from apps.languages.models import Language


class LanguageSerializer(serializers.ModelSerializer):
    """
    Сериализатор модели 'Язык'.
    """
    class Meta:
        fields = '__all__'
        model = Language
