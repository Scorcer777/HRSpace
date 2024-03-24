from rest_framework import serializers

from apps.cities.models import City


class CitySerializer(serializers.ModelSerializer):
    """
    Сериализатор модели 'Город'.
    """
    class Meta:
        fields = ('id', 'name')
        model = City
