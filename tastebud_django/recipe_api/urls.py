from django.urls import path
from .views import RecipeSearch

urlpatterns = [
    path('',RecipeSearch.as_view())
]