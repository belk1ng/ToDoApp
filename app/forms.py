from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
	class Meta:
		model = Task
		fields = '__all__'

	task = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control',
																		 'placeholder': 'Добавить задание'}))