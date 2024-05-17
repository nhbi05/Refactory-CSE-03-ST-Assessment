from django.db import models
from django.core.exceptions import ValidationError
from datetime import date, timedelta

class StudentApplication(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    
    COURSE_CHOICES = [
        ('chs', 'Certificate in Health Science'),
        ('cat', 'Certificate in Applied Technology'),
        ('bit', 'Bachelor of Information Technology'),
        ('bbt', 'Bachelors in Business Technology'),
        ('mph', 'Master of Public Health'),
    ]

    ENTRY_SCHEME_CHOICES = [
        ('alevel', 'A-Level certificate'),
        ('adult', 'Adult/Mature Learning'),
        ('certificate', 'Certificate'),
        ('diploma', 'Diploma'),
        ('bachelors', 'Bachelors'),
    ]

    INTAKE_CHOICES = [
        ('january', 'January Intake'),
        ('may', 'May Intake'),
        ('august', 'August Intake'),
    ]

    SPONSORSHIP_CHOICES = [
        ('private', 'Private'),
        ('government', 'Government'),
        ('bursary', 'Bursary'),
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    course = models.CharField(max_length=100, choices=COURSE_CHOICES)
    intake = models.CharField(max_length=50, choices=INTAKE_CHOICES)
    entry_scheme = models.CharField(max_length=100, choices=ENTRY_SCHEME_CHOICES)
    sponsorship = models.CharField(max_length=100, choices=SPONSORSHIP_CHOICES)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default='male')
    date_of_birth = models.DateField()
    residence = models.CharField(max_length=50)


    def clean(self):
        # Date of birth validation
        if self.date_of_birth >= date.today() - timedelta(days=18*365):
            raise ValidationError('Applicant must be at least 18 years old.')
        if self.date_of_birth >= date.today():
            raise ValidationError('Date of birth cannot be in the future.')
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
