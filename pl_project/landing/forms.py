from .models import Feedback
from django.forms import ModelForm, TextInput, Textarea


class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'