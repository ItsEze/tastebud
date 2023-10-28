from django.shortcuts import render
from rest_framework.views import APIView, Response
from dotenv import load_dotenv
import requests
import os

# Create your views here.
load_dotenv()

class RecipeSearch(APIView):

    def get(self, request):
        
        q = request.GET.get('q')
        health = request.GET.get('health')
        cuisineType = request.GET.get('cuisineType')
        mealType = request.GET.get('mealType')
        dishType = request.GET.get('dishType')

        query_params = {
        'app_id': os.environ['APPLICATION_ID'],
        'app_key': os.environ['APPLICATION_KEYS'],
        'type': 'public',
        }

        if q:
            query_params['q'] = q
        if health:
            query_params['health'] = health
        if cuisineType:
            query_params['cuisineType'] = cuisineType
        if mealType:
            query_params['mealType'] = mealType
        if dishType:
            query_params['dishType'] = dishType
            
        endpoint = 'https://api.edamam.com/api/recipes/v2/'
        endpoint += '?'
        endpoint += '&'.join([f'{key}={value}' for key, value in query_params.items()])
        
        response = requests.get(endpoint)
        responseJSON = response.json()

        return Response(responseJSON)
       
       
        