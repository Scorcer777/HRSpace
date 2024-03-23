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

    def create_application(self, current_user: UserT) -> Application:
        application = Application.objects.create(
            user=current_user,
            **self.validated_data['application']
        )
        return application

    def create_job_info(self, application: Application) -> JobInfo:
        job_info = JobInfo.objects.create(
            application=application,
            **self.validated_data['job_info']
        )
        return job_info

    def create_candidate_requirements(
            self, application: Application
    ) -> CandidateRequirements:
        try:
            language_skills = self.validated_data[
                'candidate_requirements'
            ].pop('language_skills')
        except KeyError:
            language_skills = None
        try:
            citizenship = self.validated_data[
                'candidate_requirements'
            ].pop('citizenship')
        except KeyError:
            citizenship = None
        candidate_requirements = CandidateRequirements.objects.create(
            application=application,
            **self.validated_data['candidate_requirements']
            )
        if language_skills is not None:
            candidate_requirements.language_skills.set(language_skills)
        if citizenship is not None:
            candidate_requirements.citizenship.set(citizenship)
        return candidate_requirements

    def create_recruit_requirements(
            self, application: Application
    ) -> RecruitRequirements:
        recruit_requirements = RecruitRequirements.objects.create(
            application=application,
            **self.validated_data['recruiter_requirements']
        )
        return recruit_requirements

    def create_payments(self, application: Application) -> Payment:
        payments = Payment.objects.create(
            application=application,
            **self.validated_data['payments']
        )
        return payments

    def update_application(self, instance: Application) -> Application:
        instance.title = self.validated_data['title']
        instance.profession = self.validated_data['profession']
        instance.city = self.validated_data['city']
        instance.min_salary = self.validated_data['min_salary']
        instance.max_salary = self.validated_data['max_salary']
        instance.number_of_employees = self.validated_data[
            'number_of_employees'
        ]
        instance.start_working = self.validated_data['start_working']
        instance.number_of_recruiters = self.validated_data[
            'number_of_recruiters'
        ]
        instance.save()
        return instance

    def update_job_info(self, instance: JobInfo) -> JobInfo:
        instance.employment_type = self.validated_data.get(
            'employment_type',
            instance.employment_type
        )
        instance.schedule = self.validated_data.get(
            'schedule', instance.schedule
        )
        instance.work_model = self.validated_data.get(
            'work_model',
            instance.work_model
        )
        instance.contract_type = self.validated_data.get(
            'contract_type',
            instance.contract_type
        )
        instance.working_conditions = self.validated_data.get(
            'working_conditions',
            instance.working_conditions
        )
        instance.description = self.validated_data.get(
            'description',
            instance.description
        )
        instance.save()
        return instance

    def update_candidate_requirements(
            self, instance: CandidateRequirements
    ) -> CandidateRequirements:
        instance.education = self.validated_data.get(
            'education',
            instance.education
        )
        instance.experience = self.validated_data.get(
            'experience', instance.experience
        )
        instance.language_skills.set(self.validated_data.get(
            'language_skills',
            instance.language_skills)
        )
        instance.driving_skills = self.validated_data.get(
            'driving_skills',
            instance.driving_skills
        )
        instance.has_medical_certificate = self.validated_data.get(
            'has_medical_certificate',
            instance.has_medical_certificate
        )
        instance.has_photo = self.validated_data.get(
            'has_photo',
            instance.has_photo
        )
        instance.citizenship.set(self.validated_data.get(
            'citizenship',
            instance.citizenship
        ))
        instance.coreskills_and_responsibilities = self.validated_data.get(
            'coreskills_and_responsibilities',
            instance.coreskills_and_responsibilities
        )
        instance.save()
        return instance

    def update_recruiter_requirements(
            self, instance: RecruitRequirements
    ) -> RecruitRequirements:
        instance.industry = self.validated_data.get(
            'industry',
            instance.industry
        )
        instance.english_skills = self.validated_data.get(
            'english_skills',
            instance.english_skills
        )
        instance.recruiter_responsibilities = self.validated_data.get(
            'recruiter_responsibilities',
            instance.recruiter_responsibilities
        )
        instance.description = self.validated_data.get(
            'description',
            instance.description
        )
        instance.candidate_resume_form = self.validated_data.get(
            'candidate_resume_form',
            instance.candidate_resume_form
        )
        instance.stop_list = self.validated_data.get(
            'stop_list',
            instance.stop_list
        )
        instance.save()
        return instance

    def update_payments(self, instance: Payment) -> Payment:
        instance.payment_amount = self.validated_data.get(
            'payment_amount',
            instance.payment_amount
        )
        instance.stop_list = self.validated_data.get(
            'payment_type',
            instance.payment_type
        )
        instance.save()
        return instance
