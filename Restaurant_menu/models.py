from django.db import models
from  django.contrib.auth.models import User

# Create your models here.
MEAL_TYPE = (
    ("starters", "Starters"),
    ("salads", "Salads"),
    ("main_course","Main Course"),
    ("desserts","Desserts"),
    ("drinks","Drinks")
)

STATUS = (
    (0, 'Unavailable'),
    (1,'Available')
)


class Item(models.Model):
    meal = models.CharField(max_length = 1000, unique = True)
    description = models.CharField(max_length = 2000)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.CharField(choices=MEAL_TYPE, max_length = 80)
    author = models.ForeignKey(User, on_delete = models.PROTECT)
    status = models.IntegerField(choices = STATUS, default = 1)
    date_created = models.DateTimeField(auto_now_add=True)
    date_update =  models.DateTimeField(auto_now=True)


    def  __str__(self):
        return self.meal