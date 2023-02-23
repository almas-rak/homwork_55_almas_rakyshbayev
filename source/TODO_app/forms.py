from django import forms

from TODO_app.models import TODO


class TodoForm(forms.ModelForm):
    class Meta:
        model = TODO
        fields = ('title', 'description', 'status', 'date_of_completion')
