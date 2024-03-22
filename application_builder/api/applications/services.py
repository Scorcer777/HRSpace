"""Модуль для обработки данных."""

from django.db import transaction

from apps.applications.models import (JobInfo, CandidateRequirements,
                                      RecruitRequirements, Application)
from apps.payments.models import Payment
from apps.users.models import UserT


class ApplicationService:
    def __init__(self, validated_data: dict):
        self.validated_data = validated_data

    @transaction.atomic
    def save(self, current_user: UserT) -> Application:
        application = self.create_application(current_user)
        self.create_job_info(application)
        self.create_candidate_requirements(application)
        self.create_recruit_requirements(application)
        self.create_payments(application)
        return application

    def create_application(self, current_user) -> Application:
        application = Application.objects.create(
            user=current_user,
            **self.validated_data['application']
        )
        return application

    def create_job_info(self, application):
        job_info = JobInfo.objects.create(
            application=application,
            **self.validated_data['job_info']
        )
        return job_info

    def create_candidate_requirements(self, application):
        language_skills = self.validated_data[
            'candidate_requirements'
        ].pop('language_skills')
        citizenship = self.validated_data[
            'candidate_requirements'
        ].pop('citizenship')
        candidate_requirements = CandidateRequirements.objects.create(
            application=application,
            **self.validated_data['candidate_requirements']
        )
        candidate_requirements.language_skills.set(language_skills)
        candidate_requirements.citizenship.set(citizenship)
        return candidate_requirements

    def create_recruit_requirements(self, application):
        recruit_requirements = RecruitRequirements.objects.create(
            application=application,
            **self.validated_data['recruiter_requirements']
        )
        return recruit_requirements

    def create_payments(self, application):
        payments = Payment.objects.create(
            application=application,
            **self.validated_data['payments']
        )
        return payments
