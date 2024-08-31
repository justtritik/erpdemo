from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class DetailsModel(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=100)
    attendance=models.FloatField()
    marksinClang=models.IntegerField()
    marksinJava=models.IntegerField()
    marksinDSA=models.IntegerField()

    def __str__(self):
        return self.name