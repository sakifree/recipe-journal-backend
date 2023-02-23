from .models import Recipe
from rest_framework import serializers

class RecipeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # the model it will serialize
        model = Recipe
        # the fields that should be included in the serialized output
        fields = ['id', 'name', 'ingredients', 'directions']