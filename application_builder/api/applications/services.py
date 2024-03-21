"""Файл для обработки входящих данных."""

from apps.applications.models import (JobInfo, CandidateRequirements,
                                      RecruitRequirements, Application)


class ApplicationService:
    @staticmethod
    def create_application(self, validated_data, current_user):
        application = Application.objects.create(
            user=current_user,
            **validated_data['application']
        )
        return application

    def create_job_info(self, validated_data, application):
        job_info = JobInfo.objects.create(
            application=application,
            **validated_data['job_info']
        )
        return job_info

    def create_candidate_requirements(self, validated_data, application):
        language_skills = validated_data[
            'candidate_requirements'
        ].pop('language_skills')
        citizenship = validated_data[
            'candidate_requirements'
        ].pop('citizenship')
        core_skills = validated_data[
            'candidate_requirements'
        ].pop('core_skills')
        candidate_requirements = CandidateRequirements.objects.create(
            application=application,
            **validated_data['candidate_requirements']
        )
        candidate_requirements.language_skills.set(language_skills)
        candidate_requirements.citizenship.set(citizenship)
        candidate_requirements.core_skills.set(core_skills)
        return candidate_requirements

    def create_recruit_requirements(self, validated_data, application):
        recruit_requirements = RecruitRequirements.objects.create(
            application=application,
            **validated_data['recruiter_requirements']
        )
        return recruit_requirements
