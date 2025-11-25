from django.forms import Form, ImageField, CharField, DateField, ChoiceField, SelectDateWidget, RadioSelect, ModelForm, HiddenInput, IntegerField
from . import utils
from .models import Ganre, Film, Comment

class FilmForm(ModelForm):
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
    class Meta: 
        model = Film
        fields = "__all__"
        widgets = {
            "issued": SelectDateWidget
        }



class GanreForm(ModelForm):
    class Meta:
        model = Ganre
        fields = '__all__'
    
class CommentForm(ModelForm):
    film = IntegerField(widget=HiddenInput())
    class Meta:
        model = Comment
        fields=["user_name", "text"]