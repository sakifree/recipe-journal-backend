from .models import Recipe
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import RecipeSerializer

# Create your views here.
class RecipeViewSet(viewsets.ModelViewSet):
    # main query for the index route
    queryset = Recipe.objects.all()
    # serializer class for serializing output
    serializer_class = RecipeSerializer
    # optional permission class set permission level
    permission_classes = [permissions.AllowAny]