from django.db import models

# Create your models here.

#IntegerField()
#CharField(max_length=255)
#DateField()
#TextField()
#EmailField()

#ForeignKey(Blog, on_delete=models.CASCADE)
#ManyToManyField(Author)

class MeasuredEntropy(models.Model):
    lable_of_dataset = models.CharField(max_length=250)
    entropy = models.FloatField()#default=NULL)

class Transactions(models.Model):
    items_bought = models.CharField(max_length=255)