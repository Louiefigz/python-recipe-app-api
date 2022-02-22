from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Recipe

from recipe.serializers import RecipeSerializer

RECIPES_URL = reverse('recipe:recipe-list')

def sample_recipe(user, **params):
    # create and return a sample recipe
    defaults = {
        'title': 'Sample Recipe',
        'time_minutes': 10,
        'price': 5.00
    }

    print('PARAMS: ', params)
    # update will look at params and set the default if not found in dict. and update 
    # any existing keys and values if found in defulats from params.
    defaults.update(params)
    return Recipe.objects.create(user=user, **defaults)

class PublicRecipeApiTests(TestCase):
    # Test unauthenticated recipe API access
    def setUp(self):
        self.client = APIClient()
    
    def test_auth_required(self):
        # Test that authentication is required
        res = self.client.get(RECIPES_URL)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)
    
class PrivateRecipeApiTests(TestCase):
    # Test unauthenticated recipe API access
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            email='test@gmail.com',
            password='testpass123'
        )
        self.client.force_authenticate(self.user)

    def test_user_retrieve_recipes(self):
        sample_recipe(user=self.user)
        sample_recipe(user=self.user)


        recipes = Recipe.objects.all().order_by('-id')

        res = self.client.get(RECIPES_URL)
        serializer = RecipeSerializer(recipes, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)
    def test_recipes_limited_to_user(self):
        otherUser = get_user_model().objects.create_user(
            email='otheruser@gmail.com',
            password='testpass133'
        )

        sample_recipe(user=otherUser)
        sample_recipe(user=self.user)

        res = self.client.get(RECIPES_URL)

        recipes = Recipe.objects.filter(user=self.user)
        print('RECIPES:    ', res.data)

        serializer = RecipeSerializer(recipes, many=True)
        print('SERIALIZER:    ', serializer.data)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data),1)
        self.assertEqual(res.data, serializer.data)

    