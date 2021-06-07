from django.db import models

# Create your models here.


class Card(models.Model):
    name =  models.CharField(max_length=30,null=True,blank=True)

    def __str__(self):
        return self.name

class FlashCard(models.Model):
    card =  models.ForeignKey(Card,on_delete=models.CASCADE,null=True,blank=True)
    number = models.IntegerField(null=True,blank=True)

    def __str__(self):

        return f' {self.card} - {self.number} '

class Collection(models.Model):
    name =  models.CharField(max_length=30,null=True,blank=True)
    flashcard =  models.ManyToManyField(FlashCard,null=True,blank=True)
    

    def __str__(self):
        return self.name