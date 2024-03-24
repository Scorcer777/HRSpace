from rest_framework import serializers

from apps.citizenships.models import Citizenship


class CitizenshipSerializer(serializers.ModelSerializer):
    """
    Сериализатор модели 'Гражданство'.
    """
    class Meta:
        fields = '__all__'
        model = Citizenship
