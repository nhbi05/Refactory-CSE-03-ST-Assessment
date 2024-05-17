from django import forms
from .models import StudentApplication
from datetime import timedelta
from datetime import date

class StudentApplicationForm(forms.ModelForm):
    class Meta:
        model = StudentApplication
        fields = '__all__'
        widgets = {
            'gender': forms.RadioSelect(choices=StudentApplication.GENDER_CHOICES),
            'course': forms.Select(choices=StudentApplication.COURSE_CHOICES),
            'entry_scheme': forms.Select(choices=StudentApplication.ENTRY_SCHEME_CHOICES),
            'intake': forms.Select(choices=StudentApplication.INTAKE_CHOICES),
            'sponsorship': forms.Select(choices=StudentApplication.SPONSORSHIP_CHOICES),
            'date_of_birth': forms.DateInput(attrs={'class':'form-control' 'datetimepicker-input', 'type':'date'}),
        }

    def clean_residence(self):
        residence = self.cleaned_data['residence']
        if len(residence) < 2:
            raise forms.ValidationError("Residence must be at least 2 characters long.")
        if len(residence) > 255:
            raise forms.ValidationError("Residence must be at most 255 characters long.")
        return residence

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if len(first_name) < 2:
            raise forms.ValidationError("Firstname must be at least 2 characters long.")
        if len(first_name) > 255:
            raise forms.ValidationError("First name must be at most 255 characters long.")
        return first_name
    
    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        if len(last_name) < 2:
            raise forms.ValidationError("Last name must be at least 2 characters long.")
        if len(last_name) > 255:
            raise forms.ValidationError("Last name must be at most 255 characters long.")
        return last_name
    
    
