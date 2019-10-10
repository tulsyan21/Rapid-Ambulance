from django import forms

class UserInputForm(forms.Form):
    TYPE_OPTIONS = [
        (True, 'Private'),
        (False, 'Government')
    ]

    DEPT_OPTIONS=[
        (1,'Critical Care and ICU'),
        (2,'Cancer Spciality'),
        (3,'Cosmetic & Plastic Surgery'),
        (4,'Neurosurgery'),
        (5,'Emergency & Trauma Services'),
        (6,'Anaesthesia'),
        (7,'Blood Bank & Transfusion Medicine'),
        (8,'Spine Surgery'),
        (9,'Radiology'),
        (10,'Orthopaedics')
    ]
    hospital_type = forms.ChoiceField(choices = TYPE_OPTIONS)
    department_needed = forms.ChoiceField(choices = DEPT_OPTIONS)
