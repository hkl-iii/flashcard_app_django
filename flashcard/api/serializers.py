from django.db.models import fields
from rest_framework import serializers
from flashcard.models import *


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'
        #exclude = ['']
        
class FlashCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlashCard
        fields = '__all__'
        #exclude = ['']

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = '__all__'
        #exclude = ['']