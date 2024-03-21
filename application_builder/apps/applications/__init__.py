MAX_LENGTH = 1000

START_WORKING = [
    ('tomorrow', 'Сможет приступить завтра'),
    ('in_week', 'В течение недели'),
    ('in_month', 'В течение месяца'),
    ('in_3_month', 'В течение 3 месяцев'),
    ('not_hurry', 'Не спешу с поиском'),
]

EMPLOYMENT_TYPES = [
    ('full-time', 'Полная занятость'),
    ('part-time', 'Частичная занятость'),
    ('project', 'Проект'),
    ('shift_work', 'Вахта'),
    ('traineeship', 'Стажировка'),
]

SCHEDULE_TYPES = [
    ('full-day', 'Полный день'),
    ('part-time', 'Неполный день'),
    ('5_on_2_off', '5/2'),
    ('2_on_2_off', 'Два через два'),
    ('24_h_on_72_h_off', 'Сутки / трое'),
    ('flexible', 'Свободный'),
    ('shift_work', 'Вахта'),
]

WORK_MODELS = [
    ('office', 'Офис'),
    ('remote', 'Удаленный'),
    ('hybrid', 'Гибрид'),
]

CONTRACT_TYPES = [
    ('contract', 'Трудовой договор'),
    ('civil-personal_contract', 'ГПХ'),
    ('individual_entrepreneurship', 'ИП'),
    ('self-employed', 'Самозанятый'),
    ('holding_multiple_positions', 'Совместительство'),
]

WORKING_CONDITIONS = [
    ('VMI', 'ДМС'),
    ('fitness', 'Фитнес'),
    ('meal_compensation', 'Оплата питания'),
    ('free_parking', 'Бесплатная парковка'),
    ('mobile_phone_compensation', 'Оплата мобильной связи'),
    ('transportation_compensation', 'Оплата проезда'),
    ('language_training', 'Языковые курсы'),
    ('professional_training', 'Профессиональные курсы'),
    ('from_age_14', 'Подходит подросткам с 14 лет'),
    (
        'for_people_with_disabilities',
        'Подходит людям с ограниченными возможностями'
    ),
]

EDUCATION_TYPES = [
    ('not_required', 'Не имеет значения'),
    ('higher', 'Высшее'),
    ('vocational', 'Среднее профессиональное'),
]

EXPERIENCES = [
    ('not_required', 'Не имеет значения'),
    ('no_experience', 'Нет опыта'),
    ('1-3_years', 'От 1 года до 3 лет'),
    ('3-6_years', 'От 3 до 6 лет'),
    ('over_6_years', 'Более 6 лет'),
]

DRIVING_SKILLS = [
    ('B', 'Категория B, легковые автомобили'),
    ('C', 'Категория C, грузовые автомобили'),
    ('D', 'Категория D, автобусы'),
    ('M', 'Категория M, мопеды'),
    ('A', 'Категория A, мотоциклы'),
]

RECRUITER_RESPONSIBILITIES = [
    ('resume_searching', 'Поиск и предоставление релевантных резюме'),
    (
        'interview_organizing',
        'Организация собеседований с заказчиком, '
        'синхронизация по времени заказчика и соискателя'
    ),
    ('recomendation_request', 'Запрос рекомендаций с предыдущих мест работы'),
    ('sending_tests', 'Отправка кандидату тестового задания'),
    (
        'sending_security_service_form',
        'Отправка кандидату анкеты службы безопасности'
    ),
    ('sending_offer', 'Отправка кандидату приглашения на работу'),
]

RESUME_FORM = [
    ('no_pre_interview', 'Резюме без предварительного собеседования'),
    (
        'with_pre_interview',
        'Резюме кандидатов, с которыми проведено интервью, '
        'с комментариями по кандидату'
    ),
]
