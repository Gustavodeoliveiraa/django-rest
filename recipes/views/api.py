from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ..models import Recipe
from ..serializer import RecipeSerializer


@api_view()
def recipe_api_list(request):
    recipes = Recipe.objects.get_published()[:10]
    serializer = RecipeSerializer(instance=recipes, many=True)
    return Response(serializer.data)


@api_view()
def recipe_api_detail(request, pk):
    # recipes = get_object_or_404(
    #     Recipe.objects.get_published().filter(pk=pk)
    # )
    recipe = Recipe.objects.get_published().filter(pk=pk).first()

    if recipe:
        serializer = RecipeSerializer(instance=recipe)
        return Response(serializer.data)
    else:
        return Response({
            'detail': 'salve',
        }, status=status.HTTP_418_IM_A_TEAPOT)
