from rest_framework import serializers

from apps.cities.models import City, Region


class CitySerializer(serializers.ModelSerializer):
    """Сериализация модели - Город."""
    class Meta:
        fields = ('id', 'name')
        model = City
