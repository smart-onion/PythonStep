from django.forms import Form, CharField, DateField, DateInput, EmailField, EmailInput, HiddenInput, MultipleHiddenInput, MultipleChoiceField
from uuid import uuid4


class EventForm(Form):
    name = CharField()
    date = DateField(widget=DateInput(attrs={'type': 'date'}))

class ParticipantForm(Form):
    email = EmailField(widget=EmailInput()) 