from rest_framework import serializers

from apps.cities.models import City, Region


#class RegionSerializer(serializers.ModelSerializer):
#    """Сериализатор модели Region."""
#
#    class Meta:
#        model = Region
#        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):
    """Сериализатор модели City."""

#    region = RegionSerializer()

    class Meta:
        model = City
        fields = ('id', 'name')
