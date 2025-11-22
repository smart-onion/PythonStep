from django.forms import Form, ImageField, CharField, DateField, ChoiceField, SelectDateWidget, HiddenInput
from . import utils


class FilmForm(Form):
    name = CharField(label="Film name:")
    description = CharField(label="Description:", required=False)
    issued = DateField(widget=SelectDateWidget())
    country = ChoiceField(choices=utils.COUNTRIES, label="Country: ")
    image = ImageField(required=False)