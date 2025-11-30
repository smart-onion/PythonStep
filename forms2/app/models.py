from django.db import models
import uuid
from datetime import datetime
from . import utils


class Ganre(models.Model):
    name = models.CharField(null=False, unique=True) 

    def __str__(self):
        return self.name

class Film(models.Model):
    name = models.CharField(null=False, max_length=20)
    description = models.TextField()
    issued = models.DateField()
    country = models.CharField(null=False, choices=utils.COUNTRIES, )
    image = models.ImageField()
    rating = models.IntegerField(null=False, choices=[
                (1,1),
                (2,2),
                (3,3),
                (4,4),
                (5,5),
            ],)
    ganre = models.OneToOneField(Ganre, on_delete=models.PROTECT, null=False)
    



    def __str__(self):
        print(self.__dict__)
        return self.name


class Meta:
    db_table = "film"
    constraints = [
        models.CheckConstraint(
            check=models.Q(rating__range=(1, 5)),
            name="rating_range_1_5"
        )
    ]

    
class Comment(models.Model):
    user_name = models.CharField(null=False)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    text = models.TextField(null=False)
    date = models.DateTimeField(default=datetime.now(), null=False)

    class Meta:
        permissions = [
            ("test", "test"),
            ("can_moderate_comments", "Moderate comments")
            
        ]
    
