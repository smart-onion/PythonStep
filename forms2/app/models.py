from django.db import models
import uuid
from . import utils
class Film(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
    )
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
    
    def __str__(self):
        return self.name
    

class Meta:
    db_table = "film"
    constraints = [
        models.CheckConstraint(
            check=models.Q(rating__range=(1, 5)),
            name="rating_range_1_5"
        )
    ]

    