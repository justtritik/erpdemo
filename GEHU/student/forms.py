# forms.py

from django import forms
from student.models import DetailsModel

class StudentDetailsForm(forms.ModelForm):
    class Meta:
        model = DetailsModel
        fields = ['attendance', 'marksinClang', 'marksinJava', 'marksinDSA']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Optionally, customize field widgets or labels here
        # Example:
        self.fields['attendance'].widget.attrs.update({'class': 'form-control'})
        self.fields['marksinClang'].widget.attrs.update({'class': 'form-control'})
        self.fields['marksinJava'].widget.attrs.update({'class': 'form-control'})
        self.fields['marksinDSA'].widget.attrs.update({'class': 'form-control'})
