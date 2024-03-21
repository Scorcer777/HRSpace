from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    """Сериализатор входа в систему"""

    email = serializers.CharField()
    password = serializers.CharField()
