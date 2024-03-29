# from app.core.models import Recipe
from rest_framework import serializers

from core.models import Tag, Ingredient, Recipe

class TagSerializer(serializers.ModelSerializer):
    # Serializer for tag objects
    
    class Meta:
        model = Tag
        fields = ('id', 'name')
        read_only_fields = ('id', )

class IngredientSerializer(serializers.ModelSerializer):
    # Serializer for Ingredient Objects
    class Meta:
        model = Ingredient
        fields = ('id', 'name')
        read_only_fields = ('id',)

class RecipeSerializer(serializers.ModelSerializer):
    ingredients = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Ingredient.objects.all()
    )
    tags = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Tag.objects.all()
    )
    class Meta:
        model = Recipe
        fields = ('id', 'title', 'time_minutes', 'price', 'link', 'ingredients', 'tags')
        read_only_fields = ('id',)

class RecipeDetailSerializer(RecipeSerializer):
    # Serialize a Recipe Detail
    # read only is to prevent us from creating an ingredient
    # many=True is the relationship. Many to many
    ingredients = IngredientSerializer(many=True, read_only=True)
    tags = TagSerializer(many=True, read_only=True)