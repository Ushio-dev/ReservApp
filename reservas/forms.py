from django import forms
from django.forms import ModelForm
from .models import Employee


class EmployeeForm(ModelForm):
       class Meta:
        model = Employee
        fields = ['name', 'lastname', 'file_number' ]
        labels = {
            'name': 'Nombre',
            'lastname': 'Apellido',
            'file_number': 'Numero de Legajo',
        }

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'width: 50%;'
            }),
            'lastname': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'width: 50%;'
            }),
            'file_number': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'width: 50%;',
                "type" : "number"
            }),

        }