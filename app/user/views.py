from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from user.serializers import UserSerializer, AuthTokenSerializer

class CreateUserView(generics.CreateAPIView):
    # Create a new user in the system
    serializer_class = UserSerializer
 
class CreateTokenView(ObtainAuthToken):
    # create a new auth token for user
    print('CreateTokenView is being hit')
    serializer_class = AuthTokenSerializer
    print('serializer class: ', serializer_class)
    # renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

