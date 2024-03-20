from rest_framework import serializers

from api.professions.serializers import ProfessionSerializer
from api.cities.serializers import CitySerializer
from apps.applications.models import Application, CandidateRequirements, JobInfo, RecruitRequirements
from apps.users.models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    """Пользователь."""
    class Meta:
        model = CustomUser


class JobInfoSerializer(serializers.ModelSerializer):
    """Сериализация модели - нформация об условиях труда."""
    class Meta:
        model = JobInfo
        fields = '__all__'


class CandidateRequirementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CandidateRequirements
        fields = '__all__'


class RecruitRequirementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecruitRequirements
        fields = '__all__'


class ApplicationSerializer(serializers.ModelSerializer):
    """Сериализация модели - заявка."""
    #user = UserSerializer(read_only=True,)
    profession = ProfessionSerializer()
    city = CitySerializer()
    job_info = JobInfoSerializer(required=False)
    candidate_requirements = CandidateRequirementsSerializer(required=False)
    recruit_requirements = RecruitRequirementsSerializer(required=False)

    class Meta:
        model = Application
        depth = 1
        read_only_fields = ('user', 'created_at')

    def validate(self, attrs):
        if attrs['min_salary'] > attrs['max_salary']:
            raise serializers.ValidationError(
                'Минимальная зарплата не может быть больше максимальной.'
            )
        if attrs['number_of_recruiters'] < 1 or attrs['number_of_recruiters'] > 10:
            raise serializers.ValidationError(
                'Количество сотрудников не должно быть меньше 1 и больше 10.'
            )
        return attrs
