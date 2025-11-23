from django.forms import Form, ImageField, CharField, DateField, ChoiceField, SelectDateWidget, RadioSelect, ModelForm, HiddenInput
from . import utils
from .models import Film

class FilmForm(ModelForm):
    class Meta:
        model=Film
        fields=["id","name", "description", "issued", "country", "image", "rating"]
        widgets = {
            "rating": RadioSelect,
            "issued": SelectDateWidget(),
            "id": HiddenInput()
        }
       
    # name = CharField(label="Film name:")
    # description = CharField(label="Description:", required=False)
    # issued = DateField(widget=SelectDateWidget())
    # country = ChoiceField(choices=utils.COUNTRIES, label="Country: ")
    # image = ImageField(required=False)
    # rating= ChoiceField(
    #     choices=[
    #         (1,1),
    #         (2,2),
    #         (3,3),
    #         (4,4),
    #         (5,5),
    #     ],
    #     widget=RadioSelect,
    #     label="Rating"
    # )

    # def __init__(self, name, description, issued, country, image, rating):
    #     self.name = name
    #     self.description = description
    #     self.issued = issued
    #     self.country = country
    #     self.image = image
    #     self.rating = rating
    #     super().__init__()

