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
        
        # response = requests.get(endpoint)
        # responseJSON = response.json()

        dummy_data = {
            "from": 1,
            "to": 20,
            "count": 9795,
            "_links": {
                "next": {
                    "href": "https://api.edamam.com/api/recipes/v2/?q=meatballs&app_key=34e59dda7e1bffb92e49c416e9449e1d&_cont=CHcVQBtNNQphDmgVQntAEX4BYlxtAwAES2VGBWMTYlV0AAEFUXlSAzQXZAR7VQpUEWZIBGtHMVV2UlICR2dDBTYVZF13UVAVLnlSVSBMPkd5BgMbUSYRVTdgMgksRlpSAAcRXTVGcV84SU4%3D&type=public&app_id=e909afd5",
                    "title": "Next page"
                }
            },
            "hits": [
                {
                    "recipe": {
                        "uri": "http://www.edamam.com/ontologies/edamam.owl#recipe_91478504c3565dce0513e980e3bb78b3",
                        "label": "Teriyaki pork meatballs",
                        "image": "https://edamam-product-images.s3.amazonaws.com/web-img/2d6/2d605ebf4ef893ea6154cf6f5e8c2336.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIQDCDrJlHnPZkAGGm1Xmkf6BwXlG37y%2BwhyBTqcd8%2Bm%2FuQIgEWgFR0z0W0ZzfbOptTpOrcW8H69gNX376f%2F0%2BRnfkkgqwgUI8f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgwxODcwMTcxNTA5ODYiDP%2FD%2FRLePqBic9UTkCqWBctfTb3DsIwgFzRZpjwiSeq%2FKQV9HqyKQZGACfijzqMIUkba7MQd2pKFwZwyxcOXbNIeQIaEFl0uEgn5%2FIrFddK3dA%2FRQ4BkgcgX0en93RS%2B1U9KWhg7medeoh6%2FfijgBVZYl99sP2TYzodkp%2Bfusu9cIK62ugLC2SRRF5EI%2BXSugQXQXUKjgzhvUK8XxtnRH3IbQcxHo2xMX4JE04dYJ1MRnx7H4JszjUIVFi%2FBUOrZZ9QLXpM2Uv2jRCFY6kC3xpOR%2Brj5N4GM4zaqelBnrB8f%2B%2FafEmcGyheJrZf1cmyHArt%2FL%2FqSRNalBv%2BAAH5f77pLXK6P1mRclYzvUJIQ7l3r4xPyh6c2GYVkzhksc3QoPtVLV0OtVf92iB56E%2FHF%2FiFfdJ9Rg3z%2BXjCumOtW%2FehrioKPeIFAzkTDsLli%2F%2FUyGIUVrc0LwdspYR8TNPHobRHr5C0kG4ny59jtmOT1%2FsLvPgcJQ0NxMAcLJCdU2FizpvwfgG5Uje9TMFurWG4wpV2jQ9EInmmtL%2FQUGHyb4A0Guy0kQBf0awrySLootSE7YHp%2BJIhiNMzCz4KjDJyS9s3n2uD8PDpAebkUtsU6thH6pLTv%2BZer11m2R7ZzXmLwtE76JIpPpA8SugXG93HaQQ564aVNLKHFoJGs4aSvFDCXIH8lGabv6W0U9hjOzwf3zDbymCXdLKRZnbf5755ZPdcIg4QQZwBtz8sp3vtmmOmlwofldxPWJf6OlGuEVpPeY7CFyJOSLYoVq1I9bftOQJsM0ddz2O87wh92x3Kwm3Lwb7t4KNB%2BBtXRPvQCSpXQ5Kn5EnsEh0xh2LBUuwmzkrOgT5NkUjy%2F%2FZNjAv0sYVoRmuqZTPPBF%2FzTxAG%2BOoQEaU%2Bmk8K5MNnkz6kGOrEBXSNmzQFfU9s7muBt1TMzWyXfYjW4P4Qv7m1NNiTYRfkdPIupI3mK1cMOOIL2iDsAwU4N2OVGe%2FUxmJxC23fzXEQnUHa6lWvsIT6U%2BNPdSPGG2d1UY8k1H3dCVHU%2FbNOBkpCcEQLaWCOOy29usIjByfVJPPeXUXCt4zRSix3SFionDqMo%2FqGoT0kKjjFumKcV3PIGy4HNiJJakVavxgr5cTCintzvwd6XXyiVyN3BPU%2Ba&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231021T172525Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFI73LNE7V%2F20231021%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=dad1c44a5e089c6bb5d1cea853804561e52d1462eb5507aded23731f829ae198",
                        "images": {
                            "THUMBNAIL": {
                                "url": "https://edamam-product-images.s3.amazonaws.com/web-img/1af/1af9675e19b196d03dcee2f3c4185a0c-s.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIQDe%2FJs8ZUT5eiJwctFVO4mrApL5kldTPFBXNIkowPZjAQIgdtPsWtZABS0Uxk74g9Uvu1I8XLsAtgHeF%2BjEcIDoElgqwgUIsv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgwxODcwMTcxNTA5ODYiDJKA2JZryvZC7EyJjSqWBe0%2BaxnoIlTCiNXZV76KGF%2BKfXM62FAjt%2F%2BPhu2cWmPtDUcEs60nR9Hh507ZaTf7MvJNLcWkSBdMbnM7Dggc2X6PCsYlWsI4YgwILPsWWgDFAodYcmKaVMMO3kP8ehHF8v5Wpk7pz5Or3lycukXCW4AgpGnToCveQexBJAI3eVx74ST%2FvBdLBxN0HkuYnwcVmwWeiiDgmKpViZjIaS4aS4HuYOW%2BlQjweoqhxJr%2BW5txGE9OxjFUxEpQDH98zmSxw259DIJU3kELTTP3ykqnltSeoeIiCFDA%2F6GwWCK4TdLToEcsZM6lSLm4ao8g8vr1lwBSL8QciTnQXqzjxvHLzgbD6B2BDTnZfJHzYFOvLHX5eBgz7%2FptbSQgFcJFoz5Fg6PgjlLDScv2NKdBbLGqma%2B1%2Fgmz62bHtUf1n6sRh%2B0YS8QCDrvsaq6pwvz90m3%2BwrxEPIYCUqKQxC8d4ymvYjkdMeOeZtUJdjVeGqTCNnfvIiTtzeHyyDifaOLllpM%2BC%2FKQ4SQ%2F6qShbAYzDuOiVTs2fDk1%2BxexGLLI%2BR1bCAgQ7piQzks38F%2FNOx00A0alz8WTTDoXKEQlIJc85lLfOejDU7IsQjPu6BrqxUgKKcNAY8H9WjmhlmBLGkTdo3c9SRq3fg6jdwvbhuZYBBhng5UWuVPzvmNL9c9JOQumITSJN3Za4oKzrVeficvhtsSDUNalEy81xsalXH7NZR1JHLeJUb9woK9rwqBdVxvvbipt%2Fxd6kOp1sD0OV2bxCJX27z0oZiI8NJnhdlcEeY3nvLJs7okIzHaRsk8CPW6CY%2F0v8IOI7rX6rtuEcXCdZYRgPh%2FkOVGdBhPMknvvnoqoL%2FH6XIKJOc3YiOuaRzSx8vl0eLDj%2BR7mMOj7wakGOrEBNi6Zqzy95R%2FfKCe4LFriR4KB281PdbY8%2B46ZBLWnM2%2F2h9jwRU3S6u%2B0n3mJy4QQE6JxGOpC2BdppMiNvGERdQH2XOJIWNX%2FuMkndFcQrPHH6V9sdda4C%2Fbhrx7UK6pQDebbQ741oXeVSRMtm5rBWNBPAoh9ugi1%2B%2B93a4P1tNVuj%2FHWfH1pLwJOJcZJpFeCUS3VqghEHzlFhVDtR3IfqmOl7PvSLMuEKfJahdNU%2BYN3&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231019T020500Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFJITURKAY%2F20231019%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=76e942610985471f5c1d7bdde7dc6a28ee484e3146faa69d8348af4c2b6fce64",
                                "width": 100,
                                "height": 100
                            },
                            "SMALL": {
                                "url": "https://edamam-product-images.s3.amazonaws.com/web-img/1af/1af9675e19b196d03dcee2f3c4185a0c-m.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIQDe%2FJs8ZUT5eiJwctFVO4mrApL5kldTPFBXNIkowPZjAQIgdtPsWtZABS0Uxk74g9Uvu1I8XLsAtgHeF%2BjEcIDoElgqwgUIsv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgwxODcwMTcxNTA5ODYiDJKA2JZryvZC7EyJjSqWBe0%2BaxnoIlTCiNXZV76KGF%2BKfXM62FAjt%2F%2BPhu2cWmPtDUcEs60nR9Hh507ZaTf7MvJNLcWkSBdMbnM7Dggc2X6PCsYlWsI4YgwILPsWWgDFAodYcmKaVMMO3kP8ehHF8v5Wpk7pz5Or3lycukXCW4AgpGnToCveQexBJAI3eVx74ST%2FvBdLBxN0HkuYnwcVmwWeiiDgmKpViZjIaS4aS4HuYOW%2BlQjweoqhxJr%2BW5txGE9OxjFUxEpQDH98zmSxw259DIJU3kELTTP3ykqnltSeoeIiCFDA%2F6GwWCK4TdLToEcsZM6lSLm4ao8g8vr1lwBSL8QciTnQXqzjxvHLzgbD6B2BDTnZfJHzYFOvLHX5eBgz7%2FptbSQgFcJFoz5Fg6PgjlLDScv2NKdBbLGqma%2B1%2Fgmz62bHtUf1n6sRh%2B0YS8QCDrvsaq6pwvz90m3%2BwrxEPIYCUqKQxC8d4ymvYjkdMeOeZtUJdjVeGqTCNnfvIiTtzeHyyDifaOLllpM%2BC%2FKQ4SQ%2F6qShbAYzDuOiVTs2fDk1%2BxexGLLI%2BR1bCAgQ7piQzks38F%2FNOx00A0alz8WTTDoXKEQlIJc85lLfOejDU7IsQjPu6BrqxUgKKcNAY8H9WjmhlmBLGkTdo3c9SRq3fg6jdwvbhuZYBBhng5UWuVPzvmNL9c9JOQumITSJN3Za4oKzrVeficvhtsSDUNalEy81xsalXH7NZR1JHLeJUb9woK9rwqBdVxvvbipt%2Fxd6kOp1sD0OV2bxCJX27z0oZiI8NJnhdlcEeY3nvLJs7okIzHaRsk8CPW6CY%2F0v8IOI7rX6rtuEcXCdZYRgPh%2FkOVGdBhPMknvvnoqoL%2FH6XIKJOc3YiOuaRzSx8vl0eLDj%2BR7mMOj7wakGOrEBNi6Zqzy95R%2FfKCe4LFriR4KB281PdbY8%2B46ZBLWnM2%2F2h9jwRU3S6u%2B0n3mJy4QQE6JxGOpC2BdppMiNvGERdQH2XOJIWNX%2FuMkndFcQrPHH6V9sdda4C%2Fbhrx7UK6pQDebbQ741oXeVSRMtm5rBWNBPAoh9ugi1%2B%2B93a4P1tNVuj%2FHWfH1pLwJOJcZJpFeCUS3VqghEHzlFhVDtR3IfqmOl7PvSLMuEKfJahdNU%2BYN3&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231019T020500Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFJITURKAY%2F20231019%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=5ee32b540a831a207af949b13b1e2b9ee9933784fde1fcff82af687e31d73029",
                                "width": 200,
                                "height": 200
                            },
                            "REGULAR": {
                                "url": "https://edamam-product-images.s3.amazonaws.com/web-img/1af/1af9675e19b196d03dcee2f3c4185a0c.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIQDe%2FJs8ZUT5eiJwctFVO4mrApL5kldTPFBXNIkowPZjAQIgdtPsWtZABS0Uxk74g9Uvu1I8XLsAtgHeF%2BjEcIDoElgqwgUIsv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgwxODcwMTcxNTA5ODYiDJKA2JZryvZC7EyJjSqWBe0%2BaxnoIlTCiNXZV76KGF%2BKfXM62FAjt%2F%2BPhu2cWmPtDUcEs60nR9Hh507ZaTf7MvJNLcWkSBdMbnM7Dggc2X6PCsYlWsI4YgwILPsWWgDFAodYcmKaVMMO3kP8ehHF8v5Wpk7pz5Or3lycukXCW4AgpGnToCveQexBJAI3eVx74ST%2FvBdLBxN0HkuYnwcVmwWeiiDgmKpViZjIaS4aS4HuYOW%2BlQjweoqhxJr%2BW5txGE9OxjFUxEpQDH98zmSxw259DIJU3kELTTP3ykqnltSeoeIiCFDA%2F6GwWCK4TdLToEcsZM6lSLm4ao8g8vr1lwBSL8QciTnQXqzjxvHLzgbD6B2BDTnZfJHzYFOvLHX5eBgz7%2FptbSQgFcJFoz5Fg6PgjlLDScv2NKdBbLGqma%2B1%2Fgmz62bHtUf1n6sRh%2B0YS8QCDrvsaq6pwvz90m3%2BwrxEPIYCUqKQxC8d4ymvYjkdMeOeZtUJdjVeGqTCNnfvIiTtzeHyyDifaOLllpM%2BC%2FKQ4SQ%2F6qShbAYzDuOiVTs2fDk1%2BxexGLLI%2BR1bCAgQ7piQzks38F%2FNOx00A0alz8WTTDoXKEQlIJc85lLfOejDU7IsQjPu6BrqxUgKKcNAY8H9WjmhlmBLGkTdo3c9SRq3fg6jdwvbhuZYBBhng5UWuVPzvmNL9c9JOQumITSJN3Za4oKzrVeficvhtsSDUNalEy81xsalXH7NZR1JHLeJUb9woK9rwqBdVxvvbipt%2Fxd6kOp1sD0OV2bxCJX27z0oZiI8NJnhdlcEeY3nvLJs7okIzHaRsk8CPW6CY%2F0v8IOI7rX6rtuEcXCdZYRgPh%2FkOVGdBhPMknvvnoqoL%2FH6XIKJOc3YiOuaRzSx8vl0eLDj%2BR7mMOj7wakGOrEBNi6Zqzy95R%2FfKCe4LFriR4KB281PdbY8%2B46ZBLWnM2%2F2h9jwRU3S6u%2B0n3mJy4QQE6JxGOpC2BdppMiNvGERdQH2XOJIWNX%2FuMkndFcQrPHH6V9sdda4C%2Fbhrx7UK6pQDebbQ741oXeVSRMtm5rBWNBPAoh9ugi1%2B%2B93a4P1tNVuj%2FHWfH1pLwJOJcZJpFeCUS3VqghEHzlFhVDtR3IfqmOl7PvSLMuEKfJahdNU%2BYN3&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231019T020500Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFJITURKAY%2F20231019%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=a2f450470b78e1a26fd7889f57fb441061e8980a610537694cf7b122931428d0",
                                "width": 300,
                                "height": 300
                            }
                        },
                        "source": "BBC Good Food",
                        "url": "https://www.bbcgoodfood.com/recipes/teriyaki-pork-meatballs",
                        "shareAs": "http://www.edamam.com/recipe/teriyaki-pork-meatballs-91478504c3565dce0513e980e3bb78b3/meatballs",
                        "yield": 4.0,
                        "dietLabels": [],
                        "healthLabels": [
                            "Dairy-Free",
                            "Peanut-Free",
                            "Tree-Nut-Free",
                            "Fish-Free",
                            "Shellfish-Free",
                            "Pork-Free",
                            "Crustacean-Free",
                            "Celery-Free",
                            "Mustard-Free",
                            "Sesame-Free",
                            "Lupine-Free",
                            "Mollusk-Free",
                            "Alcohol-Free",
                            "No oil added",
                            "Sulfite-Free",
                            "Kosher"
                        ],
                        "cautions": [
                            "Sulfites"
                        ],
                        "ingredientLines": [
                            "250g dried medium egg noodles",
                            "12 fresh pork meatballs",
                            "300g pak choi",
                            "6 tbsp teriyaki sauce"
                        ],
                        "ingredients": [
                            {
                                "text": "250g dried medium egg noodles",
                                "quantity": 250.0,
                                "measure": "gram",
                                "food": "egg noodles",
                                "weight": 250.0,
                                "foodCategory": "grains",
                                "foodId": "food_aefg3gqa71nrtpbhjfo3yb36kd81",
                                "image": "https://www.edamam.com/food-img/800/800c9c0d7cef6b5474723682ffa2878d.jpg"
                            },
                            {
                                "text": "12 fresh pork meatballs",
                                "quantity": 12.0,
                                "measure": "<unit>",
                                "food": "meatballs",
                                "weight": 1020.0,
                                "foodCategory": "meats",
                                "foodId": "food_boq91pbbhklr6sb0d9sbybzgklkm",
                                "image": "https://www.edamam.com/food-img/cfa/cfae8f9276eaf8f0d9349ba662744a0c.jpg"
                            },
                            {
                                "text": "300g pak choi",
                                "quantity": 300.0,
                                "measure": "gram",
                                "food": "pak choi",
                                "weight": 300.0,
                                "foodCategory": "vegetables",
                                "foodId": "food_asmb473b3s2fxpaf8pd9hb2uvp5e",
                                "image": "https://www.edamam.com/food-img/12f/12f9b47f4f87062491bce23963c2ad43.jpg"
                            },
                            {
                                "text": "6 tbsp teriyaki sauce",
                                "quantity": 6.0,
                                "measure": "tablespoon",
                                "food": "teriyaki sauce",
                                "weight": 108.0,
                                "foodCategory": "canned soup",
                                "foodId": "food_a1ams9uatame3sa7rv6s8b5oanh7",
                                "image": "https://www.edamam.com/food-img/09e/09ea224087dca731115d8a7501e121aa.jpg"
                            }
                        ],
                        "calories": 3685.92,
                        "totalCO2Emissions": 102210.37272726401,
                        "co2EmissionsClass": "G",
                        "totalWeight": 1678.0,
                        "totalTime": 14.0,
                        "cuisineType": [
                            "japanese"
                        ],
                        "mealType": [
                            "lunch/dinner"
                        ],
                        "dishType": [
                            "main course"
                        ],
                        "totalNutrients": {
                            "ENERC_KCAL": {
                                "label": "Energy",
                                "quantity": 3685.92,
                                "unit": "kcal"
                            },
                            "FAT": {
                                "label": "Fat",
                                "quantity": 215.72160000000002,
                                "unit": "g"
                            },
                            "FASAT": {
                                "label": "Saturated",
                                "quantity": 80.34700000000001,
                                "unit": "g"
                            },
                            "FATRN": {
                                "label": "Trans",
                                "quantity": 12.188500000000001,
                                "unit": "g"
                            },
                            "FAMS": {
                                "label": "Monounsaturated",
                                "quantity": 93.44000000000001,
                                "unit": "g"
                            },
                            "FAPU": {
                                "label": "Polyunsaturated",
                                "quantity": 8.927200000000001,
                                "unit": "g"
                            },
                            "CHOCDF": {
                                "label": "Carbs",
                                "quantity": 201.63799999999998,
                                "unit": "g"
                            },
                            "CHOCDF.net": {
                                "label": "Carbohydrates (net)",
                                "quantity": 190.27999999999997,
                                "unit": "g"
                            },
                            "FIBTG": {
                                "label": "Fiber",
                                "quantity": 11.358,
                                "unit": "g"
                            },
                            "SUGAR": {
                                "label": "Sugars",
                                "quantity": 23.467999999999996,
                                "unit": "g"
                            },
                            "PROCNT": {
                                "label": "Protein",
                                "quantity": 221.8444,
                                "unit": "g"
                            },
                            "CHOLE": {
                                "label": "Cholesterol",
                                "quantity": 934.2,
                                "unit": "mg"
                            },
                            "NA": {
                                "label": "Sodium",
                                "quantity": 5057.1,
                                "unit": "mg"
                            },
                            "CA": {
                                "label": "Calcium",
                                "quantity": 613.1,
                                "unit": "mg"
                            },
                            "MG": {
                                "label": "Magnesium",
                                "quantity": 441.28,
                                "unit": "mg"
                            },
                            "K": {
                                "label": "Potassium",
                                "quantity": 4363.0,
                                "unit": "mg"
                            },
                            "FE": {
                                "label": "Iron",
                                "quantity": 34.049,
                                "unit": "mg"
                            },
                            "ZN": {
                                "label": "Zinc",
                                "quantity": 48.114,
                                "unit": "mg"
                            },
                            "P": {
                                "label": "Phosphorus",
                                "quantity": 2491.4200000000005,
                                "unit": "mg"
                            },
                            "VITA_RAE": {
                                "label": "Vitamin A",
                                "quantity": 752.3,
                                "unit": "µg"
                            },
                            "VITC": {
                                "label": "Vitamin C",
                                "quantity": 135.0,
                                "unit": "mg"
                            },
                            "THIA": {
                                "label": "Thiamin (B1)",
                                "quantity": 3.416,
                                "unit": "mg"
                            },
                            "RIBF": {
                                "label": "Riboflavin (B2)",
                                "quantity": 2.8908,
                                "unit": "mg"
                            },
                            "NIA": {
                                "label": "Niacin (B3)",
                                "quantity": 66.99260000000001,
                                "unit": "mg"
                            },
                            "VITB6A": {
                                "label": "Vitamin B6",
                                "quantity": 4.5246,
                                "unit": "mg"
                            },
                            "FOLDFE": {
                                "label": "Folate equivalent (total)",
                                "quantity": 1203.0400000000002,
                                "unit": "µg"
                            },
                            "FOLFD": {
                                "label": "Folate (food)",
                                "quantity": 350.53999999999996,
                                "unit": "µg"
                            },
                            "FOLAC": {
                                "label": "Folic acid",
                                "quantity": 502.5,
                                "unit": "µg"
                            },
                            "VITB12": {
                                "label": "Vitamin B12",
                                "quantity": 22.553000000000004,
                                "unit": "µg"
                            },
                            "VITD": {
                                "label": "Vitamin D",
                                "quantity": 1.7700000000000002,
                                "unit": "µg"
                            },
                            "TOCPHA": {
                                "label": "Vitamin E",
                                "quantity": 2.9290000000000003,
                                "unit": "mg"
                            },
                            "VITK1": {
                                "label": "Vitamin K",
                                "quantity": 156.11,
                                "unit": "µg"
                            },
                            "WATER": {
                                "label": "Water",
                                "quantity": 1012.9209999999999,
                                "unit": "g"
                            }
                        },
                        "totalDaily": {
                            "ENERC_KCAL": {
                                "label": "Energy",
                                "quantity": 184.296,
                                "unit": "%"
                            },
                            "FAT": {
                                "label": "Fat",
                                "quantity": 331.87938461538465,
                                "unit": "%"
                            },
                            "FASAT": {
                                "label": "Saturated",
                                "quantity": 401.735,
                                "unit": "%"
                            },
                            "CHOCDF": {
                                "label": "Carbs",
                                "quantity": 67.21266666666666,
                                "unit": "%"
                            },
                            "FIBTG": {
                                "label": "Fiber",
                                "quantity": 45.431999999999995,
                                "unit": "%"
                            },
                            "PROCNT": {
                                "label": "Protein",
                                "quantity": 443.68880000000007,
                                "unit": "%"
                            },
                            "CHOLE": {
                                "label": "Cholesterol",
                                "quantity": 311.4,
                                "unit": "%"
                            },
                            "NA": {
                                "label": "Sodium",
                                "quantity": 210.71250000000003,
                                "unit": "%"
                            },
                            "CA": {
                                "label": "Calcium",
                                "quantity": 61.31,
                                "unit": "%"
                            },
                            "MG": {
                                "label": "Magnesium",
                                "quantity": 105.06666666666666,
                                "unit": "%"
                            },
                            "K": {
                                "label": "Potassium",
                                "quantity": 92.82978723404256,
                                "unit": "%"
                            },
                            "FE": {
                                "label": "Iron",
                                "quantity": 189.16111111111113,
                                "unit": "%"
                            },
                            "ZN": {
                                "label": "Zinc",
                                "quantity": 437.4,
                                "unit": "%"
                            },
                            "P": {
                                "label": "Phosphorus",
                                "quantity": 355.91714285714295,
                                "unit": "%"
                            },
                            "VITA_RAE": {
                                "label": "Vitamin A",
                                "quantity": 83.58888888888889,
                                "unit": "%"
                            },
                            "VITC": {
                                "label": "Vitamin C",
                                "quantity": 150.0,
                                "unit": "%"
                            },
                            "THIA": {
                                "label": "Thiamin (B1)",
                                "quantity": 284.66666666666663,
                                "unit": "%"
                            },
                            "RIBF": {
                                "label": "Riboflavin (B2)",
                                "quantity": 222.36923076923074,
                                "unit": "%"
                            },
                            "NIA": {
                                "label": "Niacin (B3)",
                                "quantity": 418.70375000000007,
                                "unit": "%"
                            },
                            "VITB6A": {
                                "label": "Vitamin B6",
                                "quantity": 348.04615384615386,
                                "unit": "%"
                            },
                            "FOLDFE": {
                                "label": "Folate equivalent (total)",
                                "quantity": 300.76000000000005,
                                "unit": "%"
                            },
                            "VITB12": {
                                "label": "Vitamin B12",
                                "quantity": 939.7083333333336,
                                "unit": "%"
                            },
                            "VITD": {
                                "label": "Vitamin D",
                                "quantity": 11.800000000000002,
                                "unit": "%"
                            },
                            "TOCPHA": {
                                "label": "Vitamin E",
                                "quantity": 19.526666666666667,
                                "unit": "%"
                            },
                            "VITK1": {
                                "label": "Vitamin K",
                                "quantity": 130.09166666666667,
                                "unit": "%"
                            }
                        },
                        "digest": [
                            {
                                "label": "Fat",
                                "tag": "FAT",
                                "schemaOrgTag": "fatContent",
                                "total": 215.72160000000002,
                                "hasRDI": True,
                                "daily": 331.87938461538465,
                                "unit": "g",
                                "sub": [
                                    {
                                        "label": "Saturated",
                                        "tag": "FASAT",
                                        "schemaOrgTag": "saturatedFatContent",
                                        "total": 80.34700000000001,
                                        "hasRDI": True,
                                        "daily": 401.735,
                                        "unit": "g"
                                    },
                                    {
                                        "label": "Trans",
                                        "tag": "FATRN",
                                        "schemaOrgTag": "transFatContent",
                                        "total": 12.188500000000001,
                                        "hasRDI": False,
                                        "daily": 0.0,
                                        "unit": "g"
                                    },
                                    {
                                        "label": "Monounsaturated",
                                        "tag": "FAMS",
                                        "schemaOrgTag": 'null',
                                        "total": 93.44000000000001,
                                        "hasRDI": False,
                                        "daily": 0.0,
                                        "unit": "g"
                                    },
                                    {
                                        "label": "Polyunsaturated",
                                        "tag": "FAPU",
                                        "schemaOrgTag": 'null',
                                        "total": 8.927200000000001,
                                        "hasRDI": False,
                                        "daily": 0.0,
                                        "unit": "g"
                                    }
                                ]
                            },
                            {
                                "label": "Carbs",
                                "tag": "CHOCDF",
                                "schemaOrgTag": "carbohydrateContent",
                                "total": 201.63799999999998,
                                "hasRDI": True,
                                "daily": 67.21266666666666,
                                "unit": "g",
                                "sub": [
                                    {
                                        "label": "Carbs (net)",
                                        "tag": "CHOCDF.net",
                                        "schemaOrgTag": 'null',
                                        "total": 190.27999999999997,
                                        "hasRDI": False,
                                        "daily": 0.0,
                                        "unit": "g"
                                    },
                                    {
                                        "label": "Fiber",
                                        "tag": "FIBTG",
                                        "schemaOrgTag": "fiberContent",
                                        "total": 11.358,
                                        "hasRDI": True,
                                        "daily": 45.431999999999995,
                                        "unit": "g"
                                    },
                                    {
                                        "label": "Sugars",
                                        "tag": "SUGAR",
                                        "schemaOrgTag": "sugarContent",
                                        "total": 23.467999999999996,
                                        "hasRDI": False,
                                        "daily": 0.0,
                                        "unit": "g"
                                    },
                                    {
                                        "label": "Sugars, added",
                                        "tag": "SUGAR.added",
                                        "schemaOrgTag": 'null',
                                        "total": 0.0,
                                        "hasRDI": False,
                                        "daily": 0.0,
                                        "unit": "g"
                                    }
                                ]
                            },
                            {
                                "label": "Protein",
                                "tag": "PROCNT",
                                "schemaOrgTag": "proteinContent",
                                "total": 221.8444,
                                "hasRDI": True,
                                "daily": 443.68880000000007,
                                "unit": "g"
                            },
                            {
                                "label": "Cholesterol",
                                "tag": "CHOLE",
                                "schemaOrgTag": "cholesterolContent",
                                "total": 934.2,
                                "hasRDI": True,
                                "daily": 311.4,
                                "unit": "mg"
                            },
                            {
                                "label": "Sodium",
                                "tag": "NA",
                                "schemaOrgTag": "sodiumContent",
                                "total": 5057.1,
                                "hasRDI": True,
                                "daily": 210.71250000000003,
                                "unit": "mg"
                            },
                            {
                                "label": "Calcium",
                                "tag": "CA",
                                "schemaOrgTag": 'null',
                                "total": 613.1,
                                "hasRDI": True,
                                "daily": 61.31,
                                "unit": "mg"
                            },
                            {
                                "label": "Magnesium",
                                "tag": "MG",
                                "schemaOrgTag": 'null',
                                "total": 441.28,
                                "hasRDI": True,
                                "daily": 105.06666666666666,
                                "unit": "mg"
                            },
                            {
                                "label": "Potassium",
                                "tag": "K",
                                "schemaOrgTag": 'null',
                                "total": 4363.0,
                                "hasRDI": True,
                                "daily": 92.82978723404256,
                                "unit": "mg"
                            },
                            {
                                "label": "Iron",
                                "tag": "FE",
                                "schemaOrgTag": 'null',
                                "total": 34.049,
                                "hasRDI": True,
                                "daily": 189.16111111111113,
                                "unit": "mg"
                            },
                            {
                                "label": "Zinc",
                                "tag": "ZN",
                                "schemaOrgTag": 'null',
                                "total": 48.114,
                                "hasRDI": True,
                                "daily": 437.4,
                                "unit": "mg"
                            },
                            {
                                "label": "Phosphorus",
                                "tag": "P",
                                "schemaOrgTag": 'null',
                                "total": 2491.4200000000005,
                                "hasRDI": True,
                                "daily": 355.91714285714295,
                                "unit": "mg"
                            },
                            {
                                "label": "Vitamin A",
                                "tag": "VITA_RAE",
                                "schemaOrgTag": 'null',
                                "total": 752.3,
                                "hasRDI": True,
                                "daily": 83.58888888888889,
                                "unit": "µg"
                            },
                            {
                                "label": "Vitamin C",
                                "tag": "VITC",
                                "schemaOrgTag": 'null',
                                "total": 135.0,
                                "hasRDI": True,
                                "daily": 150.0,
                                "unit": "mg"
                            },
                            {
                                "label": "Thiamin (B1)",
                                "tag": "THIA",
                                "schemaOrgTag": 'null',
                                "total": 3.416,
                                "hasRDI": True,
                                "daily": 284.66666666666663,
                                "unit": "mg"
                            },
                            {
                                "label": "Riboflavin (B2)",
                                "tag": "RIBF",
                                "schemaOrgTag": 'null',
                                "total": 2.8908,
                                "hasRDI": True,
                                "daily": 222.36923076923074,
                                "unit": "mg"
                            },
                            {
                                "label": "Niacin (B3)",
                                "tag": "NIA",
                                "schemaOrgTag": 'null',
                                "total": 66.99260000000001,
                                "hasRDI": True,
                                "daily": 418.70375000000007,
                                "unit": "mg"
                            },
                            {
                                "label": "Vitamin B6",
                                "tag": "VITB6A",
                                "schemaOrgTag": 'null',
                                "total": 4.5246,
                                "hasRDI": True,
                                "daily": 348.04615384615386,
                                "unit": "mg"
                            },
                            {
                                "label": "Folate equivalent (total)",
                                "tag": "FOLDFE",
                                "schemaOrgTag": 'null',
                                "total": 1203.0400000000002,
                                "hasRDI": True,
                                "daily": 300.76000000000005,
                                "unit": "µg"
                            },
                            {
                                "label": "Folate (food)",
                                "tag": "FOLFD",
                                "schemaOrgTag": 'null',
                                "total": 350.53999999999996,
                                "hasRDI": False,
                                "daily": 0.0,
                                "unit": "µg"
                            },
                            {
                                "label": "Folic acid",
                                "tag": "FOLAC",
                                "schemaOrgTag": 'null',
                                "total": 502.5,
                                "hasRDI": False,
                                "daily": 0.0,
                                "unit": "µg"
                            },
                            {
                                "label": "Vitamin B12",
                                "tag": "VITB12",
                                "schemaOrgTag": 'null',
                                "total": 22.553000000000004,
                                "hasRDI": True,
                                "daily": 939.7083333333336,
                                "unit": "µg"
                            },
                            {
                                "label": "Vitamin D",
                                "tag": "VITD",
                                "schemaOrgTag": 'null',
                                "total": 1.7700000000000002,
                                "hasRDI": True,
                                "daily": 11.800000000000002,
                                "unit": "µg"
                            },
                            {
                                "label": "Vitamin E",
                                "tag": "TOCPHA",
                                "schemaOrgTag": 'null',
                                "total": 2.9290000000000003,
                                "hasRDI": True,
                                "daily": 19.526666666666667,
                                "unit": "mg"
                            },
                            {
                                "label": "Vitamin K",
                                "tag": "VITK1",
                                "schemaOrgTag": 'null',
                                "total": 156.11,
                                "hasRDI": True,
                                "daily": 130.09166666666667,
                                "unit": "µg"
                            },
                            {
                                "label": "Sugar alcohols",
                                "tag": "Sugar.alcohol",
                                "schemaOrgTag": 'null',
                                "total": 0.0,
                                "hasRDI": False,
                                "daily": 0.0,
                                "unit": "g"
                            },
                            {
                                "label": "Water",
                                "tag": "WATER",
                                "schemaOrgTag": 'null',
                                "total": 1012.9209999999999,
                                "hasRDI": False,
                                "daily": 0.0,
                                "unit": "g"
                            }
                        ]
                    },
                    "_links": {
                        "self": {
                            "href": "https://api.edamam.com/api/recipes/v2/91478504c3565dce0513e980e3bb78b3?type=public&app_id=e909afd5&app_key=34e59dda7e1bffb92e49c416e9449e1d",
                            "title": "Self"
                        }
                    }
                }
            ]}
        

        # return Response(responseJSON)
        return Response(dummy_data)
       
       
        