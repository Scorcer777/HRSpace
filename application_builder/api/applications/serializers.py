from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.db import transaction

from apps.applications.models import (JobInfo, CandidateRequirements,
                                      RecruitRequirements, Application)
from apps.applications import (EMPLOYMENT_TYPES, WORK_MODELS,
                               SCHEDULE_TYPES, CONTRACT_TYPES,
                               WORKING_CONDITIONS, EDUCATION_TYPES,
                               EXPERIENCES, DRIVING_SKILLS,
                               RECRUITER_RESPONSIBILITIES)
from .services import ApplicationService


User = get_user_model()


class ApplicationCreateSerializer(serializers.ModelSerializer):
    """Сериализатор для валидации данных раздела общей информации."""
    class Meta:
        model = Application
        fields = (
            'title',
            'profession',
            'city',
            'min_salary',
            'max_salary',
            'number_of_employees',
            'start_working',
            'number_of_recruiters',
        )


class JobInfoCreateSerializer(serializers.ModelSerializer):
    """Сериализатор для валидации данных раздела условий труда."""
    employment_type = serializers.MultipleChoiceField(
        allow_blank=True,
        allow_null=True,
        choices=EMPLOYMENT_TYPES,
        required=False
    )
    schedule = serializers.MultipleChoiceField(
        allow_blank=True,
        allow_null=True,
        choices=SCHEDULE_TYPES,
        required=False
    )
    work_model = serializers.MultipleChoiceField(
        allow_blank=True,
        allow_null=True,
        choices=WORK_MODELS,
        required=False)
    contract_type = serializers.MultipleChoiceField(
        allow_blank=True,
        allow_null=True,
        choices=CONTRACT_TYPES,
        required=False
    )
    working_conditions = serializers.MultipleChoiceField(
        allow_blank=True,
        allow_null=True,
        choices=WORKING_CONDITIONS,
        required=False
    )

    class Meta:
        model = JobInfo
        fields = (
            'employment_type',
            'schedule',
            'work_model',
            'contract_type',
            'working_conditions',
            'description'
        )


class CandidateRequirementsCreateSerializer(serializers.ModelSerializer):
    """Сериализатор для валидации  данных раздела требований к соискателю."""
    education = serializers.MultipleChoiceField(
        allow_blank=True,
        allow_null=True,
        choices=EDUCATION_TYPES,
        required=False
    )
    experience = serializers.MultipleChoiceField(
        allow_blank=True,
        allow_null=True,
        choices=EXPERIENCES,
        required=False
    )
    driving_skills = serializers.MultipleChoiceField(
        allow_blank=True,
        allow_null=True,
        choices=DRIVING_SKILLS,
        required=False
    )

    class Meta:
        model = CandidateRequirements
        fields = (
            'education',
            'experience',
            'language_skills',
            'driving_skills',
            'has_medical_certificate',
            'has_photo',
            'citizenship',
            'core_skills',
            'requirements_description'
        )


class RecruiterRequirementsCreateSerializer(serializers.ModelSerializer):
    """Сериализатор для создания разделя требований к рекрутеру."""
    recruiter_responsibilities = serializers.MultipleChoiceField(
        allow_blank=True,
        allow_null=True,
        choices=RECRUITER_RESPONSIBILITIES, required=False)

    class Meta:
        model = RecruitRequirements
        fields = (
            'city',
            'industry',
            'english_skills',
            'recruiter_responsibilities',
            'description',
            'candidate_resume_form',
            'stop_list'
        )


class FullApplicationCreateSerializer(serializers.Serializer):
    """Сериализатор для создания заявки."""
    application = ApplicationCreateSerializer()
    job_info = JobInfoCreateSerializer()
    candidate_requirements = CandidateRequirementsCreateSerializer()
    recruiter_requirements = RecruiterRequirementsCreateSerializer()

    @transaction.atomic
    def save(self):
        current_user = self.context.get('request').user
        service = ApplicationService()
        # Creation of an Application object.
        application = service.create_application(
            self.validated_data, current_user
        )
        # Creation of an JobInfo object.
        service.create_job_info(self.validated_data, application)
        # Creation of a CandidateRequirements object.
        service.create_candidate_requirements(self.validated_data, application)
        # Creation of a RecruitRequirements object.
        return self.instance


class ApplicationReadSerializer(serializers.ModelSerializer):
    """Сериализатор для чтения раздела общей информации."""
    user = serializers.StringRelatedField()
    profession = serializers.StringRelatedField()
    city = serializers.StringRelatedField()

    class Meta:
        model = Application
        fields = (
            'user',
            'title',
            'profession',
            'city',
            'min_salary',
            'max_salary',
            'number_of_employees',
            'start_working',
            'number_of_recruiters',
        )
        read_only_fields = '__all__'


class JobInfoReadSerializer(serializers.ModelSerializer):
    """Сериализатор для чтения раздела условий труда."""

    class Meta:
        model = JobInfo
        fields = (
            'employment_type',
            'schedule',
            'work_model',
            'contract_type',
            'working_conditions',
            'description'
        )
        read_only_fields = '__all__'


class CandidateRequirementsReadSerializer(serializers.ModelSerializer):
    """Сериализатор для чтения раздела требований к кандидату."""
    language_skills = serializers.StringRelatedField(many=True)
    citizenship = serializers.StringRelatedField(many=True)
    core_skills = serializers.StringRelatedField(many=True)

    class Meta:
        model = CandidateRequirements
        fields = (
            'education',
            'experience',
            'language_skills',
            'driving_skills',
            'has_medical_certificate',
            'has_photo',
            'citizenship',
            'core_skills',
            'requirements_description'
        )


class RecruiterRequirementsReadSerializer(serializers.ModelSerializer):
    """Сериализатор для чтения раздела требований к рекрутеру."""
    city = serializers.StringRelatedField(many=True)
    industry = serializers.StringRelatedField(many=True)

    class Meta:
        model = RecruitRequirements
        fields = (
            'city',
            'industry',
            'english_skills',
            'recruiter_responsibilities',
            'description',
            'candidate_resume_form',
            'stop_list'
        )
        read_only_fields = '__all__'


class FullApplicationReadSerializer(serializers.Serializer):
    """Сериализатор для чтения заяки целиком."""
    application = ApplicationReadSerializer()
    job_info = JobInfoReadSerializer()
    candidate_requirements = CandidateRequirementsReadSerializer()
    recruiter_requirements = RecruiterRequirementsReadSerializer()
