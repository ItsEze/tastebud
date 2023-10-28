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

        dummy_data =  {
            "from": 1,
    "to": 20,
    "count": 10000,
    "_links": {
        "next": {
            "href": "https://api.edamam.com/api/recipes/v2/?q=tacos&app_key=34e59dda7e1bffb92e49c416e9449e1d&_cont=CHcVQBtNNQphDmgVQntAEX4BYlNtAgoGQ2RHBGQSYVZzAAQVX3cSUGdFYgd1VwRTEmIUAGMSMgMgUQMCEDEWAGpGMFBxUBFqX3cWQT1OcV9xBB8VADQWVhFCPwoxXVZEITQeVDcBaR4-SQ%3D%3D&type=public&app_id=e909afd5",
            "title": "Next page"
        }
    },
    "hits": [
        {
            "recipe": {
                "uri": "http://www.edamam.com/ontologies/edamam.owl#recipe_6c6b5baf220ceb5b25b7c9695f91046e",
                "label": "Crisp Tacos Picadillo",
                "image": "https://edamam-product-images.s3.amazonaws.com/web-img/32d/32da8c201c42d8aae7a7f51449c83e2a.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLWVhc3QtMSJIMEYCIQCP2Gbt%2ByPQIVKV%2FafgML7WXbkOusL9fCs6d1le6dFKYAIhAJcnuEh%2B1NzOso38QgGaVBwaVQAMxyMJATg%2FR%2Fl0jl96KsEFCJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMMTg3MDE3MTUwOTg2IgydADkJdybnmhdEGwQqlQUNCCJJEzulouVCRRPPDPN9Ik9nmgPZk%2Fam6u04CTug5FWfzto4W1y6mlAuXr3EHPB%2FvTcZ%2BmAkgcS5%2FRfKsviGgYg1PBDbKvJFWJigqXNb6jHaHO3eyZnXpof0Qk2PachTFyGGF7upzvEiKr6BGB6DtCoEGe3wCd0iFSMS%2Ft8LIlICGGYaaCvWq9TXeaXkel5jju8XxawzfW0OY8ad1NODjiJJ%2FJ02goRzRa3HwZdXj0P4%2FwwiBHg8BMnsBu5XvhNCt9Gz%2Bxp9cZIC8TMv%2FY8rOvepaH28zVl5BjLGle3tn5syTeLiH6OS68I4OndB2qqeqZqdi9cu6zb1H0y8aKh8r8IIaHqXhP6jBXwOxUN8uimNrMJnaDPxNdvFPuR5yx8UApiuserTd1b1ZIBFiBJ6lavYUBrkLW%2B7bZIJltsNTSxF2GTKFWoXHKGf3%2FXYj%2FniRUh%2BB3xUXrXh8PzVKChkdfuCxirnj5UG2XCrj22%2BBJG8S8UHiExHaIwt01Nel6V7Y0IlXWvwqK8YEx%2FHOI%2FewXERfrnIQDCsrQyC7qTLL3HndUW2Ke8ib2iC%2BPgaP6xDqkqdlhOSojQHG4rfwcyVOFOzeauzAO7Rc77mb0rCUJdMckP6nKiD7nrtjlZXznFmYhCvjmWQF2l06Jl7xQsr%2BjkGAeoXo9X%2FiC11ZTNfxOVIe3LWWkRvMwGWvgvtgF4ZEDGaLXgsbO4I8%2FpSmGD4ox9ZWDfX%2BtTURCyBYVXqYpQ4TpgMhHqAtTUr4TNc7GRLVbfi1xqZNQDt1Sfdzh3Xq88dOJyKsyUs7rcFuuxoNyxvqstWVaAyRglOH1n%2BpV0xA7%2FKEHa%2F8%2FzH6uaXeIp3eLJN1%2BGlAQc1sP2jehPHqGi5Lc7YMOKk8akGOrABqEMeyIMA72vRUvaZqcs7N77uX3kDw2%2BTfyF8pS8HYdR1%2BEU1ekEPGlPPLyTo0NFmbmMa4urw%2B19eIvlGSnFjiSeee%2F%2BeotdKLVnDgZ5aNxOYivkgUqjazWNTWX1qdv7Jq7GWrNDLwjZiU5zLvpcjSyzLyGAVIo8pW14m4aC3jppuzjKpasygGK2%2Bf%2BmxisMAkIdRRS5aXW9PY%2FuwiBnL3qiZT5RtAdamISZZM9jUAWY%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231028T003610Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFPXEGMX3T%2F20231028%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=c05a327b637c44a7893483521ef702c1ab041e869b09c0ede35084e47d091df5",
                "images": {
                    "THUMBNAIL": {
                        "url": "https://edamam-product-images.s3.amazonaws.com/web-img/32d/32da8c201c42d8aae7a7f51449c83e2a-s.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLWVhc3QtMSJIMEYCIQCP2Gbt%2ByPQIVKV%2FafgML7WXbkOusL9fCs6d1le6dFKYAIhAJcnuEh%2B1NzOso38QgGaVBwaVQAMxyMJATg%2FR%2Fl0jl96KsEFCJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMMTg3MDE3MTUwOTg2IgydADkJdybnmhdEGwQqlQUNCCJJEzulouVCRRPPDPN9Ik9nmgPZk%2Fam6u04CTug5FWfzto4W1y6mlAuXr3EHPB%2FvTcZ%2BmAkgcS5%2FRfKsviGgYg1PBDbKvJFWJigqXNb6jHaHO3eyZnXpof0Qk2PachTFyGGF7upzvEiKr6BGB6DtCoEGe3wCd0iFSMS%2Ft8LIlICGGYaaCvWq9TXeaXkel5jju8XxawzfW0OY8ad1NODjiJJ%2FJ02goRzRa3HwZdXj0P4%2FwwiBHg8BMnsBu5XvhNCt9Gz%2Bxp9cZIC8TMv%2FY8rOvepaH28zVl5BjLGle3tn5syTeLiH6OS68I4OndB2qqeqZqdi9cu6zb1H0y8aKh8r8IIaHqXhP6jBXwOxUN8uimNrMJnaDPxNdvFPuR5yx8UApiuserTd1b1ZIBFiBJ6lavYUBrkLW%2B7bZIJltsNTSxF2GTKFWoXHKGf3%2FXYj%2FniRUh%2BB3xUXrXh8PzVKChkdfuCxirnj5UG2XCrj22%2BBJG8S8UHiExHaIwt01Nel6V7Y0IlXWvwqK8YEx%2FHOI%2FewXERfrnIQDCsrQyC7qTLL3HndUW2Ke8ib2iC%2BPgaP6xDqkqdlhOSojQHG4rfwcyVOFOzeauzAO7Rc77mb0rCUJdMckP6nKiD7nrtjlZXznFmYhCvjmWQF2l06Jl7xQsr%2BjkGAeoXo9X%2FiC11ZTNfxOVIe3LWWkRvMwGWvgvtgF4ZEDGaLXgsbO4I8%2FpSmGD4ox9ZWDfX%2BtTURCyBYVXqYpQ4TpgMhHqAtTUr4TNc7GRLVbfi1xqZNQDt1Sfdzh3Xq88dOJyKsyUs7rcFuuxoNyxvqstWVaAyRglOH1n%2BpV0xA7%2FKEHa%2F8%2FzH6uaXeIp3eLJN1%2BGlAQc1sP2jehPHqGi5Lc7YMOKk8akGOrABqEMeyIMA72vRUvaZqcs7N77uX3kDw2%2BTfyF8pS8HYdR1%2BEU1ekEPGlPPLyTo0NFmbmMa4urw%2B19eIvlGSnFjiSeee%2F%2BeotdKLVnDgZ5aNxOYivkgUqjazWNTWX1qdv7Jq7GWrNDLwjZiU5zLvpcjSyzLyGAVIo8pW14m4aC3jppuzjKpasygGK2%2Bf%2BmxisMAkIdRRS5aXW9PY%2FuwiBnL3qiZT5RtAdamISZZM9jUAWY%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231028T003610Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFPXEGMX3T%2F20231028%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=1829444005ca0ab2a0b9e4bc7bb01319d330f3a4821eaf63331ba47e77244393",
                        "width": 100,
                        "height": 100
                    },
                    "SMALL": {
                        "url": "https://edamam-product-images.s3.amazonaws.com/web-img/32d/32da8c201c42d8aae7a7f51449c83e2a-m.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLWVhc3QtMSJIMEYCIQCP2Gbt%2ByPQIVKV%2FafgML7WXbkOusL9fCs6d1le6dFKYAIhAJcnuEh%2B1NzOso38QgGaVBwaVQAMxyMJATg%2FR%2Fl0jl96KsEFCJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMMTg3MDE3MTUwOTg2IgydADkJdybnmhdEGwQqlQUNCCJJEzulouVCRRPPDPN9Ik9nmgPZk%2Fam6u04CTug5FWfzto4W1y6mlAuXr3EHPB%2FvTcZ%2BmAkgcS5%2FRfKsviGgYg1PBDbKvJFWJigqXNb6jHaHO3eyZnXpof0Qk2PachTFyGGF7upzvEiKr6BGB6DtCoEGe3wCd0iFSMS%2Ft8LIlICGGYaaCvWq9TXeaXkel5jju8XxawzfW0OY8ad1NODjiJJ%2FJ02goRzRa3HwZdXj0P4%2FwwiBHg8BMnsBu5XvhNCt9Gz%2Bxp9cZIC8TMv%2FY8rOvepaH28zVl5BjLGle3tn5syTeLiH6OS68I4OndB2qqeqZqdi9cu6zb1H0y8aKh8r8IIaHqXhP6jBXwOxUN8uimNrMJnaDPxNdvFPuR5yx8UApiuserTd1b1ZIBFiBJ6lavYUBrkLW%2B7bZIJltsNTSxF2GTKFWoXHKGf3%2FXYj%2FniRUh%2BB3xUXrXh8PzVKChkdfuCxirnj5UG2XCrj22%2BBJG8S8UHiExHaIwt01Nel6V7Y0IlXWvwqK8YEx%2FHOI%2FewXERfrnIQDCsrQyC7qTLL3HndUW2Ke8ib2iC%2BPgaP6xDqkqdlhOSojQHG4rfwcyVOFOzeauzAO7Rc77mb0rCUJdMckP6nKiD7nrtjlZXznFmYhCvjmWQF2l06Jl7xQsr%2BjkGAeoXo9X%2FiC11ZTNfxOVIe3LWWkRvMwGWvgvtgF4ZEDGaLXgsbO4I8%2FpSmGD4ox9ZWDfX%2BtTURCyBYVXqYpQ4TpgMhHqAtTUr4TNc7GRLVbfi1xqZNQDt1Sfdzh3Xq88dOJyKsyUs7rcFuuxoNyxvqstWVaAyRglOH1n%2BpV0xA7%2FKEHa%2F8%2FzH6uaXeIp3eLJN1%2BGlAQc1sP2jehPHqGi5Lc7YMOKk8akGOrABqEMeyIMA72vRUvaZqcs7N77uX3kDw2%2BTfyF8pS8HYdR1%2BEU1ekEPGlPPLyTo0NFmbmMa4urw%2B19eIvlGSnFjiSeee%2F%2BeotdKLVnDgZ5aNxOYivkgUqjazWNTWX1qdv7Jq7GWrNDLwjZiU5zLvpcjSyzLyGAVIo8pW14m4aC3jppuzjKpasygGK2%2Bf%2BmxisMAkIdRRS5aXW9PY%2FuwiBnL3qiZT5RtAdamISZZM9jUAWY%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231028T003610Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3599&X-Amz-Credential=ASIASXCYXIIFPXEGMX3T%2F20231028%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=2a08abc1ecead10c2d7d0c6c7d0fe7a456acfcc2682e6d80facb0a8066f43a76",
                        "width": 200,
                        "height": 200
                    },
                    "REGULAR": {
                        "url": "https://edamam-product-images.s3.amazonaws.com/web-img/32d/32da8c201c42d8aae7a7f51449c83e2a.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLWVhc3QtMSJIMEYCIQCP2Gbt%2ByPQIVKV%2FafgML7WXbkOusL9fCs6d1le6dFKYAIhAJcnuEh%2B1NzOso38QgGaVBwaVQAMxyMJATg%2FR%2Fl0jl96KsEFCJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMMTg3MDE3MTUwOTg2IgydADkJdybnmhdEGwQqlQUNCCJJEzulouVCRRPPDPN9Ik9nmgPZk%2Fam6u04CTug5FWfzto4W1y6mlAuXr3EHPB%2FvTcZ%2BmAkgcS5%2FRfKsviGgYg1PBDbKvJFWJigqXNb6jHaHO3eyZnXpof0Qk2PachTFyGGF7upzvEiKr6BGB6DtCoEGe3wCd0iFSMS%2Ft8LIlICGGYaaCvWq9TXeaXkel5jju8XxawzfW0OY8ad1NODjiJJ%2FJ02goRzRa3HwZdXj0P4%2FwwiBHg8BMnsBu5XvhNCt9Gz%2Bxp9cZIC8TMv%2FY8rOvepaH28zVl5BjLGle3tn5syTeLiH6OS68I4OndB2qqeqZqdi9cu6zb1H0y8aKh8r8IIaHqXhP6jBXwOxUN8uimNrMJnaDPxNdvFPuR5yx8UApiuserTd1b1ZIBFiBJ6lavYUBrkLW%2B7bZIJltsNTSxF2GTKFWoXHKGf3%2FXYj%2FniRUh%2BB3xUXrXh8PzVKChkdfuCxirnj5UG2XCrj22%2BBJG8S8UHiExHaIwt01Nel6V7Y0IlXWvwqK8YEx%2FHOI%2FewXERfrnIQDCsrQyC7qTLL3HndUW2Ke8ib2iC%2BPgaP6xDqkqdlhOSojQHG4rfwcyVOFOzeauzAO7Rc77mb0rCUJdMckP6nKiD7nrtjlZXznFmYhCvjmWQF2l06Jl7xQsr%2BjkGAeoXo9X%2FiC11ZTNfxOVIe3LWWkRvMwGWvgvtgF4ZEDGaLXgsbO4I8%2FpSmGD4ox9ZWDfX%2BtTURCyBYVXqYpQ4TpgMhHqAtTUr4TNc7GRLVbfi1xqZNQDt1Sfdzh3Xq88dOJyKsyUs7rcFuuxoNyxvqstWVaAyRglOH1n%2BpV0xA7%2FKEHa%2F8%2FzH6uaXeIp3eLJN1%2BGlAQc1sP2jehPHqGi5Lc7YMOKk8akGOrABqEMeyIMA72vRUvaZqcs7N77uX3kDw2%2BTfyF8pS8HYdR1%2BEU1ekEPGlPPLyTo0NFmbmMa4urw%2B19eIvlGSnFjiSeee%2F%2BeotdKLVnDgZ5aNxOYivkgUqjazWNTWX1qdv7Jq7GWrNDLwjZiU5zLvpcjSyzLyGAVIo8pW14m4aC3jppuzjKpasygGK2%2Bf%2BmxisMAkIdRRS5aXW9PY%2FuwiBnL3qiZT5RtAdamISZZM9jUAWY%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231028T003610Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFPXEGMX3T%2F20231028%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=c05a327b637c44a7893483521ef702c1ab041e869b09c0ede35084e47d091df5",
                        "width": 300,
                        "height": 300
                    },
                    "LARGE": {
                        "url": "https://edamam-product-images.s3.amazonaws.com/web-img/32d/32da8c201c42d8aae7a7f51449c83e2a-l.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLWVhc3QtMSJIMEYCIQCP2Gbt%2ByPQIVKV%2FafgML7WXbkOusL9fCs6d1le6dFKYAIhAJcnuEh%2B1NzOso38QgGaVBwaVQAMxyMJATg%2FR%2Fl0jl96KsEFCJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMMTg3MDE3MTUwOTg2IgydADkJdybnmhdEGwQqlQUNCCJJEzulouVCRRPPDPN9Ik9nmgPZk%2Fam6u04CTug5FWfzto4W1y6mlAuXr3EHPB%2FvTcZ%2BmAkgcS5%2FRfKsviGgYg1PBDbKvJFWJigqXNb6jHaHO3eyZnXpof0Qk2PachTFyGGF7upzvEiKr6BGB6DtCoEGe3wCd0iFSMS%2Ft8LIlICGGYaaCvWq9TXeaXkel5jju8XxawzfW0OY8ad1NODjiJJ%2FJ02goRzRa3HwZdXj0P4%2FwwiBHg8BMnsBu5XvhNCt9Gz%2Bxp9cZIC8TMv%2FY8rOvepaH28zVl5BjLGle3tn5syTeLiH6OS68I4OndB2qqeqZqdi9cu6zb1H0y8aKh8r8IIaHqXhP6jBXwOxUN8uimNrMJnaDPxNdvFPuR5yx8UApiuserTd1b1ZIBFiBJ6lavYUBrkLW%2B7bZIJltsNTSxF2GTKFWoXHKGf3%2FXYj%2FniRUh%2BB3xUXrXh8PzVKChkdfuCxirnj5UG2XCrj22%2BBJG8S8UHiExHaIwt01Nel6V7Y0IlXWvwqK8YEx%2FHOI%2FewXERfrnIQDCsrQyC7qTLL3HndUW2Ke8ib2iC%2BPgaP6xDqkqdlhOSojQHG4rfwcyVOFOzeauzAO7Rc77mb0rCUJdMckP6nKiD7nrtjlZXznFmYhCvjmWQF2l06Jl7xQsr%2BjkGAeoXo9X%2FiC11ZTNfxOVIe3LWWkRvMwGWvgvtgF4ZEDGaLXgsbO4I8%2FpSmGD4ox9ZWDfX%2BtTURCyBYVXqYpQ4TpgMhHqAtTUr4TNc7GRLVbfi1xqZNQDt1Sfdzh3Xq88dOJyKsyUs7rcFuuxoNyxvqstWVaAyRglOH1n%2BpV0xA7%2FKEHa%2F8%2FzH6uaXeIp3eLJN1%2BGlAQc1sP2jehPHqGi5Lc7YMOKk8akGOrABqEMeyIMA72vRUvaZqcs7N77uX3kDw2%2BTfyF8pS8HYdR1%2BEU1ekEPGlPPLyTo0NFmbmMa4urw%2B19eIvlGSnFjiSeee%2F%2BeotdKLVnDgZ5aNxOYivkgUqjazWNTWX1qdv7Jq7GWrNDLwjZiU5zLvpcjSyzLyGAVIo8pW14m4aC3jppuzjKpasygGK2%2Bf%2BmxisMAkIdRRS5aXW9PY%2FuwiBnL3qiZT5RtAdamISZZM9jUAWY%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231028T003610Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFPXEGMX3T%2F20231028%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=bfebe88fc4af16ec425067659e0d79010387e8844cbb40f6505fbae95baf4877",
                        "width": 600,
                        "height": 600
                    }
                },
                "source": "Lottie + Doof",
                "url": "http://www.lottieanddoof.com/2009/07/picadillo/",
                "shareAs": "http://www.edamam.com/recipe/crisp-tacos-picadillo-6c6b5baf220ceb5b25b7c9695f91046e/tacos",
                "yield": 14.0,
                "dietLabels": [],
                "healthLabels": [
                    "Egg-Free",
                    "Peanut-Free",
                    "Tree-Nut-Free",
                    "Soy-Free",
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
                    "Sulfite-Free"
                ],
                "cautions": [
                    "Eggs",
                    "Milk",
                    "Sulfites"
                ],
                "ingredientLines": [
                    "2 tsp Vegetable Oil (picadillo)",
                    "1/2 x white onion (large), chopped (1 1/2 cups) (picadillo)",
                    "1 lb Ground Chuck (80 percent lean) (picadillo)",
                    "1 tbsp minced garlic cloves(1 to 2 cloves) (picadillo)",
                    "2 x tomatoes (medium), diced (2 3/4 cups) (picadillo)",
                    "1 1/2 tsp Paprika (picadillo)",
                    "1 tsp ancho chile powder (picadillo)",
                    "1 tsp Dried Oregano (picadillo)",
                    "1 tsp coarse salt (picadillo)",
                    "1 tsp freshly ground pepper (picadillo)",
                    "3/4 tsp Ground Cumin (picadillo)",
                    "1 1/2 cup water (picadillo)",
                    "3 tsp White Vinegar (picadillo)",
                    "vegetable oil for frying (tacos)",
                    "20 x Corn Tortillas (tacos)",
                    "Iceberg Lettuce Shredded,for serving (tacos)",
                    "white onion shredded,for serving (tacos)",
                    "shredded cheddar cheese (tacos)",
                    "salsa Picante, for serving (tacos)"
                ],
                "ingredients": [
                    {
                        "text": "2 tsp Vegetable Oil (picadillo)",
                        "quantity": 2.0,
                        "measure": "teaspoon",
                        "food": "Vegetable Oil",
                        "weight": 9.333333333964529,
                        "foodCategory": "Oils",
                        "foodId": "food_bt1mzi2ah2sfg8bv7no1qai83w8s",
                        "image": "https://www.edamam.com/food-img/6e5/6e51a63a6300a8ea1b4c4cc68dfaba33.jpg"
                    },
                    {
                        "text": "1/2 x white onion (large), chopped (1 1/2 cups) (picadillo)",
                        "quantity": 1.5,
                        "measure": "cup",
                        "food": "white onion",
                        "weight": 240.0,
                        "foodCategory": "vegetables",
                        "foodId": "food_bmrvi4ob4binw9a5m7l07amlfcoy",
                        "image": "https://www.edamam.com/food-img/205/205e6bf2399b85d34741892ef91cc603.jpg"
                    },
                    {
                        "text": "1 lb Ground Chuck (80 percent lean) (picadillo)",
                        "quantity": 1.0,
                        "measure": "pound",
                        "food": "Ground Chuck",
                        "weight": 453.59237,
                        "foodCategory": "meats",
                        "foodId": "food_bknby1la98smrsbwnthinbam42nj",
                        "image": "https://www.edamam.com/food-img/bab/bab88ab3ea40d34e4c8ae35d6b30344a.jpg"
                    },
                    {
                        "text": "1 tbsp minced garlic cloves(1 to 2 cloves) (picadillo)",
                        "quantity": 1.5,
                        "measure": "clove",
                        "food": "garlic",
                        "weight": 4.5,
                        "foodCategory": "vegetables",
                        "foodId": "food_avtcmx6bgjv1jvay6s6stan8dnyp",
                        "image": "https://www.edamam.com/food-img/6ee/6ee142951f48aaf94f4312409f8d133d.jpg"
                    },
                    {
                        "text": "2 x tomatoes (medium), diced (2 3/4 cups) (picadillo)",
                        "quantity": 2.75,
                        "measure": "cup",
                        "food": "tomatoes",
                        "weight": 409.75,
                        "foodCategory": "vegetables",
                        "foodId": "food_a6k79rrahp8fe2b26zussa3wtkqh",
                        "image": "https://www.edamam.com/food-img/23e/23e727a14f1035bdc2733bb0477efbd2.jpg"
                    },
                    {
                        "text": "1 1/2 tsp Paprika (picadillo)",
                        "quantity": 1.5,
                        "measure": "teaspoon",
                        "food": "Paprika",
                        "weight": 3.4499999999999997,
                        "foodCategory": "Condiments and sauces",
                        "foodId": "food_a9dpcnjb883g67b3lq82ca0421ql",
                        "image": "https://www.edamam.com/food-img/474/474d63763b9d8b9da98c5f43a114648c.jpg"
                    },
                    {
                        "text": "1 tsp ancho chile powder (picadillo)",
                        "quantity": 1.0,
                        "measure": "teaspoon",
                        "food": "ancho chile powder",
                        "weight": 2.7,
                        "foodCategory": "Condiments and sauces",
                        "foodId": "food_aii2sclb4r123rbfr2ybjasrl3nc",
                        "image": "https://www.edamam.com/food-img/e6f/e6f19043caefc23b5feda5520076617e.jpg"
                    },
                    {
                        "text": "1 tsp Dried Oregano (picadillo)",
                        "quantity": 1.0,
                        "measure": "teaspoon",
                        "food": "Dried Oregano",
                        "weight": 1.0,
                        "foodCategory": "Condiments and sauces",
                        "foodId": "food_bkkw6v3bdf0sqiazmzyuiax7i8jr",
                        "image": "https://www.edamam.com/food-img/1b0/1b0eaffb1c261606e0d82fed8e9747a7.jpg"
                    },
                    {
                        "text": "1 tsp coarse salt (picadillo)",
                        "quantity": 1.0,
                        "measure": "teaspoon",
                        "food": "coarse salt",
                        "weight": 4.854166666912875,
                        "foodCategory": "Condiments and sauces",
                        "foodId": "food_a1vgrj1bs8rd1majvmd9ubz8ttkg",
                        "image": "https://www.edamam.com/food-img/694/6943ea510918c6025795e8dc6e6eaaeb.jpg"
                    },
                    {
                        "text": "1 tsp freshly ground pepper (picadillo)",
                        "quantity": 1.0,
                        "measure": "teaspoon",
                        "food": "ground pepper",
                        "weight": 2.9,
                        "foodCategory": "Condiments and sauces",
                        "foodId": "food_b6ywzluaaxv02wad7s1r9ag4py89",
                        "image": "https://www.edamam.com/food-img/c6e/c6e5c3bd8d3bc15175d9766971a4d1b2.jpg"
                    },
                    {
                        "text": "3/4 tsp Ground Cumin (picadillo)",
                        "quantity": 0.75,
                        "measure": "teaspoon",
                        "food": "Cumin",
                        "weight": 1.5750000000000002,
                        "foodCategory": "Condiments and sauces",
                        "foodId": "food_a8jjbx4biqndasapojdb5by3e92e",
                        "image": "https://www.edamam.com/food-img/07e/07e2a4eb77ce46591033846504817d35.jpg"
                    },
                    {
                        "text": "1 1/2 cup water (picadillo)",
                        "quantity": 1.5,
                        "measure": "cup",
                        "food": "water",
                        "weight": 354.88235475,
                        "foodCategory": "water",
                        "foodId": "food_a99vzubbk1ayrsad318rvbzr3dh0",
                        "image": "https://www.edamam.com/food-img/5dd/5dd9d1361847b2ca53c4b19a8f92627e.jpg"
                    },
                    {
                        "text": "3 tsp White Vinegar (picadillo)",
                        "quantity": 3.0,
                        "measure": "teaspoon",
                        "food": "White Vinegar",
                        "weight": 15.0,
                        "foodCategory": "Condiments and sauces",
                        "foodId": "food_am3vwadag9arxtadrwyfcau2w3b2",
                        "image": "https://www.edamam.com/food-img/5f6/5f69b84c399d778c4728e9ab4f8065a2.jpg"
                    },
                    {
                        "text": "vegetable oil for frying (tacos)",
                        "quantity": 0.0,
                        "measure": '',
                        "food": "vegetable oil",
                        "weight": 30.389706256611934,
                        "foodCategory": "Oils",
                        "foodId": "food_bt1mzi2ah2sfg8bv7no1qai83w8s",
                        "image": "https://www.edamam.com/food-img/6e5/6e51a63a6300a8ea1b4c4cc68dfaba33.jpg"
                    },
                    {
                        "text": "20 x Corn Tortillas (tacos)",
                        "quantity": 20.0,
                        "measure": "<unit>",
                        "food": "Corn Tortillas",
                        "weight": 480.0,
                        "foodCategory": "quick breads and pastries",
                        "foodId": "food_bhw0b95agm97s0abfignnb8fsvb3",
                        "image": "https://www.edamam.com/food-img/b8a/b8ad23dcc06f2324f944e47eb579d644.jpg"
                    },
                    {
                        "text": "Iceberg Lettuce Shredded,for serving (tacos)",
                        "quantity": 1.0,
                        "measure": "serving",
                        "food": "Iceberg Lettuce",
                        "weight": 89.0,
                        "foodCategory": "vegetables",
                        "foodId": "food_advhqk1a09o2noblosrg6a4z10xv",
                        "image": "https://www.edamam.com/food-img/3c0/3c00c5ba27678b2f8e1c58b342bd98c7.jpg"
                    },
                    {
                        "text": "white onion shredded,for serving (tacos)",
                        "quantity": 1.0,
                        "measure": "serving",
                        "food": "white onion",
                        "weight": 32.0,
                        "foodCategory": "vegetables",
                        "foodId": "food_bmrvi4ob4binw9a5m7l07amlfcoy",
                        "image": "https://www.edamam.com/food-img/205/205e6bf2399b85d34741892ef91cc603.jpg"
                    },
                    {
                        "text": "shredded cheddar cheese (tacos)",
                        "quantity": 0.0,
                        "measure": '',
                        "food": "cheddar cheese",
                        "weight": 0.0,
                        "foodCategory": "Cheese",
                        "foodId": "food_bhppgmha1u27voagb8eptbp9g376",
                        "image": "https://www.edamam.com/food-img/bcd/bcd94dde1fcde1475b5bf0540f821c5d.jpg"
                    },
                    {
                        "text": "shredded cheddar cheese (tacos)",
                        "quantity": 0.0,
                        "measure": '',
                        "food": "tacos",
                        "weight": 0.0,
                        "foodCategory": "quick breads and pastries",
                        "foodId": "food_amx6njaaa4q9lsaz4k98faejx12a",
                        "image": "https://www.edamam.com/food-img/def/def506222dc404affdfbf7b7133a34c6.jpg"
                    },
                    {
                        "text": "salsa Picante, for serving (tacos)",
                        "quantity": 1.0,
                        "measure": "serving",
                        "food": "salsa",
                        "weight": 130.0,
                        "foodCategory": "canned soup",
                        "foodId": "food_b0t3obfawlm5k2b6erxscacez35u",
                        "image": "https://www.edamam.com/food-img/995/995d0f166754a0475c181b9c156fec43.jpg"
                    }
                ],
                "calories": 4457.683405292573,
                "totalCO2Emissions": 47450.30478677662,
                "co2EmissionsClass": "G",
                "totalWeight": 2515.0854552509145,
                "totalTime": 0.0,
                "cuisineType": [
                    "mexican"
                ],
                "mealType": [
                    "lunch/dinner"
                ],
                "dishType": [
                    "sandwiches"
                ],
                "totalNutrients": {
                    "ENERC_KCAL": {
                        "label": "Energy",
                        "quantity": 4457.683405292573,
                        "unit": "kcal"
                    },
                    "FAT": {
                        "label": "Fat",
                        "quantity": 328.0609168310015,
                        "unit": "g"
                    },
                    "FASAT": {
                        "label": "Saturated",
                        "quantity": 30.5483822685935,
                        "unit": "g"
                    },
                    "FATRN": {
                        "label": "Trans",
                        "quantity": 3.3573725196067916,
                        "unit": "g"
                    },
                    "FAMS": {
                        "label": "Monounsaturated",
                        "quantity": 223.9929709224811,
                        "unit": "g"
                    },
                    "FAPU": {
                        "label": "Polyunsaturated",
                        "quantity": 58.900629937614276,
                        "unit": "g"
                    },
                    "CHOCDF": {
                        "label": "Carbs",
                        "quantity": 271.5091010940001,
                        "unit": "g"
                    },
                    "CHOCDF.net": {
                        "label": "Carbohydrates (net)",
                        "quantity": 225.47840609400006,
                        "unit": "g"
                    },
                    "FIBTG": {
                        "label": "Fiber",
                        "quantity": 46.030694999999994,
                        "unit": "g"
                    },
                    "SUGAR": {
                        "label": "Sugars",
                        "quantity": 32.20742425,
                        "unit": "g"
                    },
                    "PROCNT": {
                        "label": "Protein",
                        "quantity": 135.93132992000002,
                        "unit": "g"
                    },
                    "CHOLE": {
                        "label": "Cholesterol",
                        "quantity": 285.7631931,
                        "unit": "mg"
                    },
                    "NA": {
                        "label": "Sodium",
                        "quantity": 3518.0905582521964,
                        "unit": "mg"
                    },
                    "CA": {
                        "label": "Calcium",
                        "quantity": 678.2914787425591,
                        "unit": "mg"
                    },
                    "MG": {
                        "label": "Magnesium",
                        "quantity": 560.8602379141691,
                        "unit": "mg"
                    },
                    "K": {
                        "label": "Potassium",
                        "quantity": 4542.883198433354,
                        "unit": "mg"
                    },
                    "FE": {
                        "label": "Iron",
                        "quantity": 20.80999503300081,
                        "unit": "mg"
                    },
                    "ZN": {
                        "label": "Zinc",
                        "quantity": 32.746867869141916,
                        "unit": "mg"
                    },
                    "P": {
                        "label": "Phosphorus",
                        "quantity": 2753.9440929000007,
                        "unit": "mg"
                    },
                    "VITA_RAE": {
                        "label": "Vitamin A",
                        "quantity": 345.29929740000006,
                        "unit": "µg"
                    },
                    "VITC": {
                        "label": "Vitamin C",
                        "quantity": 75.9957575,
                        "unit": "mg"
                    },
                    "THIA": {
                        "label": "Thiamin (B1)",
                        "quantity": 1.187434721,
                        "unit": "mg"
                    },
                    "RIBF": {
                        "label": "Riboflavin (B2)",
                        "quantity": 1.3731780540000003,
                        "unit": "mg"
                    },
                    "NIA": {
                        "label": "Niacin (B3)",
                        "quantity": 34.254424543,
                        "unit": "mg"
                    },
                    "VITB6A": {
                        "label": "Vitamin B6",
                        "quantity": 4.696232911600001,
                        "unit": "mg"
                    },
                    "FOLDFE": {
                        "label": "Folate equivalent (total)",
                        "quantity": 177.2706461,
                        "unit": "µg"
                    },
                    "FOLFD": {
                        "label": "Folate (food)",
                        "quantity": 177.2706461,
                        "unit": "µg"
                    },
                    "FOLAC": {
                        "label": "Folic acid",
                        "quantity": 0.0,
                        "unit": "µg"
                    },
                    "VITB12": {
                        "label": "Vitamin B12",
                        "quantity": 10.296546799000001,
                        "unit": "µg"
                    },
                    "VITD": {
                        "label": "Vitamin D",
                        "quantity": 0.4535923700000001,
                        "unit": "µg"
                    },
                    "TOCPHA": {
                        "label": "Vitamin E",
                        "quantity": 71.54381618181233,
                        "unit": "mg"
                    },
                    "VITK1": {
                        "label": "Vitamin K",
                        "quantity": 81.06171305000001,
                        "unit": "µg"
                    },
                    "WATER": {
                        "label": "Water",
                        "quantity": 1695.4347217385837,
                        "unit": "g"
                    }
                },
                "totalDaily": {
                    "ENERC_KCAL": {
                        "label": "Energy",
                        "quantity": 222.88417026462866,
                        "unit": "%"
                    },
                    "FAT": {
                        "label": "Fat",
                        "quantity": 504.7091028169254,
                        "unit": "%"
                    },
                    "FASAT": {
                        "label": "Saturated",
                        "quantity": 152.7419113429675,
                        "unit": "%"
                    },
                    "CHOCDF": {
                        "label": "Carbs",
                        "quantity": 90.50303369800002,
                        "unit": "%"
                    },
                    "FIBTG": {
                        "label": "Fiber",
                        "quantity": 184.12277999999998,
                        "unit": "%"
                    },
                    "PROCNT": {
                        "label": "Protein",
                        "quantity": 271.86265984000005,
                        "unit": "%"
                    },
                    "CHOLE": {
                        "label": "Cholesterol",
                        "quantity": 95.25439770000001,
                        "unit": "%"
                    },
                    "NA": {
                        "label": "Sodium",
                        "quantity": 146.58710659384153,
                        "unit": "%"
                    },
                    "CA": {
                        "label": "Calcium",
                        "quantity": 67.82914787425591,
                        "unit": "%"
                    },
                    "MG": {
                        "label": "Magnesium",
                        "quantity": 133.53815188432597,
                        "unit": "%"
                    },
                    "K": {
                        "label": "Potassium",
                        "quantity": 96.65708932836922,
                        "unit": "%"
                    },
                    "FE": {
                        "label": "Iron",
                        "quantity": 115.61108351667116,
                        "unit": "%"
                    },
                    "ZN": {
                        "label": "Zinc",
                        "quantity": 297.69879881038105,
                        "unit": "%"
                    },
                    "P": {
                        "label": "Phosphorus",
                        "quantity": 393.42058470000006,
                        "unit": "%"
                    },
                    "VITA_RAE": {
                        "label": "Vitamin A",
                        "quantity": 38.36658860000001,
                        "unit": "%"
                    },
                    "VITC": {
                        "label": "Vitamin C",
                        "quantity": 84.43973055555556,
                        "unit": "%"
                    },
                    "THIA": {
                        "label": "Thiamin (B1)",
                        "quantity": 98.95289341666667,
                        "unit": "%"
                    },
                    "RIBF": {
                        "label": "Riboflavin (B2)",
                        "quantity": 105.6290810769231,
                        "unit": "%"
                    },
                    "NIA": {
                        "label": "Niacin (B3)",
                        "quantity": 214.09015339375,
                        "unit": "%"
                    },
                    "VITB6A": {
                        "label": "Vitamin B6",
                        "quantity": 361.2486855076924,
                        "unit": "%"
                    },
                    "FOLDFE": {
                        "label": "Folate equivalent (total)",
                        "quantity": 44.31766152499999,
                        "unit": "%"
                    },
                    "VITB12": {
                        "label": "Vitamin B12",
                        "quantity": 429.02278329166677,
                        "unit": "%"
                    },
                    "VITD": {
                        "label": "Vitamin D",
                        "quantity": 3.0239491333333337,
                        "unit": "%"
                    },
                    "TOCPHA": {
                        "label": "Vitamin E",
                        "quantity": 476.95877454541557,
                        "unit": "%"
                    },
                    "VITK1": {
                        "label": "Vitamin K",
                        "quantity": 67.55142754166667,
                        "unit": "%"
                    }
                },
                "digest": [
                    {
                        "label": "Fat",
                        "tag": "FAT",
                        "schemaOrgTag": "fatContent",
                        "total": 328.0609168310015,
                        "hasRDI": True,
                        "daily": 504.7091028169254,
                        "unit": "g",
                        "sub": [
                            {
                                "label": "Saturated",
                                "tag": "FASAT",
                                "schemaOrgTag": "saturatedFatContent",
                                "total": 30.5483822685935,
                                "hasRDI": True,
                                "daily": 152.7419113429675,
                                "unit": "g"
                            },
                            {
                                "label": "Trans",
                                "tag": "FATRN",
                                "schemaOrgTag": "transFatContent",
                                "total": 3.3573725196067916,
                                "hasRDI": False,
                                "daily": 0.0,
                                "unit": "g"
                            },
                            {
                                "label": "Monounsaturated",
                                "tag": "FAMS",
                                "schemaOrgTag": '',
                                "total": 223.9929709224811,
                                "hasRDI": False,
                                "daily": 0.0,
                                "unit": "g"
                            },
                            {
                                "label": "Polyunsaturated",
                                "tag": "FAPU",
                                "schemaOrgTag": '',
                                "total": 58.900629937614276,
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
                        "total": 271.5091010940001,
                        "hasRDI": True,
                        "daily": 90.50303369800002,
                        "unit": "g",
                        "sub": [
                            {
                                "label": "Carbs (net)",
                                "tag": "CHOCDF.net",
                                "schemaOrgTag": '',
                                "total": 225.47840609400006,
                                "hasRDI": False,
                                "daily": 0.0,
                                "unit": "g"
                            },
                            {
                                "label": "Fiber",
                                "tag": "FIBTG",
                                "schemaOrgTag": "fiberContent",
                                "total": 46.030694999999994,
                                "hasRDI": True,
                                "daily": 184.12277999999998,
                                "unit": "g"
                            },
                            {
                                "label": "Sugars",
                                "tag": "SUGAR",
                                "schemaOrgTag": "sugarContent",
                                "total": 32.20742425,
                                "hasRDI": False,
                                "daily": 0.0,
                                "unit": "g"
                            },
                            {
                                "label": "Sugars, added",
                                "tag": "SUGAR.added",
                                "schemaOrgTag": '',
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
                        "total": 135.93132992000002,
                        "hasRDI": True,
                        "daily": 271.86265984000005,
                        "unit": "g"
                    },
                    {
                        "label": "Cholesterol",
                        "tag": "CHOLE",
                        "schemaOrgTag": "cholesterolContent",
                        "total": 285.7631931,
                        "hasRDI": True,
                        "daily": 95.25439770000001,
                        "unit": "mg"
                    },
                    {
                        "label": "Sodium",
                        "tag": "NA",
                        "schemaOrgTag": "sodiumContent",
                        "total": 3518.0905582521964,
                        "hasRDI": True,
                        "daily": 146.58710659384153,
                        "unit": "mg"
                    },
                    {
                        "label": "Calcium",
                        "tag": "CA",
                        "schemaOrgTag": '',
                        "total": 678.2914787425591,
                        "hasRDI": True,
                        "daily": 67.82914787425591,
                        "unit": "mg"
                    },
                    {
                        "label": "Magnesium",
                        "tag": "MG",
                        "schemaOrgTag": '',
                        "total": 560.8602379141691,
                        "hasRDI": True,
                        "daily": 133.53815188432597,
                        "unit": "mg"
                    },
                    {
                        "label": "Potassium",
                        "tag": "K",
                        "schemaOrgTag": '',
                        "total": 4542.883198433354,
                        "hasRDI": True,
                        "daily": 96.65708932836922,
                        "unit": "mg"
                    },
                    {
                        "label": "Iron",
                        "tag": "FE",
                        "schemaOrgTag": '',
                        "total": 20.80999503300081,
                        "hasRDI": True,
                        "daily": 115.61108351667116,
                        "unit": "mg"
                    },
                    {
                        "label": "Zinc",
                        "tag": "ZN",
                        "schemaOrgTag": '',
                        "total": 32.746867869141916,
                        "hasRDI": True,
                        "daily": 297.69879881038105,
                        "unit": "mg"
                    },
                    {
                        "label": "Phosphorus",
                        "tag": "P",
                        "schemaOrgTag": '',
                        "total": 2753.9440929000007,
                        "hasRDI": True,
                        "daily": 393.42058470000006,
                        "unit": "mg"
                    },
                    {
                        "label": "Vitamin A",
                        "tag": "VITA_RAE",
                        "schemaOrgTag": '',
                        "total": 345.29929740000006,
                        "hasRDI": True,
                        "daily": 38.36658860000001,
                        "unit": "µg"
                    },
                    {
                        "label": "Vitamin C",
                        "tag": "VITC",
                        "schemaOrgTag": '',
                        "total": 75.9957575,
                        "hasRDI": True,
                        "daily": 84.43973055555556,
                        "unit": "mg"
                    },
                    {
                        "label": "Thiamin (B1)",
                        "tag": "THIA",
                        "schemaOrgTag": '',
                        "total": 1.187434721,
                        "hasRDI": True,
                        "daily": 98.95289341666667,
                        "unit": "mg"
                    },
                    {
                        "label": "Riboflavin (B2)",
                        "tag": "RIBF",
                        "schemaOrgTag": '',
                        "total": 1.3731780540000003,
                        "hasRDI": True,
                        "daily": 105.6290810769231,
                        "unit": "mg"
                    },
                    {
                        "label": "Niacin (B3)",
                        "tag": "NIA",
                        "schemaOrgTag": '',
                        "total": 34.254424543,
                        "hasRDI": True,
                        "daily": 214.09015339375,
                        "unit": "mg"
                    },
                    {
                        "label": "Vitamin B6",
                        "tag": "VITB6A",
                        "schemaOrgTag": '',
                        "total": 4.696232911600001,
                        "hasRDI": True,
                        "daily": 361.2486855076924,
                        "unit": "mg"
                    },
                    {
                        "label": "Folate equivalent (total)",
                        "tag": "FOLDFE",
                        "schemaOrgTag": '',
                        "total": 177.2706461,
                        "hasRDI": True,
                        "daily": 44.31766152499999,
                        "unit": "µg"
                    },
                    {
                        "label": "Folate (food)",
                        "tag": "FOLFD",
                        "schemaOrgTag": '',
                        "total": 177.2706461,
                        "hasRDI": False,
                        "daily": 0.0,
                        "unit": "µg"
                    },
                    {
                        "label": "Folic acid",
                        "tag": "FOLAC",
                        "schemaOrgTag": '',
                        "total": 0.0,
                        "hasRDI": False,
                        "daily": 0.0,
                        "unit": "µg"
                    },
                    {
                        "label": "Vitamin B12",
                        "tag": "VITB12",
                        "schemaOrgTag": '',
                        "total": 10.296546799000001,
                        "hasRDI": True,
                        "daily": 429.02278329166677,
                        "unit": "µg"
                    },
                    {
                        "label": "Vitamin D",
                        "tag": "VITD",
                        "schemaOrgTag": '',
                        "total": 0.4535923700000001,
                        "hasRDI": True,
                        "daily": 3.0239491333333337,
                        "unit": "µg"
                    },
                    {
                        "label": "Vitamin E",
                        "tag": "TOCPHA",
                        "schemaOrgTag": '',
                        "total": 71.54381618181233,
                        "hasRDI": True,
                        "daily": 476.95877454541557,
                        "unit": "mg"
                    },
                    {
                        "label": "Vitamin K",
                        "tag": "VITK1",
                        "schemaOrgTag": '',
                        "total": 81.06171305000001,
                        "hasRDI": True,
                        "daily": 67.55142754166667,
                        "unit": "µg"
                    },
                    {
                        "label": "Sugar alcohols",
                        "tag": "Sugar.alcohol",
                        "schemaOrgTag": '',
                        "total": 0.0,
                        "hasRDI": False,
                        "daily": 0.0,
                        "unit": "g"
                    },
                    {
                        "label": "Water",
                        "tag": "WATER",
                        "schemaOrgTag": '',
                        "total": 1695.4347217385837,
                        "hasRDI": False,
                        "daily": 0.0,
                        "unit": "g"
                    }
                ]
            },
            "_links": {
                "self": {
                    "title": "Self",
                    "href": "https://api.edamam.com/api/recipes/v2/6c6b5baf220ceb5b25b7c9695f91046e?type=public&app_id=e909afd5&app_key=34e59dda7e1bffb92e49c416e9449e1d"
                }
            }
        },
        {
            "recipe": {
                "uri": "http://www.edamam.com/ontologies/edamam.owl#recipe_5e7b278b580ccea8ab485607dff5416a",
                "label": "Picadillo Tacos",
                "image": "https://edamam-product-images.s3.amazonaws.com/web-img/274/274e308efd9040b2a6a6963864a7c215.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLWVhc3QtMSJIMEYCIQCP2Gbt%2ByPQIVKV%2FafgML7WXbkOusL9fCs6d1le6dFKYAIhAJcnuEh%2B1NzOso38QgGaVBwaVQAMxyMJATg%2FR%2Fl0jl96KsEFCJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMMTg3MDE3MTUwOTg2IgydADkJdybnmhdEGwQqlQUNCCJJEzulouVCRRPPDPN9Ik9nmgPZk%2Fam6u04CTug5FWfzto4W1y6mlAuXr3EHPB%2FvTcZ%2BmAkgcS5%2FRfKsviGgYg1PBDbKvJFWJigqXNb6jHaHO3eyZnXpof0Qk2PachTFyGGF7upzvEiKr6BGB6DtCoEGe3wCd0iFSMS%2Ft8LIlICGGYaaCvWq9TXeaXkel5jju8XxawzfW0OY8ad1NODjiJJ%2FJ02goRzRa3HwZdXj0P4%2FwwiBHg8BMnsBu5XvhNCt9Gz%2Bxp9cZIC8TMv%2FY8rOvepaH28zVl5BjLGle3tn5syTeLiH6OS68I4OndB2qqeqZqdi9cu6zb1H0y8aKh8r8IIaHqXhP6jBXwOxUN8uimNrMJnaDPxNdvFPuR5yx8UApiuserTd1b1ZIBFiBJ6lavYUBrkLW%2B7bZIJltsNTSxF2GTKFWoXHKGf3%2FXYj%2FniRUh%2BB3xUXrXh8PzVKChkdfuCxirnj5UG2XCrj22%2BBJG8S8UHiExHaIwt01Nel6V7Y0IlXWvwqK8YEx%2FHOI%2FewXERfrnIQDCsrQyC7qTLL3HndUW2Ke8ib2iC%2BPgaP6xDqkqdlhOSojQHG4rfwcyVOFOzeauzAO7Rc77mb0rCUJdMckP6nKiD7nrtjlZXznFmYhCvjmWQF2l06Jl7xQsr%2BjkGAeoXo9X%2FiC11ZTNfxOVIe3LWWkRvMwGWvgvtgF4ZEDGaLXgsbO4I8%2FpSmGD4ox9ZWDfX%2BtTURCyBYVXqYpQ4TpgMhHqAtTUr4TNc7GRLVbfi1xqZNQDt1Sfdzh3Xq88dOJyKsyUs7rcFuuxoNyxvqstWVaAyRglOH1n%2BpV0xA7%2FKEHa%2F8%2FzH6uaXeIp3eLJN1%2BGlAQc1sP2jehPHqGi5Lc7YMOKk8akGOrABqEMeyIMA72vRUvaZqcs7N77uX3kDw2%2BTfyF8pS8HYdR1%2BEU1ekEPGlPPLyTo0NFmbmMa4urw%2B19eIvlGSnFjiSeee%2F%2BeotdKLVnDgZ5aNxOYivkgUqjazWNTWX1qdv7Jq7GWrNDLwjZiU5zLvpcjSyzLyGAVIo8pW14m4aC3jppuzjKpasygGK2%2Bf%2BmxisMAkIdRRS5aXW9PY%2FuwiBnL3qiZT5RtAdamISZZM9jUAWY%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231028T003610Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFPXEGMX3T%2F20231028%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=592c2620bf04dd51c8c7a3703a27f4997ed4b3bbcc40b4b9cf69b97fa057c69e",
                "images": {
                    "THUMBNAIL": {
                        "url": "https://edamam-product-images.s3.amazonaws.com/web-img/274/274e308efd9040b2a6a6963864a7c215-s.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLWVhc3QtMSJIMEYCIQCP2Gbt%2ByPQIVKV%2FafgML7WXbkOusL9fCs6d1le6dFKYAIhAJcnuEh%2B1NzOso38QgGaVBwaVQAMxyMJATg%2FR%2Fl0jl96KsEFCJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMMTg3MDE3MTUwOTg2IgydADkJdybnmhdEGwQqlQUNCCJJEzulouVCRRPPDPN9Ik9nmgPZk%2Fam6u04CTug5FWfzto4W1y6mlAuXr3EHPB%2FvTcZ%2BmAkgcS5%2FRfKsviGgYg1PBDbKvJFWJigqXNb6jHaHO3eyZnXpof0Qk2PachTFyGGF7upzvEiKr6BGB6DtCoEGe3wCd0iFSMS%2Ft8LIlICGGYaaCvWq9TXeaXkel5jju8XxawzfW0OY8ad1NODjiJJ%2FJ02goRzRa3HwZdXj0P4%2FwwiBHg8BMnsBu5XvhNCt9Gz%2Bxp9cZIC8TMv%2FY8rOvepaH28zVl5BjLGle3tn5syTeLiH6OS68I4OndB2qqeqZqdi9cu6zb1H0y8aKh8r8IIaHqXhP6jBXwOxUN8uimNrMJnaDPxNdvFPuR5yx8UApiuserTd1b1ZIBFiBJ6lavYUBrkLW%2B7bZIJltsNTSxF2GTKFWoXHKGf3%2FXYj%2FniRUh%2BB3xUXrXh8PzVKChkdfuCxirnj5UG2XCrj22%2BBJG8S8UHiExHaIwt01Nel6V7Y0IlXWvwqK8YEx%2FHOI%2FewXERfrnIQDCsrQyC7qTLL3HndUW2Ke8ib2iC%2BPgaP6xDqkqdlhOSojQHG4rfwcyVOFOzeauzAO7Rc77mb0rCUJdMckP6nKiD7nrtjlZXznFmYhCvjmWQF2l06Jl7xQsr%2BjkGAeoXo9X%2FiC11ZTNfxOVIe3LWWkRvMwGWvgvtgF4ZEDGaLXgsbO4I8%2FpSmGD4ox9ZWDfX%2BtTURCyBYVXqYpQ4TpgMhHqAtTUr4TNc7GRLVbfi1xqZNQDt1Sfdzh3Xq88dOJyKsyUs7rcFuuxoNyxvqstWVaAyRglOH1n%2BpV0xA7%2FKEHa%2F8%2FzH6uaXeIp3eLJN1%2BGlAQc1sP2jehPHqGi5Lc7YMOKk8akGOrABqEMeyIMA72vRUvaZqcs7N77uX3kDw2%2BTfyF8pS8HYdR1%2BEU1ekEPGlPPLyTo0NFmbmMa4urw%2B19eIvlGSnFjiSeee%2F%2BeotdKLVnDgZ5aNxOYivkgUqjazWNTWX1qdv7Jq7GWrNDLwjZiU5zLvpcjSyzLyGAVIo8pW14m4aC3jppuzjKpasygGK2%2Bf%2BmxisMAkIdRRS5aXW9PY%2FuwiBnL3qiZT5RtAdamISZZM9jUAWY%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231028T003610Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFPXEGMX3T%2F20231028%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=e5789fd8e9587b8e532349b59feb0e0ac18844922eba1c7cabde353b12472e25",
                        "width": 100,
                        "height": 100
                    },
                    "SMALL": {
                        "url": "https://edamam-product-images.s3.amazonaws.com/web-img/274/274e308efd9040b2a6a6963864a7c215-m.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLWVhc3QtMSJIMEYCIQCP2Gbt%2ByPQIVKV%2FafgML7WXbkOusL9fCs6d1le6dFKYAIhAJcnuEh%2B1NzOso38QgGaVBwaVQAMxyMJATg%2FR%2Fl0jl96KsEFCJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMMTg3MDE3MTUwOTg2IgydADkJdybnmhdEGwQqlQUNCCJJEzulouVCRRPPDPN9Ik9nmgPZk%2Fam6u04CTug5FWfzto4W1y6mlAuXr3EHPB%2FvTcZ%2BmAkgcS5%2FRfKsviGgYg1PBDbKvJFWJigqXNb6jHaHO3eyZnXpof0Qk2PachTFyGGF7upzvEiKr6BGB6DtCoEGe3wCd0iFSMS%2Ft8LIlICGGYaaCvWq9TXeaXkel5jju8XxawzfW0OY8ad1NODjiJJ%2FJ02goRzRa3HwZdXj0P4%2FwwiBHg8BMnsBu5XvhNCt9Gz%2Bxp9cZIC8TMv%2FY8rOvepaH28zVl5BjLGle3tn5syTeLiH6OS68I4OndB2qqeqZqdi9cu6zb1H0y8aKh8r8IIaHqXhP6jBXwOxUN8uimNrMJnaDPxNdvFPuR5yx8UApiuserTd1b1ZIBFiBJ6lavYUBrkLW%2B7bZIJltsNTSxF2GTKFWoXHKGf3%2FXYj%2FniRUh%2BB3xUXrXh8PzVKChkdfuCxirnj5UG2XCrj22%2BBJG8S8UHiExHaIwt01Nel6V7Y0IlXWvwqK8YEx%2FHOI%2FewXERfrnIQDCsrQyC7qTLL3HndUW2Ke8ib2iC%2BPgaP6xDqkqdlhOSojQHG4rfwcyVOFOzeauzAO7Rc77mb0rCUJdMckP6nKiD7nrtjlZXznFmYhCvjmWQF2l06Jl7xQsr%2BjkGAeoXo9X%2FiC11ZTNfxOVIe3LWWkRvMwGWvgvtgF4ZEDGaLXgsbO4I8%2FpSmGD4ox9ZWDfX%2BtTURCyBYVXqYpQ4TpgMhHqAtTUr4TNc7GRLVbfi1xqZNQDt1Sfdzh3Xq88dOJyKsyUs7rcFuuxoNyxvqstWVaAyRglOH1n%2BpV0xA7%2FKEHa%2F8%2FzH6uaXeIp3eLJN1%2BGlAQc1sP2jehPHqGi5Lc7YMOKk8akGOrABqEMeyIMA72vRUvaZqcs7N77uX3kDw2%2BTfyF8pS8HYdR1%2BEU1ekEPGlPPLyTo0NFmbmMa4urw%2B19eIvlGSnFjiSeee%2F%2BeotdKLVnDgZ5aNxOYivkgUqjazWNTWX1qdv7Jq7GWrNDLwjZiU5zLvpcjSyzLyGAVIo8pW14m4aC3jppuzjKpasygGK2%2Bf%2BmxisMAkIdRRS5aXW9PY%2FuwiBnL3qiZT5RtAdamISZZM9jUAWY%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231028T003610Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3599&X-Amz-Credential=ASIASXCYXIIFPXEGMX3T%2F20231028%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=145b0d385765a3f47fecfc3bc29f96c01df33876fbda334b088ede77985faea0",
                        "width": 200,
                        "height": 200
                    },
                    "REGULAR": {
                        "url": "https://edamam-product-images.s3.amazonaws.com/web-img/274/274e308efd9040b2a6a6963864a7c215.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLWVhc3QtMSJIMEYCIQCP2Gbt%2ByPQIVKV%2FafgML7WXbkOusL9fCs6d1le6dFKYAIhAJcnuEh%2B1NzOso38QgGaVBwaVQAMxyMJATg%2FR%2Fl0jl96KsEFCJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMMTg3MDE3MTUwOTg2IgydADkJdybnmhdEGwQqlQUNCCJJEzulouVCRRPPDPN9Ik9nmgPZk%2Fam6u04CTug5FWfzto4W1y6mlAuXr3EHPB%2FvTcZ%2BmAkgcS5%2FRfKsviGgYg1PBDbKvJFWJigqXNb6jHaHO3eyZnXpof0Qk2PachTFyGGF7upzvEiKr6BGB6DtCoEGe3wCd0iFSMS%2Ft8LIlICGGYaaCvWq9TXeaXkel5jju8XxawzfW0OY8ad1NODjiJJ%2FJ02goRzRa3HwZdXj0P4%2FwwiBHg8BMnsBu5XvhNCt9Gz%2Bxp9cZIC8TMv%2FY8rOvepaH28zVl5BjLGle3tn5syTeLiH6OS68I4OndB2qqeqZqdi9cu6zb1H0y8aKh8r8IIaHqXhP6jBXwOxUN8uimNrMJnaDPxNdvFPuR5yx8UApiuserTd1b1ZIBFiBJ6lavYUBrkLW%2B7bZIJltsNTSxF2GTKFWoXHKGf3%2FXYj%2FniRUh%2BB3xUXrXh8PzVKChkdfuCxirnj5UG2XCrj22%2BBJG8S8UHiExHaIwt01Nel6V7Y0IlXWvwqK8YEx%2FHOI%2FewXERfrnIQDCsrQyC7qTLL3HndUW2Ke8ib2iC%2BPgaP6xDqkqdlhOSojQHG4rfwcyVOFOzeauzAO7Rc77mb0rCUJdMckP6nKiD7nrtjlZXznFmYhCvjmWQF2l06Jl7xQsr%2BjkGAeoXo9X%2FiC11ZTNfxOVIe3LWWkRvMwGWvgvtgF4ZEDGaLXgsbO4I8%2FpSmGD4ox9ZWDfX%2BtTURCyBYVXqYpQ4TpgMhHqAtTUr4TNc7GRLVbfi1xqZNQDt1Sfdzh3Xq88dOJyKsyUs7rcFuuxoNyxvqstWVaAyRglOH1n%2BpV0xA7%2FKEHa%2F8%2FzH6uaXeIp3eLJN1%2BGlAQc1sP2jehPHqGi5Lc7YMOKk8akGOrABqEMeyIMA72vRUvaZqcs7N77uX3kDw2%2BTfyF8pS8HYdR1%2BEU1ekEPGlPPLyTo0NFmbmMa4urw%2B19eIvlGSnFjiSeee%2F%2BeotdKLVnDgZ5aNxOYivkgUqjazWNTWX1qdv7Jq7GWrNDLwjZiU5zLvpcjSyzLyGAVIo8pW14m4aC3jppuzjKpasygGK2%2Bf%2BmxisMAkIdRRS5aXW9PY%2FuwiBnL3qiZT5RtAdamISZZM9jUAWY%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231028T003610Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFPXEGMX3T%2F20231028%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=592c2620bf04dd51c8c7a3703a27f4997ed4b3bbcc40b4b9cf69b97fa057c69e",
                        "width": 300,
                        "height": 300
                    },
                    "LARGE": {
                        "url": "https://edamam-product-images.s3.amazonaws.com/web-img/274/274e308efd9040b2a6a6963864a7c215-l.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLWVhc3QtMSJIMEYCIQCP2Gbt%2ByPQIVKV%2FafgML7WXbkOusL9fCs6d1le6dFKYAIhAJcnuEh%2B1NzOso38QgGaVBwaVQAMxyMJATg%2FR%2Fl0jl96KsEFCJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMMTg3MDE3MTUwOTg2IgydADkJdybnmhdEGwQqlQUNCCJJEzulouVCRRPPDPN9Ik9nmgPZk%2Fam6u04CTug5FWfzto4W1y6mlAuXr3EHPB%2FvTcZ%2BmAkgcS5%2FRfKsviGgYg1PBDbKvJFWJigqXNb6jHaHO3eyZnXpof0Qk2PachTFyGGF7upzvEiKr6BGB6DtCoEGe3wCd0iFSMS%2Ft8LIlICGGYaaCvWq9TXeaXkel5jju8XxawzfW0OY8ad1NODjiJJ%2FJ02goRzRa3HwZdXj0P4%2FwwiBHg8BMnsBu5XvhNCt9Gz%2Bxp9cZIC8TMv%2FY8rOvepaH28zVl5BjLGle3tn5syTeLiH6OS68I4OndB2qqeqZqdi9cu6zb1H0y8aKh8r8IIaHqXhP6jBXwOxUN8uimNrMJnaDPxNdvFPuR5yx8UApiuserTd1b1ZIBFiBJ6lavYUBrkLW%2B7bZIJltsNTSxF2GTKFWoXHKGf3%2FXYj%2FniRUh%2BB3xUXrXh8PzVKChkdfuCxirnj5UG2XCrj22%2BBJG8S8UHiExHaIwt01Nel6V7Y0IlXWvwqK8YEx%2FHOI%2FewXERfrnIQDCsrQyC7qTLL3HndUW2Ke8ib2iC%2BPgaP6xDqkqdlhOSojQHG4rfwcyVOFOzeauzAO7Rc77mb0rCUJdMckP6nKiD7nrtjlZXznFmYhCvjmWQF2l06Jl7xQsr%2BjkGAeoXo9X%2FiC11ZTNfxOVIe3LWWkRvMwGWvgvtgF4ZEDGaLXgsbO4I8%2FpSmGD4ox9ZWDfX%2BtTURCyBYVXqYpQ4TpgMhHqAtTUr4TNc7GRLVbfi1xqZNQDt1Sfdzh3Xq88dOJyKsyUs7rcFuuxoNyxvqstWVaAyRglOH1n%2BpV0xA7%2FKEHa%2F8%2FzH6uaXeIp3eLJN1%2BGlAQc1sP2jehPHqGi5Lc7YMOKk8akGOrABqEMeyIMA72vRUvaZqcs7N77uX3kDw2%2BTfyF8pS8HYdR1%2BEU1ekEPGlPPLyTo0NFmbmMa4urw%2B19eIvlGSnFjiSeee%2F%2BeotdKLVnDgZ5aNxOYivkgUqjazWNTWX1qdv7Jq7GWrNDLwjZiU5zLvpcjSyzLyGAVIo8pW14m4aC3jppuzjKpasygGK2%2Bf%2BmxisMAkIdRRS5aXW9PY%2FuwiBnL3qiZT5RtAdamISZZM9jUAWY%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231028T003610Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFPXEGMX3T%2F20231028%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=bcb580d23ab9a0e8dbaebd7cbfb632a8fee373ee458e6695e73c577dceba3b63",
                        "width": 600,
                        "height": 600
                    }
                },
                "source": "Honest Cooking",
                "url": "http://honestcooking.com/picadillo-tacos-recipe/",
                "shareAs": "http://www.edamam.com/recipe/picadillo-tacos-5e7b278b580ccea8ab485607dff5416a/tacos",
                "yield": 4.0,
                "dietLabels": [],
                "healthLabels": [
                    "Dairy-Free",
                    "Egg-Free",
                    "Peanut-Free",
                    "Tree-Nut-Free",
                    "Soy-Free",
                    "Fish-Free",
                    "Shellfish-Free",
                    "Crustacean-Free",
                    "Celery-Free",
                    "Mustard-Free",
                    "Sesame-Free",
                    "Lupine-Free",
                    "Mollusk-Free",
                    "Alcohol-Free",
                    "Sulfite-Free"
                ],
                "cautions": [
                    "Eggs",
                    "Milk",
                    "Sulfites"
                ],
                "ingredientLines": [
                    "1 lb ground pork",
                    "¼ cup + 2 tbsp golden raisins",
                    "¼ cup pimento olives, diced",
                    "½ sweet red pepper, diced",
                    "¼ medium onion, diced",
                    "1 tsp agave",
                    "¼ cup of water",
                    "8 hard tacos shells",
                    "Salt and pepper to taste"
                ],
                "ingredients": [
                    {
                        "text": "1 lb ground pork",
                        "quantity": 1.0,
                        "measure": "pound",
                        "food": "ground pork",
                        "weight": 453.59237,
                        "foodCategory": "meats",
                        "foodId": "food_a9ztr5sboipvteae9jcusblxo9ec",
                        "image": "https://www.edamam.com/food-img/5aa/5aafbc5ff7ea82f835cdb9a7fcd9a02e.jpg"
                    },
                    {
                        "text": "¼ cup + 2 tbsp golden raisins",
                        "quantity": 0.25,
                        "measure": "cup",
                        "food": "golden raisins",
                        "weight": 36.25,
                        "foodCategory": "fruit",
                        "foodId": "food_a5xnxgkadye5y6ag1qnwxafwj1rc",
                        "image": "https://www.edamam.com/food-img/ffb/ffb9885ac25e1c1520cb0a92c7e09001.jpg"
                    },
                    {
                        "text": "¼ cup + 2 tbsp golden raisins",
                        "quantity": 2.0,
                        "measure": "tablespoon",
                        "food": "golden raisins",
                        "weight": 18.12499999969356,
                        "foodCategory": "fruit",
                        "foodId": "food_a5xnxgkadye5y6ag1qnwxafwj1rc",
                        "image": "https://www.edamam.com/food-img/ffb/ffb9885ac25e1c1520cb0a92c7e09001.jpg"
                    },
                    {
                        "text": "¼ cup pimento olives, diced",
                        "quantity": 0.25,
                        "measure": "cup",
                        "food": "olives",
                        "weight": 33.600000000568,
                        "foodCategory": "canned fruit",
                        "foodId": "food_bt7u5w5a064gusa46msxfb38ag06",
                        "image": "https://www.edamam.com/food-img/822/8221f2141e8dafd469414b20777735ca.jpg"
                    },
                    {
                        "text": "½ sweet red pepper, diced",
                        "quantity": 0.5,
                        "measure": "<unit>",
                        "food": "sweet red pepper",
                        "weight": 59.5,
                        "foodCategory": "vegetables",
                        "foodId": "food_a8g63g7ak6bnmvbu7agxibp4a0dy",
                        "image": "https://www.edamam.com/food-img/4dc/4dc48b1a506d334b4ab6671b9d56a18f.jpeg"
                    },
                    {
                        "text": "¼ medium onion, diced",
                        "quantity": 0.25,
                        "measure": "<unit>",
                        "food": "onion",
                        "weight": 27.5,
                        "foodCategory": "vegetables",
                        "foodId": "food_bmrvi4ob4binw9a5m7l07amlfcoy",
                        "image": "https://www.edamam.com/food-img/205/205e6bf2399b85d34741892ef91cc603.jpg"
                    },
                    {
                        "text": "1 tsp agave",
                        "quantity": 1.0,
                        "measure": "teaspoon",
                        "food": "agave",
                        "weight": 6.933333333685,
                        "foodCategory": "sugar syrups",
                        "foodId": "food_bj8pkd1bgey1rlbp58zagbjhpfi0",
                        "image": "https://www.edamam.com/food-img/3b5/3b5425ed8e35a486b4138cc8720ae9e4.jpg"
                    },
                    {
                        "text": "¼ cup of water",
                        "quantity": 0.25,
                        "measure": "cup",
                        "food": "water",
                        "weight": 59.147059125,
                        "foodCategory": "water",
                        "foodId": "food_a99vzubbk1ayrsad318rvbzr3dh0",
                        "image": "https://www.edamam.com/food-img/5dd/5dd9d1361847b2ca53c4b19a8f92627e.jpg"
                    },
                    {
                        "text": "8 hard tacos shells",
                        "quantity": 8.0,
                        "measure": "<unit>",
                        "food": "tacos shells",
                        "weight": 101.6,
                        "foodCategory": "quick breads and pastries",
                        "foodId": "food_amx6njaaa4q9lsaz4k98faejx12a",
                        "image": "https://www.edamam.com/food-img/def/def506222dc404affdfbf7b7133a34c6.jpg"
                    },
                    {
                        "text": "Salt and pepper to taste",
                        "quantity": 0.0,
                        "measure": '',
                        "food": "Salt",
                        "weight": 4.77748657475368,
                        "foodCategory": "Condiments and sauces",
                        "foodId": "food_btxz81db72hwbra2pncvebzzzum9",
                        "image": "https://www.edamam.com/food-img/694/6943ea510918c6025795e8dc6e6eaaeb.jpg"
                    },
                    {
                        "text": "Salt and pepper to taste",
                        "quantity": 0.0,
                        "measure": '',
                        "food": "pepper",
                        "weight": 2.38874328737684,
                        "foodCategory": "Condiments and sauces",
                        "foodId": "food_b6ywzluaaxv02wad7s1r9ag4py89",
                        "image": "https://www.edamam.com/food-img/c6e/c6e5c3bd8d3bc15175d9766971a4d1b2.jpg"
                    }
                ],
                "calories": 1931.5037620853916,
                "totalCO2Emissions": 6193.463686936257,
                "co2EmissionsClass": "F",
                "totalWeight": 801.2336291049739,
                "totalTime": 25.0,
                "cuisineType": [
                    "mexican"
                ],
                "mealType": [
                    "lunch/dinner"
                ],
                "dishType": [
                    "sandwiches"
                ],
                "totalNutrients": {
                    "ENERC_KCAL": {
                        "label": "Energy",
                        "quantity": 1931.5037620853916,
                        "unit": "kcal"
                    },
                    "FAT": {
                        "label": "Fat",
                        "quantity": 122.36540547122979,
                        "unit": "g"
                    },
                    "FASAT": {
                        "label": "Saturated",
                        "quantity": 43.79260180070729,
                        "unit": "g"
                    },
                    "FATRN": {
                        "label": "Trans",
                        "quantity": 0.174752,
                        "unit": "g"
                    },
                    "FAMS": {
                        "label": "Monounsaturated",
                        "quantity": 52.47356504093713,
                        "unit": "g"
                    },
                    "FAPU": {
                        "label": "Polyunsaturated",
                        "quantity": 14.61528667501142,
                        "unit": "g"
                    },
                    "CHOCDF": {
                        "label": "Carbs",
                        "quantity": 122.99991903731093,
                        "unit": "g"
                    },
                    "CHOCDF.net": {
                        "label": "Carbohydrates (net)",
                        "quantity": 111.19272531892136,
                        "unit": "g"
                    },
                    "FIBTG": {
                        "label": "Fiber",
                        "quantity": 11.807193718389566,
                        "unit": "g"
                    },
                    "SUGAR": {
                        "label": "Sugars",
                        "quantity": 45.85132962375423,
                        "unit": "g"
                    },
                    "SUGAR.added": {
                        "label": "Sugars, added",
                        "quantity": 4.92266666691635,
                        "unit": "g"
                    },
                    "PROCNT": {
                        "label": "Protein",
                        "quantity": 86.37538983188189,
                        "unit": "g"
                    },
                    "CHOLE": {
                        "label": "Cholesterol",
                        "quantity": 326.5865064,
                        "unit": "mg"
                    },
                    "NA": {
                        "label": "Sodium",
                        "quantity": 1857.21322138296,
                        "unit": "mg"
                    },
                    "CA": {
                        "label": "Calcium",
                        "quantity": 252.94078594320922,
                        "unit": "mg"
                    },
                    "MG": {
                        "label": "Magnesium",
                        "quantity": 205.47799314616643,
                        "unit": "mg"
                    },
                    "K": {
                        "label": "Potassium",
                        "quantity": 2142.5046574885637,
                        "unit": "mg"
                    },
                    "FE": {
                        "label": "Iron",
                        "quantity": 8.854925336320505,
                        "unit": "mg"
                    },
                    "ZN": {
                        "label": "Zinc",
                        "quantity": 12.122337514391052,
                        "unit": "mg"
                    },
                    "P": {
                        "label": "Phosphorus",
                        "quantity": 1113.6606118937632,
                        "unit": "mg"
                    },
                    "VITA_RAE": {
                        "label": "Vitamin A",
                        "quantity": 109.85980808768831,
                        "unit": "µg"
                    },
                    "VITC": {
                        "label": "Vitamin C",
                        "quantity": 83.4125465899953,
                        "unit": "mg"
                    },
                    "THIA": {
                        "label": "Thiamin (B1)",
                        "quantity": 3.5924699911503595,
                        "unit": "mg"
                    },
                    "RIBF": {
                        "label": "Riboflavin (B2)",
                        "quantity": 1.3133780574166931,
                        "unit": "mg"
                    },
                    "NIA": {
                        "label": "Niacin (B3)",
                        "quantity": 22.859772531472817,
                        "unit": "mg"
                    },
                    "VITB6A": {
                        "label": "Vitamin B6",
                        "quantity": 2.3352582700653284,
                        "unit": "mg"
                    },
                    "FOLDFE": {
                        "label": "Folate equivalent (total)",
                        "quantity": 143.67195485884486,
                        "unit": "µg"
                    },
                    "FOLFD": {
                        "label": "Folate (food)",
                        "quantity": 104.04795485884488,
                        "unit": "µg"
                    },
                    "FOLAC": {
                        "label": "Folic acid",
                        "quantity": 24.384,
                        "unit": "µg"
                    },
                    "VITB12": {
                        "label": "Vitamin B12",
                        "quantity": 3.17514659,
                        "unit": "µg"
                    },
                    "VITD": {
                        "label": "Vitamin D",
                        "quantity": 0.0,
                        "unit": "µg"
                    },
                    "TOCPHA": {
                        "label": "Vitamin E",
                        "quantity": 2.2911329301977235,
                        "unit": "mg"
                    },
                    "VITK1": {
                        "label": "Vitamin K",
                        "quantity": 18.054163991295244,
                        "unit": "µg"
                    },
                    "WATER": {
                        "label": "Water",
                        "quantity": 457.38241229392315,
                        "unit": "g"
                    }
                },
                "totalDaily": {
                    "ENERC_KCAL": {
                        "label": "Energy",
                        "quantity": 96.57518810426957,
                        "unit": "%"
                    },
                    "FAT": {
                        "label": "Fat",
                        "quantity": 188.25446995573813,
                        "unit": "%"
                    },
                    "FASAT": {
                        "label": "Saturated",
                        "quantity": 218.96300900353646,
                        "unit": "%"
                    },
                    "CHOCDF": {
                        "label": "Carbs",
                        "quantity": 40.99997301243698,
                        "unit": "%"
                    },
                    "FIBTG": {
                        "label": "Fiber",
                        "quantity": 47.228774873558265,
                        "unit": "%"
                    },
                    "PROCNT": {
                        "label": "Protein",
                        "quantity": 172.75077966376378,
                        "unit": "%"
                    },
                    "CHOLE": {
                        "label": "Cholesterol",
                        "quantity": 108.8621688,
                        "unit": "%"
                    },
                    "NA": {
                        "label": "Sodium",
                        "quantity": 77.38388422429,
                        "unit": "%"
                    },
                    "CA": {
                        "label": "Calcium",
                        "quantity": 25.294078594320922,
                        "unit": "%"
                    },
                    "MG": {
                        "label": "Magnesium",
                        "quantity": 48.92333170146819,
                        "unit": "%"
                    },
                    "K": {
                        "label": "Potassium",
                        "quantity": 45.58520547848008,
                        "unit": "%"
                    },
                    "FE": {
                        "label": "Iron",
                        "quantity": 49.194029646225026,
                        "unit": "%"
                    },
                    "ZN": {
                        "label": "Zinc",
                        "quantity": 110.20306831264593,
                        "unit": "%"
                    },
                    "P": {
                        "label": "Phosphorus",
                        "quantity": 159.09437312768046,
                        "unit": "%"
                    },
                    "VITA_RAE": {
                        "label": "Vitamin A",
                        "quantity": 12.20664534307648,
                        "unit": "%"
                    },
                    "VITC": {
                        "label": "Vitamin C",
                        "quantity": 92.68060732221701,
                        "unit": "%"
                    },
                    "THIA": {
                        "label": "Thiamin (B1)",
                        "quantity": 299.37249926252997,
                        "unit": "%"
                    },
                    "RIBF": {
                        "label": "Riboflavin (B2)",
                        "quantity": 101.02908133974562,
                        "unit": "%"
                    },
                    "NIA": {
                        "label": "Niacin (B3)",
                        "quantity": 142.8735783217051,
                        "unit": "%"
                    },
                    "VITB6A": {
                        "label": "Vitamin B6",
                        "quantity": 179.6352515434868,
                        "unit": "%"
                    },
                    "FOLDFE": {
                        "label": "Folate equivalent (total)",
                        "quantity": 35.917988714711214,
                        "unit": "%"
                    },
                    "VITB12": {
                        "label": "Vitamin B12",
                        "quantity": 132.29777458333334,
                        "unit": "%"
                    },
                    "VITD": {
                        "label": "Vitamin D",
                        "quantity": 0.0,
                        "unit": "%"
                    },
                    "TOCPHA": {
                        "label": "Vitamin E",
                        "quantity": 15.27421953465149,
                        "unit": "%"
                    },
                    "VITK1": {
                        "label": "Vitamin K",
                        "quantity": 15.045136659412703,
                        "unit": "%"
                    }
                },
                "digest": [
                    {
                        "label": "Fat",
                        "tag": "FAT",
                        "schemaOrgTag": "fatContent",
                        "total": 122.36540547122979,
                        "hasRDI": True,
                        "daily": 188.25446995573813,
                        "unit": "g",
                        "sub": [
                            {
                                "label": "Saturated",
                                "tag": "FASAT",
                                "schemaOrgTag": "saturatedFatContent",
                                "total": 43.79260180070729,
                                "hasRDI": True,
                                "daily": 218.96300900353646,
                                "unit": "g"
                            },
                            {
                                "label": "Trans",
                                "tag": "FATRN",
                                "schemaOrgTag": "transFatContent",
                                "total": 0.174752,
                                "hasRDI": False,
                                "daily": 0.0,
                                "unit": "g"
                            },
                            {
                                "label": "Monounsaturated",
                                "tag": "FAMS",
                                "schemaOrgTag": '',
                                "total": 52.47356504093713,
                                "hasRDI": False,
                                "daily": 0.0,
                                "unit": "g"
                            },
                            {
                                "label": "Polyunsaturated",
                                "tag": "FAPU",
                                "schemaOrgTag": '',
                                "total": 14.61528667501142,
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
                        "total": 122.99991903731093,
                        "hasRDI": True,
                        "daily": 40.99997301243698,
                        "unit": "g",
                        "sub": [
                            {
                                "label": "Carbs (net)",
                                "tag": "CHOCDF.net",
                                "schemaOrgTag": '',
                                "total": 111.19272531892136,
                                "hasRDI": False,
                                "daily": 0.0,
                                "unit": "g"
                            },
                            {
                                "label": "Fiber",
                                "tag": "FIBTG",
                                "schemaOrgTag": "fiberContent",
                                "total": 11.807193718389566,
                                "hasRDI": True,
                                "daily": 47.228774873558265,
                                "unit": "g"
                            },
                            {
                                "label": "Sugars",
                                "tag": "SUGAR",
                                "schemaOrgTag": "sugarContent",
                                "total": 45.85132962375423,
                                "hasRDI": False,
                                "daily": 0.0,
                                "unit": "g"
                            },
                            {
                                "label": "Sugars, added",
                                "tag": "SUGAR.added",
                                "schemaOrgTag": '',
                                "total": 4.92266666691635,
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
                        "total": 86.37538983188189,
                        "hasRDI": True,
                        "daily": 172.75077966376378,
                        "unit": "g"
                    },
                    {
                        "label": "Cholesterol",
                        "tag": "CHOLE",
                        "schemaOrgTag": "cholesterolContent",
                        "total": 326.5865064,
                        "hasRDI": True,
                        "daily": 108.8621688,
                        "unit": "mg"
                    },
                    {
                        "label": "Sodium",
                        "tag": "NA",
                        "schemaOrgTag": "sodiumContent",
                        "total": 1857.21322138296,
                        "hasRDI": True,
                        "daily": 77.38388422429,
                        "unit": "mg"
                    },
                    {
                        "label": "Calcium",
                        "tag": "CA",
                        "schemaOrgTag": '',
                        "total": 252.94078594320922,
                        "hasRDI": True,
                        "daily": 25.294078594320922,
                        "unit": "mg"
                    },
                    {
                        "label": "Magnesium",
                        "tag": "MG",
                        "schemaOrgTag": '',
                        "total": 205.47799314616643,
                        "hasRDI": True,
                        "daily": 48.92333170146819,
                        "unit": "mg"
                    },
                    {
                        "label": "Potassium",
                        "tag": "K",
                        "schemaOrgTag": '',
                        "total": 2142.5046574885637,
                        "hasRDI": True,
                        "daily": 45.58520547848008,
                        "unit": "mg"
                    },
                    {
                        "label": "Iron",
                        "tag": "FE",
                        "schemaOrgTag": '',
                        "total": 8.854925336320505,
                        "hasRDI": True,
                        "daily": 49.194029646225026,
                        "unit": "mg"
                    },
                    {
                        "label": "Zinc",
                        "tag": "ZN",
                        "schemaOrgTag": '',
                        "total": 12.122337514391052,
                        "hasRDI": True,
                        "daily": 110.20306831264593,
                        "unit": "mg"
                    },
                    {
                        "label": "Phosphorus",
                        "tag": "P",
                        "schemaOrgTag": '',
                        "total": 1113.6606118937632,
                        "hasRDI": True,
                        "daily": 159.09437312768046,
                        "unit": "mg"
                    },
                    {
                        "label": "Vitamin A",
                        "tag": "VITA_RAE",
                        "schemaOrgTag": '',
                        "total": 109.85980808768831,
                        "hasRDI": True,
                        "daily": 12.20664534307648,
                        "unit": "µg"
                    },
                    {
                        "label": "Vitamin C",
                        "tag": "VITC",
                        "schemaOrgTag": '',
                        "total": 83.4125465899953,
                        "hasRDI": True,
                        "daily": 92.68060732221701,
                        "unit": "mg"
                    },
                    {
                        "label": "Thiamin (B1)",
                        "tag": "THIA",
                        "schemaOrgTag": '',
                        "total": 3.5924699911503595,
                        "hasRDI": True,
                        "daily": 299.37249926252997,
                        "unit": "mg"
                    },
                    {
                        "label": "Riboflavin (B2)",
                        "tag": "RIBF",
                        "schemaOrgTag": '',
                        "total": 1.3133780574166931,
                        "hasRDI": True,
                        "daily": 101.02908133974562,
                        "unit": "mg"
                    },
                    {
                        "label": "Niacin (B3)",
                        "tag": "NIA",
                        "schemaOrgTag": '',
                        "total": 22.859772531472817,
                        "hasRDI": True,
                        "daily": 142.8735783217051,
                        "unit": "mg"
                    },
                    {
                        "label": "Vitamin B6",
                        "tag": "VITB6A",
                        "schemaOrgTag": '',
                        "total": 2.3352582700653284,
                        "hasRDI": True,
                        "daily": 179.6352515434868,
                        "unit": "mg"
                    },
                    {
                        "label": "Folate equivalent (total)",
                        "tag": "FOLDFE",
                        "schemaOrgTag": '',
                        "total": 143.67195485884486,
                        "hasRDI": True,
                        "daily": 35.917988714711214,
                        "unit": "µg"
                    },
                    {
                        "label": "Folate (food)",
                        "tag": "FOLFD",
                        "schemaOrgTag": '',
                        "total": 104.04795485884488,
                        "hasRDI": False,
                        "daily": 0.0,
                        "unit": "µg"
                    },
                    {
                        "label": "Folic acid",
                        "tag": "FOLAC",
                        "schemaOrgTag": '',
                        "total": 24.384,
                        "hasRDI": False,
                        "daily": 0.0,
                        "unit": "µg"
                    },
                    {
                        "label": "Vitamin B12",
                        "tag": "VITB12",
                        "schemaOrgTag": '',
                        "total": 3.17514659,
                        "hasRDI": True,
                        "daily": 132.29777458333334,
                        "unit": "µg"
                    },
                    {
                        "label": "Vitamin D",
                        "tag": "VITD",
                        "schemaOrgTag": '',
                        "total": 0.0,
                        "hasRDI": True,
                        "daily": 0.0,
                        "unit": "µg"
                    },
                    {
                        "label": "Vitamin E",
                        "tag": "TOCPHA",
                        "schemaOrgTag": '',
                        "total": 2.2911329301977235,
                        "hasRDI": True,
                        "daily": 15.27421953465149,
                        "unit": "mg"
                    },
                    {
                        "label": "Vitamin K",
                        "tag": "VITK1",
                        "schemaOrgTag": '',
                        "total": 18.054163991295244,
                        "hasRDI": True,
                        "daily": 15.045136659412703,
                        "unit": "µg"
                    },
                    {
                        "label": "Sugar alcohols",
                        "tag": "Sugar.alcohol",
                        "schemaOrgTag": '',
                        "total": 0.0,
                        "hasRDI": False,
                        "daily": 0.0,
                        "unit": "g"
                    },
                    {
                        "label": "Water",
                        "tag": "WATER",
                        "schemaOrgTag": '',
                        "total": 457.38241229392315,
                        "hasRDI": False,
                        "daily": 0.0,
                        "unit": "g"
                    }
                ]
            },
            "_links": {
                "self": {
                    "title": "Self",
                    "href": "https://api.edamam.com/api/recipes/v2/5e7b278b580ccea8ab485607dff5416a?type=public&app_id=e909afd5&app_key=34e59dda7e1bffb92e49c416e9449e1d"
                }
            }
        },
        {
            "recipe": {
                "uri": "http://www.edamam.com/ontologies/edamam.owl#recipe_cf02d702a2e9d992468b83c9e2088305",
                "label": "Crunchy-Shell Cauliflower Tacos",
                "image": "https://edamam-product-images.s3.amazonaws.com/web-img/524/524287b1ee813c40207b3d3f3b4d9bcd.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLWVhc3QtMSJIMEYCIQCP2Gbt%2ByPQIVKV%2FafgML7WXbkOusL9fCs6d1le6dFKYAIhAJcnuEh%2B1NzOso38QgGaVBwaVQAMxyMJATg%2FR%2Fl0jl96KsEFCJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMMTg3MDE3MTUwOTg2IgydADkJdybnmhdEGwQqlQUNCCJJEzulouVCRRPPDPN9Ik9nmgPZk%2Fam6u04CTug5FWfzto4W1y6mlAuXr3EHPB%2FvTcZ%2BmAkgcS5%2FRfKsviGgYg1PBDbKvJFWJigqXNb6jHaHO3eyZnXpof0Qk2PachTFyGGF7upzvEiKr6BGB6DtCoEGe3wCd0iFSMS%2Ft8LIlICGGYaaCvWq9TXeaXkel5jju8XxawzfW0OY8ad1NODjiJJ%2FJ02goRzRa3HwZdXj0P4%2FwwiBHg8BMnsBu5XvhNCt9Gz%2Bxp9cZIC8TMv%2FY8rOvepaH28zVl5BjLGle3tn5syTeLiH6OS68I4OndB2qqeqZqdi9cu6zb1H0y8aKh8r8IIaHqXhP6jBXwOxUN8uimNrMJnaDPxNdvFPuR5yx8UApiuserTd1b1ZIBFiBJ6lavYUBrkLW%2B7bZIJltsNTSxF2GTKFWoXHKGf3%2FXYj%2FniRUh%2BB3xUXrXh8PzVKChkdfuCxirnj5UG2XCrj22%2BBJG8S8UHiExHaIwt01Nel6V7Y0IlXWvwqK8YEx%2FHOI%2FewXERfrnIQDCsrQyC7qTLL3HndUW2Ke8ib2iC%2BPgaP6xDqkqdlhOSojQHG4rfwcyVOFOzeauzAO7Rc77mb0rCUJdMckP6nKiD7nrtjlZXznFmYhCvjmWQF2l06Jl7xQsr%2BjkGAeoXo9X%2FiC11ZTNfxOVIe3LWWkRvMwGWvgvtgF4ZEDGaLXgsbO4I8%2FpSmGD4ox9ZWDfX%2BtTURCyBYVXqYpQ4TpgMhHqAtTUr4TNc7GRLVbfi1xqZNQDt1Sfdzh3Xq88dOJyKsyUs7rcFuuxoNyxvqstWVaAyRglOH1n%2BpV0xA7%2FKEHa%2F8%2FzH6uaXeIp3eLJN1%2BGlAQc1sP2jehPHqGi5Lc7YMOKk8akGOrABqEMeyIMA72vRUvaZqcs7N77uX3kDw2%2BTfyF8pS8HYdR1%2BEU1ekEPGlPPLyTo0NFmbmMa4urw%2B19eIvlGSnFjiSeee%2F%2BeotdKLVnDgZ5aNxOYivkgUqjazWNTWX1qdv7Jq7GWrNDLwjZiU5zLvpcjSyzLyGAVIo8pW14m4aC3jppuzjKpasygGK2%2Bf%2BmxisMAkIdRRS5aXW9PY%2FuwiBnL3qiZT5RtAdamISZZM9jUAWY%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231028T003610Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3599&X-Amz-Credential=ASIASXCYXIIFPXEGMX3T%2F20231028%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=c0847575151fc559896f2406467063c10a4b5deee19306cccda579728ce76c39",
                "images": {
                    "THUMBNAIL": {
                        "url": "https://edamam-product-images.s3.amazonaws.com/web-img/524/524287b1ee813c40207b3d3f3b4d9bcd-s.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLWVhc3QtMSJIMEYCIQCP2Gbt%2ByPQIVKV%2FafgML7WXbkOusL9fCs6d1le6dFKYAIhAJcnuEh%2B1NzOso38QgGaVBwaVQAMxyMJATg%2FR%2Fl0jl96KsEFCJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMMTg3MDE3MTUwOTg2IgydADkJdybnmhdEGwQqlQUNCCJJEzulouVCRRPPDPN9Ik9nmgPZk%2Fam6u04CTug5FWfzto4W1y6mlAuXr3EHPB%2FvTcZ%2BmAkgcS5%2FRfKsviGgYg1PBDbKvJFWJigqXNb6jHaHO3eyZnXpof0Qk2PachTFyGGF7upzvEiKr6BGB6DtCoEGe3wCd0iFSMS%2Ft8LIlICGGYaaCvWq9TXeaXkel5jju8XxawzfW0OY8ad1NODjiJJ%2FJ02goRzRa3HwZdXj0P4%2FwwiBHg8BMnsBu5XvhNCt9Gz%2Bxp9cZIC8TMv%2FY8rOvepaH28zVl5BjLGle3tn5syTeLiH6OS68I4OndB2qqeqZqdi9cu6zb1H0y8aKh8r8IIaHqXhP6jBXwOxUN8uimNrMJnaDPxNdvFPuR5yx8UApiuserTd1b1ZIBFiBJ6lavYUBrkLW%2B7bZIJltsNTSxF2GTKFWoXHKGf3%2FXYj%2FniRUh%2BB3xUXrXh8PzVKChkdfuCxirnj5UG2XCrj22%2BBJG8S8UHiExHaIwt01Nel6V7Y0IlXWvwqK8YEx%2FHOI%2FewXERfrnIQDCsrQyC7qTLL3HndUW2Ke8ib2iC%2BPgaP6xDqkqdlhOSojQHG4rfwcyVOFOzeauzAO7Rc77mb0rCUJdMckP6nKiD7nrtjlZXznFmYhCvjmWQF2l06Jl7xQsr%2BjkGAeoXo9X%2FiC11ZTNfxOVIe3LWWkRvMwGWvgvtgF4ZEDGaLXgsbO4I8%2FpSmGD4ox9ZWDfX%2BtTURCyBYVXqYpQ4TpgMhHqAtTUr4TNc7GRLVbfi1xqZNQDt1Sfdzh3Xq88dOJyKsyUs7rcFuuxoNyxvqstWVaAyRglOH1n%2BpV0xA7%2FKEHa%2F8%2FzH6uaXeIp3eLJN1%2BGlAQc1sP2jehPHqGi5Lc7YMOKk8akGOrABqEMeyIMA72vRUvaZqcs7N77uX3kDw2%2BTfyF8pS8HYdR1%2BEU1ekEPGlPPLyTo0NFmbmMa4urw%2B19eIvlGSnFjiSeee%2F%2BeotdKLVnDgZ5aNxOYivkgUqjazWNTWX1qdv7Jq7GWrNDLwjZiU5zLvpcjSyzLyGAVIo8pW14m4aC3jppuzjKpasygGK2%2Bf%2BmxisMAkIdRRS5aXW9PY%2FuwiBnL3qiZT5RtAdamISZZM9jUAWY%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231028T003610Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFPXEGMX3T%2F20231028%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=b6f7d32f22d5557b361630f9605d6c8619b6100394257852f811d5d087da718a",
                        "width": 100,
                        "height": 100
                    },
                    "SMALL": {
                        "url": "https://edamam-product-images.s3.amazonaws.com/web-img/524/524287b1ee813c40207b3d3f3b4d9bcd-m.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLWVhc3QtMSJIMEYCIQCP2Gbt%2ByPQIVKV%2FafgML7WXbkOusL9fCs6d1le6dFKYAIhAJcnuEh%2B1NzOso38QgGaVBwaVQAMxyMJATg%2FR%2Fl0jl96KsEFCJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMMTg3MDE3MTUwOTg2IgydADkJdybnmhdEGwQqlQUNCCJJEzulouVCRRPPDPN9Ik9nmgPZk%2Fam6u04CTug5FWfzto4W1y6mlAuXr3EHPB%2FvTcZ%2BmAkgcS5%2FRfKsviGgYg1PBDbKvJFWJigqXNb6jHaHO3eyZnXpof0Qk2PachTFyGGF7upzvEiKr6BGB6DtCoEGe3wCd0iFSMS%2Ft8LIlICGGYaaCvWq9TXeaXkel5jju8XxawzfW0OY8ad1NODjiJJ%2FJ02goRzRa3HwZdXj0P4%2FwwiBHg8BMnsBu5XvhNCt9Gz%2Bxp9cZIC8TMv%2FY8rOvepaH28zVl5BjLGle3tn5syTeLiH6OS68I4OndB2qqeqZqdi9cu6zb1H0y8aKh8r8IIaHqXhP6jBXwOxUN8uimNrMJnaDPxNdvFPuR5yx8UApiuserTd1b1ZIBFiBJ6lavYUBrkLW%2B7bZIJltsNTSxF2GTKFWoXHKGf3%2FXYj%2FniRUh%2BB3xUXrXh8PzVKChkdfuCxirnj5UG2XCrj22%2BBJG8S8UHiExHaIwt01Nel6V7Y0IlXWvwqK8YEx%2FHOI%2FewXERfrnIQDCsrQyC7qTLL3HndUW2Ke8ib2iC%2BPgaP6xDqkqdlhOSojQHG4rfwcyVOFOzeauzAO7Rc77mb0rCUJdMckP6nKiD7nrtjlZXznFmYhCvjmWQF2l06Jl7xQsr%2BjkGAeoXo9X%2FiC11ZTNfxOVIe3LWWkRvMwGWvgvtgF4ZEDGaLXgsbO4I8%2FpSmGD4ox9ZWDfX%2BtTURCyBYVXqYpQ4TpgMhHqAtTUr4TNc7GRLVbfi1xqZNQDt1Sfdzh3Xq88dOJyKsyUs7rcFuuxoNyxvqstWVaAyRglOH1n%2BpV0xA7%2FKEHa%2F8%2FzH6uaXeIp3eLJN1%2BGlAQc1sP2jehPHqGi5Lc7YMOKk8akGOrABqEMeyIMA72vRUvaZqcs7N77uX3kDw2%2BTfyF8pS8HYdR1%2BEU1ekEPGlPPLyTo0NFmbmMa4urw%2B19eIvlGSnFjiSeee%2F%2BeotdKLVnDgZ5aNxOYivkgUqjazWNTWX1qdv7Jq7GWrNDLwjZiU5zLvpcjSyzLyGAVIo8pW14m4aC3jppuzjKpasygGK2%2Bf%2BmxisMAkIdRRS5aXW9PY%2FuwiBnL3qiZT5RtAdamISZZM9jUAWY%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231028T003610Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFPXEGMX3T%2F20231028%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=27255a39e0ad0136a7a924722bb1de6246bfb0f077bfa05c20aa5b77822ddfcf",
                        "width": 200,
                        "height": 200
                    },
                    "REGULAR": {
                        "url": "https://edamam-product-images.s3.amazonaws.com/web-img/524/524287b1ee813c40207b3d3f3b4d9bcd.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLWVhc3QtMSJIMEYCIQCP2Gbt%2ByPQIVKV%2FafgML7WXbkOusL9fCs6d1le6dFKYAIhAJcnuEh%2B1NzOso38QgGaVBwaVQAMxyMJATg%2FR%2Fl0jl96KsEFCJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMMTg3MDE3MTUwOTg2IgydADkJdybnmhdEGwQqlQUNCCJJEzulouVCRRPPDPN9Ik9nmgPZk%2Fam6u04CTug5FWfzto4W1y6mlAuXr3EHPB%2FvTcZ%2BmAkgcS5%2FRfKsviGgYg1PBDbKvJFWJigqXNb6jHaHO3eyZnXpof0Qk2PachTFyGGF7upzvEiKr6BGB6DtCoEGe3wCd0iFSMS%2Ft8LIlICGGYaaCvWq9TXeaXkel5jju8XxawzfW0OY8ad1NODjiJJ%2FJ02goRzRa3HwZdXj0P4%2FwwiBHg8BMnsBu5XvhNCt9Gz%2Bxp9cZIC8TMv%2FY8rOvepaH28zVl5BjLGle3tn5syTeLiH6OS68I4OndB2qqeqZqdi9cu6zb1H0y8aKh8r8IIaHqXhP6jBXwOxUN8uimNrMJnaDPxNdvFPuR5yx8UApiuserTd1b1ZIBFiBJ6lavYUBrkLW%2B7bZIJltsNTSxF2GTKFWoXHKGf3%2FXYj%2FniRUh%2BB3xUXrXh8PzVKChkdfuCxirnj5UG2XCrj22%2BBJG8S8UHiExHaIwt01Nel6V7Y0IlXWvwqK8YEx%2FHOI%2FewXERfrnIQDCsrQyC7qTLL3HndUW2Ke8ib2iC%2BPgaP6xDqkqdlhOSojQHG4rfwcyVOFOzeauzAO7Rc77mb0rCUJdMckP6nKiD7nrtjlZXznFmYhCvjmWQF2l06Jl7xQsr%2BjkGAeoXo9X%2FiC11ZTNfxOVIe3LWWkRvMwGWvgvtgF4ZEDGaLXgsbO4I8%2FpSmGD4ox9ZWDfX%2BtTURCyBYVXqYpQ4TpgMhHqAtTUr4TNc7GRLVbfi1xqZNQDt1Sfdzh3Xq88dOJyKsyUs7rcFuuxoNyxvqstWVaAyRglOH1n%2BpV0xA7%2FKEHa%2F8%2FzH6uaXeIp3eLJN1%2BGlAQc1sP2jehPHqGi5Lc7YMOKk8akGOrABqEMeyIMA72vRUvaZqcs7N77uX3kDw2%2BTfyF8pS8HYdR1%2BEU1ekEPGlPPLyTo0NFmbmMa4urw%2B19eIvlGSnFjiSeee%2F%2BeotdKLVnDgZ5aNxOYivkgUqjazWNTWX1qdv7Jq7GWrNDLwjZiU5zLvpcjSyzLyGAVIo8pW14m4aC3jppuzjKpasygGK2%2Bf%2BmxisMAkIdRRS5aXW9PY%2FuwiBnL3qiZT5RtAdamISZZM9jUAWY%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231028T003610Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFPXEGMX3T%2F20231028%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=4f8100c761f5a54305ddb947b0dd4d4f938c2df581d6c60f79e74b4f4227f6c7",
                        "width": 300,
                        "height": 300
                    },
                    "LARGE": {
                        "url": "https://edamam-product-images.s3.amazonaws.com/web-img/524/524287b1ee813c40207b3d3f3b4d9bcd-l.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLWVhc3QtMSJIMEYCIQCP2Gbt%2ByPQIVKV%2FafgML7WXbkOusL9fCs6d1le6dFKYAIhAJcnuEh%2B1NzOso38QgGaVBwaVQAMxyMJATg%2FR%2Fl0jl96KsEFCJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMMTg3MDE3MTUwOTg2IgydADkJdybnmhdEGwQqlQUNCCJJEzulouVCRRPPDPN9Ik9nmgPZk%2Fam6u04CTug5FWfzto4W1y6mlAuXr3EHPB%2FvTcZ%2BmAkgcS5%2FRfKsviGgYg1PBDbKvJFWJigqXNb6jHaHO3eyZnXpof0Qk2PachTFyGGF7upzvEiKr6BGB6DtCoEGe3wCd0iFSMS%2Ft8LIlICGGYaaCvWq9TXeaXkel5jju8XxawzfW0OY8ad1NODjiJJ%2FJ02goRzRa3HwZdXj0P4%2FwwiBHg8BMnsBu5XvhNCt9Gz%2Bxp9cZIC8TMv%2FY8rOvepaH28zVl5BjLGle3tn5syTeLiH6OS68I4OndB2qqeqZqdi9cu6zb1H0y8aKh8r8IIaHqXhP6jBXwOxUN8uimNrMJnaDPxNdvFPuR5yx8UApiuserTd1b1ZIBFiBJ6lavYUBrkLW%2B7bZIJltsNTSxF2GTKFWoXHKGf3%2FXYj%2FniRUh%2BB3xUXrXh8PzVKChkdfuCxirnj5UG2XCrj22%2BBJG8S8UHiExHaIwt01Nel6V7Y0IlXWvwqK8YEx%2FHOI%2FewXERfrnIQDCsrQyC7qTLL3HndUW2Ke8ib2iC%2BPgaP6xDqkqdlhOSojQHG4rfwcyVOFOzeauzAO7Rc77mb0rCUJdMckP6nKiD7nrtjlZXznFmYhCvjmWQF2l06Jl7xQsr%2BjkGAeoXo9X%2FiC11ZTNfxOVIe3LWWkRvMwGWvgvtgF4ZEDGaLXgsbO4I8%2FpSmGD4ox9ZWDfX%2BtTURCyBYVXqYpQ4TpgMhHqAtTUr4TNc7GRLVbfi1xqZNQDt1Sfdzh3Xq88dOJyKsyUs7rcFuuxoNyxvqstWVaAyRglOH1n%2BpV0xA7%2FKEHa%2F8%2FzH6uaXeIp3eLJN1%2BGlAQc1sP2jehPHqGi5Lc7YMOKk8akGOrABqEMeyIMA72vRUvaZqcs7N77uX3kDw2%2BTfyF8pS8HYdR1%2BEU1ekEPGlPPLyTo0NFmbmMa4urw%2B19eIvlGSnFjiSeee%2F%2BeotdKLVnDgZ5aNxOYivkgUqjazWNTWX1qdv7Jq7GWrNDLwjZiU5zLvpcjSyzLyGAVIo8pW14m4aC3jppuzjKpasygGK2%2Bf%2BmxisMAkIdRRS5aXW9PY%2FuwiBnL3qiZT5RtAdamISZZM9jUAWY%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231028T003610Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFPXEGMX3T%2F20231028%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=7731cf6154e8d66878f14aa9a6fd247fb9c01fa9d0cbb6cf6904516ac01240fc",
                        "width": 600,
                        "height": 600
                    }
                },
                "source": "Food52",
                "url": "https://food52.com/recipes/76795-crunchy-shell-cauliflower-tacos",
                "shareAs": "http://www.edamam.com/recipe/crunchy-shell-cauliflower-tacos-cf02d702a2e9d992468b83c9e2088305/tacos",
                "yield": 8.0,
                "dietLabels": [],
                "healthLabels": [
                    "Sugar-Conscious",
                    "Vegetarian",
                    "Pescatarian",
                    "Mediterranean",
                    "Egg-Free",
                    "Peanut-Free",
                    "Tree-Nut-Free",
                    "Soy-Free",
                    "Fish-Free",
                    "Shellfish-Free",
                    "Pork-Free",
                    "Red-Meat-Free",
                    "Crustacean-Free",
                    "Celery-Free",
                    "Mustard-Free",
                    "Sesame-Free",
                    "Lupine-Free",
                    "Mollusk-Free",
                    "Alcohol-Free",
                    "Sulfite-Free",
                    "Kosher"
                ],
                "cautions": [
                    "Eggs",
                    "Milk",
                    "Sulfites"
                ],
                "ingredientLines": [
                    "1 head cauliflower",
                    "3 tablespoons extra-virgin olive oil",
                    "3 1/2 teaspoons chili powder",
                    "3/4 teaspoon kosher salt, plus more to taste",
                    "8 hard-shell tacos",
                    "1 cup shredded iceberg lettuce",
                    "1 cup grated pepper jack cheese"
                ],
                "ingredients": [
                    {
                        "text": "1 head cauliflower",
                        "quantity": 1.0,
                        "measure": "head",
                        "food": "cauliflower",
                        "weight": 537.7777777777777,
                        "foodCategory": "vegetables",
                        "foodId": "food_buqfaxubzh6hi5asev8a5aj9sr71",
                        "image": "https://www.edamam.com/food-img/ca2/ca217d31067dffd35ce1215e7f336bd8.jpg"
                    },
                    {
                        "text": "3 tablespoons extra-virgin olive oil",
                        "quantity": 3.0,
                        "measure": "tablespoon",
                        "food": "extra-virgin olive oil",
                        "weight": 40.5,
                        "foodCategory": "Oils",
                        "foodId": "food_b1d1icuad3iktrbqby0hiagafaz7",
                        "image": "https://www.edamam.com/food-img/4d6/4d651eaa8a353647746290c7a9b29d84.jpg"
                    },
                    {
                        "text": "3 1/2 teaspoons chili powder",
                        "quantity": 3.5,
                        "measure": "teaspoon",
                        "food": "chili powder",
                        "weight": 9.450000000000001,
                        "foodCategory": "Condiments and sauces",
                        "foodId": "food_aii2sclb4r123rbfr2ybjasrl3nc",
                        "image": "https://www.edamam.com/food-img/e6f/e6f19043caefc23b5feda5520076617e.jpg"
                    },
                    {
                        "text": "3/4 teaspoon kosher salt, plus more to taste",
                        "quantity": 0.75,
                        "measure": "teaspoon",
                        "food": "kosher salt",
                        "weight": 3.6406250001846567,
                        "foodCategory": "Condiments and sauces",
                        "foodId": "food_a1vgrj1bs8rd1majvmd9ubz8ttkg",
                        "image": "https://www.edamam.com/food-img/694/6943ea510918c6025795e8dc6e6eaaeb.jpg"
                    },
                    {
                        "text": "8 hard-shell tacos",
                        "quantity": 8.0,
                        "measure": "<unit>",
                        "food": "tacos",
                        "weight": 101.6,
                        "foodCategory": "quick breads and pastries",
                        "foodId": "food_amx6njaaa4q9lsaz4k98faejx12a",
                        "image": "https://www.edamam.com/food-img/def/def506222dc404affdfbf7b7133a34c6.jpg"
                    },
                    {
                        "text": "1 cup shredded iceberg lettuce",
                        "quantity": 1.0,
                        "measure": "cup",
                        "food": "iceberg lettuce",
                        "weight": 72.0,
                        "foodCategory": "vegetables",
                        "foodId": "food_advhqk1a09o2noblosrg6a4z10xv",
                        "image": "https://www.edamam.com/food-img/3c0/3c00c5ba27678b2f8e1c58b342bd98c7.jpg"
                    },
                    {
                        "text": "1 cup grated pepper jack cheese",
                        "quantity": 1.0,
                        "measure": "cup",
                        "food": "jack cheese",
                        "weight": 132.0,
                        "foodCategory": "Cheese",
                        "foodId": "food_atp17pta7d5it2a80ct13ard6aj3",
                        "image": "https://www.edamam.com/food-img/590/59062b9f8d57ebc7d831b7b7c231f726.jpg"
                    }
                ],
                "calories": 1505.1694444444445,
                "totalCO2Emissions": 3950.5524687599827,
                "co2EmissionsClass": "D",
                "totalWeight": 894.656833312142,
                "totalTime": 50.0,
                "cuisineType": [
                    "american"
                ],
                "mealType": [
                    "lunch/dinner"
                ],
                "dishType": [
                    "bread"
                ],
                "totalNutrients": {
                    "ENERC_KCAL": {
                        "label": "Energy",
                        "quantity": 1505.1694444444445,
                        "unit": "kcal"
                    },
                    "FAT": {
                        "label": "Fat",
                        "quantity": 105.6027277777778,
                        "unit": "g"
                    },
                    "FASAT": {
                        "label": "Saturated",
                        "quantity": 38.959141111111116,
                        "unit": "g"
                    },
                    "FATRN": {
                        "label": "Trans",
                        "quantity": 0.174752,
                        "unit": "g"
                    },
                    "FAMS": {
                        "label": "Monounsaturated",
                        "quantity": 48.65654944444445,
                        "unit": "g"
                    },
                    "FAPU": {
                        "label": "Polyunsaturated",
                        "quantity": 12.004116111111111,
                        "unit": "g"
                    },
                    "CHOCDF": {
                        "label": "Carbs",
                        "quantity": 98.97620555555557,
                        "unit": "g"
                    },
                    "CHOCDF.net": {
                        "label": "Carbohydrates (net)",
                        "quantity": 77.26085,
                        "unit": "g"
                    },
                    "FIBTG": {
                        "label": "Fiber",
                        "quantity": 21.715355555555558,
                        "unit": "g"
                    },
                    "SUGAR": {
                        "label": "Sugars",
                        "quantity": 14.553410555555557,
                        "unit": "g"
                    },
                    "PROCNT": {
                        "label": "Protein",
                        "quantity": 51.101643333333335,
                        "unit": "g"
                    },
                    "CHOLE": {
                        "label": "Cholesterol",
                        "quantity": 117.48,
                        "unit": "mg"
                    },
                    "NA": {
                        "label": "Sodium",
                        "quantity": 2077.415880666667,
                        "unit": "mg"
                    },
                    "CA": {
                        "label": "Calcium",
                        "quantity": 1249.5000844393585,
                        "unit": "mg"
                    },
                    "MG": {
                        "label": "Magnesium",
                        "quantity": 219.76845722201028,
                        "unit": "mg"
                    },
                    "K": {
                        "label": "Potassium",
                        "quantity": 2235.8778799983047,
                        "unit": "mg"
                    },
                    "FE": {
                        "label": "Iron",
                        "quantity": 7.036542549930069,
                        "unit": "mg"
                    },
                    "ZN": {
                        "label": "Zinc",
                        "quantity": 7.5634390555343645,
                        "unit": "mg"
                    },
                    "P": {
                        "label": "Phosphorus",
                        "quantity": 1102.1802222222223,
                        "unit": "mg"
                    },
                    "VITA_RAE": {
                        "label": "Vitamin A",
                        "quantity": 420.236,
                        "unit": "µg"
                    },
                    "VITC": {
                        "label": "Vitamin C",
                        "quantity": 261.2910388888889,
                        "unit": "mg"
                    },
                    "THIA": {
                        "label": "Thiamin (B1)",
                        "quantity": 0.561289888888889,
                        "unit": "mg"
                    },
                    "RIBF": {
                        "label": "Riboflavin (B2)",
                        "quantity": 1.0255766666666668,
                        "unit": "mg"
                    },
                    "NIA": {
                        "label": "Niacin (B3)",
                        "quantity": 5.933973333333334,
                        "unit": "mg"
                    },
                    "VITB6A": {
                        "label": "Vitamin B6",
                        "quantity": 1.527784111111111,
                        "unit": "mg"
                    },
                    "FOLDFE": {
                        "label": "Folate equivalent (total)",
                        "quantity": 440.1793333333333,
                        "unit": "µg"
                    },
                    "FOLFD": {
                        "label": "Folate (food)",
                        "quantity": 400.5553333333333,
                        "unit": "µg"
                    },
                    "FOLAC": {
                        "label": "Folic acid",
                        "quantity": 24.384,
                        "unit": "µg"
                    },
                    "VITB12": {
                        "label": "Vitamin B12",
                        "quantity": 1.0956,
                        "unit": "µg"
                    },
                    "VITD": {
                        "label": "Vitamin D",
                        "quantity": 0.792,
                        "unit": "µg"
                    },
                    "TOCPHA": {
                        "label": "Vitamin E",
                        "quantity": 11.036512222222225,
                        "unit": "mg"
                    },
                    "VITK1": {
                        "label": "Vitamin K",
                        "quantity": 147.14315555555555,
                        "unit": "µg"
                    },
                    "WATER": {
                        "label": "Water",
                        "quantity": 625.7709914444021,
                        "unit": "g"
                    }
                },
                "totalDaily": {
                    "ENERC_KCAL": {
                        "label": "Energy",
                        "quantity": 75.25847222222222,
                        "unit": "%"
                    },
                    "FAT": {
                        "label": "Fat",
                        "quantity": 162.46573504273508,
                        "unit": "%"
                    },
                    "FASAT": {
                        "label": "Saturated",
                        "quantity": 194.79570555555557,
                        "unit": "%"
                    },
                    "CHOCDF": {
                        "label": "Carbs",
                        "quantity": 32.99206851851852,
                        "unit": "%"
                    },
                    "FIBTG": {
                        "label": "Fiber",
                        "quantity": 86.86142222222223,
                        "unit": "%"
                    },
                    "PROCNT": {
                        "label": "Protein",
                        "quantity": 102.20328666666666,
                        "unit": "%"
                    },
                    "CHOLE": {
                        "label": "Cholesterol",
                        "quantity": 39.16,
                        "unit": "%"
                    },
                    "NA": {
                        "label": "Sodium",
                        "quantity": 86.55899502777778,
                        "unit": "%"
                    },
                    "CA": {
                        "label": "Calcium",
                        "quantity": 124.95000844393584,
                        "unit": "%"
                    },
                    "MG": {
                        "label": "Magnesium",
                        "quantity": 52.32582314809769,
                        "unit": "%"
                    },
                    "K": {
                        "label": "Potassium",
                        "quantity": 47.571869787197976,
                        "unit": "%"
                    },
                    "FE": {
                        "label": "Iron",
                        "quantity": 39.09190305516705,
                        "unit": "%"
                    },
                    "ZN": {
                        "label": "Zinc",
                        "quantity": 68.75853686849422,
                        "unit": "%"
                    },
                    "P": {
                        "label": "Phosphorus",
                        "quantity": 157.45431746031747,
                        "unit": "%"
                    },
                    "VITA_RAE": {
                        "label": "Vitamin A",
                        "quantity": 46.69288888888889,
                        "unit": "%"
                    },
                    "VITC": {
                        "label": "Vitamin C",
                        "quantity": 290.3233765432099,
                        "unit": "%"
                    },
                    "THIA": {
                        "label": "Thiamin (B1)",
                        "quantity": 46.774157407407415,
                        "unit": "%"
                    },
                    "RIBF": {
                        "label": "Riboflavin (B2)",
                        "quantity": 78.89051282051282,
                        "unit": "%"
                    },
                    "NIA": {
                        "label": "Niacin (B3)",
                        "quantity": 37.08733333333334,
                        "unit": "%"
                    },
                    "VITB6A": {
                        "label": "Vitamin B6",
                        "quantity": 117.52185470085469,
                        "unit": "%"
                    },
                    "FOLDFE": {
                        "label": "Folate equivalent (total)",
                        "quantity": 110.04483333333333,
                        "unit": "%"
                    },
                    "VITB12": {
                        "label": "Vitamin B12",
                        "quantity": 45.65,
                        "unit": "%"
                    },
                    "VITD": {
                        "label": "Vitamin D",
                        "quantity": 5.28,
                        "unit": "%"
                    },
                    "TOCPHA": {
                        "label": "Vitamin E",
                        "quantity": 73.57674814814817,
                        "unit": "%"
                    },
                    "VITK1": {
                        "label": "Vitamin K",
                        "quantity": 122.6192962962963,
                        "unit": "%"
                    }
                },
                "digest": [
                    {
                        "label": "Fat",
                        "tag": "FAT",
                        "schemaOrgTag": "fatContent",
                        "total": 105.6027277777778,
                        "hasRDI": True,
                        "daily": 162.46573504273508,
                        "unit": "g",
                        "sub": [
                            {
                                "label": "Saturated",
                                "tag": "FASAT",
                                "schemaOrgTag": "saturatedFatContent",
                                "total": 38.959141111111116,
                                "hasRDI": True,
                                "daily": 194.79570555555557,
                                "unit": "g"
                            },
                            {
                                "label": "Trans",
                                "tag": "FATRN",
                                "schemaOrgTag": "transFatContent",
                                "total": 0.174752,
                                "hasRDI": False,
                                "daily": 0.0,
                                "unit": "g"
                            },
                            {
                                "label": "Monounsaturated",
                                "tag": "FAMS",
                                "schemaOrgTag": '',
                                "total": 48.65654944444445,
                                "hasRDI": False,
                                "daily": 0.0,
                                "unit": "g"
                            },
                            {
                                "label": "Polyunsaturated",
                                "tag": "FAPU",
                                "schemaOrgTag": '',
                                "total": 12.004116111111111,
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
                        "total": 98.97620555555557,
                        "hasRDI": True,
                        "daily": 32.99206851851852,
                        "unit": "g",
                        "sub": [
                            {
                                "label": "Carbs (net)",
                                "tag": "CHOCDF.net",
                                "schemaOrgTag": '',
                                "total": 77.26085,
                                "hasRDI": False,
                                "daily": 0.0,
                                "unit": "g"
                            },
                            {
                                "label": "Fiber",
                                "tag": "FIBTG",
                                "schemaOrgTag": "fiberContent",
                                "total": 21.715355555555558,
                                "hasRDI": True,
                                "daily": 86.86142222222223,
                                "unit": "g"
                            },
                            {
                                "label": "Sugars",
                                "tag": "SUGAR",
                                "schemaOrgTag": "sugarContent",
                                "total": 14.553410555555557,
                                "hasRDI": False,
                                "daily": 0.0,
                                "unit": "g"
                            },
                            {
                                "label": "Sugars, added",
                                "tag": "SUGAR.added",
                                "schemaOrgTag": '',
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
                        "total": 51.101643333333335,
                        "hasRDI": True,
                        "daily": 102.20328666666666,
                        "unit": "g"
                    },
                    {
                        "label": "Cholesterol",
                        "tag": "CHOLE",
                        "schemaOrgTag": "cholesterolContent",
                        "total": 117.48,
                        "hasRDI": True,
                        "daily": 39.16,
                        "unit": "mg"
                    },
                    {
                        "label": "Sodium",
                        "tag": "NA",
                        "schemaOrgTag": "sodiumContent",
                        "total": 2077.415880666667,
                        "hasRDI": True,
                        "daily": 86.55899502777778,
                        "unit": "mg"
                    },
                    {
                        "label": "Calcium",
                        "tag": "CA",
                        "schemaOrgTag": '',
                        "total": 1249.5000844393585,
                        "hasRDI": True,
                        "daily": 124.95000844393584,
                        "unit": "mg"
                    },
                    {
                        "label": "Magnesium",
                        "tag": "MG",
                        "schemaOrgTag": '',
                        "total": 219.76845722201028,
                        "hasRDI": True,
                        "daily": 52.32582314809769,
                        "unit": "mg"
                    },
                    {
                        "label": "Potassium",
                        "tag": "K",
                        "schemaOrgTag": '',
                        "total": 2235.8778799983047,
                        "hasRDI": True,
                        "daily": 47.571869787197976,
                        "unit": "mg"
                    },
                    {
                        "label": "Iron",
                        "tag": "FE",
                        "schemaOrgTag": '',
                        "total": 7.036542549930069,
                        "hasRDI": True,
                        "daily": 39.09190305516705,
                        "unit": "mg"
                    },
                    {
                        "label": "Zinc",
                        "tag": "ZN",
                        "schemaOrgTag": '',
                        "total": 7.5634390555343645,
                        "hasRDI": True,
                        "daily": 68.75853686849422,
                        "unit": "mg"
                    },
                    {
                        "label": "Phosphorus",
                        "tag": "P",
                        "schemaOrgTag": '',
                        "total": 1102.1802222222223,
                        "hasRDI": True,
                        "daily": 157.45431746031747,
                        "unit": "mg"
                    },
                    {
                        "label": "Vitamin A",
                        "tag": "VITA_RAE",
                        "schemaOrgTag": '',
                        "total": 420.236,
                        "hasRDI": True,
                        "daily": 46.69288888888889,
                        "unit": "µg"
                    },
                    {
                        "label": "Vitamin C",
                        "tag": "VITC",
                        "schemaOrgTag": '',
                        "total": 261.2910388888889,
                        "hasRDI": True,
                        "daily": 290.3233765432099,
                        "unit": "mg"
                    },
                    {
                        "label": "Thiamin (B1)",
                        "tag": "THIA",
                        "schemaOrgTag": '',
                        "total": 0.561289888888889,
                        "hasRDI": True,
                        "daily": 46.774157407407415,
                        "unit": "mg"
                    },
                    {
                        "label": "Riboflavin (B2)",
                        "tag": "RIBF",
                        "schemaOrgTag": '',
                        "total": 1.0255766666666668,
                        "hasRDI": True,
                        "daily": 78.89051282051282,
                        "unit": "mg"
                    },
                    {
                        "label": "Niacin (B3)",
                        "tag": "NIA",
                        "schemaOrgTag": '',
                        "total": 5.933973333333334,
                        "hasRDI": True,
                        "daily": 37.08733333333334,
                        "unit": "mg"
                    },
                    {
                        "label": "Vitamin B6",
                        "tag": "VITB6A",
                        "schemaOrgTag": '',
                        "total": 1.527784111111111,
                        "hasRDI": True,
                        "daily": 117.52185470085469,
                        "unit": "mg"
                    },
                    {
                        "label": "Folate equivalent (total)",
                        "tag": "FOLDFE",
                        "schemaOrgTag": '',
                        "total": 440.1793333333333,
                        "hasRDI": True,
                        "daily": 110.04483333333333,
                        "unit": "µg"
                    },
                    {
                        "label": "Folate (food)",
                        "tag": "FOLFD",
                        "schemaOrgTag": '',
                        "total": 400.5553333333333,
                        "hasRDI": False,
                        "daily": 0.0,
                        "unit": "µg"
                    },
                    {
                        "label": "Folic acid",
                        "tag": "FOLAC",
                        "schemaOrgTag": '',
                        "total": 24.384,
                        "hasRDI": False,
                        "daily": 0.0,
                        "unit": "µg"
                    },
                    {
                        "label": "Vitamin B12",
                        "tag": "VITB12",
                        "schemaOrgTag": '',
                        "total": 1.0956,
                        "hasRDI": True,
                        "daily": 45.65,
                        "unit": "µg"
                    },
                    {
                        "label": "Vitamin D",
                        "tag": "VITD",
                        "schemaOrgTag": '',
                        "total": 0.792,
                        "hasRDI": True,
                        "daily": 5.28,
                        "unit": "µg"
                    },
                    {
                        "label": "Vitamin E",
                        "tag": "TOCPHA",
                        "schemaOrgTag": '',
                        "total": 11.036512222222225,
                        "hasRDI": True,
                        "daily": 73.57674814814817,
                        "unit": "mg"
                    },
                    {
                        "label": "Vitamin K",
                        "tag": "VITK1",
                        "schemaOrgTag": '',
                        "total": 147.14315555555555,
                        "hasRDI": True,
                        "daily": 122.6192962962963,
                        "unit": "µg"
                    },
                    {
                        "label": "Sugar alcohols",
                        "tag": "Sugar.alcohol",
                        "schemaOrgTag": '',
                        "total": 0.0,
                        "hasRDI": False,
                        "daily": 0.0,
                        "unit": "g"
                    },
                    {
                        "label": "Water",
                        "tag": "WATER",
                        "schemaOrgTag": '',
                        "total": 625.7709914444021,
                        "hasRDI": False,
                        "daily": 0.0,
                        "unit": "g"
                    }
                ]
            },
            "_links": {
                "self": {
                    "title": "Self",
                    "href": "https://api.edamam.com/api/recipes/v2/cf02d702a2e9d992468b83c9e2088305?type=public&app_id=e909afd5&app_key=34e59dda7e1bffb92e49c416e9449e1d"
                }
            }
        },
        {
            "recipe": {
                "uri": "http://www.edamam.com/ontologies/edamam.owl#recipe_ce0bc81e09d1b295975106fb64519e68",
                "label": "Salmon tacos with lime dressing",
                "image": "https://edamam-product-images.s3.amazonaws.com/web-img/e3e/e3ed7834d5b7db9538ec9f586722e6fb.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLWVhc3QtMSJIMEYCIQCP2Gbt%2ByPQIVKV%2FafgML7WXbkOusL9fCs6d1le6dFKYAIhAJcnuEh%2B1NzOso38QgGaVBwaVQAMxyMJATg%2FR%2Fl0jl96KsEFCJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMMTg3MDE3MTUwOTg2IgydADkJdybnmhdEGwQqlQUNCCJJEzulouVCRRPPDPN9Ik9nmgPZk%2Fam6u04CTug5FWfzto4W1y6mlAuXr3EHPB%2FvTcZ%2BmAkgcS5%2FRfKsviGgYg1PBDbKvJFWJigqXNb6jHaHO3eyZnXpof0Qk2PachTFyGGF7upzvEiKr6BGB6DtCoEGe3wCd0iFSMS%2Ft8LIlICGGYaaCvWq9TXeaXkel5jju8XxawzfW0OY8ad1NODjiJJ%2FJ02goRzRa3HwZdXj0P4%2FwwiBHg8BMnsBu5XvhNCt9Gz%2Bxp9cZIC8TMv%2FY8rOvepaH28zVl5BjLGle3tn5syTeLiH6OS68I4OndB2qqeqZqdi9cu6zb1H0y8aKh8r8IIaHqXhP6jBXwOxUN8uimNrMJnaDPxNdvFPuR5yx8UApiuserTd1b1ZIBFiBJ6lavYUBrkLW%2B7bZIJltsNTSxF2GTKFWoXHKGf3%2FXYj%2FniRUh%2BB3xUXrXh8PzVKChkdfuCxirnj5UG2XCrj22%2BBJG8S8UHiExHaIwt01Nel6V7Y0IlXWvwqK8YEx%2FHOI%2FewXERfrnIQDCsrQyC7qTLL3HndUW2Ke8ib2iC%2BPgaP6xDqkqdlhOSojQHG4rfwcyVOFOzeauzAO7Rc77mb0rCUJdMckP6nKiD7nrtjlZXznFmYhCvjmWQF2l06Jl7xQsr%2BjkGAeoXo9X%2FiC11ZTNfxOVIe3LWWkRvMwGWvgvtgF4ZEDGaLXgsbO4I8%2FpSmGD4ox9ZWDfX%2BtTURCyBYVXqYpQ4TpgMhHqAtTUr4TNc7GRLVbfi1xqZNQDt1Sfdzh3Xq88dOJyKsyUs7rcFuuxoNyxvqstWVaAyRglOH1n%2BpV0xA7%2FKEHa%2F8%2FzH6uaXeIp3eLJN1%2BGlAQc1sP2jehPHqGi5Lc7YMOKk8akGOrABqEMeyIMA72vRUvaZqcs7N77uX3kDw2%2BTfyF8pS8HYdR1%2BEU1ekEPGlPPLyTo0NFmbmMa4urw%2B19eIvlGSnFjiSeee%2F%2BeotdKLVnDgZ5aNxOYivkgUqjazWNTWX1qdv7Jq7GWrNDLwjZiU5zLvpcjSyzLyGAVIo8pW14m4aC3jppuzjKpasygGK2%2Bf%2BmxisMAkIdRRS5aXW9PY%2FuwiBnL3qiZT5RtAdamISZZM9jUAWY%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231028T003610Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFPXEGMX3T%2F20231028%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=5d228027d7e4779271668a0eb9592763a65773a43af43bf0c0f639a4b0ac44e3",
                "images": {
                    "THUMBNAIL": {
                        "url": "https://edamam-product-images.s3.amazonaws.com/web-img/e3e/e3ed7834d5b7db9538ec9f586722e6fb-s.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLWVhc3QtMSJIMEYCIQCP2Gbt%2ByPQIVKV%2FafgML7WXbkOusL9fCs6d1le6dFKYAIhAJcnuEh%2B1NzOso38QgGaVBwaVQAMxyMJATg%2FR%2Fl0jl96KsEFCJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMMTg3MDE3MTUwOTg2IgydADkJdybnmhdEGwQqlQUNCCJJEzulouVCRRPPDPN9Ik9nmgPZk%2Fam6u04CTug5FWfzto4W1y6mlAuXr3EHPB%2FvTcZ%2BmAkgcS5%2FRfKsviGgYg1PBDbKvJFWJigqXNb6jHaHO3eyZnXpof0Qk2PachTFyGGF7upzvEiKr6BGB6DtCoEGe3wCd0iFSMS%2Ft8LIlICGGYaaCvWq9TXeaXkel5jju8XxawzfW0OY8ad1NODjiJJ%2FJ02goRzRa3HwZdXj0P4%2FwwiBHg8BMnsBu5XvhNCt9Gz%2Bxp9cZIC8TMv%2FY8rOvepaH28zVl5BjLGle3tn5syTeLiH6OS68I4OndB2qqeqZqdi9cu6zb1H0y8aKh8r8IIaHqXhP6jBXwOxUN8uimNrMJnaDPxNdvFPuR5yx8UApiuserTd1b1ZIBFiBJ6lavYUBrkLW%2B7bZIJltsNTSxF2GTKFWoXHKGf3%2FXYj%2FniRUh%2BB3xUXrXh8PzVKChkdfuCxirnj5UG2XCrj22%2BBJG8S8UHiExHaIwt01Nel6V7Y0IlXWvwqK8YEx%2FHOI%2FewXERfrnIQDCsrQyC7qTLL3HndUW2Ke8ib2iC%2BPgaP6xDqkqdlhOSojQHG4rfwcyVOFOzeauzAO7Rc77mb0rCUJdMckP6nKiD7nrtjlZXznFmYhCvjmWQF2l06Jl7xQsr%2BjkGAeoXo9X%2FiC11ZTNfxOVIe3LWWkRvMwGWvgvtgF4ZEDGaLXgsbO4I8%2FpSmGD4ox9ZWDfX%2BtTURCyBYVXqYpQ4TpgMhHqAtTUr4TNc7GRLVbfi1xqZNQDt1Sfdzh3Xq88dOJyKsyUs7rcFuuxoNyxvqstWVaAyRglOH1n%2BpV0xA7%2FKEHa%2F8%2FzH6uaXeIp3eLJN1%2BGlAQc1sP2jehPHqGi5Lc7YMOKk8akGOrABqEMeyIMA72vRUvaZqcs7N77uX3kDw2%2BTfyF8pS8HYdR1%2BEU1ekEPGlPPLyTo0NFmbmMa4urw%2B19eIvlGSnFjiSeee%2F%2BeotdKLVnDgZ5aNxOYivkgUqjazWNTWX1qdv7Jq7GWrNDLwjZiU5zLvpcjSyzLyGAVIo8pW14m4aC3jppuzjKpasygGK2%2Bf%2BmxisMAkIdRRS5aXW9PY%2FuwiBnL3qiZT5RtAdamISZZM9jUAWY%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231028T003610Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFPXEGMX3T%2F20231028%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=26240e878e8cb99f39e1928f17911b8c746122ad38792c75d2a16017ff7e1109",
                        "width": 100,
                        "height": 100
                    },
                    "SMALL": {
                        "url": "https://edamam-product-images.s3.amazonaws.com/web-img/e3e/e3ed7834d5b7db9538ec9f586722e6fb-m.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLWVhc3QtMSJIMEYCIQCP2Gbt%2ByPQIVKV%2FafgML7WXbkOusL9fCs6d1le6dFKYAIhAJcnuEh%2B1NzOso38QgGaVBwaVQAMxyMJATg%2FR%2Fl0jl96KsEFCJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMMTg3MDE3MTUwOTg2IgydADkJdybnmhdEGwQqlQUNCCJJEzulouVCRRPPDPN9Ik9nmgPZk%2Fam6u04CTug5FWfzto4W1y6mlAuXr3EHPB%2FvTcZ%2BmAkgcS5%2FRfKsviGgYg1PBDbKvJFWJigqXNb6jHaHO3eyZnXpof0Qk2PachTFyGGF7upzvEiKr6BGB6DtCoEGe3wCd0iFSMS%2Ft8LIlICGGYaaCvWq9TXeaXkel5jju8XxawzfW0OY8ad1NODjiJJ%2FJ02goRzRa3HwZdXj0P4%2FwwiBHg8BMnsBu5XvhNCt9Gz%2Bxp9cZIC8TMv%2FY8rOvepaH28zVl5BjLGle3tn5syTeLiH6OS68I4OndB2qqeqZqdi9cu6zb1H0y8aKh8r8IIaHqXhP6jBXwOxUN8uimNrMJnaDPxNdvFPuR5yx8UApiuserTd1b1ZIBFiBJ6lavYUBrkLW%2B7bZIJltsNTSxF2GTKFWoXHKGf3%2FXYj%2FniRUh%2BB3xUXrXh8PzVKChkdfuCxirnj5UG2XCrj22%2BBJG8S8UHiExHaIwt01Nel6V7Y0IlXWvwqK8YEx%2FHOI%2FewXERfrnIQDCsrQyC7qTLL3HndUW2Ke8ib2iC%2BPgaP6xDqkqdlhOSojQHG4rfwcyVOFOzeauzAO7Rc77mb0rCUJdMckP6nKiD7nrtjlZXznFmYhCvjmWQF2l06Jl7xQsr%2BjkGAeoXo9X%2FiC11ZTNfxOVIe3LWWkRvMwGWvgvtgF4ZEDGaLXgsbO4I8%2FpSmGD4ox9ZWDfX%2BtTURCyBYVXqYpQ4TpgMhHqAtTUr4TNc7GRLVbfi1xqZNQDt1Sfdzh3Xq88dOJyKsyUs7rcFuuxoNyxvqstWVaAyRglOH1n%2BpV0xA7%2FKEHa%2F8%2FzH6uaXeIp3eLJN1%2BGlAQc1sP2jehPHqGi5Lc7YMOKk8akGOrABqEMeyIMA72vRUvaZqcs7N77uX3kDw2%2BTfyF8pS8HYdR1%2BEU1ekEPGlPPLyTo0NFmbmMa4urw%2B19eIvlGSnFjiSeee%2F%2BeotdKLVnDgZ5aNxOYivkgUqjazWNTWX1qdv7Jq7GWrNDLwjZiU5zLvpcjSyzLyGAVIo8pW14m4aC3jppuzjKpasygGK2%2Bf%2BmxisMAkIdRRS5aXW9PY%2FuwiBnL3qiZT5RtAdamISZZM9jUAWY%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231028T003610Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFPXEGMX3T%2F20231028%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=aa2aabe1207c4bea1bccec71d85219b6f5b0bd819b474c1751dcdeb1c5ef2524",
                        "width": 200,
                        "height": 200
                    },
                    "REGULAR": {
                        "url": "https://edamam-product-images.s3.amazonaws.com/web-img/e3e/e3ed7834d5b7db9538ec9f586722e6fb.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLWVhc3QtMSJIMEYCIQCP2Gbt%2ByPQIVKV%2FafgML7WXbkOusL9fCs6d1le6dFKYAIhAJcnuEh%2B1NzOso38QgGaVBwaVQAMxyMJATg%2FR%2Fl0jl96KsEFCJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMMTg3MDE3MTUwOTg2IgydADkJdybnmhdEGwQqlQUNCCJJEzulouVCRRPPDPN9Ik9nmgPZk%2Fam6u04CTug5FWfzto4W1y6mlAuXr3EHPB%2FvTcZ%2BmAkgcS5%2FRfKsviGgYg1PBDbKvJFWJigqXNb6jHaHO3eyZnXpof0Qk2PachTFyGGF7upzvEiKr6BGB6DtCoEGe3wCd0iFSMS%2Ft8LIlICGGYaaCvWq9TXeaXkel5jju8XxawzfW0OY8ad1NODjiJJ%2FJ02goRzRa3HwZdXj0P4%2FwwiBHg8BMnsBu5XvhNCt9Gz%2Bxp9cZIC8TMv%2FY8rOvepaH28zVl5BjLGle3tn5syTeLiH6OS68I4OndB2qqeqZqdi9cu6zb1H0y8aKh8r8IIaHqXhP6jBXwOxUN8uimNrMJnaDPxNdvFPuR5yx8UApiuserTd1b1ZIBFiBJ6lavYUBrkLW%2B7bZIJltsNTSxF2GTKFWoXHKGf3%2FXYj%2FniRUh%2BB3xUXrXh8PzVKChkdfuCxirnj5UG2XCrj22%2BBJG8S8UHiExHaIwt01Nel6V7Y0IlXWvwqK8YEx%2FHOI%2FewXERfrnIQDCsrQyC7qTLL3HndUW2Ke8ib2iC%2BPgaP6xDqkqdlhOSojQHG4rfwcyVOFOzeauzAO7Rc77mb0rCUJdMckP6nKiD7nrtjlZXznFmYhCvjmWQF2l06Jl7xQsr%2BjkGAeoXo9X%2FiC11ZTNfxOVIe3LWWkRvMwGWvgvtgF4ZEDGaLXgsbO4I8%2FpSmGD4ox9ZWDfX%2BtTURCyBYVXqYpQ4TpgMhHqAtTUr4TNc7GRLVbfi1xqZNQDt1Sfdzh3Xq88dOJyKsyUs7rcFuuxoNyxvqstWVaAyRglOH1n%2BpV0xA7%2FKEHa%2F8%2FzH6uaXeIp3eLJN1%2BGlAQc1sP2jehPHqGi5Lc7YMOKk8akGOrABqEMeyIMA72vRUvaZqcs7N77uX3kDw2%2BTfyF8pS8HYdR1%2BEU1ekEPGlPPLyTo0NFmbmMa4urw%2B19eIvlGSnFjiSeee%2F%2BeotdKLVnDgZ5aNxOYivkgUqjazWNTWX1qdv7Jq7GWrNDLwjZiU5zLvpcjSyzLyGAVIo8pW14m4aC3jppuzjKpasygGK2%2Bf%2BmxisMAkIdRRS5aXW9PY%2FuwiBnL3qiZT5RtAdamISZZM9jUAWY%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231028T003610Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFPXEGMX3T%2F20231028%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=5d228027d7e4779271668a0eb9592763a65773a43af43bf0c0f639a4b0ac44e3",
                        "width": 300,
                        "height": 300
                    }
                },
                "source": "BBC Good Food",
                "url": "https://www.bbcgoodfood.com/recipes/salmon-tacos-lime-dressing",
                "shareAs": "http://www.edamam.com/recipe/salmon-tacos-with-lime-dressing-ce0bc81e09d1b295975106fb64519e68/tacos",
                "yield": 4.0,
                "dietLabels": [
                    "High-Fiber",
                    "Low-Carb"
                ],
                "healthLabels": [
                    "Pescatarian",
                    "Mediterranean",
                    "Egg-Free",
                    "Peanut-Free",
                    "Tree-Nut-Free",
                    "Soy-Free",
                    "Shellfish-Free",
                    "Pork-Free",
                    "Red-Meat-Free",
                    "Crustacean-Free",
                    "Celery-Free",
                    "Mustard-Free",
                    "Sesame-Free",
                    "Lupine-Free",
                    "Mollusk-Free",
                    "Alcohol-Free",
                    "Sulfite-Free"
                ],
                "cautions": [
                    "Eggs",
                    "Milk",
                    "Sulfites"
                ],
                "ingredientLines": [
                    "olive oil , for the foil",
                    "500g piece salmon fillet",
                    "8 soft corn tacos",
                    "2 limes , zested and juiced",
                    "200g natural yogurt",
                    "2 ripe avocados , peeled and cubed",
                    "10 cherry tomatoes , halved",
                    "1 small red chilli , deseeded and sliced (optional)"
                ],
                "ingredients": [
                    {
                        "text": "olive oil , for the foil",
                        "quantity": 0.0,
                        "measure": '',
                        "food": "olive oil",
                        "weight": 20.69036,
                        "foodCategory": "Oils",
                        "foodId": "food_b1d1icuad3iktrbqby0hiagafaz7",
                        "image": "https://www.edamam.com/food-img/4d6/4d651eaa8a353647746290c7a9b29d84.jpg"
                    },
                    {
                        "text": "500g piece salmon fillet",
                        "quantity": 500.0,
                        "measure": "gram",
                        "food": "salmon",
                        "weight": 500.0,
                        "foodCategory": "seafood",
                        "foodId": "food_bhncugnadgibupafbeeapbislbom",
                        "image": "https://www.edamam.com/food-img/9a0/9a0f38422e9f21dcedbc2dca0d8209ac.jpg"
                    },
                    {
                        "text": "8 soft corn tacos",
                        "quantity": 8.0,
                        "measure": "<unit>",
                        "food": "tacos",
                        "weight": 101.6,
                        "foodCategory": "quick breads and pastries",
                        "foodId": "food_amx6njaaa4q9lsaz4k98faejx12a",
                        "image": "https://www.edamam.com/food-img/def/def506222dc404affdfbf7b7133a34c6.jpg"
                    },
                    {
                        "text": "2 limes , zested and juiced",
                        "quantity": 2.0,
                        "measure": "<unit>",
                        "food": "limes",
                        "weight": 134.0,
                        "foodCategory": "fruit",
                        "foodId": "food_av58muyb8kg92fbk0g8g8aui5knv",
                        "image": "https://www.edamam.com/food-img/48a/48a123c9576647c4ada6a41df5eeb22a.jpg"
                    },
                    {
                        "text": "200g natural yogurt",
                        "quantity": 200.0,
                        "measure": "gram",
                        "food": "yogurt",
                        "weight": 200.0,
                        "foodCategory": "yogurt",
                        "foodId": "food_a79ojfkbgdeekgblqmky9bunr8f6",
                        "image": "https://www.edamam.com/food-img/933/933eb3791b3a2175e007f1607d56b7e2.jpg"
                    },
                    {
                        "text": "2 ripe avocados , peeled and cubed",
                        "quantity": 2.0,
                        "measure": "<unit>",
                        "food": "avocados",
                        "weight": 402.0,
                        "foodCategory": "fruit",
                        "foodId": "food_b0yuze4b1g3afpanijno5abtiu28",
                        "image": "https://www.edamam.com/food-img/984/984a707ea8e9c6bf5f6498970a9e6d9d.jpg"
                    },
                    {
                        "text": "10 cherry tomatoes , halved",
                        "quantity": 10.0,
                        "measure": "<unit>",
                        "food": "cherry tomatoes",
                        "weight": 150.0,
                        "foodCategory": "vegetables",
                        "foodId": "food_a30b0hpbvavginafe0tocbf6ymje",
                        "image": "https://www.edamam.com/food-img/23e/23e727a14f1035bdc2733bb0477efbd2.jpg"
                    },
                    {
                        "text": "1 small red chilli , deseeded and sliced (optional)",
                        "quantity": 1.0,
                        "measure": "<unit>",
                        "food": "red chilli",
                        "weight": 33.75,
                        "foodCategory": "vegetables",
                        "foodId": "food_a6g98mqatzj7vca6ms3bnbzqxf3s",
                        "image": "https://www.edamam.com/food-img/469/469213672957a242638e20c27e3e8acd.jpeg"
                    }
                ],
                "calories": 2552.4187824,
                "totalCO2Emissions": 12732.142193625465,
                "co2EmissionsClass": "G",
                "totalWeight": 1542.04036,
                "totalTime": 25.0,
                "cuisineType": [
                    "nordic"
                ],
                "mealType": [
                    "lunch/dinner"
                ],
                "dishType": [
                    "sandwiches"
                ],
                "totalNutrients": {
                    "ENERC_KCAL": {
                        "label": "Energy",
                        "quantity": 2552.4187824,
                        "unit": "kcal"
                    },
                    "FAT": {
                        "label": "Fat",
                        "quantity": 176.14966,
                        "unit": "g"
                    },
                    "FASAT": {
                        "label": "Saturated",
                        "quantity": 38.16712468,
                        "unit": "g"
                    },
                    "FATRN": {
                        "label": "Trans",
                        "quantity": 0.174752,
                        "unit": "g"
                    },
                    "FAMS": {
                        "label": "Monounsaturated",
                        "quantity": 82.2670628,
                        "unit": "g"
                    },
                    "FAPU": {
                        "label": "Polyunsaturated",
                        "quantity": 34.9897503,
                        "unit": "g"
                    },
                    "CHOCDF": {
                        "label": "Carbs",
                        "quantity": 131.00497500000003,
                        "unit": "g"
                    },
                    "CHOCDF.net": {
                        "label": "Carbohydrates (net)",
                        "quantity": 91.20552500000002,
                        "unit": "g"
                    },
                    "FIBTG": {
                        "label": "Fiber",
                        "quantity": 39.79945,
                        "unit": "g"
                    },
                    "SUGAR": {
                        "label": "Sugars",
                        "quantity": 21.49555,
                        "unit": "g"
                    },
                    "PROCNT": {
                        "label": "Protein",
                        "quantity": 126.381685,
                        "unit": "g"
                    },
                    "CHOLE": {
                        "label": "Cholesterol",
                        "quantity": 301.0,
                        "unit": "mg"
                    },
                    "NA": {
                        "label": "Sodium",
                        "quantity": 757.9553072,
                        "unit": "mg"
                    },
                    "CA": {
                        "label": "Calcium",
                        "quantity": 500.9919036,
                        "unit": "mg"
                    },
                    "MG": {
                        "label": "Magnesium",
                        "quantity": 392.21049999999997,
                        "unit": "mg"
                    },
                    "K": {
                        "label": "Potassium",
                        "quantity": 4910.4579036000005,
                        "unit": "mg"
                    },
                    "FE": {
                        "label": "Iron",
                        "quantity": 7.349731016000001,
                        "unit": "mg"
                    },
                    "ZN": {
                        "label": "Zinc",
                        "quantity": 7.67871,
                        "unit": "mg"
                    },
                    "P": {
                        "label": "Phosphorus",
                        "quantity": 1910.4005,
                        "unit": "mg"
                    },
                    "VITA_RAE": {
                        "label": "Vitamin A",
                        "quantity": 455.036,
                        "unit": "µg"
                    },
                    "VITC": {
                        "label": "Vitamin C",
                        "quantity": 168.84400000000002,
                        "unit": "mg"
                    },
                    "THIA": {
                        "label": "Thiamin (B1)",
                        "quantity": 1.701796,
                        "unit": "mg"
                    },
                    "RIBF": {
                        "label": "Riboflavin (B2)",
                        "quantity": 1.7472050000000001,
                        "unit": "mg"
                    },
                    "NIA": {
                        "label": "Niacin (B3)",
                        "quantity": 53.97222,
                        "unit": "mg"
                    },
                    "VITB6A": {
                        "label": "Vitamin B6",
                        "quantity": 4.831783000000001,
                        "unit": "mg"
                    },
                    "FOLDFE": {
                        "label": "Folate equivalent (total)",
                        "quantity": 596.9625000000001,
                        "unit": "µg"
                    },
                    "FOLFD": {
                        "label": "Folate (food)",
                        "quantity": 557.3385000000001,
                        "unit": "µg"
                    },
                    "FOLAC": {
                        "label": "Folic acid",
                        "quantity": 24.384,
                        "unit": "µg"
                    },
                    "VITB12": {
                        "label": "Vitamin B12",
                        "quantity": 16.889999999999997,
                        "unit": "µg"
                    },
                    "VITD": {
                        "label": "Vitamin D",
                        "quantity": 55.2,
                        "unit": "µg"
                    },
                    "TOCPHA": {
                        "label": "Vitamin E",
                        "quantity": 31.20952684,
                        "unit": "mg"
                    },
                    "VITK1": {
                        "label": "Vitamin K",
                        "quantity": 125.89219672000002,
                        "unit": "µg"
                    },
                    "WATER": {
                        "label": "Water",
                        "quantity": 1090.8384,
                        "unit": "g"
                    }
                },
                "totalDaily": {
                    "ENERC_KCAL": {
                        "label": "Energy",
                        "quantity": 127.62093911999999,
                        "unit": "%"
                    },
                    "FAT": {
                        "label": "Fat",
                        "quantity": 270.99947692307694,
                        "unit": "%"
                    },
                    "FASAT": {
                        "label": "Saturated",
                        "quantity": 190.8356234,
                        "unit": "%"
                    },
                    "CHOCDF": {
                        "label": "Carbs",
                        "quantity": 43.66832500000001,
                        "unit": "%"
                    },
                    "FIBTG": {
                        "label": "Fiber",
                        "quantity": 159.1978,
                        "unit": "%"
                    },
                    "PROCNT": {
                        "label": "Protein",
                        "quantity": 252.76337,
                        "unit": "%"
                    },
                    "CHOLE": {
                        "label": "Cholesterol",
                        "quantity": 100.33333333333333,
                        "unit": "%"
                    },
                    "NA": {
                        "label": "Sodium",
                        "quantity": 31.58147113333333,
                        "unit": "%"
                    },
                    "CA": {
                        "label": "Calcium",
                        "quantity": 50.09919036,
                        "unit": "%"
                    },
                    "MG": {
                        "label": "Magnesium",
                        "quantity": 93.38345238095238,
                        "unit": "%"
                    },
                    "K": {
                        "label": "Potassium",
                        "quantity": 104.47782773617023,
                        "unit": "%"
                    },
                    "FE": {
                        "label": "Iron",
                        "quantity": 40.83183897777778,
                        "unit": "%"
                    },
                    "ZN": {
                        "label": "Zinc",
                        "quantity": 69.80645454545454,
                        "unit": "%"
                    },
                    "P": {
                        "label": "Phosphorus",
                        "quantity": 272.9143571428571,
                        "unit": "%"
                    },
                    "VITA_RAE": {
                        "label": "Vitamin A",
                        "quantity": 50.559555555555555,
                        "unit": "%"
                    },
                    "VITC": {
                        "label": "Vitamin C",
                        "quantity": 187.60444444444445,
                        "unit": "%"
                    },
                    "THIA": {
                        "label": "Thiamin (B1)",
                        "quantity": 141.81633333333335,
                        "unit": "%"
                    },
                    "RIBF": {
                        "label": "Riboflavin (B2)",
                        "quantity": 134.4003846153846,
                        "unit": "%"
                    },
                    "NIA": {
                        "label": "Niacin (B3)",
                        "quantity": 337.326375,
                        "unit": "%"
                    },
                    "VITB6A": {
                        "label": "Vitamin B6",
                        "quantity": 371.6756153846154,
                        "unit": "%"
                    },
                    "FOLDFE": {
                        "label": "Folate equivalent (total)",
                        "quantity": 149.24062500000002,
                        "unit": "%"
                    },
                    "VITB12": {
                        "label": "Vitamin B12",
                        "quantity": 703.7499999999999,
                        "unit": "%"
                    },
                    "VITD": {
                        "label": "Vitamin D",
                        "quantity": 368.0,
                        "unit": "%"
                    },
                    "TOCPHA": {
                        "label": "Vitamin E",
                        "quantity": 208.06351226666666,
                        "unit": "%"
                    },
                    "VITK1": {
                        "label": "Vitamin K",
                        "quantity": 104.91016393333334,
                        "unit": "%"
                    }
                },
                "digest": [
                    {
                        "label": "Fat",
                        "tag": "FAT",
                        "schemaOrgTag": "fatContent",
                        "total": 176.14966,
                        "hasRDI": True,
                        "daily": 270.99947692307694,
                        "unit": "g",
                        "sub": [
                            {
                                "label": "Saturated",
                                "tag": "FASAT",
                                "schemaOrgTag": "saturatedFatContent",
                                "total": 38.16712468,
                                "hasRDI": True,
                                "daily": 190.8356234,
                                "unit": "g"
                            },
                            {
                                "label": "Trans",
                                "tag": "FATRN",
                                "schemaOrgTag": "transFatContent",
                                "total": 0.174752,
                                "hasRDI": False,
                                "daily": 0.0,
                                "unit": "g"
                            },
                            {
                                "label": "Monounsaturated",
                                "tag": "FAMS",
                                "schemaOrgTag": '',
                                "total": 82.2670628,
                                "hasRDI": False,
                                "daily": 0.0,
                                "unit": "g"
                            },
                            {
                                "label": "Polyunsaturated",
                                "tag": "FAPU",
                                "schemaOrgTag": '',
                                "total": 34.9897503,
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
                        "total": 131.00497500000003,
                        "hasRDI": True,
                        "daily": 43.66832500000001,
                        "unit": "g",
                        "sub": [
                            {
                                "label": "Carbs (net)",
                                "tag": "CHOCDF.net",
                                "schemaOrgTag": '',
                                "total": 91.20552500000002,
                                "hasRDI": False,
                                "daily": 0.0,
                                "unit": "g"
                            },
                            {
                                "label": "Fiber",
                                "tag": "FIBTG",
                                "schemaOrgTag": "fiberContent",
                                "total": 39.79945,
                                "hasRDI": True,
                                "daily": 159.1978,
                                "unit": "g"
                            },
                            {
                                "label": "Sugars",
                                "tag": "SUGAR",
                                "schemaOrgTag": "sugarContent",
                                "total": 21.49555,
                                "hasRDI": False,
                                "daily": 0.0,
                                "unit": "g"
                            },
                            {
                                "label": "Sugars, added",
                                "tag": "SUGAR.added",
                                "schemaOrgTag": '',
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
                        "total": 126.381685,
                        "hasRDI": True,
                        "daily": 252.76337,
                        "unit": "g"
                    },
                    {
                        "label": "Cholesterol",
                        "tag": "CHOLE",
                        "schemaOrgTag": "cholesterolContent",
                        "total": 301.0,
                        "hasRDI": True,
                        "daily": 100.33333333333333,
                        "unit": "mg"
                    },
                    {
                        "label": "Sodium",
                        "tag": "NA",
                        "schemaOrgTag": "sodiumContent",
                        "total": 757.9553072,
                        "hasRDI": True,
                        "daily": 31.58147113333333,
                        "unit": "mg"
                    },
                    {
                        "label": "Calcium",
                        "tag": "CA",
                        "schemaOrgTag": '',
                        "total": 500.9919036,
                        "hasRDI": True,
                        "daily": 50.09919036,
                        "unit": "mg"
                    },
                    {
                        "label": "Magnesium",
                        "tag": "MG",
                        "schemaOrgTag": '',
                        "total": 392.21049999999997,
                        "hasRDI": True,
                        "daily": 93.38345238095238,
                        "unit": "mg"
                    },
                    {
                        "label": "Potassium",
                        "tag": "K",
                        "schemaOrgTag": '',
                        "total": 4910.4579036000005,
                        "hasRDI": True,
                        "daily": 104.47782773617023,
                        "unit": "mg"
                    },
                    {
                        "label": "Iron",
                        "tag": "FE",
                        "schemaOrgTag": '',
                        "total": 7.349731016000001,
                        "hasRDI": True,
                        "daily": 40.83183897777778,
                        "unit": "mg"
                    },
                    {
                        "label": "Zinc",
                        "tag": "ZN",
                        "schemaOrgTag": '',
                        "total": 7.67871,
                        "hasRDI": True,
                        "daily": 69.80645454545454,
                        "unit": "mg"
                    },
                    {
                        "label": "Phosphorus",
                        "tag": "P",
                        "schemaOrgTag": '',
                        "total": 1910.4005,
                        "hasRDI": True,
                        "daily": 272.9143571428571,
                        "unit": "mg"
                    },
                    {
                        "label": "Vitamin A",
                        "tag": "VITA_RAE",
                        "schemaOrgTag": '',
                        "total": 455.036,
                        "hasRDI": True,
                        "daily": 50.559555555555555,
                        "unit": "µg"
                    },
                    {
                        "label": "Vitamin C",
                        "tag": "VITC",
                        "schemaOrgTag": '',
                        "total": 168.84400000000002,
                        "hasRDI": True,
                        "daily": 187.60444444444445,
                        "unit": "mg"
                    },
                    {
                        "label": "Thiamin (B1)",
                        "tag": "THIA",
                        "schemaOrgTag": '',
                        "total": 1.701796,
                        "hasRDI": True,
                        "daily": 141.81633333333335,
                        "unit": "mg"
                    },
                    {
                        "label": "Riboflavin (B2)",
                        "tag": "RIBF",
                        "schemaOrgTag": '',
                        "total": 1.7472050000000001,
                        "hasRDI": True,
                        "daily": 134.4003846153846,
                        "unit": "mg"
                    },
                    {
                        "label": "Niacin (B3)",
                        "tag": "NIA",
                        "schemaOrgTag": '',
                        "total": 53.97222,
                        "hasRDI": True,
                        "daily": 337.326375,
                        "unit": "mg"
                    },
                    {
                        "label": "Vitamin B6",
                        "tag": "VITB6A",
                        "schemaOrgTag": '',
                        "total": 4.831783000000001,
                        "hasRDI": True,
                        "daily": 371.6756153846154,
                        "unit": "mg"
                    },
                    {
                        "label": "Folate equivalent (total)",
                        "tag": "FOLDFE",
                        "schemaOrgTag": '',
                        "total": 596.9625000000001,
                        "hasRDI": True,
                        "daily": 149.24062500000002,
                        "unit": "µg"
                    },
                    {
                        "label": "Folate (food)",
                        "tag": "FOLFD",
                        "schemaOrgTag": '',
                        "total": 557.3385000000001,
                        "hasRDI": False,
                        "daily": 0.0,
                        "unit": "µg"
                    },
                    {
                        "label": "Folic acid",
                        "tag": "FOLAC",
                        "schemaOrgTag": '',
                        "total": 24.384,
                        "hasRDI": False,
                        "daily": 0.0,
                        "unit": "µg"
                    },
                    {
                        "label": "Vitamin B12",
                        "tag": "VITB12",
                        "schemaOrgTag": '',
                        "total": 16.889999999999997,
                        "hasRDI": True,
                        "daily": 703.7499999999999,
                        "unit": "µg"
                    },
                    {
                        "label": "Vitamin D",
                        "tag": "VITD",
                        "schemaOrgTag": '',
                        "total": 55.2,
                        "hasRDI": True,
                        "daily": 368.0,
                        "unit": "µg"
                    },
                    {
                        "label": "Vitamin E",
                        "tag": "TOCPHA",
                        "schemaOrgTag": '',
                        "total": 31.20952684,
                        "hasRDI": True,
                        "daily": 208.06351226666666,
                        "unit": "mg"
                    },
                    {
                        "label": "Vitamin K",
                        "tag": "VITK1",
                        "schemaOrgTag": '',
                        "total": 125.89219672000002,
                        "hasRDI": True,
                        "daily": 104.91016393333334,
                        "unit": "µg"
                    },
                    {
                        "label": "Sugar alcohols",
                        "tag": "Sugar.alcohol",
                        "schemaOrgTag": '',
                        "total": 0.0,
                        "hasRDI": False,
                        "daily": 0.0,
                        "unit": "g"
                    },
                    {
                        "label": "Water",
                        "tag": "WATER",
                        "schemaOrgTag": '',
                        "total": 1090.8384,
                        "hasRDI": False,
                        "daily": 0.0,
                        "unit": "g"
                    }
                ]
            },
            "_links": {
                "self": {
                    "title": "Self",
                    "href": "https://api.edamam.com/api/recipes/v2/ce0bc81e09d1b295975106fb64519e68?type=public&app_id=e909afd5&app_key=34e59dda7e1bffb92e49c416e9449e1d"
                }
            }
        },
        {
            "recipe": {
                "uri": "http://www.edamam.com/ontologies/edamam.owl#recipe_85ce76a7da821d73e6b3bd18b041fc46",
                "label": "Crock-Pot Chicken Tacos Recipe",
                "image": "https://edamam-product-images.s3.amazonaws.com/web-img/e67/e670c8de536f4beceedc0f4707efec50.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLWVhc3QtMSJIMEYCIQCP2Gbt%2ByPQIVKV%2FafgML7WXbkOusL9fCs6d1le6dFKYAIhAJcnuEh%2B1NzOso38QgGaVBwaVQAMxyMJATg%2FR%2Fl0jl96KsEFCJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMMTg3MDE3MTUwOTg2IgydADkJdybnmhdEGwQqlQUNCCJJEzulouVCRRPPDPN9Ik9nmgPZk%2Fam6u04CTug5FWfzto4W1y6mlAuXr3EHPB%2FvTcZ%2BmAkgcS5%2FRfKsviGgYg1PBDbKvJFWJigqXNb6jHaHO3eyZnXpof0Qk2PachTFyGGF7upzvEiKr6BGB6DtCoEGe3wCd0iFSMS%2Ft8LIlICGGYaaCvWq9TXeaXkel5jju8XxawzfW0OY8ad1NODjiJJ%2FJ02goRzRa3HwZdXj0P4%2FwwiBHg8BMnsBu5XvhNCt9Gz%2Bxp9cZIC8TMv%2FY8rOvepaH28zVl5BjLGle3tn5syTeLiH6OS68I4OndB2qqeqZqdi9cu6zb1H0y8aKh8r8IIaHqXhP6jBXwOxUN8uimNrMJnaDPxNdvFPuR5yx8UApiuserTd1b1ZIBFiBJ6lavYUBrkLW%2B7bZIJltsNTSxF2GTKFWoXHKGf3%2FXYj%2FniRUh%2BB3xUXrXh8PzVKChkdfuCxirnj5UG2XCrj22%2BBJG8S8UHiExHaIwt01Nel6V7Y0IlXWvwqK8YEx%2FHOI%2FewXERfrnIQDCsrQyC7qTLL3HndUW2Ke8ib2iC%2BPgaP6xDqkqdlhOSojQHG4rfwcyVOFOzeauzAO7Rc77mb0rCUJdMckP6nKiD7nrtjlZXznFmYhCvjmWQF2l06Jl7xQsr%2BjkGAeoXo9X%2FiC11ZTNfxOVIe3LWWkRvMwGWvgvtgF4ZEDGaLXgsbO4I8%2FpSmGD4ox9ZWDfX%2BtTURCyBYVXqYpQ4TpgMhHqAtTUr4TNc7GRLVbfi1xqZNQDt1Sfdzh3Xq88dOJyKsyUs7rcFuuxoNyxvqstWVaAyRglOH1n%2BpV0xA7%2FKEHa%2F8%2FzH6uaXeIp3eLJN1%2BGlAQc1sP2jehPHqGi5Lc7YMOKk8akGOrABqEMeyIMA72vRUvaZqcs7N77uX3kDw2%2BTfyF8pS8HYdR1%2BEU1ekEPGlPPLyTo0NFmbmMa4urw%2B19eIvlGSnFjiSeee%2F%2BeotdKLVnDgZ5aNxOYivkgUqjazWNTWX1qdv7Jq7GWrNDLwjZiU5zLvpcjSyzLyGAVIo8pW14m4aC3jppuzjKpasygGK2%2Bf%2BmxisMAkIdRRS5aXW9PY%2FuwiBnL3qiZT5RtAdamISZZM9jUAWY%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231028T003610Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFPXEGMX3T%2F20231028%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=a95836b0740464aa63c193194c087c966fa1f49420735198ab3f524bb0b9573d",
                "images": {
                    "THUMBNAIL": {
                        "url": "https://edamam-product-images.s3.amazonaws.com/web-img/e67/e670c8de536f4beceedc0f4707efec50-s.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLWVhc3QtMSJIMEYCIQCP2Gbt%2ByPQIVKV%2FafgML7WXbkOusL9fCs6d1le6dFKYAIhAJcnuEh%2B1NzOso38QgGaVBwaVQAMxyMJATg%2FR%2Fl0jl96KsEFCJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMMTg3MDE3MTUwOTg2IgydADkJdybnmhdEGwQqlQUNCCJJEzulouVCRRPPDPN9Ik9nmgPZk%2Fam6u04CTug5FWfzto4W1y6mlAuXr3EHPB%2FvTcZ%2BmAkgcS5%2FRfKsviGgYg1PBDbKvJFWJigqXNb6jHaHO3eyZnXpof0Qk2PachTFyGGF7upzvEiKr6BGB6DtCoEGe3wCd0iFSMS%2Ft8LIlICGGYaaCvWq9TXeaXkel5jju8XxawzfW0OY8ad1NODjiJJ%2FJ02goRzRa3HwZdXj0P4%2FwwiBHg8BMnsBu5XvhNCt9Gz%2Bxp9cZIC8TMv%2FY8rOvepaH28zVl5BjLGle3tn5syTeLiH6OS68I4OndB2qqeqZqdi9cu6zb1H0y8aKh8r8IIaHqXhP6jBXwOxUN8uimNrMJnaDPxNdvFPuR5yx8UApiuserTd1b1ZIBFiBJ6lavYUBrkLW%2B7bZIJltsNTSxF2GTKFWoXHKGf3%2FXYj%2FniRUh%2BB3xUXrXh8PzVKChkdfuCxirnj5UG2XCrj22%2BBJG8S8UHiExHaIwt01Nel6V7Y0IlXWvwqK8YEx%2FHOI%2FewXERfrnIQDCsrQyC7qTLL3HndUW2Ke8ib2iC%2BPgaP6xDqkqdlhOSojQHG4rfwcyVOFOzeauzAO7Rc77mb0rCUJdMckP6nKiD7nrtjlZXznFmYhCvjmWQF2l06Jl7xQsr%2BjkGAeoXo9X%2FiC11ZTNfxOVIe3LWWkRvMwGWvgvtgF4ZEDGaLXgsbO4I8%2FpSmGD4ox9ZWDfX%2BtTURCyBYVXqYpQ4TpgMhHqAtTUr4TNc7GRLVbfi1xqZNQDt1Sfdzh3Xq88dOJyKsyUs7rcFuuxoNyxvqstWVaAyRglOH1n%2BpV0xA7%2FKEHa%2F8%2FzH6uaXeIp3eLJN1%2BGlAQc1sP2jehPHqGi5Lc7YMOKk8akGOrABqEMeyIMA72vRUvaZqcs7N77uX3kDw2%2BTfyF8pS8HYdR1%2BEU1ekEPGlPPLyTo0NFmbmMa4urw%2B19eIvlGSnFjiSeee%2F%2BeotdKLVnDgZ5aNxOYivkgUqjazWNTWX1qdv7Jq7GWrNDLwjZiU5zLvpcjSyzLyGAVIo8pW14m4aC3jppuzjKpasygGK2%2Bf%2BmxisMAkIdRRS5aXW9PY%2FuwiBnL3qiZT5RtAdamISZZM9jUAWY%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231028T003610Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFPXEGMX3T%2F20231028%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=a6c301bc3e576d8f363d42168e5227623b76c6ead5326fea7b83c3571dc85dfa",
                        "width": 100,
                        "height": 100
                    },
                    "SMALL": {
                        "url": "https://edamam-product-images.s3.amazonaws.com/web-img/e67/e670c8de536f4beceedc0f4707efec50-m.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLWVhc3QtMSJIMEYCIQCP2Gbt%2ByPQIVKV%2FafgML7WXbkOusL9fCs6d1le6dFKYAIhAJcnuEh%2B1NzOso38QgGaVBwaVQAMxyMJATg%2FR%2Fl0jl96KsEFCJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMMTg3MDE3MTUwOTg2IgydADkJdybnmhdEGwQqlQUNCCJJEzulouVCRRPPDPN9Ik9nmgPZk%2Fam6u04CTug5FWfzto4W1y6mlAuXr3EHPB%2FvTcZ%2BmAkgcS5%2FRfKsviGgYg1PBDbKvJFWJigqXNb6jHaHO3eyZnXpof0Qk2PachTFyGGF7upzvEiKr6BGB6DtCoEGe3wCd0iFSMS%2Ft8LIlICGGYaaCvWq9TXeaXkel5jju8XxawzfW0OY8ad1NODjiJJ%2FJ02goRzRa3HwZdXj0P4%2FwwiBHg8BMnsBu5XvhNCt9Gz%2Bxp9cZIC8TMv%2FY8rOvepaH28zVl5BjLGle3tn5syTeLiH6OS68I4OndB2qqeqZqdi9cu6zb1H0y8aKh8r8IIaHqXhP6jBXwOxUN8uimNrMJnaDPxNdvFPuR5yx8UApiuserTd1b1ZIBFiBJ6lavYUBrkLW%2B7bZIJltsNTSxF2GTKFWoXHKGf3%2FXYj%2FniRUh%2BB3xUXrXh8PzVKChkdfuCxirnj5UG2XCrj22%2BBJG8S8UHiExHaIwt01Nel6V7Y0IlXWvwqK8YEx%2FHOI%2FewXERfrnIQDCsrQyC7qTLL3HndUW2Ke8ib2iC%2BPgaP6xDqkqdlhOSojQHG4rfwcyVOFOzeauzAO7Rc77mb0rCUJdMckP6nKiD7nrtjlZXznFmYhCvjmWQF2l06Jl7xQsr%2BjkGAeoXo9X%2FiC11ZTNfxOVIe3LWWkRvMwGWvgvtgF4ZEDGaLXgsbO4I8%2FpSmGD4ox9ZWDfX%2BtTURCyBYVXqYpQ4TpgMhHqAtTUr4TNc7GRLVbfi1xqZNQDt1Sfdzh3Xq88dOJyKsyUs7rcFuuxoNyxvqstWVaAyRglOH1n%2BpV0xA7%2FKEHa%2F8%2FzH6uaXeIp3eLJN1%2BGlAQc1sP2jehPHqGi5Lc7YMOKk8akGOrABqEMeyIMA72vRUvaZqcs7N77uX3kDw2%2BTfyF8pS8HYdR1%2BEU1ekEPGlPPLyTo0NFmbmMa4urw%2B19eIvlGSnFjiSeee%2F%2BeotdKLVnDgZ5aNxOYivkgUqjazWNTWX1qdv7Jq7GWrNDLwjZiU5zLvpcjSyzLyGAVIo8pW14m4aC3jppuzjKpasygGK2%2Bf%2BmxisMAkIdRRS5aXW9PY%2FuwiBnL3qiZT5RtAdamISZZM9jUAWY%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231028T003610Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFPXEGMX3T%2F20231028%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=c838073c7e3ca5b1e306506ab8c4fe8d0eb8769bf6225629d624291dbd4c5bcf",
                        "width": 200,
                        "height": 200
                    },
                    "REGULAR": {
                        "url": "https://edamam-product-images.s3.amazonaws.com/web-img/e67/e670c8de536f4beceedc0f4707efec50.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLWVhc3QtMSJIMEYCIQCP2Gbt%2ByPQIVKV%2FafgML7WXbkOusL9fCs6d1le6dFKYAIhAJcnuEh%2B1NzOso38QgGaVBwaVQAMxyMJATg%2FR%2Fl0jl96KsEFCJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMMTg3MDE3MTUwOTg2IgydADkJdybnmhdEGwQqlQUNCCJJEzulouVCRRPPDPN9Ik9nmgPZk%2Fam6u04CTug5FWfzto4W1y6mlAuXr3EHPB%2FvTcZ%2BmAkgcS5%2FRfKsviGgYg1PBDbKvJFWJigqXNb6jHaHO3eyZnXpof0Qk2PachTFyGGF7upzvEiKr6BGB6DtCoEGe3wCd0iFSMS%2Ft8LIlICGGYaaCvWq9TXeaXkel5jju8XxawzfW0OY8ad1NODjiJJ%2FJ02goRzRa3HwZdXj0P4%2FwwiBHg8BMnsBu5XvhNCt9Gz%2Bxp9cZIC8TMv%2FY8rOvepaH28zVl5BjLGle3tn5syTeLiH6OS68I4OndB2qqeqZqdi9cu6zb1H0y8aKh8r8IIaHqXhP6jBXwOxUN8uimNrMJnaDPxNdvFPuR5yx8UApiuserTd1b1ZIBFiBJ6lavYUBrkLW%2B7bZIJltsNTSxF2GTKFWoXHKGf3%2FXYj%2FniRUh%2BB3xUXrXh8PzVKChkdfuCxirnj5UG2XCrj22%2BBJG8S8UHiExHaIwt01Nel6V7Y0IlXWvwqK8YEx%2FHOI%2FewXERfrnIQDCsrQyC7qTLL3HndUW2Ke8ib2iC%2BPgaP6xDqkqdlhOSojQHG4rfwcyVOFOzeauzAO7Rc77mb0rCUJdMckP6nKiD7nrtjlZXznFmYhCvjmWQF2l06Jl7xQsr%2BjkGAeoXo9X%2FiC11ZTNfxOVIe3LWWkRvMwGWvgvtgF4ZEDGaLXgsbO4I8%2FpSmGD4ox9ZWDfX%2BtTURCyBYVXqYpQ4TpgMhHqAtTUr4TNc7GRLVbfi1xqZNQDt1Sfdzh3Xq88dOJyKsyUs7rcFuuxoNyxvqstWVaAyRglOH1n%2BpV0xA7%2FKEHa%2F8%2FzH6uaXeIp3eLJN1%2BGlAQc1sP2jehPHqGi5Lc7YMOKk8akGOrABqEMeyIMA72vRUvaZqcs7N77uX3kDw2%2BTfyF8pS8HYdR1%2BEU1ekEPGlPPLyTo0NFmbmMa4urw%2B19eIvlGSnFjiSeee%2F%2BeotdKLVnDgZ5aNxOYivkgUqjazWNTWX1qdv7Jq7GWrNDLwjZiU5zLvpcjSyzLyGAVIo8pW14m4aC3jppuzjKpasygGK2%2Bf%2BmxisMAkIdRRS5aXW9PY%2FuwiBnL3qiZT5RtAdamISZZM9jUAWY%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231028T003610Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFPXEGMX3T%2F20231028%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=a95836b0740464aa63c193194c087c966fa1f49420735198ab3f524bb0b9573d",
                        "width": 300,
                        "height": 300
                    }
                },
                "source": "The Daily Meal",
                "url": "http://www.thedailymeal.com/crock-pot-chicken-tacos-recipe",
                "shareAs": "http://www.edamam.com/recipe/crock-pot-chicken-tacos-recipe-85ce76a7da821d73e6b3bd18b041fc46/tacos",
                "yield": 6.0,
                "dietLabels": [],
                "healthLabels": [
                    "Sugar-Conscious",
                    "Egg-Free",
                    "Peanut-Free",
                    "Tree-Nut-Free",
                    "Soy-Free",
                    "Fish-Free",
                    "Shellfish-Free",
                    "Pork-Free",
                    "Red-Meat-Free",
                    "Crustacean-Free",
                    "Celery-Free",
                    "Mustard-Free",
                    "Sesame-Free",
                    "Lupine-Free",
                    "Mollusk-Free",
                    "Alcohol-Free",
                    "Sulfite-Free"
                ],
                "cautions": [
                    "Eggs",
                    "Milk",
                    "Sulfites",
                    "FODMAP"
                ],
                "ingredientLines": [
                    "6 frozen chicken breasts",
                    "1 Cup salsa",
                    "1 packet of taco seasoning",
                    "1/4 Cup ranch dressing",
                    "18 hard or soft tacos"
                ],
                "ingredients": [
                    {
                        "text": "6 frozen chicken breasts",
                        "quantity": 6.0,
                        "measure": "<unit>",
                        "food": "chicken breasts",
                        "weight": 1632.0,
                        "foodCategory": "Poultry",
                        "foodId": "food_bdrxu94aj3x2djbpur8dhagfhkcn",
                        "image": "https://www.edamam.com/food-img/da5/da510379d3650787338ca16fb69f4c94.jpg"
                    },
                    {
                        "text": "1 Cup salsa",
                        "quantity": 1.0,
                        "measure": "cup",
                        "food": "salsa",
                        "weight": 259.0,
                        "foodCategory": "canned soup",
                        "foodId": "food_b0t3obfawlm5k2b6erxscacez35u",
                        "image": "https://www.edamam.com/food-img/995/995d0f166754a0475c181b9c156fec43.jpg"
                    },
                    {
                        "text": "1 packet of taco seasoning",
                        "quantity": 1.0,
                        "measure": "packet",
                        "food": "seasoning",
                        "weight": 4.4,
                        "foodCategory": "Condiments and sauces",
                        "foodId": "food_aj7w3xab0epj7cbgkbkpwadysovd",
                        "image": "https://www.edamam.com/food-img/c23/c23e20823b442067307aa436969358f1.jpg"
                    },
                    {
                        "text": "1/4 Cup ranch dressing",
                        "quantity": 0.25,
                        "measure": "cup",
                        "food": "ranch dressing",
                        "weight": 60.00000000101442,
                        "foodCategory": "Condiments and sauces",
                        "foodId": "food_bc9tefubd2gfrja8awxleabejftg",
                        "image": "https://www.edamam.com/food-img/8e3/8e382411445728d5003021e32549f81c.jpg"
                    },
                    {
                        "text": "18 hard or soft tacos",
                        "quantity": 18.0,
                        "measure": "<unit>",
                        "food": "tacos",
                        "weight": 228.6,
                        "foodCategory": "quick breads and pastries",
                        "foodId": "food_amx6njaaa4q9lsaz4k98faejx12a",
                        "image": "https://www.edamam.com/food-img/def/def506222dc404affdfbf7b7133a34c6.jpg"
                    }
                ],
                "calories": 3393.154000004362,
                "totalCO2Emissions": 17256.253565224153,
                "co2EmissionsClass": "G",
                "totalWeight": 2184.0000000010145,
                "totalTime": 0.0,
                "cuisineType": [
                    "mexican"
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
                        "quantity": 3393.1540000043624,
                        "unit": "kcal"
                    },
                    "FAT": {
                        "label": "Fat",
                        "quantity": 120.06482000045142,
                        "unit": "g"
                    },
                    "FASAT": {
                        "label": "Saturated",
                        "quantity": 29.793910000070603,
                        "unit": "g"
                    },
                    "FATRN": {
                        "label": "Trans",
                        "quantity": 0.6166320000018463,
                        "unit": "g"
                    },
                    "FAMS": {
                        "label": "Monounsaturated",
                        "quantity": 32.72918000009333,
                        "unit": "g"
                    },
                    "FAPU": {
                        "label": "Polyunsaturated",
                        "quantity": 35.26006000026172,
                        "unit": "g"
                    },
                    "CHOCDF": {
                        "label": "Carbs",
                        "quantity": 168.78500000005985,
                        "unit": "g"
                    },
                    "CHOCDF.net": {
                        "label": "Carbohydrates (net)",
                        "quantity": 148.05060000005986,
                        "unit": "g"
                    },
                    "FIBTG": {
                        "label": "Fiber",
                        "quantity": 20.7344,
                        "unit": "g"
                    },
                    "SUGAR": {
                        "label": "Sugars",
                        "quantity": 16.708100000047576,
                        "unit": "g"
                    },
                    "PROCNT": {
                        "label": "Protein",
                        "quantity": 387.0040200000134,
                        "unit": "g"
                    },
                    "CHOLE": {
                        "label": "Cholesterol",
                        "quantity": 1206.9600000002638,
                        "unit": "mg"
                    },
                    "NA": {
                        "label": "Sodium",
                        "quantity": 3858.34200000914,
                        "unit": "mg"
                    },
                    "CA": {
                        "label": "Calcium",
                        "quantity": 448.524000000284,
                        "unit": "mg"
                    },
                    "MG": {
                        "label": "Magnesium",
                        "quantity": 698.4040000000507,
                        "unit": "mg"
                    },
                    "K": {
                        "label": "Potassium",
                        "quantity": 6759.69200000065,
                        "unit": "mg"
                    },
                    "FE": {
                        "label": "Iron",
                        "quantity": 12.608440000003043,
                        "unit": "mg"
                    },
                    "ZN": {
                        "label": "Zinc",
                        "quantity": 15.484420000001727,
                        "unit": "mg"
                    },
                    "P": {
                        "label": "Phosphorus",
                        "quantity": 4213.392000001886,
                        "unit": "mg"
                    },
                    "VITA_RAE": {
                        "label": "Vitamin A",
                        "quantity": 223.54400000015215,
                        "unit": "µg"
                    },
                    "VITC": {
                        "label": "Vitamin C",
                        "quantity": 5.449,
                        "unit": "mg"
                    },
                    "THIA": {
                        "label": "Thiamin (B1)",
                        "quantity": 2.133942000000152,
                        "unit": "mg"
                    },
                    "RIBF": {
                        "label": "Riboflavin (B2)",
                        "quantity": 3.2150040000008824,
                        "unit": "mg"
                    },
                    "NIA": {
                        "label": "Niacin (B3)",
                        "quantity": 163.93300000000056,
                        "unit": "mg"
                    },
                    "VITB6A": {
                        "label": "Vitamin B6",
                        "quantity": 14.221138000000305,
                        "unit": "mg"
                    },
                    "FOLDFE": {
                        "label": "Folate equivalent (total)",
                        "quantity": 360.0220000000406,
                        "unit": "µg"
                    },
                    "FOLFD": {
                        "label": "Folate (food)",
                        "quantity": 270.8680000000406,
                        "unit": "µg"
                    },
                    "FOLAC": {
                        "label": "Folic acid",
                        "quantity": 54.864000000000004,
                        "unit": "µg"
                    },
                    "VITB12": {
                        "label": "Vitamin B12",
                        "quantity": 3.529200000001725,
                        "unit": "µg"
                    },
                    "VITD": {
                        "label": "Vitamin D",
                        "quantity": 0.06000000000101442,
                        "unit": "µg"
                    },
                    "TOCPHA": {
                        "label": "Vitamin E",
                        "quantity": 15.421820000022517,
                        "unit": "mg"
                    },
                    "VITK1": {
                        "label": "Vitamin K",
                        "quantity": 146.61660000135933,
                        "unit": "µg"
                    },
                    "WATER": {
                        "label": "Water",
                        "quantity": 1479.7950400004638,
                        "unit": "g"
                    }
                },
                "totalDaily": {
                    "ENERC_KCAL": {
                        "label": "Energy",
                        "quantity": 169.6577000002181,
                        "unit": "%"
                    },
                    "FAT": {
                        "label": "Fat",
                        "quantity": 184.71510769300218,
                        "unit": "%"
                    },
                    "FASAT": {
                        "label": "Saturated",
                        "quantity": 148.96955000035302,
                        "unit": "%"
                    },
                    "CHOCDF": {
                        "label": "Carbs",
                        "quantity": 56.261666666686615,
                        "unit": "%"
                    },
                    "FIBTG": {
                        "label": "Fiber",
                        "quantity": 82.9376,
                        "unit": "%"
                    },
                    "PROCNT": {
                        "label": "Protein",
                        "quantity": 774.0080400000268,
                        "unit": "%"
                    },
                    "CHOLE": {
                        "label": "Cholesterol",
                        "quantity": 402.32000000008793,
                        "unit": "%"
                    },
                    "NA": {
                        "label": "Sodium",
                        "quantity": 160.76425000038083,
                        "unit": "%"
                    },
                    "CA": {
                        "label": "Calcium",
                        "quantity": 44.852400000028396,
                        "unit": "%"
                    },
                    "MG": {
                        "label": "Magnesium",
                        "quantity": 166.28666666667874,
                        "unit": "%"
                    },
                    "K": {
                        "label": "Potassium",
                        "quantity": 143.82323404256704,
                        "unit": "%"
                    },
                    "FE": {
                        "label": "Iron",
                        "quantity": 70.0468888889058,
                        "unit": "%"
                    },
                    "ZN": {
                        "label": "Zinc",
                        "quantity": 140.76745454547023,
                        "unit": "%"
                    },
                    "P": {
                        "label": "Phosphorus",
                        "quantity": 601.9131428574123,
                        "unit": "%"
                    },
                    "VITA_RAE": {
                        "label": "Vitamin A",
                        "quantity": 24.83822222223913,
                        "unit": "%"
                    },
                    "VITC": {
                        "label": "Vitamin C",
                        "quantity": 6.054444444444444,
                        "unit": "%"
                    },
                    "THIA": {
                        "label": "Thiamin (B1)",
                        "quantity": 177.8285000000127,
                        "unit": "%"
                    },
                    "RIBF": {
                        "label": "Riboflavin (B2)",
                        "quantity": 247.30800000006786,
                        "unit": "%"
                    },
                    "NIA": {
                        "label": "Niacin (B3)",
                        "quantity": 1024.5812500000036,
                        "unit": "%"
                    },
                    "VITB6A": {
                        "label": "Vitamin B6",
                        "quantity": 1093.9336923077158,
                        "unit": "%"
                    },
                    "FOLDFE": {
                        "label": "Folate equivalent (total)",
                        "quantity": 90.00550000001014,
                        "unit": "%"
                    },
                    "VITB12": {
                        "label": "Vitamin B12",
                        "quantity": 147.0500000000719,
                        "unit": "%"
                    },
                    "VITD": {
                        "label": "Vitamin D",
                        "quantity": 0.40000000000676283,
                        "unit": "%"
                    },
                    "TOCPHA": {
                        "label": "Vitamin E",
                        "quantity": 102.81213333348344,
                        "unit": "%"
                    },
                    "VITK1": {
                        "label": "Vitamin K",
                        "quantity": 122.18050000113277,
                        "unit": "%"
                    }
                },
                "digest": [
                    {
                        "label": "Fat",
                        "tag": "FAT",
                        "schemaOrgTag": "fatContent",
                        "total": 120.06482000045142,
                        "hasRDI": True,
                        "daily": 184.71510769300218,
                        "unit": "g",
                        "sub": [
                            {
                                "label": "Saturated",
                                "tag": "FASAT",
                                "schemaOrgTag": "saturatedFatContent",
                                "total": 29.793910000070603,
                                "hasRDI": True,
                                "daily": 148.96955000035302,
                                "unit": "g"
                            },
                            {
                                "label": "Trans",
                                "tag": "FATRN",
                                "schemaOrgTag": "transFatContent",
                                "total": 0.6166320000018463,
                                "hasRDI": False,
                                "daily": 0.0,
                                "unit": "g"
                            },
                            {
                                "label": "Monounsaturated",
                                "tag": "FAMS",
                                "schemaOrgTag": '',
                                "total": 32.72918000009333,
                                "hasRDI": False,
                                "daily": 0.0,
                                "unit": "g"
                            },
                            {
                                "label": "Polyunsaturated",
                                "tag": "FAPU",
                                "schemaOrgTag": '',
                                "total": 35.26006000026172,
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
                        "total": 168.78500000005985,
                        "hasRDI": True,
                        "daily": 56.261666666686615,
                        "unit": "g",
                        "sub": [
                            {
                                "label": "Carbs (net)",
                                "tag": "CHOCDF.net",
                                "schemaOrgTag": '',
                                "total": 148.05060000005986,
                                "hasRDI": False,
                                "daily": 0.0,
                                "unit": "g"
                            },
                            {
                                "label": "Fiber",
                                "tag": "FIBTG",
                                "schemaOrgTag": "fiberContent",
                                "total": 20.7344,
                                "hasRDI": True,
                                "daily": 82.9376,
                                "unit": "g"
                            },
                            {
                                "label": "Sugars",
                                "tag": "SUGAR",
                                "schemaOrgTag": "sugarContent",
                                "total": 16.708100000047576,
                                "hasRDI": False,
                                "daily": 0.0,
                                "unit": "g"
                            },
                            {
                                "label": "Sugars, added",
                                "tag": "SUGAR.added",
                                "schemaOrgTag": '',
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
                        "total": 387.0040200000134,
                        "hasRDI": True,
                        "daily": 774.0080400000268,
                        "unit": "g"
                    },
                    {
                        "label": "Cholesterol",
                        "tag": "CHOLE",
                        "schemaOrgTag": "cholesterolContent",
                        "total": 1206.9600000002638,
                        "hasRDI": True,
                        "daily": 402.32000000008793,
                        "unit": "mg"
                    },
                    {
                        "label": "Sodium",
                        "tag": "NA",
                        "schemaOrgTag": "sodiumContent",
                        "total": 3858.34200000914,
                        "hasRDI": True,
                        "daily": 160.76425000038083,
                        "unit": "mg"
                    },
                    {
                        "label": "Calcium",
                        "tag": "CA",
                        "schemaOrgTag": '',
                        "total": 448.524000000284,
                        "hasRDI": True,
                        "daily": 44.852400000028396,
                        "unit": "mg"
                    },
                    {
                        "label": "Magnesium",
                        "tag": "MG",
                        "schemaOrgTag": '',
                        "total": 698.4040000000507,
                        "hasRDI": True,
                        "daily": 166.28666666667874,
                        "unit": "mg"
                    },
                    {
                        "label": "Potassium",
                        "tag": "K",
                        "schemaOrgTag": '',
                        "total": 6759.69200000065,
                        "hasRDI": True,
                        "daily": 143.82323404256704,
                        "unit": "mg"
                    },
                    {
                        "label": "Iron",
                        "tag": "FE",
                        "schemaOrgTag": '',
                        "total": 12.608440000003043,
                        "hasRDI": True,
                        "daily": 70.0468888889058,
                        "unit": "mg"
                    },
                    {
                        "label": "Zinc",
                        "tag": "ZN",
                        "schemaOrgTag": '',
                        "total": 15.484420000001727,
                        "hasRDI": True,
                        "daily": 140.76745454547023,
                        "unit": "mg"
                    },
                    {
                        "label": "Phosphorus",
                        "tag": "P",
                        "schemaOrgTag": '',
                        "total": 4213.392000001886,
                        "hasRDI": True,
                        "daily": 601.9131428574123,
                        "unit": "mg"
                    },
                    {
                        "label": "Vitamin A",
                        "tag": "VITA_RAE",
                        "schemaOrgTag": '',
                        "total": 223.54400000015215,
                        "hasRDI": True,
                        "daily": 24.83822222223913,
                        "unit": "µg"
                    },
                    {
                        "label": "Vitamin C",
                        "tag": "VITC",
                        "schemaOrgTag": '',
                        "total": 5.449,
                        "hasRDI": True,
                        "daily": 6.054444444444444,
                        "unit": "mg"
                    },
                    {
                        "label": "Thiamin (B1)",
                        "tag": "THIA",
                        "schemaOrgTag": '',
                        "total": 2.133942000000152,
                        "hasRDI": True,
                        "daily": 177.8285000000127,
                        "unit": "mg"
                    },
                    {
                        "label": "Riboflavin (B2)",
                        "tag": "RIBF",
                        "schemaOrgTag": '',
                        "total": 3.2150040000008824,
                        "hasRDI": True,
                        "daily": 247.30800000006786,
                        "unit": "mg"
                    },
                    {
                        "label": "Niacin (B3)",
                        "tag": "NIA",
                        "schemaOrgTag": '',
                        "total": 163.93300000000056,
                        "hasRDI": True,
                        "daily": 1024.5812500000036,
                        "unit": "mg"
                    },
                    {
                        "label": "Vitamin B6",
                        "tag": "VITB6A",
                        "schemaOrgTag": '',
                        "total": 14.221138000000305,
                        "hasRDI": True,
                        "daily": 1093.9336923077158,
                        "unit": "mg"
                    },
                    {
                        "label": "Folate equivalent (total)",
                        "tag": "FOLDFE",
                        "schemaOrgTag": '',
                        "total": 360.0220000000406,
                        "hasRDI": True,
                        "daily": 90.00550000001014,
                        "unit": "µg"
                    },
                    {
                        "label": "Folate (food)",
                        "tag": "FOLFD",
                        "schemaOrgTag": '',
                        "total": 270.8680000000406,
                        "hasRDI": False,
                        "daily": 0.0,
                        "unit": "µg"
                    },
                    {
                        "label": "Folic acid",
                        "tag": "FOLAC",
                        "schemaOrgTag": '',
                        "total": 54.864000000000004,
                        "hasRDI": False,
                        "daily": 0.0,
                        "unit": "µg"
                    },
                    {
                        "label": "Vitamin B12",
                        "tag": "VITB12",
                        "schemaOrgTag": '',
                        "total": 3.529200000001725,
                        "hasRDI": True,
                        "daily": 147.0500000000719,
                        "unit": "µg"
                    },
                    {
                        "label": "Vitamin D",
                        "tag": "VITD",
                        "schemaOrgTag": '',
                        "total": 0.06000000000101442,
                        "hasRDI": True,
                        "daily": 0.40000000000676283,
                        "unit": "µg"
                    },
                    {
                        "label": "Vitamin E",
                        "tag": "TOCPHA",
                        "schemaOrgTag": '',
                        "total": 15.421820000022517,
                        "hasRDI": True,
                        "daily": 102.81213333348344,
                        "unit": "mg"
                    },
                    {
                        "label": "Vitamin K",
                        "tag": "VITK1",
                        "schemaOrgTag": '',
                        "total": 146.61660000135933,
                        "hasRDI": True,
                        "daily": 122.18050000113277,
                        "unit": "µg"
                    },
                    {
                        "label": "Sugar alcohols",
                        "tag": "Sugar.alcohol",
                        "schemaOrgTag": '',
                        "total": 0.0,
                        "hasRDI": False,
                        "daily": 0.0,
                        "unit": "g"
                    },
                    {
                        "label": "Water",
                        "tag": "WATER",
                        "schemaOrgTag": '',
                        "total": 1479.7950400004638,
                        "hasRDI": False,
                        "daily": 0.0,
                        "unit": "g"
                    }
                ]
            },
            "_links": {
                "self": {
                    "title": "Self",
                    "href": "https://api.edamam.com/api/recipes/v2/85ce76a7da821d73e6b3bd18b041fc46?type=public&app_id=e909afd5&app_key=34e59dda7e1bffb92e49c416e9449e1d"
                }
            }
        },
        {
            "recipe": {
                "uri": "http://www.edamam.com/ontologies/edamam.owl#recipe_3127a0a089c8aad44645b1a4fe8867a1",
                "label": "Steak Tacos With Roasted Tomato Green Chile Salsa Recipe",
                "image": "https://edamam-product-images.s3.amazonaws.com/web-img/32c/32c34ba27baf89a2788b3cca9a44b5dd.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLWVhc3QtMSJIMEYCIQCP2Gbt%2ByPQIVKV%2FafgML7WXbkOusL9fCs6d1le6dFKYAIhAJcnuEh%2B1NzOso38QgGaVBwaVQAMxyMJATg%2FR%2Fl0jl96KsEFCJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMMTg3MDE3MTUwOTg2IgydADkJdybnmhdEGwQqlQUNCCJJEzulouVCRRPPDPN9Ik9nmgPZk%2Fam6u04CTug5FWfzto4W1y6mlAuXr3EHPB%2FvTcZ%2BmAkgcS5%2FRfKsviGgYg1PBDbKvJFWJigqXNb6jHaHO3eyZnXpof0Qk2PachTFyGGF7upzvEiKr6BGB6DtCoEGe3wCd0iFSMS%2Ft8LIlICGGYaaCvWq9TXeaXkel5jju8XxawzfW0OY8ad1NODjiJJ%2FJ02goRzRa3HwZdXj0P4%2FwwiBHg8BMnsBu5XvhNCt9Gz%2Bxp9cZIC8TMv%2FY8rOvepaH28zVl5BjLGle3tn5syTeLiH6OS68I4OndB2qqeqZqdi9cu6zb1H0y8aKh8r8IIaHqXhP6jBXwOxUN8uimNrMJnaDPxNdvFPuR5yx8UApiuserTd1b1ZIBFiBJ6lavYUBrkLW%2B7bZIJltsNTSxF2GTKFWoXHKGf3%2FXYj%2FniRUh%2BB3xUXrXh8PzVKChkdfuCxirnj5UG2XCrj22%2BBJG8S8UHiExHaIwt01Nel6V7Y0IlXWvwqK8YEx%2FHOI%2FewXERfrnIQDCsrQyC7qTLL3HndUW2Ke8ib2iC%2BPgaP6xDqkqdlhOSojQHG4rfwcyVOFOzeauzAO7Rc77mb0rCUJdMckP6nKiD7nrtjlZXznFmYhCvjmWQF2l06Jl7xQsr%2BjkGAeoXo9X%2FiC11ZTNfxOVIe3LWWkRvMwGWvgvtgF4ZEDGaLXgsbO4I8%2FpSmGD4ox9ZWDfX%2BtTURCyBYVXqYpQ4TpgMhHqAtTUr4TNc7GRLVbfi1xqZNQDt1Sfdzh3Xq88dOJyKsyUs7rcFuuxoNyxvqstWVaAyRglOH1n%2BpV0xA7%2FKEHa%2F8%2FzH6uaXeIp3eLJN1%2BGlAQc1sP2jehPHqGi5Lc7YMOKk8akGOrABqEMeyIMA72vRUvaZqcs7N77uX3kDw2%2BTfyF8pS8HYdR1%2BEU1ekEPGlPPLyTo0NFmbmMa4urw%2B19eIvlGSnFjiSeee%2F%2BeotdKLVnDgZ5aNxOYivkgUqjazWNTWX1qdv7Jq7GWrNDLwjZiU5zLvpcjSyzLyGAVIo8pW14m4aC3jppuzjKpasygGK2%2Bf%2BmxisMAkIdRRS5aXW9PY%2FuwiBnL3qiZT5RtAdamISZZM9jUAWY%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231028T003610Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3599&X-Amz-Credential=ASIASXCYXIIFPXEGMX3T%2F20231028%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=ae494565f50ed1760e8e447fc5fd317565f2db158e20f59a446e438bad69dc30",
                "images": {
                    "THUMBNAIL": {
                        "url": "https://edamam-product-images.s3.amazonaws.com/web-img/32c/32c34ba27baf89a2788b3cca9a44b5dd-s.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLWVhc3QtMSJIMEYCIQCP2Gbt%2ByPQIVKV%2FafgML7WXbkOusL9fCs6d1le6dFKYAIhAJcnuEh%2B1NzOso38QgGaVBwaVQAMxyMJATg%2FR%2Fl0jl96KsEFCJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMMTg3MDE3MTUwOTg2IgydADkJdybnmhdEGwQqlQUNCCJJEzulouVCRRPPDPN9Ik9nmgPZk%2Fam6u04CTug5FWfzto4W1y6mlAuXr3EHPB%2FvTcZ%2BmAkgcS5%2FRfKsviGgYg1PBDbKvJFWJigqXNb6jHaHO3eyZnXpof0Qk2PachTFyGGF7upzvEiKr6BGB6DtCoEGe3wCd0iFSMS%2Ft8LIlICGGYaaCvWq9TXeaXkel5jju8XxawzfW0OY8ad1NODjiJJ%2FJ02goRzRa3HwZdXj0P4%2FwwiBHg8BMnsBu5XvhNCt9Gz%2Bxp9cZIC8TMv%2FY8rOvepaH28zVl5BjLGle3tn5syTeLiH6OS68I4OndB2qqeqZqdi9cu6zb1H0y8aKh8r8IIaHqXhP6jBXwOxUN8uimNrMJnaDPxNdvFPuR5yx8UApiuserTd1b1ZIBFiBJ6lavYUBrkLW%2B7bZIJltsNTSxF2GTKFWoXHKGf3%2FXYj%2FniRUh%2BB3xUXrXh8PzVKChkdfuCxirnj5UG2XCrj22%2BBJG8S8UHiExHaIwt01Nel6V7Y0IlXWvwqK8YEx%2FHOI%2FewXERfrnIQDCsrQyC7qTLL3HndUW2Ke8ib2iC%2BPgaP6xDqkqdlhOSojQHG4rfwcyVOFOzeauzAO7Rc77mb0rCUJdMckP6nKiD7nrtjlZXznFmYhCvjmWQF2l06Jl7xQsr%2BjkGAeoXo9X%2FiC11ZTNfxOVIe3LWWkRvMwGWvgvtgF4ZEDGaLXgsbO4I8%2FpSmGD4ox9ZWDfX%2BtTURCyBYVXqYpQ4TpgMhHqAtTUr4TNc7GRLVbfi1xqZNQDt1Sfdzh3Xq88dOJyKsyUs7rcFuuxoNyxvqstWVaAyRglOH1n%2BpV0xA7%2FKEHa%2F8%2FzH6uaXeIp3eLJN1%2BGlAQc1sP2jehPHqGi5Lc7YMOKk8akGOrABqEMeyIMA72vRUvaZqcs7N77uX3kDw2%2BTfyF8pS8HYdR1%2BEU1ekEPGlPPLyTo0NFmbmMa4urw%2B19eIvlGSnFjiSeee%2F%2BeotdKLVnDgZ5aNxOYivkgUqjazWNTWX1qdv7Jq7GWrNDLwjZiU5zLvpcjSyzLyGAVIo8pW14m4aC3jppuzjKpasygGK2%2Bf%2BmxisMAkIdRRS5aXW9PY%2FuwiBnL3qiZT5RtAdamISZZM9jUAWY%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231028T003610Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFPXEGMX3T%2F20231028%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=bb6620f1cca5a42a29164fd9ad3e960dbfaec105497cf36fd4b4ef47961dc034",
                        "width": 100,
                        "height": 100
                    },
                    "SMALL": {
                        "url": "https://edamam-product-images.s3.amazonaws.com/web-img/32c/32c34ba27baf89a2788b3cca9a44b5dd-m.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLWVhc3QtMSJIMEYCIQCP2Gbt%2ByPQIVKV%2FafgML7WXbkOusL9fCs6d1le6dFKYAIhAJcnuEh%2B1NzOso38QgGaVBwaVQAMxyMJATg%2FR%2Fl0jl96KsEFCJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMMTg3MDE3MTUwOTg2IgydADkJdybnmhdEGwQqlQUNCCJJEzulouVCRRPPDPN9Ik9nmgPZk%2Fam6u04CTug5FWfzto4W1y6mlAuXr3EHPB%2FvTcZ%2BmAkgcS5%2FRfKsviGgYg1PBDbKvJFWJigqXNb6jHaHO3eyZnXpof0Qk2PachTFyGGF7upzvEiKr6BGB6DtCoEGe3wCd0iFSMS%2Ft8LIlICGGYaaCvWq9TXeaXkel5jju8XxawzfW0OY8ad1NODjiJJ%2FJ02goRzRa3HwZdXj0P4%2FwwiBHg8BMnsBu5XvhNCt9Gz%2Bxp9cZIC8TMv%2FY8rOvepaH28zVl5BjLGle3tn5syTeLiH6OS68I4OndB2qqeqZqdi9cu6zb1H0y8aKh8r8IIaHqXhP6jBXwOxUN8uimNrMJnaDPxNdvFPuR5yx8UApiuserTd1b1ZIBFiBJ6lavYUBrkLW%2B7bZIJltsNTSxF2GTKFWoXHKGf3%2FXYj%2FniRUh%2BB3xUXrXh8PzVKChkdfuCxirnj5UG2XCrj22%2BBJG8S8UHiExHaIwt01Nel6V7Y0IlXWvwqK8YEx%2FHOI%2FewXERfrnIQDCsrQyC7qTLL3HndUW2Ke8ib2iC%2BPgaP6xDqkqdlhOSojQHG4rfwcyVOFOzeauzAO7Rc77mb0rCUJdMckP6nKiD7nrtjlZXznFmYhCvjmWQF2l06Jl7xQsr%2BjkGAeoXo9X%2FiC11ZTNfxOVIe3LWWkRvMwGWvgvtgF4ZEDGaLXgsbO4I8%2FpSmGD4ox9ZWDfX%2BtTURCyBYVXqYpQ4TpgMhHqAtTUr4TNc7GRLVbfi1xqZNQDt1Sfdzh3Xq88dOJyKsyUs7rcFuuxoNyxvqstWVaAyRglOH1n%2BpV0xA7%2FKEHa%2F8%2FzH6uaXeIp3eLJN1%2BGlAQc1sP2jehPHqGi5Lc7YMOKk8akGOrABqEMeyIMA72vRUvaZqcs7N77uX3kDw2%2BTfyF8pS8HYdR1%2BEU1ekEPGlPPLyTo0NFmbmMa4urw%2B19eIvlGSnFjiSeee%2F%2BeotdKLVnDgZ5aNxOYivkgUqjazWNTWX1qdv7Jq7GWrNDLwjZiU5zLvpcjSyzLyGAVIo8pW14m4aC3jppuzjKpasygGK2%2Bf%2BmxisMAkIdRRS5aXW9PY%2FuwiBnL3qiZT5RtAdamISZZM9jUAWY%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231028T003610Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFPXEGMX3T%2F20231028%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=706be858377339d144d2365437cb5c5726c48ab746d925321ed33bbd795fe769",
                        "width": 200,
                        "height": 200
                    },
                    "REGULAR": {
                        "url": "https://edamam-product-images.s3.amazonaws.com/web-img/32c/32c34ba27baf89a2788b3cca9a44b5dd.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLWVhc3QtMSJIMEYCIQCP2Gbt%2ByPQIVKV%2FafgML7WXbkOusL9fCs6d1le6dFKYAIhAJcnuEh%2B1NzOso38QgGaVBwaVQAMxyMJATg%2FR%2Fl0jl96KsEFCJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMMTg3MDE3MTUwOTg2IgydADkJdybnmhdEGwQqlQUNCCJJEzulouVCRRPPDPN9Ik9nmgPZk%2Fam6u04CTug5FWfzto4W1y6mlAuXr3EHPB%2FvTcZ%2BmAkgcS5%2FRfKsviGgYg1PBDbKvJFWJigqXNb6jHaHO3eyZnXpof0Qk2PachTFyGGF7upzvEiKr6BGB6DtCoEGe3wCd0iFSMS%2Ft8LIlICGGYaaCvWq9TXeaXkel5jju8XxawzfW0OY8ad1NODjiJJ%2FJ02goRzRa3HwZdXj0P4%2FwwiBHg8BMnsBu5XvhNCt9Gz%2Bxp9cZIC8TMv%2FY8rOvepaH28zVl5BjLGle3tn5syTeLiH6OS68I4OndB2qqeqZqdi9cu6zb1H0y8aKh8r8IIaHqXhP6jBXwOxUN8uimNrMJnaDPxNdvFPuR5yx8UApiuserTd1b1ZIBFiBJ6lavYUBrkLW%2B7bZIJltsNTSxF2GTKFWoXHKGf3%2FXYj%2FniRUh%2BB3xUXrXh8PzVKChkdfuCxirnj5UG2XCrj22%2BBJG8S8UHiExHaIwt01Nel6V7Y0IlXWvwqK8YEx%2FHOI%2FewXERfrnIQDCsrQyC7qTLL3HndUW2Ke8ib2iC%2BPgaP6xDqkqdlhOSojQHG4rfwcyVOFOzeauzAO7Rc77mb0rCUJdMckP6nKiD7nrtjlZXznFmYhCvjmWQF2l06Jl7xQsr%2BjkGAeoXo9X%2FiC11ZTNfxOVIe3LWWkRvMwGWvgvtgF4ZEDGaLXgsbO4I8%2FpSmGD4ox9ZWDfX%2BtTURCyBYVXqYpQ4TpgMhHqAtTUr4TNc7GRLVbfi1xqZNQDt1Sfdzh3Xq88dOJyKsyUs7rcFuuxoNyxvqstWVaAyRglOH1n%2BpV0xA7%2FKEHa%2F8%2FzH6uaXeIp3eLJN1%2BGlAQc1sP2jehPHqGi5Lc7YMOKk8akGOrABqEMeyIMA72vRUvaZqcs7N77uX3kDw2%2BTfyF8pS8HYdR1%2BEU1ekEPGlPPLyTo0NFmbmMa4urw%2B19eIvlGSnFjiSeee%2F%2BeotdKLVnDgZ5aNxOYivkgUqjazWNTWX1qdv7Jq7GWrNDLwjZiU5zLvpcjSyzLyGAVIo8pW14m4aC3jppuzjKpasygGK2%2Bf%2BmxisMAkIdRRS5aXW9PY%2FuwiBnL3qiZT5RtAdamISZZM9jUAWY%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231028T003610Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFPXEGMX3T%2F20231028%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=b3632325752f4e48f00ab1a5c9290f9d3bfda570c3b24a0140fbd1116d4dcadf",
                        "width": 300,
                        "height": 300
                    }
                },
                "source": "Serious Eats",
                "url": "http://www.seriouseats.com/recipes/2011/05/steak-tacos-with-roasted-tomato-green-chile-salsa-recipe.html",
                "shareAs": "http://www.edamam.com/recipe/steak-tacos-with-roasted-tomato-green-chile-salsa-recipe-3127a0a089c8aad44645b1a4fe8867a1/tacos",
                "yield": 6.0,
                "dietLabels": [
                    "High-Fiber"
                ],
                "healthLabels": [
                    "Dairy-Free",
                    "Egg-Free",
                    "Peanut-Free",
                    "Tree-Nut-Free",
                    "Soy-Free",
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
                    "Sulfite-Free",
                    "Kosher"
                ],
                "cautions": [
                    "Eggs",
                    "Milk",
                    "Sulfites"
                ],
                "ingredientLines": [
                    "For Tacos:",
                    "1/4 cup chopped white onion",
                    "3 garlic cloves, minced",
                    "3 tablespoons lime juice",
                    "1/4 teaspoon cumin",
                    "1/2 teaspoon salt",
                    "1 1/2 pounds skirt steak, fat trimmed",
                    "2 poblano peppers",
                    "24 small corn tortillas, warm",
                    "For Salsa:",
                    "3 tomatoes",
                    "4 serrano chilies",
                    "3 cloves garlic",
                    "1/4 cup chopped white onion",
                    "1/3 cup chopped fresh cilantro",
                    "Salt",
                    "1 tablespoon fresh lime juice"
                ],
                "ingredients": [
                    {
                        "text": "1/4 cup chopped white onion",
                        "quantity": 0.25,
                        "measure": "cup",
                        "food": "white onion",
                        "weight": 40.0,
                        "foodCategory": "vegetables",
                        "foodId": "food_bmrvi4ob4binw9a5m7l07amlfcoy",
                        "image": "https://www.edamam.com/food-img/205/205e6bf2399b85d34741892ef91cc603.jpg"
                    },
                    {
                        "text": "3 garlic cloves, minced",
                        "quantity": 3.0,
                        "measure": "clove",
                        "food": "garlic",
                        "weight": 9.0,
                        "foodCategory": "vegetables",
                        "foodId": "food_avtcmx6bgjv1jvay6s6stan8dnyp",
                        "image": "https://www.edamam.com/food-img/6ee/6ee142951f48aaf94f4312409f8d133d.jpg"
                    },
                    {
                        "text": "3 tablespoons lime juice",
                        "quantity": 3.0,
                        "measure": "tablespoon",
                        "food": "lime juice",
                        "weight": 46.199999999218896,
                        "foodCategory": "fruit",
                        "foodId": "food_b0iywbmaujvd4eblrooo9bsvn7e6",
                        "image": "https://www.edamam.com/food-img/8f0/8f0c10eb3dbf476a05e61018e76ea220.jpg"
                    },
                    {
                        "text": "1/4 teaspoon cumin",
                        "quantity": 0.25,
                        "measure": "teaspoon",
                        "food": "cumin",
                        "weight": 0.525,
                        "foodCategory": "Condiments and sauces",
                        "foodId": "food_a8jjbx4biqndasapojdb5by3e92e",
                        "image": "https://www.edamam.com/food-img/07e/07e2a4eb77ce46591033846504817d35.jpg"
                    },
                    {
                        "text": "1/2 teaspoon salt",
                        "quantity": 0.5,
                        "measure": "teaspoon",
                        "food": "salt",
                        "weight": 3.0,
                        "foodCategory": "Condiments and sauces",
                        "foodId": "food_btxz81db72hwbra2pncvebzzzum9",
                        "image": "https://www.edamam.com/food-img/694/6943ea510918c6025795e8dc6e6eaaeb.jpg"
                    },
                    {
                        "text": "1 1/2 pounds skirt steak, fat trimmed",
                        "quantity": 1.5,
                        "measure": "pound",
                        "food": "skirt steak",
                        "weight": 680.388555,
                        "foodCategory": "meats",
                        "foodId": "food_agvdl6pajjrz8sbghz0cdaz6q4yf",
                        "image": "https://www.edamam.com/food-img/e1d/e1dc9aaf420f55f30dd24768e532594a.jpg"
                    },
                    {
                        "text": "2 poblano peppers",
                        "quantity": 2.0,
                        "measure": "<unit>",
                        "food": "poblano peppers",
                        "weight": 90.0,
                        "foodCategory": "vegetables",
                        "foodId": "food_bv2gevdbd1orbiarnp1vfaez1r85",
                        "image": "https://www.edamam.com/food-img/73f/73ff2eeb21372fe15b0ec51f9ecf368d.jpeg"
                    },
                    {
                        "text": "24 small corn tortillas, warm",
                        "quantity": 24.0,
                        "measure": "<unit>",
                        "food": "corn tortillas",
                        "weight": 576.0,
                        "foodCategory": "quick breads and pastries",
                        "foodId": "food_bhw0b95agm97s0abfignnb8fsvb3",
                        "image": "https://www.edamam.com/food-img/b8a/b8ad23dcc06f2324f944e47eb579d644.jpg"
                    },
                    {
                        "text": "3 tomatoes",
                        "quantity": 3.0,
                        "measure": "<unit>",
                        "food": "tomatoes",
                        "weight": 369.0,
                        "foodCategory": "vegetables",
                        "foodId": "food_a6k79rrahp8fe2b26zussa3wtkqh",
                        "image": "https://www.edamam.com/food-img/23e/23e727a14f1035bdc2733bb0477efbd2.jpg"
                    },
                    {
                        "text": "4 serrano chilies",
                        "quantity": 4.0,
                        "measure": "<unit>",
                        "food": "serrano chilies",
                        "weight": 24.4,
                        "foodCategory": "vegetables",
                        "foodId": "food_akybxs9atrgwona5nz3jgbo3vor5",
                        "image": "https://www.edamam.com/food-img/e3d/e3d161d6cfe5ef287053aed5461738ba.jpg"
                    },
                    {
                        "text": "3 cloves garlic",
                        "quantity": 3.0,
                        "measure": "clove",
                        "food": "garlic",
                        "weight": 9.0,
                        "foodCategory": "vegetables",
                        "foodId": "food_avtcmx6bgjv1jvay6s6stan8dnyp",
                        "image": "https://www.edamam.com/food-img/6ee/6ee142951f48aaf94f4312409f8d133d.jpg"
                    },
                    {
                        "text": "1/4 cup chopped white onion",
                        "quantity": 0.25,
                        "measure": "cup",
                        "food": "white onion",
                        "weight": 40.0,
                        "foodCategory": "vegetables",
                        "foodId": "food_bmrvi4ob4binw9a5m7l07amlfcoy",
                        "image": "https://www.edamam.com/food-img/205/205e6bf2399b85d34741892ef91cc603.jpg"
                    },
                    {
                        "text": "1/3 cup chopped fresh cilantro",
                        "quantity": 0.3333333333333333,
                        "measure": "cup",
                        "food": "cilantro",
                        "weight": 5.333333333333333,
                        "foodCategory": "vegetables",
                        "foodId": "food_alhzhuwb4lc7jnb5s6f02by60bzp",
                        "image": "https://www.edamam.com/food-img/d57/d57e375b6ff99a90c7ee2b1990a1af36.jpg"
                    },
                    {
                        "text": "Salt",
                        "quantity": 0.0,
                        "measure": '',
                        "food": "Salt",
                        "weight": 11.44948132999375,
                        "foodCategory": "Condiments and sauces",
                        "foodId": "food_btxz81db72hwbra2pncvebzzzum9",
                        "image": "https://www.edamam.com/food-img/694/6943ea510918c6025795e8dc6e6eaaeb.jpg"
                    },
                    {
                        "text": "1 tablespoon fresh lime juice",
                        "quantity": 1.0,
                        "measure": "tablespoon",
                        "food": "lime juice",
                        "weight": 15.399999999739633,
                        "foodCategory": "fruit",
                        "foodId": "food_b0iywbmaujvd4eblrooo9bsvn7e6",
                        "image": "https://www.edamam.com/food-img/8f0/8f0c10eb3dbf476a05e61018e76ea220.jpg"
                    }
                ],
                "calories": 2770.081098916406,
                "totalCO2Emissions": 69683.3599265045,
                "co2EmissionsClass": "G",
                "totalWeight": 1914.760145135889,
                "totalTime": 0.0,
                "cuisineType": [
                    "mexican"
                ],
                "mealType": [
                    "lunch/dinner"
                ],
                "dishType": [
                    "condiments and sauces"
                ],
                "totalNutrients": {
                    "ENERC_KCAL": {
                        "label": "Energy",
                        "quantity": 2770.081098916406,
                        "unit": "kcal"
                    },
                    "FAT": {
                        "label": "Fat",
                        "quantity": 104.88902337333263,
                        "unit": "g"
                    },
                    "FASAT": {
                        "label": "Saturated",
                        "quantity": 37.03281998316658,
                        "unit": "g"
                    },
                    "FATRN": {
                        "label": "Trans",
                        "quantity": 4.66066160175,
                        "unit": "g"
                    },
                    "FAMS": {
                        "label": "Monounsaturated",
                        "quantity": 45.11264882216659,
                        "unit": "g"
                    },
                    "FAPU": {
                        "label": "Polyunsaturated",
                        "quantity": 12.784795121133097,
                        "unit": "g"
                    },
                    "CHOCDF": {
                        "label": "Carbs",
                        "quantity": 300.44340333324567,
                        "unit": "g"
                    },
                    "CHOCDF.net": {
                        "label": "Carbohydrates (net)",
                        "quantity": 255.28574499991652,
                        "unit": "g"
                    },
                    "FIBTG": {
                        "label": "Fiber",
                        "quantity": 45.15765833332916,
                        "unit": "g"
                    },
                    "SUGAR": {
                        "label": "Sugars",
                        "quantity": 24.9692724999824,
                        "unit": "g"
                    },
                    "PROCNT": {
                        "label": "Protein",
                        "quantity": 177.55242955499563,
                        "unit": "g"
                    },
                    "CHOLE": {
                        "label": "Cholesterol",
                        "quantity": 442.25256075000004,
                        "unit": "mg"
                    },
                    "NA": {
                        "label": "Sodium",
                        "quantity": 4430.613533878978,
                        "unit": "mg"
                    },
                    "CA": {
                        "label": "Calcium",
                        "quantity": 633.5155782660509,
                        "unit": "mg"
                    },
                    "MG": {
                        "label": "Magnesium",
                        "quantity": 640.0870102346194,
                        "unit": "mg"
                    },
                    "K": {
                        "label": "Potassium",
                        "quantity": 4353.4941569097355,
                        "unit": "mg"
                    },
                    "FE": {
                        "label": "Iron",
                        "quantity": 21.941379182450934,
                        "unit": "mg"
                    },
                    "ZN": {
                        "label": "Zinc",
                        "quantity": 49.580996656969425,
                        "unit": "mg"
                    },
                    "P": {
                        "label": "Phosphorus",
                        "quantity": 2992.6632691998543,
                        "unit": "mg"
                    },
                    "VITA_RAE": {
                        "label": "Vitamin A",
                        "quantity": 266.3048755333125,
                        "unit": "µg"
                    },
                    "VITC": {
                        "label": "Vitamin C",
                        "quantity": 310.8050249996876,
                        "unit": "mg"
                    },
                    "THIA": {
                        "label": "Thiamin (B1)",
                        "quantity": 1.2278222674830732,
                        "unit": "mg"
                    },
                    "RIBF": {
                        "label": "Riboflavin (B2)",
                        "quantity": 2.477339276249844,
                        "unit": "mg"
                    },
                    "NIA": {
                        "label": "Niacin (B3)",
                        "quantity": 47.015875593998516,
                        "unit": "mg"
                    },
                    "VITB6A": {
                        "label": "Vitamin B6",
                        "quantity": 5.154138118766271,
                        "unit": "mg"
                    },
                    "FOLDFE": {
                        "label": "Folate equivalent (total)",
                        "quantity": 156.1328233165625,
                        "unit": "µg"
                    },
                    "FOLFD": {
                        "label": "Folate (food)",
                        "quantity": 156.1328233165625,
                        "unit": "µg"
                    },
                    "FOLAC": {
                        "label": "Folic acid",
                        "quantity": 0.0,
                        "unit": "µg"
                    },
                    "VITB12": {
                        "label": "Vitamin B12",
                        "quantity": 16.737558453000002,
                        "unit": "µg"
                    },
                    "VITD": {
                        "label": "Vitamin D",
                        "quantity": 0.6803885550000001,
                        "unit": "µg"
                    },
                    "TOCPHA": {
                        "label": "Vitamin E",
                        "quantity": 5.868156376831043,
                        "unit": "mg"
                    },
                    "VITK1": {
                        "label": "Vitamin K",
                        "quantity": 72.66331165832707,
                        "unit": "µg"
                    },
                    "WATER": {
                        "label": "Water",
                        "quantity": 1309.906052475995,
                        "unit": "g"
                    }
                },
                "totalDaily": {
                    "ENERC_KCAL": {
                        "label": "Energy",
                        "quantity": 138.50405494582031,
                        "unit": "%"
                    },
                    "FAT": {
                        "label": "Fat",
                        "quantity": 161.3677282666656,
                        "unit": "%"
                    },
                    "FASAT": {
                        "label": "Saturated",
                        "quantity": 185.1640999158329,
                        "unit": "%"
                    },
                    "CHOCDF": {
                        "label": "Carbs",
                        "quantity": 100.14780111108189,
                        "unit": "%"
                    },
                    "FIBTG": {
                        "label": "Fiber",
                        "quantity": 180.63063333331667,
                        "unit": "%"
                    },
                    "PROCNT": {
                        "label": "Protein",
                        "quantity": 355.10485910999125,
                        "unit": "%"
                    },
                    "CHOLE": {
                        "label": "Cholesterol",
                        "quantity": 147.41752025000002,
                        "unit": "%"
                    },
                    "NA": {
                        "label": "Sodium",
                        "quantity": 184.60889724495743,
                        "unit": "%"
                    },
                    "CA": {
                        "label": "Calcium",
                        "quantity": 63.35155782660509,
                        "unit": "%"
                    },
                    "MG": {
                        "label": "Magnesium",
                        "quantity": 152.4016691034808,
                        "unit": "%"
                    },
                    "K": {
                        "label": "Potassium",
                        "quantity": 92.62753525339862,
                        "unit": "%"
                    },
                    "FE": {
                        "label": "Iron",
                        "quantity": 121.89655101361629,
                        "unit": "%"
                    },
                    "ZN": {
                        "label": "Zinc",
                        "quantity": 450.73633324517664,
                        "unit": "%"
                    },
                    "P": {
                        "label": "Phosphorus",
                        "quantity": 427.52332417140775,
                        "unit": "%"
                    },
                    "VITA_RAE": {
                        "label": "Vitamin A",
                        "quantity": 29.589430614812503,
                        "unit": "%"
                    },
                    "VITC": {
                        "label": "Vitamin C",
                        "quantity": 345.33891666631956,
                        "unit": "%"
                    },
                    "THIA": {
                        "label": "Thiamin (B1)",
                        "quantity": 102.31852229025611,
                        "unit": "%"
                    },
                    "RIBF": {
                        "label": "Riboflavin (B2)",
                        "quantity": 190.56455971152647,
                        "unit": "%"
                    },
                    "NIA": {
                        "label": "Niacin (B3)",
                        "quantity": 293.84922246249073,
                        "unit": "%"
                    },
                    "VITB6A": {
                        "label": "Vitamin B6",
                        "quantity": 396.4721629820209,
                        "unit": "%"
                    },
                    "FOLDFE": {
                        "label": "Folate equivalent (total)",
                        "quantity": 39.03320582914063,
                        "unit": "%"
                    },
                    "VITB12": {
                        "label": "Vitamin B12",
                        "quantity": 697.3982688750001,
                        "unit": "%"
                    },
                    "VITD": {
                        "label": "Vitamin D",
                        "quantity": 4.535923700000001,
                        "unit": "%"
                    },
                    "TOCPHA": {
                        "label": "Vitamin E",
                        "quantity": 39.12104251220695,
                        "unit": "%"
                    },
                    "VITK1": {
                        "label": "Vitamin K",
                        "quantity": 60.552759715272565,
                        "unit": "%"
                    }
                },
                "digest": [
                    {
                        "label": "Fat",
                        "tag": "FAT",
                        "schemaOrgTag": "fatContent",
                        "total": 104.88902337333263,
                        "hasRDI": True,
                        "daily": 161.3677282666656,
                        "unit": "g",
                        "sub": [
                            {
                                "label": "Saturated",
                                "tag": "FASAT",
                                "schemaOrgTag": "saturatedFatContent",
                                "total": 37.03281998316658,
                                "hasRDI": True,
                                "daily": 185.1640999158329,
                                "unit": "g"
                            },
                            {
                                "label": "Trans",
                                "tag": "FATRN",
                                "schemaOrgTag": "transFatContent",
                                "total": 4.66066160175,
                                "hasRDI": False,
                                "daily": 0.0,
                                "unit": "g"
                            },
                            {
                                "label": "Monounsaturated",
                                "tag": "FAMS",
                                "schemaOrgTag": '',
                                "total": 45.11264882216659,
                                "hasRDI": False,
                                "daily": 0.0,
                                "unit": "g"
                            },
                            {
                                "label": "Polyunsaturated",
                                "tag": "FAPU",
                                "schemaOrgTag": '',
                                "total": 12.784795121133097,
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
                        "total": 300.44340333324567,
                        "hasRDI": True,
                        "daily": 100.14780111108189,
                        "unit": "g",
                        "sub": [
                            {
                                "label": "Carbs (net)",
                                "tag": "CHOCDF.net",
                                "schemaOrgTag": '',
                                "total": 255.28574499991652,
                                "hasRDI": False,
                                "daily": 0.0,
                                "unit": "g"
                            },
                            {
                                "label": "Fiber",
                                "tag": "FIBTG",
                                "schemaOrgTag": "fiberContent",
                                "total": 45.15765833332916,
                                "hasRDI": True,
                                "daily": 180.63063333331667,
                                "unit": "g"
                            },
                            {
                                "label": "Sugars",
                                "tag": "SUGAR",
                                "schemaOrgTag": "sugarContent",
                                "total": 24.9692724999824,
                                "hasRDI": False,
                                "daily": 0.0,
                                "unit": "g"
                            },
                            {
                                "label": "Sugars, added",
                                "tag": "SUGAR.added",
                                "schemaOrgTag": '',
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
                        "total": 177.55242955499563,
                        "hasRDI": True,
                        "daily": 355.10485910999125,
                        "unit": "g"
                    },
                    {
                        "label": "Cholesterol",
                        "tag": "CHOLE",
                        "schemaOrgTag": "cholesterolContent",
                        "total": 442.25256075000004,
                        "hasRDI": True,
                        "daily": 147.41752025000002,
                        "unit": "mg"
                    },
                    {
                        "label": "Sodium",
                        "tag": "NA",
                        "schemaOrgTag": "sodiumContent",
                        "total": 4430.613533878978,
                        "hasRDI": True,
                        "daily": 184.60889724495743,
                        "unit": "mg"
                    },
                    {
                        "label": "Calcium",
                        "tag": "CA",
                        "schemaOrgTag": '',
                        "total": 633.5155782660509,
                        "hasRDI": True,
                        "daily": 63.35155782660509,
                        "unit": "mg"
                    },
                    {
                        "label": "Magnesium",
                        "tag": "MG",
                        "schemaOrgTag": '',
                        "total": 640.0870102346194,
                        "hasRDI": True,
                        "daily": 152.4016691034808,
                        "unit": "mg"
                    },
                    {
                        "label": "Potassium",
                        "tag": "K",
                        "schemaOrgTag": '',
                        "total": 4353.4941569097355,
                        "hasRDI": True,
                        "daily": 92.62753525339862,
                        "unit": "mg"
                    },
                    {
                        "label": "Iron",
                        "tag": "FE",
                        "schemaOrgTag": '',
                        "total": 21.941379182450934,
                        "hasRDI": True,
                        "daily": 121.89655101361629,
                        "unit": "mg"
                    },
                    {
                        "label": "Zinc",
                        "tag": "ZN",
                        "schemaOrgTag": '',
                        "total": 49.580996656969425,
                        "hasRDI": True,
                        "daily": 450.73633324517664,
                        "unit": "mg"
                    },
                    {
                        "label": "Phosphorus",
                        "tag": "P",
                        "schemaOrgTag": '',
                        "total": 2992.6632691998543,
                        "hasRDI": True,
                        "daily": 427.52332417140775,
                        "unit": "mg"
                    },
                    {
                        "label": "Vitamin A",
                        "tag": "VITA_RAE",
                        "schemaOrgTag": '',
                        "total": 266.3048755333125,
                        "hasRDI": True,
                        "daily": 29.589430614812503,
                        "unit": "µg"
                    },
                    {
                        "label": "Vitamin C",
                        "tag": "VITC",
                        "schemaOrgTag": '',
                        "total": 310.8050249996876,
                        "hasRDI": True,
                        "daily": 345.33891666631956,
                        "unit": "mg"
                    },
                    {
                        "label": "Thiamin (B1)",
                        "tag": "THIA",
                        "schemaOrgTag": '',
                        "total": 1.2278222674830732,
                        "hasRDI": True,
                        "daily": 102.31852229025611,
                        "unit": "mg"
                    },
                    {
                        "label": "Riboflavin (B2)",
                        "tag": "RIBF",
                        "schemaOrgTag": '',
                        "total": 2.477339276249844,
                        "hasRDI": True,
                        "daily": 190.56455971152647,
                        "unit": "mg"
                    },
                    {
                        "label": "Niacin (B3)",
                        "tag": "NIA",
                        "schemaOrgTag": '',
                        "total": 47.015875593998516,
                        "hasRDI": True,
                        "daily": 293.84922246249073,
                        "unit": "mg"
                    },
                    {
                        "label": "Vitamin B6",
                        "tag": "VITB6A",
                        "schemaOrgTag": '',
                        "total": 5.154138118766271,
                        "hasRDI": True,
                        "daily": 396.4721629820209,
                        "unit": "mg"
                    },
                    {
                        "label": "Folate equivalent (total)",
                        "tag": "FOLDFE",
                        "schemaOrgTag": '',
                        "total": 156.1328233165625,
                        "hasRDI": True,
                        "daily": 39.03320582914063,
                        "unit": "µg"
                    },
                    {
                        "label": "Folate (food)",
                        "tag": "FOLFD",
                        "schemaOrgTag": '',
                        "total": 156.1328233165625,
                        "hasRDI": False,
                        "daily": 0.0,
                        "unit": "µg"
                    },
                    {
                        "label": "Folic acid",
                        "tag": "FOLAC",
                        "schemaOrgTag": '',
                        "total": 0.0,
                        "hasRDI": False,
                        "daily": 0.0,
                        "unit": "µg"
                    },
                    {
                        "label": "Vitamin B12",
                        "tag": "VITB12",
                        "schemaOrgTag": '',
                        "total": 16.737558453000002,
                        "hasRDI": True,
                        "daily": 697.3982688750001,
                        "unit": "µg"
                    },
                    {
                        "label": "Vitamin D",
                        "tag": "VITD",
                        "schemaOrgTag": '',
                        "total": 0.6803885550000001,
                        "hasRDI": True,
                        "daily": 4.535923700000001,
                        "unit": "µg"
                    },
                    {
                        "label": "Vitamin E",
                        "tag": "TOCPHA",
                        "schemaOrgTag": '',
                        "total": 5.868156376831043,
                        "hasRDI": True,
                        "daily": 39.12104251220695,
                        "unit": "mg"
                    },
                    {
                        "label": "Vitamin K",
                        "tag": "VITK1",
                        "schemaOrgTag": '',
                        "total": 72.66331165832707,
                        "hasRDI": True,
                        "daily": 60.552759715272565,
                        "unit": "µg"
                    },
                    {
                        "label": "Sugar alcohols",
                        "tag": "Sugar.alcohol",
                        "schemaOrgTag": '',
                        "total": 0.0,
                        "hasRDI": False,
                        "daily": 0.0,
                        "unit": "g"
                    },
                    {
                        "label": "Water",
                        "tag": "WATER",
                        "schemaOrgTag": '',
                        "total": 1309.906052475995,
                        "hasRDI": False,
                        "daily": 0.0,
                        "unit": "g"
                    }
                ]
            },
            "_links": {
                "self": {
                    "title": "Self",
                    "href": "https://api.edamam.com/api/recipes/v2/3127a0a089c8aad44645b1a4fe8867a1?type=public&app_id=e909afd5&app_key=34e59dda7e1bffb92e49c416e9449e1d"
                }
            }
        },
        {
            "recipe": {
                "uri": "http://www.edamam.com/ontologies/edamam.owl#recipe_b74d2752729d5889aa6af3396cc91322",
                "label": "Fresh Tuna Tacos",
                "image": "https://edamam-product-images.s3.amazonaws.com/web-img/ab3/ab324ad2c1653b50ce2d8d0781386751.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLWVhc3QtMSJIMEYCIQCP2Gbt%2ByPQIVKV%2FafgML7WXbkOusL9fCs6d1le6dFKYAIhAJcnuEh%2B1NzOso38QgGaVBwaVQAMxyMJATg%2FR%2Fl0jl96KsEFCJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMMTg3MDE3MTUwOTg2IgydADkJdybnmhdEGwQqlQUNCCJJEzulouVCRRPPDPN9Ik9nmgPZk%2Fam6u04CTug5FWfzto4W1y6mlAuXr3EHPB%2FvTcZ%2BmAkgcS5%2FRfKsviGgYg1PBDbKvJFWJigqXNb6jHaHO3eyZnXpof0Qk2PachTFyGGF7upzvEiKr6BGB6DtCoEGe3wCd0iFSMS%2Ft8LIlICGGYaaCvWq9TXeaXkel5jju8XxawzfW0OY8ad1NODjiJJ%2FJ02goRzRa3HwZdXj0P4%2FwwiBHg8BMnsBu5XvhNCt9Gz%2Bxp9cZIC8TMv%2FY8rOvepaH28zVl5BjLGle3tn5syTeLiH6OS68I4OndB2qqeqZqdi9cu6zb1H0y8aKh8r8IIaHqXhP6jBXwOxUN8uimNrMJnaDPxNdvFPuR5yx8UApiuserTd1b1ZIBFiBJ6lavYUBrkLW%2B7bZIJltsNTSxF2GTKFWoXHKGf3%2FXYj%2FniRUh%2BB3xUXrXh8PzVKChkdfuCxirnj5UG2XCrj22%2BBJG8S8UHiExHaIwt01Nel6V7Y0IlXWvwqK8YEx%2FHOI%2FewXERfrnIQDCsrQyC7qTLL3HndUW2Ke8ib2iC%2BPgaP6xDqkqdlhOSojQHG4rfwcyVOFOzeauzAO7Rc77mb0rCUJdMckP6nKiD7nrtjlZXznFmYhCvjmWQF2l06Jl7xQsr%2BjkGAeoXo9X%2FiC11ZTNfxOVIe3LWWkRvMwGWvgvtgF4ZEDGaLXgsbO4I8%2FpSmGD4ox9ZWDfX%2BtTURCyBYVXqYpQ4TpgMhHqAtTUr4TNc7GRLVbfi1xqZNQDt1Sfdzh3Xq88dOJyKsyUs7rcFuuxoNyxvqstWVaAyRglOH1n%2BpV0xA7%2FKEHa%2F8%2FzH6uaXeIp3eLJN1%2BGlAQc1sP2jehPHqGi5Lc7YMOKk8akGOrABqEMeyIMA72vRUvaZqcs7N77uX3kDw2%2BTfyF8pS8HYdR1%2BEU1ekEPGlPPLyTo0NFmbmMa4urw%2B19eIvlGSnFjiSeee%2F%2BeotdKLVnDgZ5aNxOYivkgUqjazWNTWX1qdv7Jq7GWrNDLwjZiU5zLvpcjSyzLyGAVIo8pW14m4aC3jppuzjKpasygGK2%2Bf%2BmxisMAkIdRRS5aXW9PY%2FuwiBnL3qiZT5RtAdamISZZM9jUAWY%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231028T003610Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFPXEGMX3T%2F20231028%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=3b8f1b4b304ba0d4b1abfeb0e8c1828d8103feab6d79614a7401f3665f7f584e",
                "images": {
                    "THUMBNAIL": {
                        "url": "https://edamam-product-images.s3.amazonaws.com/web-img/ab3/ab324ad2c1653b50ce2d8d0781386751-s.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLWVhc3QtMSJIMEYCIQCP2Gbt%2ByPQIVKV%2FafgML7WXbkOusL9fCs6d1le6dFKYAIhAJcnuEh%2B1NzOso38QgGaVBwaVQAMxyMJATg%2FR%2Fl0jl96KsEFCJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMMTg3MDE3MTUwOTg2IgydADkJdybnmhdEGwQqlQUNCCJJEzulouVCRRPPDPN9Ik9nmgPZk%2Fam6u04CTug5FWfzto4W1y6mlAuXr3EHPB%2FvTcZ%2BmAkgcS5%2FRfKsviGgYg1PBDbKvJFWJigqXNb6jHaHO3eyZnXpof0Qk2PachTFyGGF7upzvEiKr6BGB6DtCoEGe3wCd0iFSMS%2Ft8LIlICGGYaaCvWq9TXeaXkel5jju8XxawzfW0OY8ad1NODjiJJ%2FJ02goRzRa3HwZdXj0P4%2FwwiBHg8BMnsBu5XvhNCt9Gz%2Bxp9cZIC8TMv%2FY8rOvepaH28zVl5BjLGle3tn5syTeLiH6OS68I4OndB2qqeqZqdi9cu6zb1H0y8aKh8r8IIaHqXhP6jBXwOxUN8uimNrMJnaDPxNdvFPuR5yx8UApiuserTd1b1ZIBFiBJ6lavYUBrkLW%2B7bZIJltsNTSxF2GTKFWoXHKGf3%2FXYj%2FniRUh%2BB3xUXrXh8PzVKChkdfuCxirnj5UG2XCrj22%2BBJG8S8UHiExHaIwt01Nel6V7Y0IlXWvwqK8YEx%2FHOI%2FewXERfrnIQDCsrQyC7qTLL3HndUW2Ke8ib2iC%2BPgaP6xDqkqdlhOSojQHG4rfwcyVOFOzeauzAO7Rc77mb0rCUJdMckP6nKiD7nrtjlZXznFmYhCvjmWQF2l06Jl7xQsr%2BjkGAeoXo9X%2FiC11ZTNfxOVIe3LWWkRvMwGWvgvtgF4ZEDGaLXgsbO4I8%2FpSmGD4ox9ZWDfX%2BtTURCyBYVXqYpQ4TpgMhHqAtTUr4TNc7GRLVbfi1xqZNQDt1Sfdzh3Xq88dOJyKsyUs7rcFuuxoNyxvqstWVaAyRglOH1n%2BpV0xA7%2FKEHa%2F8%2FzH6uaXeIp3eLJN1%2BGlAQc1sP2jehPHqGi5Lc7YMOKk8akGOrABqEMeyIMA72vRUvaZqcs7N77uX3kDw2%2BTfyF8pS8HYdR1%2BEU1ekEPGlPPLyTo0NFmbmMa4urw%2B19eIvlGSnFjiSeee%2F%2BeotdKLVnDgZ5aNxOYivkgUqjazWNTWX1qdv7Jq7GWrNDLwjZiU5zLvpcjSyzLyGAVIo8pW14m4aC3jppuzjKpasygGK2%2Bf%2BmxisMAkIdRRS5aXW9PY%2FuwiBnL3qiZT5RtAdamISZZM9jUAWY%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231028T003610Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFPXEGMX3T%2F20231028%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=732736fd77f172b0807d9c92a7fa1f5caf2dec4c6fe7072c0418fcfe7c4a2b3b",
                        "width": 100,
                        "height": 100
                    },
                    "SMALL": {
                        "url": "https://edamam-product-images.s3.amazonaws.com/web-img/ab3/ab324ad2c1653b50ce2d8d0781386751-m.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLWVhc3QtMSJIMEYCIQCP2Gbt%2ByPQIVKV%2FafgML7WXbkOusL9fCs6d1le6dFKYAIhAJcnuEh%2B1NzOso38QgGaVBwaVQAMxyMJATg%2FR%2Fl0jl96KsEFCJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMMTg3MDE3MTUwOTg2IgydADkJdybnmhdEGwQqlQUNCCJJEzulouVCRRPPDPN9Ik9nmgPZk%2Fam6u04CTug5FWfzto4W1y6mlAuXr3EHPB%2FvTcZ%2BmAkgcS5%2FRfKsviGgYg1PBDbKvJFWJigqXNb6jHaHO3eyZnXpof0Qk2PachTFyGGF7upzvEiKr6BGB6DtCoEGe3wCd0iFSMS%2Ft8LIlICGGYaaCvWq9TXeaXkel5jju8XxawzfW0OY8ad1NODjiJJ%2FJ02goRzRa3HwZdXj0P4%2FwwiBHg8BMnsBu5XvhNCt9Gz%2Bxp9cZIC8TMv%2FY8rOvepaH28zVl5BjLGle3tn5syTeLiH6OS68I4OndB2qqeqZqdi9cu6zb1H0y8aKh8r8IIaHqXhP6jBXwOxUN8uimNrMJnaDPxNdvFPuR5yx8UApiuserTd1b1ZIBFiBJ6lavYUBrkLW%2B7bZIJltsNTSxF2GTKFWoXHKGf3%2FXYj%2FniRUh%2BB3xUXrXh8PzVKChkdfuCxirnj5UG2XCrj22%2BBJG8S8UHiExHaIwt01Nel6V7Y0IlXWvwqK8YEx%2FHOI%2FewXERfrnIQDCsrQyC7qTLL3HndUW2Ke8ib2iC%2BPgaP6xDqkqdlhOSojQHG4rfwcyVOFOzeauzAO7Rc77mb0rCUJdMckP6nKiD7nrtjlZXznFmYhCvjmWQF2l06Jl7xQsr%2BjkGAeoXo9X%2FiC11ZTNfxOVIe3LWWkRvMwGWvgvtgF4ZEDGaLXgsbO4I8%2FpSmGD4ox9ZWDfX%2BtTURCyBYVXqYpQ4TpgMhHqAtTUr4TNc7GRLVbfi1xqZNQDt1Sfdzh3Xq88dOJyKsyUs7rcFuuxoNyxvqstWVaAyRglOH1n%2BpV0xA7%2FKEHa%2F8%2FzH6uaXeIp3eLJN1%2BGlAQc1sP2jehPHqGi5Lc7YMOKk8akGOrABqEMeyIMA72vRUvaZqcs7N77uX3kDw2%2BTfyF8pS8HYdR1%2BEU1ekEPGlPPLyTo0NFmbmMa4urw%2B19eIvlGSnFjiSeee%2F%2BeotdKLVnDgZ5aNxOYivkgUqjazWNTWX1qdv7Jq7GWrNDLwjZiU5zLvpcjSyzLyGAVIo8pW14m4aC3jppuzjKpasygGK2%2Bf%2BmxisMAkIdRRS5aXW9PY%2FuwiBnL3qiZT5RtAdamISZZM9jUAWY%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231028T003610Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFPXEGMX3T%2F20231028%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=b533a8a386223ef743196ab24ac53ab1abc62144031b368640fdc84801984832",
                        "width": 200,
                        "height": 200
                    },
                    "REGULAR": {
                        "url": "https://edamam-product-images.s3.amazonaws.com/web-img/ab3/ab324ad2c1653b50ce2d8d0781386751.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLWVhc3QtMSJIMEYCIQCP2Gbt%2ByPQIVKV%2FafgML7WXbkOusL9fCs6d1le6dFKYAIhAJcnuEh%2B1NzOso38QgGaVBwaVQAMxyMJATg%2FR%2Fl0jl96KsEFCJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMMTg3MDE3MTUwOTg2IgydADkJdybnmhdEGwQqlQUNCCJJEzulouVCRRPPDPN9Ik9nmgPZk%2Fam6u04CTug5FWfzto4W1y6mlAuXr3EHPB%2FvTcZ%2BmAkgcS5%2FRfKsviGgYg1PBDbKvJFWJigqXNb6jHaHO3eyZnXpof0Qk2PachTFyGGF7upzvEiKr6BGB6DtCoEGe3wCd0iFSMS%2Ft8LIlICGGYaaCvWq9TXeaXkel5jju8XxawzfW0OY8ad1NODjiJJ%2FJ02goRzRa3HwZdXj0P4%2FwwiBHg8BMnsBu5XvhNCt9Gz%2Bxp9cZIC8TMv%2FY8rOvepaH28zVl5BjLGle3tn5syTeLiH6OS68I4OndB2qqeqZqdi9cu6zb1H0y8aKh8r8IIaHqXhP6jBXwOxUN8uimNrMJnaDPxNdvFPuR5yx8UApiuserTd1b1ZIBFiBJ6lavYUBrkLW%2B7bZIJltsNTSxF2GTKFWoXHKGf3%2FXYj%2FniRUh%2BB3xUXrXh8PzVKChkdfuCxirnj5UG2XCrj22%2BBJG8S8UHiExHaIwt01Nel6V7Y0IlXWvwqK8YEx%2FHOI%2FewXERfrnIQDCsrQyC7qTLL3HndUW2Ke8ib2iC%2BPgaP6xDqkqdlhOSojQHG4rfwcyVOFOzeauzAO7Rc77mb0rCUJdMckP6nKiD7nrtjlZXznFmYhCvjmWQF2l06Jl7xQsr%2BjkGAeoXo9X%2FiC11ZTNfxOVIe3LWWkRvMwGWvgvtgF4ZEDGaLXgsbO4I8%2FpSmGD4ox9ZWDfX%2BtTURCyBYVXqYpQ4TpgMhHqAtTUr4TNc7GRLVbfi1xqZNQDt1Sfdzh3Xq88dOJyKsyUs7rcFuuxoNyxvqstWVaAyRglOH1n%2BpV0xA7%2FKEHa%2F8%2FzH6uaXeIp3eLJN1%2BGlAQc1sP2jehPHqGi5Lc7YMOKk8akGOrABqEMeyIMA72vRUvaZqcs7N77uX3kDw2%2BTfyF8pS8HYdR1%2BEU1ekEPGlPPLyTo0NFmbmMa4urw%2B19eIvlGSnFjiSeee%2F%2BeotdKLVnDgZ5aNxOYivkgUqjazWNTWX1qdv7Jq7GWrNDLwjZiU5zLvpcjSyzLyGAVIo8pW14m4aC3jppuzjKpasygGK2%2Bf%2BmxisMAkIdRRS5aXW9PY%2FuwiBnL3qiZT5RtAdamISZZM9jUAWY%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231028T003610Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFPXEGMX3T%2F20231028%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=3b8f1b4b304ba0d4b1abfeb0e8c1828d8103feab6d79614a7401f3665f7f584e",
                        "width": 300,
                        "height": 300
                    }
                },
                "source": "Epicurious",
                "url": "https://www.epicurious.com/recipes/food/views/fresh-tuna-tacos-104809",
                "shareAs": "http://www.edamam.com/recipe/fresh-tuna-tacos-b74d2752729d5889aa6af3396cc91322/tacos",
                "yield": 4.0,
                "dietLabels": [],
                "healthLabels": [
                    "Sugar-Conscious",
                    "Pescatarian",
                    "Mediterranean",
                    "Egg-Free",
                    "Peanut-Free",
                    "Tree-Nut-Free",
                    "Soy-Free",
                    "Shellfish-Free",
                    "Pork-Free",
                    "Red-Meat-Free",
                    "Crustacean-Free",
                    "Celery-Free",
                    "Mustard-Free",
                    "Sesame-Free",
                    "Lupine-Free",
                    "Mollusk-Free",
                    "Alcohol-Free",
                    "Sulfite-Free",
                    "Kosher"
                ],
                "cautions": [
                    "Eggs",
                    "Milk",
                    "Sulfites"
                ],
                "ingredientLines": [
                    "1/3 cup sour cream",
                    "1/4 cup chopped red onion",
                    "3 tablespoons chopped cilantro",
                    "1 teaspoon minced canned chipotle chilies*",
                    "1 8-ounce ahi tuna steak, cut into 3/4-inch pieces",
                    "1 tablespoon taco seasoning mix",
                    "1 tablespoon vegetable oil",
                    "4 taco shells"
                ],
                "ingredients": [
                    {
                        "text": "1/3 cup sour cream",
                        "quantity": 0.3333333333333333,
                        "measure": "cup",
                        "food": "sour cream",
                        "weight": 76.66666666666666,
                        "foodCategory": "Dairy",
                        "foodId": "food_adp9fcubzl3lr7bcvzn3rbfiiiwq",
                        "image": "https://www.edamam.com/food-img/f9d/f9d6183267b041b0aff9a10b89c9c15f.jpg"
                    },
                    {
                        "text": "1/4 cup chopped red onion",
                        "quantity": 0.25,
                        "measure": "cup",
                        "food": "red onion",
                        "weight": 40.0,
                        "foodCategory": "vegetables",
                        "foodId": "food_bmrvi4ob4binw9a5m7l07amlfcoy",
                        "image": "https://www.edamam.com/food-img/205/205e6bf2399b85d34741892ef91cc603.jpg"
                    },
                    {
                        "text": "3 tablespoons chopped cilantro",
                        "quantity": 3.0,
                        "measure": "tablespoon",
                        "food": "cilantro",
                        "weight": 2.999999999949279,
                        "foodCategory": "vegetables",
                        "foodId": "food_alhzhuwb4lc7jnb5s6f02by60bzp",
                        "image": "https://www.edamam.com/food-img/d57/d57e375b6ff99a90c7ee2b1990a1af36.jpg"
                    },
                    {
                        "text": "1 teaspoon minced canned chipotle chilies*",
                        "quantity": 1.0,
                        "measure": "teaspoon",
                        "food": "chipotle chilies",
                        "weight": 2.83333333347704,
                        "foodCategory": "canned vegetables",
                        "foodId": "food_bumzpysb5k05cibmscqp2a0fwgpa",
                        "image": "https://www.edamam.com/food-img/c34/c343c40fbfe50bd72bbb3890c83a4315.jpeg"
                    },
                    {
                        "text": "1 8-ounce ahi tuna steak, cut into 3/4-inch pieces",
                        "quantity": 8.0,
                        "measure": "ounce",
                        "food": "tuna steak",
                        "weight": 226.796185,
                        "foodCategory": "seafood",
                        "foodId": "food_bu5s7alaj4fjv8bf9qxvnba38oay",
                        "image": "https://www.edamam.com/food-img/022/022db6571bd5b3dfbd3ef8941c775d12.jpg"
                    },
                    {
                        "text": "1 tablespoon taco seasoning mix",
                        "quantity": 1.0,
                        "measure": "tablespoon",
                        "food": "taco seasoning",
                        "weight": 8.54999999942178,
                        "foodCategory": "Condiments and sauces",
                        "foodId": "food_boffkg3ap17ef6a47lzm6b655i8w",
                        "image": "https://www.edamam.com/food-img/b3d/b3d804a544f099eabb941f255c1618a6.jpg"
                    },
                    {
                        "text": "1 tablespoon vegetable oil",
                        "quantity": 1.0,
                        "measure": "tablespoon",
                        "food": "vegetable oil",
                        "weight": 14.0,
                        "foodCategory": "Oils",
                        "foodId": "food_bt1mzi2ah2sfg8bv7no1qai83w8s",
                        "image": "https://www.edamam.com/food-img/6e5/6e51a63a6300a8ea1b4c4cc68dfaba33.jpg"
                    },
                    {
                        "text": "4 taco shells",
                        "quantity": 4.0,
                        "measure": "<unit>",
                        "food": "taco shells",
                        "weight": 50.8,
                        "foodCategory": "quick breads and pastries",
                        "foodId": "food_amx6njaaa4q9lsaz4k98faejx12a",
                        "image": "https://www.edamam.com/food-img/def/def506222dc404affdfbf7b7133a34c6.jpg"
                    }
                ],
                "calories": 809.3918416481567,
                "totalCO2Emissions": 5091.140733434635,
                "co2EmissionsClass": "F",
                "totalWeight": 422.6461849995148,
                "totalTime": 0.0,
                "cuisineType": [
                    "mexican"
                ],
                "mealType": [
                    "lunch/dinner"
                ],
                "dishType": [
                    "salad"
                ],
                "totalNutrients": {
                    "ENERC_KCAL": {
                        "label": "Energy",
                        "quantity": 809.3918416481567,
                        "unit": "kcal"
                    },
                    "FAT": {
                        "label": "Fat",
                        "quantity": 41.11746797316654,
                        "unit": "g"
                    },
                    "FASAT": {
                        "label": "Saturated",
                        "quantity": 12.669126104866674,
                        "unit": "g"
                    },
                    "FATRN": {
                        "label": "Trans",
                        "quantity": 0.8413100562666667,
                        "unit": "g"
                    },
                    "FAMS": {
                        "label": "Monounsaturated",
                        "quantity": 17.40122357459987,
                        "unit": "g"
                    },
                    "FAPU": {
                        "label": "Polyunsaturated",
                        "quantity": 6.144282058616726,
                        "unit": "g"
                    },
                    "CHOCDF": {
                        "label": "Carbs",
                        "quantity": 44.75726666633677,
                        "unit": "g"
                    },
                    "CHOCDF.net": {
                        "label": "Carbohydrates (net)",
                        "quantity": 39.41568333307989,
                        "unit": "g"
                    },
                    "FIBTG": {
                        "label": "Fiber",
                        "quantity": 5.341583333256878,
                        "unit": "g"
                    },
                    "SUGAR": {
                        "label": "Sugars",
                        "quantity": 6.115899999941883,
                        "unit": "g"
                    },
                    "PROCNT": {
                        "label": "Protein",
                        "quantity": 61.37936580664086,
                        "unit": "g"
                    },
                    "CHOLE": {
                        "label": "Cholesterol",
                        "quantity": 133.68384548333333,
                        "unit": "mg"
                    },
                    "NA": {
                        "label": "Sodium",
                        "quantity": 942.1469498766929,
                        "unit": "mg"
                    },
                    "CA": {
                        "label": "Calcium",
                        "quantity": 148.71351406664274,
                        "unit": "mg"
                    },
                    "MG": {
                        "label": "Magnesium",
                        "quantity": 134.38599808334027,
                        "unit": "mg"
                    },
                    "K": {
                        "label": "Potassium",
                        "quantity": 1378.180842510889,
                        "unit": "mg"
                    },
                    "FE": {
                        "label": "Iron",
                        "quantity": 3.3999839577915227,
                        "unit": "mg"
                    },
                    "ZN": {
                        "label": "Zinc",
                        "quantity": 1.9978425511666575,
                        "unit": "mg"
                    },
                    "P": {
                        "label": "Phosphorus",
                        "quantity": 820.6457276333335,
                        "unit": "mg"
                    },
                    "VITA_RAE": {
                        "label": "Vitamin A",
                        "quantity": 163.36631330068414,
                        "unit": "µg"
                    },
                    "VITC": {
                        "label": "Vitamin C",
                        "quantity": 6.386666666750693,
                        "unit": "mg"
                    },
                    "THIA": {
                        "label": "Thiamin (B1)",
                        "quantity": 0.41365749829999476,
                        "unit": "mg"
                    },
                    "RIBF": {
                        "label": "Riboflavin (B2)",
                        "quantity": 0.4473322794166564,
                        "unit": "mg"
                    },
                    "NIA": {
                        "label": "Niacin (B3)",
                        "quantity": 43.080920891667255,
                        "unit": "mg"
                    },
                    "VITB6A": {
                        "label": "Vitamin B6",
                        "quantity": 2.307370739383478,
                        "unit": "mg"
                    },
                    "FOLDFE": {
                        "label": "Folate equivalent (total)",
                        "quantity": 62.05925703331626,
                        "unit": "µg"
                    },
                    "FOLFD": {
                        "label": "Folate (food)",
                        "quantity": 42.24725703331626,
                        "unit": "µg"
                    },
                    "FOLAC": {
                        "label": "Folic acid",
                        "quantity": 12.192,
                        "unit": "µg"
                    },
                    "VITB12": {
                        "label": "Vitamin B12",
                        "quantity": 4.878360648,
                        "unit": "µg"
                    },
                    "VITD": {
                        "label": "Vitamin D",
                        "quantity": 3.855535145,
                        "unit": "µg"
                    },
                    "TOCPHA": {
                        "label": "Vitamin E",
                        "quantity": 4.340714177333058,
                        "unit": "mg"
                    },
                    "VITK1": {
                        "label": "Vitamin K",
                        "quantity": 15.452096184855268,
                        "unit": "µg"
                    },
                    "WATER": {
                        "label": "Water",
                        "quantity": 268.63789356671987,
                        "unit": "g"
                    }
                },
                "totalDaily": {
                    "ENERC_KCAL": {
                        "label": "Energy",
                        "quantity": 40.469592082407836,
                        "unit": "%"
                    },
                    "FAT": {
                        "label": "Fat",
                        "quantity": 63.25764303564083,
                        "unit": "%"
                    },
                    "FASAT": {
                        "label": "Saturated",
                        "quantity": 63.345630524333366,
                        "unit": "%"
                    },
                    "CHOCDF": {
                        "label": "Carbs",
                        "quantity": 14.919088888778925,
                        "unit": "%"
                    },
                    "FIBTG": {
                        "label": "Fiber",
                        "quantity": 21.366333333027516,
                        "unit": "%"
                    },
                    "PROCNT": {
                        "label": "Protein",
                        "quantity": 122.75873161328173,
                        "unit": "%"
                    },
                    "CHOLE": {
                        "label": "Cholesterol",
                        "quantity": 44.561281827777776,
                        "unit": "%"
                    },
                    "NA": {
                        "label": "Sodium",
                        "quantity": 39.25612291152888,
                        "unit": "%"
                    },
                    "CA": {
                        "label": "Calcium",
                        "quantity": 14.871351406664274,
                        "unit": "%"
                    },
                    "MG": {
                        "label": "Magnesium",
                        "quantity": 31.996666210319113,
                        "unit": "%"
                    },
                    "K": {
                        "label": "Potassium",
                        "quantity": 29.32299664916785,
                        "unit": "%"
                    },
                    "FE": {
                        "label": "Iron",
                        "quantity": 18.88879976550846,
                        "unit": "%"
                    },
                    "ZN": {
                        "label": "Zinc",
                        "quantity": 18.162205010605977,
                        "unit": "%"
                    },
                    "P": {
                        "label": "Phosphorus",
                        "quantity": 117.23510394761908,
                        "unit": "%"
                    },
                    "VITA_RAE": {
                        "label": "Vitamin A",
                        "quantity": 18.151812588964905,
                        "unit": "%"
                    },
                    "VITC": {
                        "label": "Vitamin C",
                        "quantity": 7.096296296389659,
                        "unit": "%"
                    },
                    "THIA": {
                        "label": "Thiamin (B1)",
                        "quantity": 34.47145819166623,
                        "unit": "%"
                    },
                    "RIBF": {
                        "label": "Riboflavin (B2)",
                        "quantity": 34.4101753397428,
                        "unit": "%"
                    },
                    "NIA": {
                        "label": "Niacin (B3)",
                        "quantity": 269.25575557292035,
                        "unit": "%"
                    },
                    "VITB6A": {
                        "label": "Vitamin B6",
                        "quantity": 177.49005687565216,
                        "unit": "%"
                    },
                    "FOLDFE": {
                        "label": "Folate equivalent (total)",
                        "quantity": 15.514814258329062,
                        "unit": "%"
                    },
                    "VITB12": {
                        "label": "Vitamin B12",
                        "quantity": 203.26502700000003,
                        "unit": "%"
                    },
                    "VITD": {
                        "label": "Vitamin D",
                        "quantity": 25.703567633333332,
                        "unit": "%"
                    },
                    "TOCPHA": {
                        "label": "Vitamin E",
                        "quantity": 28.93809451555372,
                        "unit": "%"
                    },
                    "VITK1": {
                        "label": "Vitamin K",
                        "quantity": 12.876746820712723,
                        "unit": "%"
                    }
                },
                "digest": [
                    {
                        "label": "Fat",
                        "tag": "FAT",
                        "schemaOrgTag": "fatContent",
                        "total": 41.11746797316654,
                        "hasRDI": True,
                        "daily": 63.25764303564083,
                        "unit": "g",
                        "sub": [
                            {
                                "label": "Saturated",
                                "tag": "FASAT",
                                "schemaOrgTag": "saturatedFatContent",
                                "total": 12.669126104866674,
                                "hasRDI": True,
                                "daily": 63.345630524333366,
                                "unit": "g"
                            },
                            {
                                "label": "Trans",
                                "tag": "FATRN",
                                "schemaOrgTag": "transFatContent",
                                "total": 0.8413100562666667,
                                "hasRDI": False,
                                "daily": 0.0,
                                "unit": "g"
                            },
                            {
                                "label": "Monounsaturated",
                                "tag": "FAMS",
                                "schemaOrgTag": '',
                                "total": 17.40122357459987,
                                "hasRDI": False,
                                "daily": 0.0,
                                "unit": "g"
                            },
                            {
                                "label": "Polyunsaturated",
                                "tag": "FAPU",
                                "schemaOrgTag": '',
                                "total": 6.144282058616726,
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
                        "total": 44.75726666633677,
                        "hasRDI": True,
                        "daily": 14.919088888778925,
                        "unit": "g",
                        "sub": [
                            {
                                "label": "Carbs (net)",
                                "tag": "CHOCDF.net",
                                "schemaOrgTag": '',
                                "total": 39.41568333307989,
                                "hasRDI": False,
                                "daily": 0.0,
                                "unit": "g"
                            },
                            {
                                "label": "Fiber",
                                "tag": "FIBTG",
                                "schemaOrgTag": "fiberContent",
                                "total": 5.341583333256878,
                                "hasRDI": True,
                                "daily": 21.366333333027516,
                                "unit": "g"
                            },
                            {
                                "label": "Sugars",
                                "tag": "SUGAR",
                                "schemaOrgTag": "sugarContent",
                                "total": 6.115899999941883,
                                "hasRDI": False,
                                "daily": 0.0,
                                "unit": "g"
                            },
                            {
                                "label": "Sugars, added",
                                "tag": "SUGAR.added",
                                "schemaOrgTag": '',
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
                        "total": 61.37936580664086,
                        "hasRDI": True,
                        "daily": 122.75873161328173,
                        "unit": "g"
                    },
                    {
                        "label": "Cholesterol",
                        "tag": "CHOLE",
                        "schemaOrgTag": "cholesterolContent",
                        "total": 133.68384548333333,
                        "hasRDI": True,
                        "daily": 44.561281827777776,
                        "unit": "mg"
                    },
                    {
                        "label": "Sodium",
                        "tag": "NA",
                        "schemaOrgTag": "sodiumContent",
                        "total": 942.1469498766929,
                        "hasRDI": True,
                        "daily": 39.25612291152888,
                        "unit": "mg"
                    },
                    {
                        "label": "Calcium",
                        "tag": "CA",
                        "schemaOrgTag": '',
                        "total": 148.71351406664274,
                        "hasRDI": True,
                        "daily": 14.871351406664274,
                        "unit": "mg"
                    },
                    {
                        "label": "Magnesium",
                        "tag": "MG",
                        "schemaOrgTag": '',
                        "total": 134.38599808334027,
                        "hasRDI": True,
                        "daily": 31.996666210319113,
                        "unit": "mg"
                    },
                    {
                        "label": "Potassium",
                        "tag": "K",
                        "schemaOrgTag": '',
                        "total": 1378.180842510889,
                        "hasRDI": True,
                        "daily": 29.32299664916785,
                        "unit": "mg"
                    },
                    {
                        "label": "Iron",
                        "tag": "FE",
                        "schemaOrgTag": '',
                        "total": 3.3999839577915227,
                        "hasRDI": True,
                        "daily": 18.88879976550846,
                        "unit": "mg"
                    },
                    {
                        "label": "Zinc",
                        "tag": "ZN",
                        "schemaOrgTag": '',
                        "total": 1.9978425511666575,
                        "hasRDI": True,
                        "daily": 18.162205010605977,
                        "unit": "mg"
                    },
                    {
                        "label": "Phosphorus",
                        "tag": "P",
                        "schemaOrgTag": '',
                        "total": 820.6457276333335,
                        "hasRDI": True,
                        "daily": 117.23510394761908,
                        "unit": "mg"
                    },
                    {
                        "label": "Vitamin A",
                        "tag": "VITA_RAE",
                        "schemaOrgTag": '',
                        "total": 163.36631330068414,
                        "hasRDI": True,
                        "daily": 18.151812588964905,
                        "unit": "µg"
                    },
                    {
                        "label": "Vitamin C",
                        "tag": "VITC",
                        "schemaOrgTag": '',
                        "total": 6.386666666750693,
                        "hasRDI": True,
                        "daily": 7.096296296389659,
                        "unit": "mg"
                    },
                    {
                        "label": "Thiamin (B1)",
                        "tag": "THIA",
                        "schemaOrgTag": '',
                        "total": 0.41365749829999476,
                        "hasRDI": True,
                        "daily": 34.47145819166623,
                        "unit": "mg"
                    },
                    {
                        "label": "Riboflavin (B2)",
                        "tag": "RIBF",
                        "schemaOrgTag": '',
                        "total": 0.4473322794166564,
                        "hasRDI": True,
                        "daily": 34.4101753397428,
                        "unit": "mg"
                    },
                    {
                        "label": "Niacin (B3)",
                        "tag": "NIA",
                        "schemaOrgTag": '',
                        "total": 43.080920891667255,
                        "hasRDI": True,
                        "daily": 269.25575557292035,
                        "unit": "mg"
                    },
                    {
                        "label": "Vitamin B6",
                        "tag": "VITB6A",
                        "schemaOrgTag": '',
                        "total": 2.307370739383478,
                        "hasRDI": True,
                        "daily": 177.49005687565216,
                        "unit": "mg"
                    },
                    {
                        "label": "Folate equivalent (total)",
                        "tag": "FOLDFE",
                        "schemaOrgTag": '',
                        "total": 62.05925703331626,
                        "hasRDI": True,
                        "daily": 15.514814258329062,
                        "unit": "µg"
                    },
                    {
                        "label": "Folate (food)",
                        "tag": "FOLFD",
                        "schemaOrgTag": '',
                        "total": 42.24725703331626,
                        "hasRDI": False,
                        "daily": 0.0,
                        "unit": "µg"
                    },
                    {
                        "label": "Folic acid",
                        "tag": "FOLAC",
                        "schemaOrgTag": '',
                        "total": 12.192,
                        "hasRDI": False,
                        "daily": 0.0,
                        "unit": "µg"
                    },
                    {
                        "label": "Vitamin B12",
                        "tag": "VITB12",
                        "schemaOrgTag": '',
                        "total": 4.878360648,
                        "hasRDI": True,
                        "daily": 203.26502700000003,
                        "unit": "µg"
                    },
                    {
                        "label": "Vitamin D",
                        "tag": "VITD",
                        "schemaOrgTag": '',
                        "total": 3.855535145,
                        "hasRDI": True,
                        "daily": 25.703567633333332,
                        "unit": "µg"
                    },
                    {
                        "label": "Vitamin E",
                        "tag": "TOCPHA",
                        "schemaOrgTag": '',
                        "total": 4.340714177333058,
                        "hasRDI": True,
                        "daily": 28.93809451555372,
                        "unit": "mg"
                    },
                    {
                        "label": "Vitamin K",
                        "tag": "VITK1",
                        "schemaOrgTag": '',
                        "total": 15.452096184855268,
                        "hasRDI": True,
                        "daily": 12.876746820712723,
                        "unit": "µg"
                    },
                    {
                        "label": "Sugar alcohols",
                        "tag": "Sugar.alcohol",
                        "schemaOrgTag": '',
                        "total": 0.0,
                        "hasRDI": False,
                        "daily": 0.0,
                        "unit": "g"
                    },
                    {
                        "label": "Water",
                        "tag": "WATER",
                        "schemaOrgTag": '',
                        "total": 268.63789356671987,
                        "hasRDI": False,
                        "daily": 0.0,
                        "unit": "g"
                    }
                ]
            },
            "_links": {
                "self": {
                    "title": "Self",
                    "href": "https://api.edamam.com/api/recipes/v2/b74d2752729d5889aa6af3396cc91322?type=public&app_id=e909afd5&app_key=34e59dda7e1bffb92e49c416e9449e1d"
                }
            }
        },
        {
            "recipe": {
                "uri": "http://www.edamam.com/ontologies/edamam.owl#recipe_1c226c5925e580ede17ebfd448e3164a",
                "label": "Salsa Egg Tacos",
                "image": "https://edamam-product-images.s3.amazonaws.com/web-img/e9b/e9bb67ed4f19a74364c9874a605de225.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLWVhc3QtMSJIMEYCIQCP2Gbt%2ByPQIVKV%2FafgML7WXbkOusL9fCs6d1le6dFKYAIhAJcnuEh%2B1NzOso38QgGaVBwaVQAMxyMJATg%2FR%2Fl0jl96KsEFCJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMMTg3MDE3MTUwOTg2IgydADkJdybnmhdEGwQqlQUNCCJJEzulouVCRRPPDPN9Ik9nmgPZk%2Fam6u04CTug5FWfzto4W1y6mlAuXr3EHPB%2FvTcZ%2BmAkgcS5%2FRfKsviGgYg1PBDbKvJFWJigqXNb6jHaHO3eyZnXpof0Qk2PachTFyGGF7upzvEiKr6BGB6DtCoEGe3wCd0iFSMS%2Ft8LIlICGGYaaCvWq9TXeaXkel5jju8XxawzfW0OY8ad1NODjiJJ%2FJ02goRzRa3HwZdXj0P4%2FwwiBHg8BMnsBu5XvhNCt9Gz%2Bxp9cZIC8TMv%2FY8rOvepaH28zVl5BjLGle3tn5syTeLiH6OS68I4OndB2qqeqZqdi9cu6zb1H0y8aKh8r8IIaHqXhP6jBXwOxUN8uimNrMJnaDPxNdvFPuR5yx8UApiuserTd1b1ZIBFiBJ6lavYUBrkLW%2B7bZIJltsNTSxF2GTKFWoXHKGf3%2FXYj%2FniRUh%2BB3xUXrXh8PzVKChkdfuCxirnj5UG2XCrj22%2BBJG8S8UHiExHaIwt01Nel6V7Y0IlXWvwqK8YEx%2FHOI%2FewXERfrnIQDCsrQyC7qTLL3HndUW2Ke8ib2iC%2BPgaP6xDqkqdlhOSojQHG4rfwcyVOFOzeauzAO7Rc77mb0rCUJdMckP6nKiD7nrtjlZXznFmYhCvjmWQF2l06Jl7xQsr%2BjkGAeoXo9X%2FiC11ZTNfxOVIe3LWWkRvMwGWvgvtgF4ZEDGaLXgsbO4I8%2FpSmGD4ox9ZWDfX%2BtTURCyBYVXqYpQ4TpgMhHqAtTUr4TNc7GRLVbfi1xqZNQDt1Sfdzh3Xq88dOJyKsyUs7rcFuuxoNyxvqstWVaAyRglOH1n%2BpV0xA7%2FKEHa%2F8%2FzH6uaXeIp3eLJN1%2BGlAQc1sP2jehPHqGi5Lc7YMOKk8akGOrABqEMeyIMA72vRUvaZqcs7N77uX3kDw2%2BTfyF8pS8HYdR1%2BEU1ekEPGlPPLyTo0NFmbmMa4urw%2B19eIvlGSnFjiSeee%2F%2BeotdKLVnDgZ5aNxOYivkgUqjazWNTWX1qdv7Jq7GWrNDLwjZiU5zLvpcjSyzLyGAVIo8pW14m4aC3jppuzjKpasygGK2%2Bf%2BmxisMAkIdRRS5aXW9PY%2FuwiBnL3qiZT5RtAdamISZZM9jUAWY%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231028T003610Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFPXEGMX3T%2F20231028%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=b48109e1e452e306e789598c8e4d41a9879fe51dfa53b0c85ed791d19ead9b13",
                "images": {
                    "THUMBNAIL": {
                        "url": "https://edamam-product-images.s3.amazonaws.com/web-img/e9b/e9bb67ed4f19a74364c9874a605de225-s.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLWVhc3QtMSJIMEYCIQCP2Gbt%2ByPQIVKV%2FafgML7WXbkOusL9fCs6d1le6dFKYAIhAJcnuEh%2B1NzOso38QgGaVBwaVQAMxyMJATg%2FR%2Fl0jl96KsEFCJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMMTg3MDE3MTUwOTg2IgydADkJdybnmhdEGwQqlQUNCCJJEzulouVCRRPPDPN9Ik9nmgPZk%2Fam6u04CTug5FWfzto4W1y6mlAuXr3EHPB%2FvTcZ%2BmAkgcS5%2FRfKsviGgYg1PBDbKvJFWJigqXNb6jHaHO3eyZnXpof0Qk2PachTFyGGF7upzvEiKr6BGB6DtCoEGe3wCd0iFSMS%2Ft8LIlICGGYaaCvWq9TXeaXkel5jju8XxawzfW0OY8ad1NODjiJJ%2FJ02goRzRa3HwZdXj0P4%2FwwiBHg8BMnsBu5XvhNCt9Gz%2Bxp9cZIC8TMv%2FY8rOvepaH28zVl5BjLGle3tn5syTeLiH6OS68I4OndB2qqeqZqdi9cu6zb1H0y8aKh8r8IIaHqXhP6jBXwOxUN8uimNrMJnaDPxNdvFPuR5yx8UApiuserTd1b1ZIBFiBJ6lavYUBrkLW%2B7bZIJltsNTSxF2GTKFWoXHKGf3%2FXYj%2FniRUh%2BB3xUXrXh8PzVKChkdfuCxirnj5UG2XCrj22%2BBJG8S8UHiExHaIwt01Nel6V7Y0IlXWvwqK8YEx%2FHOI%2FewXERfrnIQDCsrQyC7qTLL3HndUW2Ke8ib2iC%2BPgaP6xDqkqdlhOSojQHG4rfwcyVOFOzeauzAO7Rc77mb0rCUJdMckP6nKiD7nrtjlZXznFmYhCvjmWQF2l06Jl7xQsr%2BjkGAeoXo9X%2FiC11ZTNfxOVIe3LWWkRvMwGWvgvtgF4ZEDGaLXgsbO4I8%2FpSmGD4ox9ZWDfX%2BtTURCyBYVXqYpQ4TpgMhHqAtTUr4TNc7GRLVbfi1xqZNQDt1Sfdzh3Xq88dOJyKsyUs7rcFuuxoNyxvqstWVaAyRglOH1n%2BpV0xA7%2FKEHa%2F8%2FzH6uaXeIp3eLJN1%2BGlAQc1sP2jehPHqGi5Lc7YMOKk8akGOrABqEMeyIMA72vRUvaZqcs7N77uX3kDw2%2BTfyF8pS8HYdR1%2BEU1ekEPGlPPLyTo0NFmbmMa4urw%2B19eIvlGSnFjiSeee%2F%2BeotdKLVnDgZ5aNxOYivkgUqjazWNTWX1qdv7Jq7GWrNDLwjZiU5zLvpcjSyzLyGAVIo8pW14m4aC3jppuzjKpasygGK2%2Bf%2BmxisMAkIdRRS5aXW9PY%2FuwiBnL3qiZT5RtAdamISZZM9jUAWY%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231028T003610Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFPXEGMX3T%2F20231028%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=c363c8f23e8bb96f6509343a7642a309b1d84607d2d4e117aa126bcb33836362",
                        "width": 100,
                        "height": 100
                    },
                    "SMALL": {
                        "url": "https://edamam-product-images.s3.amazonaws.com/web-img/e9b/e9bb67ed4f19a74364c9874a605de225-m.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLWVhc3QtMSJIMEYCIQCP2Gbt%2ByPQIVKV%2FafgML7WXbkOusL9fCs6d1le6dFKYAIhAJcnuEh%2B1NzOso38QgGaVBwaVQAMxyMJATg%2FR%2Fl0jl96KsEFCJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMMTg3MDE3MTUwOTg2IgydADkJdybnmhdEGwQqlQUNCCJJEzulouVCRRPPDPN9Ik9nmgPZk%2Fam6u04CTug5FWfzto4W1y6mlAuXr3EHPB%2FvTcZ%2BmAkgcS5%2FRfKsviGgYg1PBDbKvJFWJigqXNb6jHaHO3eyZnXpof0Qk2PachTFyGGF7upzvEiKr6BGB6DtCoEGe3wCd0iFSMS%2Ft8LIlICGGYaaCvWq9TXeaXkel5jju8XxawzfW0OY8ad1NODjiJJ%2FJ02goRzRa3HwZdXj0P4%2FwwiBHg8BMnsBu5XvhNCt9Gz%2Bxp9cZIC8TMv%2FY8rOvepaH28zVl5BjLGle3tn5syTeLiH6OS68I4OndB2qqeqZqdi9cu6zb1H0y8aKh8r8IIaHqXhP6jBXwOxUN8uimNrMJnaDPxNdvFPuR5yx8UApiuserTd1b1ZIBFiBJ6lavYUBrkLW%2B7bZIJltsNTSxF2GTKFWoXHKGf3%2FXYj%2FniRUh%2BB3xUXrXh8PzVKChkdfuCxirnj5UG2XCrj22%2BBJG8S8UHiExHaIwt01Nel6V7Y0IlXWvwqK8YEx%2FHOI%2FewXERfrnIQDCsrQyC7qTLL3HndUW2Ke8ib2iC%2BPgaP6xDqkqdlhOSojQHG4rfwcyVOFOzeauzAO7Rc77mb0rCUJdMckP6nKiD7nrtjlZXznFmYhCvjmWQF2l06Jl7xQsr%2BjkGAeoXo9X%2FiC11ZTNfxOVIe3LWWkRvMwGWvgvtgF4ZEDGaLXgsbO4I8%2FpSmGD4ox9ZWDfX%2BtTURCyBYVXqYpQ4TpgMhHqAtTUr4TNc7GRLVbfi1xqZNQDt1Sfdzh3Xq88dOJyKsyUs7rcFuuxoNyxvqstWVaAyRglOH1n%2BpV0xA7%2FKEHa%2F8%2FzH6uaXeIp3eLJN1%2BGlAQc1sP2jehPHqGi5Lc7YMOKk8akGOrABqEMeyIMA72vRUvaZqcs7N77uX3kDw2%2BTfyF8pS8HYdR1%2BEU1ekEPGlPPLyTo0NFmbmMa4urw%2B19eIvlGSnFjiSeee%2F%2BeotdKLVnDgZ5aNxOYivkgUqjazWNTWX1qdv7Jq7GWrNDLwjZiU5zLvpcjSyzLyGAVIo8pW14m4aC3jppuzjKpasygGK2%2Bf%2BmxisMAkIdRRS5aXW9PY%2FuwiBnL3qiZT5RtAdamISZZM9jUAWY%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231028T003610Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFPXEGMX3T%2F20231028%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=92af54edef3cfdcc0ccebd772f716ac7498b64bf6434e70157f421f44212eb86",
                        "width": 200,
                        "height": 200
                    },
                    "REGULAR": {
                        "url": "https://edamam-product-images.s3.amazonaws.com/web-img/e9b/e9bb67ed4f19a74364c9874a605de225.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLWVhc3QtMSJIMEYCIQCP2Gbt%2ByPQIVKV%2FafgML7WXbkOusL9fCs6d1le6dFKYAIhAJcnuEh%2B1NzOso38QgGaVBwaVQAMxyMJATg%2FR%2Fl0jl96KsEFCJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMMTg3MDE3MTUwOTg2IgydADkJdybnmhdEGwQqlQUNCCJJEzulouVCRRPPDPN9Ik9nmgPZk%2Fam6u04CTug5FWfzto4W1y6mlAuXr3EHPB%2FvTcZ%2BmAkgcS5%2FRfKsviGgYg1PBDbKvJFWJigqXNb6jHaHO3eyZnXpof0Qk2PachTFyGGF7upzvEiKr6BGB6DtCoEGe3wCd0iFSMS%2Ft8LIlICGGYaaCvWq9TXeaXkel5jju8XxawzfW0OY8ad1NODjiJJ%2FJ02goRzRa3HwZdXj0P4%2FwwiBHg8BMnsBu5XvhNCt9Gz%2Bxp9cZIC8TMv%2FY8rOvepaH28zVl5BjLGle3tn5syTeLiH6OS68I4OndB2qqeqZqdi9cu6zb1H0y8aKh8r8IIaHqXhP6jBXwOxUN8uimNrMJnaDPxNdvFPuR5yx8UApiuserTd1b1ZIBFiBJ6lavYUBrkLW%2B7bZIJltsNTSxF2GTKFWoXHKGf3%2FXYj%2FniRUh%2BB3xUXrXh8PzVKChkdfuCxirnj5UG2XCrj22%2BBJG8S8UHiExHaIwt01Nel6V7Y0IlXWvwqK8YEx%2FHOI%2FewXERfrnIQDCsrQyC7qTLL3HndUW2Ke8ib2iC%2BPgaP6xDqkqdlhOSojQHG4rfwcyVOFOzeauzAO7Rc77mb0rCUJdMckP6nKiD7nrtjlZXznFmYhCvjmWQF2l06Jl7xQsr%2BjkGAeoXo9X%2FiC11ZTNfxOVIe3LWWkRvMwGWvgvtgF4ZEDGaLXgsbO4I8%2FpSmGD4ox9ZWDfX%2BtTURCyBYVXqYpQ4TpgMhHqAtTUr4TNc7GRLVbfi1xqZNQDt1Sfdzh3Xq88dOJyKsyUs7rcFuuxoNyxvqstWVaAyRglOH1n%2BpV0xA7%2FKEHa%2F8%2FzH6uaXeIp3eLJN1%2BGlAQc1sP2jehPHqGi5Lc7YMOKk8akGOrABqEMeyIMA72vRUvaZqcs7N77uX3kDw2%2BTfyF8pS8HYdR1%2BEU1ekEPGlPPLyTo0NFmbmMa4urw%2B19eIvlGSnFjiSeee%2F%2BeotdKLVnDgZ5aNxOYivkgUqjazWNTWX1qdv7Jq7GWrNDLwjZiU5zLvpcjSyzLyGAVIo8pW14m4aC3jppuzjKpasygGK2%2Bf%2BmxisMAkIdRRS5aXW9PY%2FuwiBnL3qiZT5RtAdamISZZM9jUAWY%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231028T003610Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFPXEGMX3T%2F20231028%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=b48109e1e452e306e789598c8e4d41a9879fe51dfa53b0c85ed791d19ead9b13",
                        "width": 300,
                        "height": 300
                    }
                },
                "source": "Martha Stewart",
                "url": "http://www.marthastewart.com/346118/salsa-egg-tacos",
                "shareAs": "http://www.edamam.com/recipe/salsa-egg-tacos-1c226c5925e580ede17ebfd448e3164a/tacos",
                "yield": 4.0,
                "dietLabels": [],
                "healthLabels": [
                    "Vegetarian",
                    "Pescatarian",
                    "Peanut-Free",
                    "Tree-Nut-Free",
                    "Soy-Free",
                    "Fish-Free",
                    "Shellfish-Free",
                    "Pork-Free",
                    "Red-Meat-Free",
                    "Crustacean-Free",
                    "Celery-Free",
                    "Mustard-Free",
                    "Sesame-Free",
                    "Lupine-Free",
                    "Mollusk-Free",
                    "Alcohol-Free",
                    "Sulfite-Free",
                    "Kosher"
                ],
                "cautions": [
                    "Eggs",
                    "Milk",
                    "Sulfites"
                ],
                "ingredientLines": [
                    "3 large eggs",
                    "1/4 teaspoon each salt and freshly ground pepper",
                    "1 cup grated monterey jack, or cheddar cheese",
                    "1 tablespoon unsalted butter, melted",
                    "3 tablespoons salsa",
                    "4 taco shells",
                    "Shredded lettuce, sour cream, and tomatoes, for topping",
                    "Tortilla chips and canned black beans, for serving (optional)"
                ],
                "ingredients": [
                    {
                        "text": "3 large eggs",
                        "quantity": 3.0,
                        "measure": "<unit>",
                        "food": "eggs",
                        "weight": 150.0,
                        "foodCategory": "Eggs",
                        "foodId": "food_bhpradua77pk16aipcvzeayg732r",
                        "image": "https://www.edamam.com/food-img/a7e/a7ec7c337cb47c6550b3b118e357f077.jpg"
                    },
                    {
                        "text": "1/4 teaspoon each salt and freshly ground pepper",
                        "quantity": 0.25,
                        "measure": "teaspoon",
                        "food": "salt",
                        "weight": 1.5,
                        "foodCategory": "Condiments and sauces",
                        "foodId": "food_btxz81db72hwbra2pncvebzzzum9",
                        "image": "https://www.edamam.com/food-img/694/6943ea510918c6025795e8dc6e6eaaeb.jpg"
                    },
                    {
                        "text": "1/4 teaspoon each salt and freshly ground pepper",
                        "quantity": 0.25,
                        "measure": "teaspoon",
                        "food": "pepper",
                        "weight": 0.575,
                        "foodCategory": "Condiments and sauces",
                        "foodId": "food_b6ywzluaaxv02wad7s1r9ag4py89",
                        "image": "https://www.edamam.com/food-img/c6e/c6e5c3bd8d3bc15175d9766971a4d1b2.jpg"
                    },
                    {
                        "text": "1 cup grated monterey jack, or cheddar cheese",
                        "quantity": 1.0,
                        "measure": "cup",
                        "food": "monterey jack",
                        "weight": 132.0,
                        "foodCategory": "Cheese",
                        "foodId": "food_atp17pta7d5it2a80ct13ard6aj3",
                        "image": "https://www.edamam.com/food-img/590/59062b9f8d57ebc7d831b7b7c231f726.jpg"
                    },
                    {
                        "text": "1 tablespoon unsalted butter, melted",
                        "quantity": 1.0,
                        "measure": "tablespoon",
                        "food": "unsalted butter",
                        "weight": 14.2,
                        "foodCategory": "Dairy",
                        "foodId": "food_awz3iefajbk1fwahq9logahmgltj",
                        "image": "https://www.edamam.com/food-img/713/71397239b670d88c04faa8d05035cab4.jpg"
                    },
                    {
                        "text": "3 tablespoons salsa",
                        "quantity": 3.0,
                        "measure": "tablespoon",
                        "food": "salsa",
                        "weight": 54.0,
                        "foodCategory": "canned soup",
                        "foodId": "food_b0t3obfawlm5k2b6erxscacez35u",
                        "image": "https://www.edamam.com/food-img/995/995d0f166754a0475c181b9c156fec43.jpg"
                    },
                    {
                        "text": "4 taco shells",
                        "quantity": 4.0,
                        "measure": "<unit>",
                        "food": "taco shells",
                        "weight": 50.8,
                        "foodCategory": "quick breads and pastries",
                        "foodId": "food_amx6njaaa4q9lsaz4k98faejx12a",
                        "image": "https://www.edamam.com/food-img/def/def506222dc404affdfbf7b7133a34c6.jpg"
                    },
                    {
                        "text": "Shredded lettuce, sour cream, and tomatoes, for topping",
                        "quantity": 0.0,
                        "measure": '',
                        "food": "lettuce",
                        "weight": 0.0,
                        "foodCategory": "vegetables",
                        "foodId": "food_bf5fxtkbc9alwoajuvsi7amonr5w",
                        "image": "https://www.edamam.com/food-img/719/71996625d0cb47e197093ecd52c97dc2.jpg"
                    },
                    {
                        "text": "Shredded lettuce, sour cream, and tomatoes, for topping",
                        "quantity": 0.0,
                        "measure": '',
                        "food": "sour cream",
                        "weight": 0.0,
                        "foodCategory": "Dairy",
                        "foodId": "food_adp9fcubzl3lr7bcvzn3rbfiiiwq",
                        "image": "https://www.edamam.com/food-img/f9d/f9d6183267b041b0aff9a10b89c9c15f.jpg"
                    },
                    {
                        "text": "Shredded lettuce, sour cream, and tomatoes, for topping",
                        "quantity": 0.0,
                        "measure": '',
                        "food": "tomatoes",
                        "weight": 0.0,
                        "foodCategory": "vegetables",
                        "foodId": "food_a6k79rrahp8fe2b26zussa3wtkqh",
                        "image": "https://www.edamam.com/food-img/23e/23e727a14f1035bdc2733bb0477efbd2.jpg"
                    },
                    {
                        "text": "Tortilla chips and canned black beans, for serving (optional)",
                        "quantity": 1.0,
                        "measure": "serving",
                        "food": "Tortilla chips",
                        "weight": 60.0,
                        "foodCategory": "savory snacks",
                        "foodId": "food_bkxl9s9bpcxmenbef89qbbofifnr",
                        "image": "https://www.edamam.com/food-img/24e/24eea039cad825c1745263674e9879df.jpg"
                    }
                ],
                "calories": 1365.7852500000001,
                "totalCO2Emissions": 4397.537035,
                "co2EmissionsClass": "E",
                "totalWeight": 461.575,
                "totalTime": 47.0,
                "cuisineType": [
                    "mexican"
                ],
                "mealType": [
                    "lunch/dinner"
                ],
                "dishType": [
                    "sandwiches"
                ],
                "totalNutrients": {
                    "ENERC_KCAL": {
                        "label": "Energy",
                        "quantity": 1365.7852500000001,
                        "unit": "kcal"
                    },
                    "FAT": {
                        "label": "Fat",
                        "quantity": 90.342145,
                        "unit": "g"
                    },
                    "FASAT": {
                        "label": "Saturated",
                        "quantity": 42.3721325,
                        "unit": "g"
                    },
                    "FATRN": {
                        "label": "Trans",
                        "quantity": 0.183976,
                        "unit": "g"
                    },
                    "FAMS": {
                        "label": "Monounsaturated",
                        "quantity": 29.050289250000002,
                        "unit": "g"
                    },
                    "FAPU": {
                        "label": "Polyunsaturated",
                        "quantity": 12.828958499999999,
                        "unit": "g"
                    },
                    "CHOCDF": {
                        "label": "Carbs",
                        "quantity": 78.63772,
                        "unit": "g"
                    },
                    "CHOCDF.net": {
                        "label": "Carbohydrates (net)",
                        "quantity": 71.242645,
                        "unit": "g"
                    },
                    "FIBTG": {
                        "label": "Fiber",
                        "quantity": 7.395075,
                        "unit": "g"
                    },
                    "SUGAR": {
                        "label": "Sugars",
                        "quantity": 4.8806,
                        "unit": "g"
                    },
                    "PROCNT": {
                        "label": "Protein",
                        "quantity": 59.46958,
                        "unit": "g"
                    },
                    "CHOLE": {
                        "label": "Cholesterol",
                        "quantity": 706.01,
                        "unit": "mg"
                    },
                    "NA": {
                        "label": "Sodium",
                        "quantity": 1741.209,
                        "unit": "mg"
                    },
                    "CA": {
                        "label": "Calcium",
                        "quantity": 1204.07525,
                        "unit": "mg"
                    },
                    "MG": {
                        "label": "Magnesium",
                        "quantity": 155.57125,
                        "unit": "mg"
                    },
                    "K": {
                        "label": "Potassium",
                        "quantity": 714.4235,
                        "unit": "mg"
                    },
                    "FE": {
                        "label": "Iron",
                        "quantity": 5.4859925,
                        "unit": "mg"
                    },
                    "ZN": {
                        "label": "Zinc",
                        "quantity": 7.7057025,
                        "unit": "mg"
                    },
                    "P": {
                        "label": "Phosphorus",
                        "quantity": 1163.9805000000001,
                        "unit": "mg"
                    },
                    "VITA_RAE": {
                        "label": "Vitamin A",
                        "quantity": 616.37125,
                        "unit": "µg"
                    },
                    "VITC": {
                        "label": "Vitamin C",
                        "quantity": 1.026,
                        "unit": "mg"
                    },
                    "THIA": {
                        "label": "Thiamin (B1)",
                        "quantity": 0.286679,
                        "unit": "mg"
                    },
                    "RIBF": {
                        "label": "Riboflavin (B2)",
                        "quantity": 1.2898830000000001,
                        "unit": "mg"
                    },
                    "NIA": {
                        "label": "Niacin (B3)",
                        "quantity": 2.6863390000000003,
                        "unit": "mg"
                    },
                    "VITB6A": {
                        "label": "Vitamin B6",
                        "quantity": 0.67858325,
                        "unit": "mg"
                    },
                    "FOLDFE": {
                        "label": "Folate equivalent (total)",
                        "quantity": 153.32375,
                        "unit": "µg"
                    },
                    "FOLFD": {
                        "label": "Folate (food)",
                        "quantity": 133.51175,
                        "unit": "µg"
                    },
                    "FOLAC": {
                        "label": "Folic acid",
                        "quantity": 12.192,
                        "unit": "µg"
                    },
                    "VITB12": {
                        "label": "Vitamin B12",
                        "quantity": 2.45474,
                        "unit": "µg"
                    },
                    "VITD": {
                        "label": "Vitamin D",
                        "quantity": 3.792,
                        "unit": "µg"
                    },
                    "TOCPHA": {
                        "label": "Vitamin E",
                        "quantity": 5.0773399999999995,
                        "unit": "mg"
                    },
                    "VITK1": {
                        "label": "Vitamin K",
                        "quantity": 12.7378,
                        "unit": "µg"
                    },
                    "WATER": {
                        "label": "Water",
                        "quantity": 223.42947500000002,
                        "unit": "g"
                    }
                },
                "totalDaily": {
                    "ENERC_KCAL": {
                        "label": "Energy",
                        "quantity": 68.2892625,
                        "unit": "%"
                    },
                    "FAT": {
                        "label": "Fat",
                        "quantity": 138.98791538461538,
                        "unit": "%"
                    },
                    "FASAT": {
                        "label": "Saturated",
                        "quantity": 211.8606625,
                        "unit": "%"
                    },
                    "CHOCDF": {
                        "label": "Carbs",
                        "quantity": 26.21257333333333,
                        "unit": "%"
                    },
                    "FIBTG": {
                        "label": "Fiber",
                        "quantity": 29.5803,
                        "unit": "%"
                    },
                    "PROCNT": {
                        "label": "Protein",
                        "quantity": 118.93915999999999,
                        "unit": "%"
                    },
                    "CHOLE": {
                        "label": "Cholesterol",
                        "quantity": 235.33666666666667,
                        "unit": "%"
                    },
                    "NA": {
                        "label": "Sodium",
                        "quantity": 72.550375,
                        "unit": "%"
                    },
                    "CA": {
                        "label": "Calcium",
                        "quantity": 120.407525,
                        "unit": "%"
                    },
                    "MG": {
                        "label": "Magnesium",
                        "quantity": 37.04077380952381,
                        "unit": "%"
                    },
                    "K": {
                        "label": "Potassium",
                        "quantity": 15.200500000000002,
                        "unit": "%"
                    },
                    "FE": {
                        "label": "Iron",
                        "quantity": 30.47773611111111,
                        "unit": "%"
                    },
                    "ZN": {
                        "label": "Zinc",
                        "quantity": 70.05184090909091,
                        "unit": "%"
                    },
                    "P": {
                        "label": "Phosphorus",
                        "quantity": 166.28292857142858,
                        "unit": "%"
                    },
                    "VITA_RAE": {
                        "label": "Vitamin A",
                        "quantity": 68.48569444444445,
                        "unit": "%"
                    },
                    "VITC": {
                        "label": "Vitamin C",
                        "quantity": 1.1400000000000001,
                        "unit": "%"
                    },
                    "THIA": {
                        "label": "Thiamin (B1)",
                        "quantity": 23.88991666666667,
                        "unit": "%"
                    },
                    "RIBF": {
                        "label": "Riboflavin (B2)",
                        "quantity": 99.22176923076924,
                        "unit": "%"
                    },
                    "NIA": {
                        "label": "Niacin (B3)",
                        "quantity": 16.789618750000002,
                        "unit": "%"
                    },
                    "VITB6A": {
                        "label": "Vitamin B6",
                        "quantity": 52.19871153846153,
                        "unit": "%"
                    },
                    "FOLDFE": {
                        "label": "Folate equivalent (total)",
                        "quantity": 38.3309375,
                        "unit": "%"
                    },
                    "VITB12": {
                        "label": "Vitamin B12",
                        "quantity": 102.28083333333335,
                        "unit": "%"
                    },
                    "VITD": {
                        "label": "Vitamin D",
                        "quantity": 25.279999999999998,
                        "unit": "%"
                    },
                    "TOCPHA": {
                        "label": "Vitamin E",
                        "quantity": 33.84893333333333,
                        "unit": "%"
                    },
                    "VITK1": {
                        "label": "Vitamin K",
                        "quantity": 10.614833333333333,
                        "unit": "%"
                    }
                },
                "digest": [
                    {
                        "label": "Fat",
                        "tag": "FAT",
                        "schemaOrgTag": "fatContent",
                        "total": 90.342145,
                        "hasRDI": True,
                        "daily": 138.98791538461538,
                        "unit": "g",
                        "sub": [
                            {
                                "label": "Saturated",
                                "tag": "FASAT",
                                "schemaOrgTag": "saturatedFatContent",
                                "total": 42.3721325,
                                "hasRDI": True,
                                "daily": 211.8606625,
                                "unit": "g"
                            },
                            {
                                "label": "Trans",
                                "tag": "FATRN",
                                "schemaOrgTag": "transFatContent",
                                "total": 0.183976,
                                "hasRDI": False,
                                "daily": 0.0,
                                "unit": "g"
                            },
                            {
                                "label": "Monounsaturated",
                                "tag": "FAMS",
                                "schemaOrgTag": '',
                                "total": 29.050289250000002,
                                "hasRDI": False,
                                "daily": 0.0,
                                "unit": "g"
                            },
                            {
                                "label": "Polyunsaturated",
                                "tag": "FAPU",
                                "schemaOrgTag": '',
                                "total": 12.828958499999999,
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
                        "total": 78.63772,
                        "hasRDI": True,
                        "daily": 26.21257333333333,
                        "unit": "g",
                        "sub": [
                            {
                                "label": "Carbs (net)",
                                "tag": "CHOCDF.net",
                                "schemaOrgTag": '',
                                "total": 71.242645,
                                "hasRDI": False,
                                "daily": 0.0,
                                "unit": "g"
                            },
                            {
                                "label": "Fiber",
                                "tag": "FIBTG",
                                "schemaOrgTag": "fiberContent",
                                "total": 7.395075,
                                "hasRDI": True,
                                "daily": 29.5803,
                                "unit": "g"
                            },
                            {
                                "label": "Sugars",
                                "tag": "SUGAR",
                                "schemaOrgTag": "sugarContent",
                                "total": 4.8806,
                                "hasRDI": False,
                                "daily": 0.0,
                                "unit": "g"
                            },
                            {
                                "label": "Sugars, added",
                                "tag": "SUGAR.added",
                                "schemaOrgTag": '',
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
                        "total": 59.46958,
                        "hasRDI": True,
                        "daily": 118.93915999999999,
                        "unit": "g"
                    },
                    {
                        "label": "Cholesterol",
                        "tag": "CHOLE",
                        "schemaOrgTag": "cholesterolContent",
                        "total": 706.01,
                        "hasRDI": True,
                        "daily": 235.33666666666667,
                        "unit": "mg"
                    },
                    {
                        "label": "Sodium",
                        "tag": "NA",
                        "schemaOrgTag": "sodiumContent",
                        "total": 1741.209,
                        "hasRDI": True,
                        "daily": 72.550375,
                        "unit": "mg"
                    },
                    {
                        "label": "Calcium",
                        "tag": "CA",
                        "schemaOrgTag": '',
                        "total": 1204.07525,
                        "hasRDI": True,
                        "daily": 120.407525,
                        "unit": "mg"
                    },
                    {
                        "label": "Magnesium",
                        "tag": "MG",
                        "schemaOrgTag": '',
                        "total": 155.57125,
                        "hasRDI": True,
                        "daily": 37.04077380952381,
                        "unit": "mg"
                    },
                    {
                        "label": "Potassium",
                        "tag": "K",
                        "schemaOrgTag": '',
                        "total": 714.4235,
                        "hasRDI": True,
                        "daily": 15.200500000000002,
                        "unit": "mg"
                    },
                    {
                        "label": "Iron",
                        "tag": "FE",
                        "schemaOrgTag": '',
                        "total": 5.4859925,
                        "hasRDI": True,
                        "daily": 30.47773611111111,
                        "unit": "mg"
                    },
                    {
                        "label": "Zinc",
                        "tag": "ZN",
                        "schemaOrgTag": '',
                        "total": 7.7057025,
                        "hasRDI": True,
                        "daily": 70.05184090909091,
                        "unit": "mg"
                    },
                    {
                        "label": "Phosphorus",
                        "tag": "P",
                        "schemaOrgTag": '',
                        "total": 1163.9805000000001,
                        "hasRDI": True,
                        "daily": 166.28292857142858,
                        "unit": "mg"
                    },
                    {
                        "label": "Vitamin A",
                        "tag": "VITA_RAE",
                        "schemaOrgTag": '',
                        "total": 616.37125,
                        "hasRDI": True,
                        "daily": 68.48569444444445,
                        "unit": "µg"
                    },
                    {
                        "label": "Vitamin C",
                        "tag": "VITC",
                        "schemaOrgTag": '',
                        "total": 1.026,
                        "hasRDI": True,
                        "daily": 1.1400000000000001,
                        "unit": "mg"
                    },
                    {
                        "label": "Thiamin (B1)",
                        "tag": "THIA",
                        "schemaOrgTag": '',
                        "total": 0.286679,
                        "hasRDI": True,
                        "daily": 23.88991666666667,
                        "unit": "mg"
                    },
                    {
                        "label": "Riboflavin (B2)",
                        "tag": "RIBF",
                        "schemaOrgTag": '',
                        "total": 1.2898830000000001,
                        "hasRDI": True,
                        "daily": 99.22176923076924,
                        "unit": "mg"
                    },
                    {
                        "label": "Niacin (B3)",
                        "tag": "NIA",
                        "schemaOrgTag": '',
                        "total": 2.6863390000000003,
                        "hasRDI": True,
                        "daily": 16.789618750000002,
                        "unit": "mg"
                    },
                    {
                        "label": "Vitamin B6",
                        "tag": "VITB6A",
                        "schemaOrgTag": '',
                        "total": 0.67858325,
                        "hasRDI": True,
                        "daily": 52.19871153846153,
                        "unit": "mg"
                    },
                    {
                        "label": "Folate equivalent (total)",
                        "tag": "FOLDFE",
                        "schemaOrgTag": '',
                        "total": 153.32375,
                        "hasRDI": True,
                        "daily": 38.3309375,
                        "unit": "µg"
                    },
                    {
                        "label": "Folate (food)",
                        "tag": "FOLFD",
                        "schemaOrgTag": '',
                        "total": 133.51175,
                        "hasRDI": False,
                        "daily": 0.0,
                        "unit": "µg"
                    },
                    {
                        "label": "Folic acid",
                        "tag": "FOLAC",
                        "schemaOrgTag": '',
                        "total": 12.192,
                        "hasRDI": False,
                        "daily": 0.0,
                        "unit": "µg"
                    },
                    {
                        "label": "Vitamin B12",
                        "tag": "VITB12",
                        "schemaOrgTag": '',
                        "total": 2.45474,
                        "hasRDI": True,
                        "daily": 102.28083333333335,
                        "unit": "µg"
                    },
                    {
                        "label": "Vitamin D",
                        "tag": "VITD",
                        "schemaOrgTag": '',
                        "total": 3.792,
                        "hasRDI": True,
                        "daily": 25.279999999999998,
                        "unit": "µg"
                    },
                    {
                        "label": "Vitamin E",
                        "tag": "TOCPHA",
                        "schemaOrgTag": '',
                        "total": 5.0773399999999995,
                        "hasRDI": True,
                        "daily": 33.84893333333333,
                        "unit": "mg"
                    },
                    {
                        "label": "Vitamin K",
                        "tag": "VITK1",
                        "schemaOrgTag": '',
                        "total": 12.7378,
                        "hasRDI": True,
                        "daily": 10.614833333333333,
                        "unit": "µg"
                    },
                    {
                        "label": "Sugar alcohols",
                        "tag": "Sugar.alcohol",
                        "schemaOrgTag": '',
                        "total": 0.0,
                        "hasRDI": False,
                        "daily": 0.0,
                        "unit": "g"
                    },
                    {
                        "label": "Water",
                        "tag": "WATER",
                        "schemaOrgTag": '',
                        "total": 223.42947500000002,
                        "hasRDI": False,
                        "daily": 0.0,
                        "unit": "g"
                    }
                ]
            },
            "_links": {
                "self": {
                    "title": "Self",
                    "href": "https://api.edamam.com/api/recipes/v2/1c226c5925e580ede17ebfd448e3164a?type=public&app_id=e909afd5&app_key=34e59dda7e1bffb92e49c416e9449e1d"
                }
            }
        },
        {
            "recipe": {
                "uri": "http://www.edamam.com/ontologies/edamam.owl#recipe_d7092856ef9cff30acd0d4ccefa317c3",
                "label": "Chicken Tacos",
                "image": "https://edamam-product-images.s3.amazonaws.com/web-img/873/873b6a37603daa3f951cb563a340fd1f.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLWVhc3QtMSJIMEYCIQCP2Gbt%2ByPQIVKV%2FafgML7WXbkOusL9fCs6d1le6dFKYAIhAJcnuEh%2B1NzOso38QgGaVBwaVQAMxyMJATg%2FR%2Fl0jl96KsEFCJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMMTg3MDE3MTUwOTg2IgydADkJdybnmhdEGwQqlQUNCCJJEzulouVCRRPPDPN9Ik9nmgPZk%2Fam6u04CTug5FWfzto4W1y6mlAuXr3EHPB%2FvTcZ%2BmAkgcS5%2FRfKsviGgYg1PBDbKvJFWJigqXNb6jHaHO3eyZnXpof0Qk2PachTFyGGF7upzvEiKr6BGB6DtCoEGe3wCd0iFSMS%2Ft8LIlICGGYaaCvWq9TXeaXkel5jju8XxawzfW0OY8ad1NODjiJJ%2FJ02goRzRa3HwZdXj0P4%2FwwiBHg8BMnsBu5XvhNCt9Gz%2Bxp9cZIC8TMv%2FY8rOvepaH28zVl5BjLGle3tn5syTeLiH6OS68I4OndB2qqeqZqdi9cu6zb1H0y8aKh8r8IIaHqXhP6jBXwOxUN8uimNrMJnaDPxNdvFPuR5yx8UApiuserTd1b1ZIBFiBJ6lavYUBrkLW%2B7bZIJltsNTSxF2GTKFWoXHKGf3%2FXYj%2FniRUh%2BB3xUXrXh8PzVKChkdfuCxirnj5UG2XCrj22%2BBJG8S8UHiExHaIwt01Nel6V7Y0IlXWvwqK8YEx%2FHOI%2FewXERfrnIQDCsrQyC7qTLL3HndUW2Ke8ib2iC%2BPgaP6xDqkqdlhOSojQHG4rfwcyVOFOzeauzAO7Rc77mb0rCUJdMckP6nKiD7nrtjlZXznFmYhCvjmWQF2l06Jl7xQsr%2BjkGAeoXo9X%2FiC11ZTNfxOVIe3LWWkRvMwGWvgvtgF4ZEDGaLXgsbO4I8%2FpSmGD4ox9ZWDfX%2BtTURCyBYVXqYpQ4TpgMhHqAtTUr4TNc7GRLVbfi1xqZNQDt1Sfdzh3Xq88dOJyKsyUs7rcFuuxoNyxvqstWVaAyRglOH1n%2BpV0xA7%2FKEHa%2F8%2FzH6uaXeIp3eLJN1%2BGlAQc1sP2jehPHqGi5Lc7YMOKk8akGOrABqEMeyIMA72vRUvaZqcs7N77uX3kDw2%2BTfyF8pS8HYdR1%2BEU1ekEPGlPPLyTo0NFmbmMa4urw%2B19eIvlGSnFjiSeee%2F%2BeotdKLVnDgZ5aNxOYivkgUqjazWNTWX1qdv7Jq7GWrNDLwjZiU5zLvpcjSyzLyGAVIo8pW14m4aC3jppuzjKpasygGK2%2Bf%2BmxisMAkIdRRS5aXW9PY%2FuwiBnL3qiZT5RtAdamISZZM9jUAWY%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231028T003610Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFPXEGMX3T%2F20231028%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=b4a01118a88cb10731c1336b50cdc3b792746ed786ef620ced74567e285f59bd",
                "images": {
                    "THUMBNAIL": {
                        "url": "https://edamam-product-images.s3.amazonaws.com/web-img/873/873b6a37603daa3f951cb563a340fd1f-s.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLWVhc3QtMSJIMEYCIQCP2Gbt%2ByPQIVKV%2FafgML7WXbkOusL9fCs6d1le6dFKYAIhAJcnuEh%2B1NzOso38QgGaVBwaVQAMxyMJATg%2FR%2Fl0jl96KsEFCJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMMTg3MDE3MTUwOTg2IgydADkJdybnmhdEGwQqlQUNCCJJEzulouVCRRPPDPN9Ik9nmgPZk%2Fam6u04CTug5FWfzto4W1y6mlAuXr3EHPB%2FvTcZ%2BmAkgcS5%2FRfKsviGgYg1PBDbKvJFWJigqXNb6jHaHO3eyZnXpof0Qk2PachTFyGGF7upzvEiKr6BGB6DtCoEGe3wCd0iFSMS%2Ft8LIlICGGYaaCvWq9TXeaXkel5jju8XxawzfW0OY8ad1NODjiJJ%2FJ02goRzRa3HwZdXj0P4%2FwwiBHg8BMnsBu5XvhNCt9Gz%2Bxp9cZIC8TMv%2FY8rOvepaH28zVl5BjLGle3tn5syTeLiH6OS68I4OndB2qqeqZqdi9cu6zb1H0y8aKh8r8IIaHqXhP6jBXwOxUN8uimNrMJnaDPxNdvFPuR5yx8UApiuserTd1b1ZIBFiBJ6lavYUBrkLW%2B7bZIJltsNTSxF2GTKFWoXHKGf3%2FXYj%2FniRUh%2BB3xUXrXh8PzVKChkdfuCxirnj5UG2XCrj22%2BBJG8S8UHiExHaIwt01Nel6V7Y0IlXWvwqK8YEx%2FHOI%2FewXERfrnIQDCsrQyC7qTLL3HndUW2Ke8ib2iC%2BPgaP6xDqkqdlhOSojQHG4rfwcyVOFOzeauzAO7Rc77mb0rCUJdMckP6nKiD7nrtjlZXznFmYhCvjmWQF2l06Jl7xQsr%2BjkGAeoXo9X%2FiC11ZTNfxOVIe3LWWkRvMwGWvgvtgF4ZEDGaLXgsbO4I8%2FpSmGD4ox9ZWDfX%2BtTURCyBYVXqYpQ4TpgMhHqAtTUr4TNc7GRLVbfi1xqZNQDt1Sfdzh3Xq88dOJyKsyUs7rcFuuxoNyxvqstWVaAyRglOH1n%2BpV0xA7%2FKEHa%2F8%2FzH6uaXeIp3eLJN1%2BGlAQc1sP2jehPHqGi5Lc7YMOKk8akGOrABqEMeyIMA72vRUvaZqcs7N77uX3kDw2%2BTfyF8pS8HYdR1%2BEU1ekEPGlPPLyTo0NFmbmMa4urw%2B19eIvlGSnFjiSeee%2F%2BeotdKLVnDgZ5aNxOYivkgUqjazWNTWX1qdv7Jq7GWrNDLwjZiU5zLvpcjSyzLyGAVIo8pW14m4aC3jppuzjKpasygGK2%2Bf%2BmxisMAkIdRRS5aXW9PY%2FuwiBnL3qiZT5RtAdamISZZM9jUAWY%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231028T003610Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFPXEGMX3T%2F20231028%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=b0a61e417782e84b0064c12e46708c66d6926f713e5a869ab073ac54f56323b4",
                        "width": 100,
                        "height": 100
                    },
                    "SMALL": {
                        "url": "https://edamam-product-images.s3.amazonaws.com/web-img/873/873b6a37603daa3f951cb563a340fd1f-m.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLWVhc3QtMSJIMEYCIQCP2Gbt%2ByPQIVKV%2FafgML7WXbkOusL9fCs6d1le6dFKYAIhAJcnuEh%2B1NzOso38QgGaVBwaVQAMxyMJATg%2FR%2Fl0jl96KsEFCJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMMTg3MDE3MTUwOTg2IgydADkJdybnmhdEGwQqlQUNCCJJEzulouVCRRPPDPN9Ik9nmgPZk%2Fam6u04CTug5FWfzto4W1y6mlAuXr3EHPB%2FvTcZ%2BmAkgcS5%2FRfKsviGgYg1PBDbKvJFWJigqXNb6jHaHO3eyZnXpof0Qk2PachTFyGGF7upzvEiKr6BGB6DtCoEGe3wCd0iFSMS%2Ft8LIlICGGYaaCvWq9TXeaXkel5jju8XxawzfW0OY8ad1NODjiJJ%2FJ02goRzRa3HwZdXj0P4%2FwwiBHg8BMnsBu5XvhNCt9Gz%2Bxp9cZIC8TMv%2FY8rOvepaH28zVl5BjLGle3tn5syTeLiH6OS68I4OndB2qqeqZqdi9cu6zb1H0y8aKh8r8IIaHqXhP6jBXwOxUN8uimNrMJnaDPxNdvFPuR5yx8UApiuserTd1b1ZIBFiBJ6lavYUBrkLW%2B7bZIJltsNTSxF2GTKFWoXHKGf3%2FXYj%2FniRUh%2BB3xUXrXh8PzVKChkdfuCxirnj5UG2XCrj22%2BBJG8S8UHiExHaIwt01Nel6V7Y0IlXWvwqK8YEx%2FHOI%2FewXERfrnIQDCsrQyC7qTLL3HndUW2Ke8ib2iC%2BPgaP6xDqkqdlhOSojQHG4rfwcyVOFOzeauzAO7Rc77mb0rCUJdMckP6nKiD7nrtjlZXznFmYhCvjmWQF2l06Jl7xQsr%2BjkGAeoXo9X%2FiC11ZTNfxOVIe3LWWkRvMwGWvgvtgF4ZEDGaLXgsbO4I8%2FpSmGD4ox9ZWDfX%2BtTURCyBYVXqYpQ4TpgMhHqAtTUr4TNc7GRLVbfi1xqZNQDt1Sfdzh3Xq88dOJyKsyUs7rcFuuxoNyxvqstWVaAyRglOH1n%2BpV0xA7%2FKEHa%2F8%2FzH6uaXeIp3eLJN1%2BGlAQc1sP2jehPHqGi5Lc7YMOKk8akGOrABqEMeyIMA72vRUvaZqcs7N77uX3kDw2%2BTfyF8pS8HYdR1%2BEU1ekEPGlPPLyTo0NFmbmMa4urw%2B19eIvlGSnFjiSeee%2F%2BeotdKLVnDgZ5aNxOYivkgUqjazWNTWX1qdv7Jq7GWrNDLwjZiU5zLvpcjSyzLyGAVIo8pW14m4aC3jppuzjKpasygGK2%2Bf%2BmxisMAkIdRRS5aXW9PY%2FuwiBnL3qiZT5RtAdamISZZM9jUAWY%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231028T003610Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFPXEGMX3T%2F20231028%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=53b17692dbd9afac6feb082da34861d12f37fca000b1342a2ec508b612247a3f",
                        "width": 200,
                        "height": 200
                    },
                    "REGULAR": {
                        "url": "https://edamam-product-images.s3.amazonaws.com/web-img/873/873b6a37603daa3f951cb563a340fd1f.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLWVhc3QtMSJIMEYCIQCP2Gbt%2ByPQIVKV%2FafgML7WXbkOusL9fCs6d1le6dFKYAIhAJcnuEh%2B1NzOso38QgGaVBwaVQAMxyMJATg%2FR%2Fl0jl96KsEFCJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMMTg3MDE3MTUwOTg2IgydADkJdybnmhdEGwQqlQUNCCJJEzulouVCRRPPDPN9Ik9nmgPZk%2Fam6u04CTug5FWfzto4W1y6mlAuXr3EHPB%2FvTcZ%2BmAkgcS5%2FRfKsviGgYg1PBDbKvJFWJigqXNb6jHaHO3eyZnXpof0Qk2PachTFyGGF7upzvEiKr6BGB6DtCoEGe3wCd0iFSMS%2Ft8LIlICGGYaaCvWq9TXeaXkel5jju8XxawzfW0OY8ad1NODjiJJ%2FJ02goRzRa3HwZdXj0P4%2FwwiBHg8BMnsBu5XvhNCt9Gz%2Bxp9cZIC8TMv%2FY8rOvepaH28zVl5BjLGle3tn5syTeLiH6OS68I4OndB2qqeqZqdi9cu6zb1H0y8aKh8r8IIaHqXhP6jBXwOxUN8uimNrMJnaDPxNdvFPuR5yx8UApiuserTd1b1ZIBFiBJ6lavYUBrkLW%2B7bZIJltsNTSxF2GTKFWoXHKGf3%2FXYj%2FniRUh%2BB3xUXrXh8PzVKChkdfuCxirnj5UG2XCrj22%2BBJG8S8UHiExHaIwt01Nel6V7Y0IlXWvwqK8YEx%2FHOI%2FewXERfrnIQDCsrQyC7qTLL3HndUW2Ke8ib2iC%2BPgaP6xDqkqdlhOSojQHG4rfwcyVOFOzeauzAO7Rc77mb0rCUJdMckP6nKiD7nrtjlZXznFmYhCvjmWQF2l06Jl7xQsr%2BjkGAeoXo9X%2FiC11ZTNfxOVIe3LWWkRvMwGWvgvtgF4ZEDGaLXgsbO4I8%2FpSmGD4ox9ZWDfX%2BtTURCyBYVXqYpQ4TpgMhHqAtTUr4TNc7GRLVbfi1xqZNQDt1Sfdzh3Xq88dOJyKsyUs7rcFuuxoNyxvqstWVaAyRglOH1n%2BpV0xA7%2FKEHa%2F8%2FzH6uaXeIp3eLJN1%2BGlAQc1sP2jehPHqGi5Lc7YMOKk8akGOrABqEMeyIMA72vRUvaZqcs7N77uX3kDw2%2BTfyF8pS8HYdR1%2BEU1ekEPGlPPLyTo0NFmbmMa4urw%2B19eIvlGSnFjiSeee%2F%2BeotdKLVnDgZ5aNxOYivkgUqjazWNTWX1qdv7Jq7GWrNDLwjZiU5zLvpcjSyzLyGAVIo8pW14m4aC3jppuzjKpasygGK2%2Bf%2BmxisMAkIdRRS5aXW9PY%2FuwiBnL3qiZT5RtAdamISZZM9jUAWY%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231028T003610Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFPXEGMX3T%2F20231028%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=b4a01118a88cb10731c1336b50cdc3b792746ed786ef620ced74567e285f59bd",
                        "width": 300,
                        "height": 300
                    }
                },
                "source": "Cookstr",
                "url": "http://www.cookstr.com/recipes/chicken-tacos-diana-kennedy",
                "shareAs": "http://www.edamam.com/recipe/chicken-tacos-d7092856ef9cff30acd0d4ccefa317c3/tacos",
                "yield": 12.0,
                "dietLabels": [
                    "Low-Carb"
                ],
                "healthLabels": [
                    "Sugar-Conscious",
                    "Egg-Free",
                    "Peanut-Free",
                    "Tree-Nut-Free",
                    "Soy-Free",
                    "Fish-Free",
                    "Shellfish-Free",
                    "Pork-Free",
                    "Red-Meat-Free",
                    "Crustacean-Free",
                    "Celery-Free",
                    "Mustard-Free",
                    "Sesame-Free",
                    "Lupine-Free",
                    "Mollusk-Free",
                    "Alcohol-Free",
                    "Sulfite-Free"
                ],
                "cautions": [
                    "Eggs",
                    "Milk",
                    "Sulfites"
                ],
                "ingredientLines": [
                    "3 tablespoons chicken fat or oil",
                    "½ cup (125 ml) finely chopped white onion",
                    "3 fresh chiles jalapenos, cut into thin strips with seeds and veins",
                    "1½ cups (375 ml) finely chopped, unpeeled tomatoes",
                    "1½ cups (375 ml) poached chicken for tacos",
                    "3 tablespoons chicken broth",
                    "Sea salt to taste",
                    "12 5-inch (12.5 cm) corn tortillas",
                    "Safflower oil for frying",
                    "1 cup (250 ml) Cooked Tomato Sauce, Sierra de Puebla and Micboacan",
                    "2 cups (500 ml) finely shredded lettuce or cabbage",
                    "¾ cup (190 ml) crème fraïche",
                    "6 tablespoons finely grated queso fresco or añejo"
                ],
                "ingredients": [
                    {
                        "text": "3 tablespoons chicken fat or oil",
                        "quantity": 3.0,
                        "measure": "tablespoon",
                        "food": "chicken fat",
                        "weight": 38.400000000000006,
                        "foodCategory": "Oils",
                        "foodId": "food_b5h84enb8kpx1jawb5qbfaqktajo",
                        "image": ''
                    },
                    {
                        "text": "½ cup (125 ml) finely chopped white onion",
                        "quantity": 125.0,
                        "measure": "milliliter",
                        "food": "white onion",
                        "weight": 84.5350567546075,
                        "foodCategory": "vegetables",
                        "foodId": "food_bmrvi4ob4binw9a5m7l07amlfcoy",
                        "image": "https://www.edamam.com/food-img/205/205e6bf2399b85d34741892ef91cc603.jpg"
                    },
                    {
                        "text": "3 fresh chiles jalapenos, cut into thin strips with seeds and veins",
                        "quantity": 3.0,
                        "measure": "chile",
                        "food": "jalapenos",
                        "weight": 42.0,
                        "foodCategory": "vegetables",
                        "foodId": "food_b7txsnbadj6plsbq27zvwah80r6y",
                        "image": "https://www.edamam.com/food-img/0df/0df9aa459870a6d477b0925c1fdb6d4c.jpg"
                    },
                    {
                        "text": "1½ cups (375 ml) finely chopped, unpeeled tomatoes",
                        "quantity": 375.0,
                        "measure": "milliliter",
                        "food": "tomatoes",
                        "weight": 236.16981480818467,
                        "foodCategory": "vegetables",
                        "foodId": "food_a6k79rrahp8fe2b26zussa3wtkqh",
                        "image": "https://www.edamam.com/food-img/23e/23e727a14f1035bdc2733bb0477efbd2.jpg"
                    },
                    {
                        "text": "1½ cups (375 ml) poached chicken for tacos",
                        "quantity": 375.0,
                        "measure": "milliliter",
                        "food": "chicken",
                        "weight": 221.9045239808447,
                        "foodCategory": "Poultry",
                        "foodId": "food_bmyxrshbfao9s1amjrvhoauob6mo",
                        "image": "https://www.edamam.com/food-img/d33/d338229d774a743f7858f6764e095878.jpg"
                    },
                    {
                        "text": "3 tablespoons chicken broth",
                        "quantity": 3.0,
                        "measure": "tablespoon",
                        "food": "chicken broth",
                        "weight": 44.99999999923919,
                        "foodCategory": "canned soup",
                        "foodId": "food_bptblvzambd16nbhewqmhaw1rnh5",
                        "image": "https://www.edamam.com/food-img/26a/26a10c4cb4e07bab54d8a687ef5ac7d8.jpg"
                    },
                    {
                        "text": "Sea salt to taste",
                        "quantity": 0.0,
                        "measure": '',
                        "food": "Sea salt",
                        "weight": 9.340645863986868,
                        "foodCategory": "Condiments and sauces",
                        "foodId": "food_a1vgrj1bs8rd1majvmd9ubz8ttkg",
                        "image": "https://www.edamam.com/food-img/694/6943ea510918c6025795e8dc6e6eaaeb.jpg"
                    },
                    {
                        "text": "12 5-inch (12.5 cm) corn tortillas",
                        "quantity": 12.0,
                        "measure": "<unit>",
                        "food": "corn tortillas",
                        "weight": 288.0,
                        "foodCategory": "quick breads and pastries",
                        "foodId": "food_bhw0b95agm97s0abfignnb8fsvb3",
                        "image": "https://www.edamam.com/food-img/b8a/b8ad23dcc06f2324f944e47eb579d644.jpg"
                    },
                    {
                        "text": "Safflower oil for frying",
                        "quantity": 0.0,
                        "measure": '',
                        "food": "Safflower oil",
                        "weight": 21.1721306250369,
                        "foodCategory": "Oils",
                        "foodId": "food_ajpf19fbv3tjgiaa2004cbv6f69t",
                        "image": "https://www.edamam.com/food-img/083/083c7a39cbe5ae179d2bf46e2216923d.jpg"
                    },
                    {
                        "text": "1 cup (250 ml) Cooked Tomato Sauce, Sierra de Puebla and Micboacan",
                        "quantity": 250.0,
                        "measure": "milliliter",
                        "food": "Tomato Sauce",
                        "weight": 258.8886113109854,
                        "foodCategory": "canned vegetables",
                        "foodId": "food_altklniaqmdz3eb1rlf1ybjv8ihn",
                        "image": ''
                    },
                    {
                        "text": "2 cups (500 ml) finely shredded lettuce or cabbage",
                        "quantity": 500.0,
                        "measure": "milliliter",
                        "food": "lettuce",
                        "weight": 116.23570303758531,
                        "foodCategory": "vegetables",
                        "foodId": "food_bf5fxtkbc9alwoajuvsi7amonr5w",
                        "image": "https://www.edamam.com/food-img/719/71996625d0cb47e197093ecd52c97dc2.jpg"
                    },
                    {
                        "text": "¾ cup (190 ml) crème fraïche",
                        "quantity": 190.0,
                        "measure": "milliliter",
                        "food": "crème fraïche",
                        "weight": 179.89060077380475,
                        "foodCategory": "Dairy",
                        "foodId": "food_ayjzu0oak0shbnaeroxs8b6t9uyy",
                        "image": "https://www.edamam.com/food-img/f9d/f9d6183267b041b0aff9a10b89c9c15f.jpg"
                    },
                    {
                        "text": "6 tablespoons finely grated queso fresco or añejo",
                        "quantity": 6.0,
                        "measure": "tablespoon",
                        "food": "queso fresco",
                        "weight": 45.7499999992265,
                        "foodCategory": "Cheese",
                        "foodId": "food_bfs6bdja03x1ambpc63a6av2y3ti",
                        "image": "https://www.edamam.com/food-img/050/050fcbd0a8b96e20d1725cf55c31413f.jpg"
                    }
                ],
                "calories": 4091.5391459229554,
                "totalCO2Emissions": 10175.522567153565,
                "co2EmissionsClass": "E",
                "totalWeight": 1784.695537833899,
                "totalTime": 60.0,
                "cuisineType": [
                    "mexican"
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
                        "quantity": 4091.539145922956,
                        "unit": "kcal"
                    },
                    "FAT": {
                        "label": "Fat",
                        "quantity": 350.51796221740295,
                        "unit": "g"
                    },
                    "FASAT": {
                        "label": "Saturated",
                        "quantity": 60.59644971384989,
                        "unit": "g"
                    },
                    "FATRN": {
                        "label": "Trans",
                        "quantity": 2.028731570414454,
                        "unit": "g"
                    },
                    "FAMS": {
                        "label": "Monounsaturated",
                        "quantity": 76.50357986420461,
                        "unit": "g"
                    },
                    "FAPU": {
                        "label": "Polyunsaturated",
                        "quantity": 187.94800246456123,
                        "unit": "g"
                    },
                    "CHOCDF": {
                        "label": "Carbs",
                        "quantity": 175.88040635104744,
                        "unit": "g"
                    },
                    "CHOCDF.net": {
                        "label": "Carbohydrates (net)",
                        "quantity": 147.12735070544267,
                        "unit": "g"
                    },
                    "FIBTG": {
                        "label": "Fiber",
                        "quantity": 28.75305564560476,
                        "unit": "g"
                    },
                    "SUGAR": {
                        "label": "Sugars",
                        "quantity": 32.27607219343178,
                        "unit": "g"
                    },
                    "PROCNT": {
                        "label": "Protein",
                        "quantity": 79.5605474405107,
                        "unit": "g"
                    },
                    "CHOLE": {
                        "label": "Cholesterol",
                        "quantity": 338.12134744162177,
                        "unit": "mg"
                    },
                    "NA": {
                        "label": "Sodium",
                        "quantity": 4137.451120530468,
                        "unit": "mg"
                    },
                    "CA": {
                        "label": "Calcium",
                        "quantity": 826.0243066817147,
                        "unit": "mg"
                    },
                    "MG": {
                        "label": "Magnesium",
                        "quantity": 377.2412231061287,
                        "unit": "mg"
                    },
                    "K": {
                        "label": "Potassium",
                        "quantity": 3119.495212764664,
                        "unit": "mg"
                    },
                    "FE": {
                        "label": "Iron",
                        "quantity": 10.716495787961536,
                        "unit": "mg"
                    },
                    "ZN": {
                        "label": "Zinc",
                        "quantity": 9.928276862987722,
                        "unit": "mg"
                    },
                    "P": {
                        "label": "Phosphorus",
                        "quantity": 1755.8976359059197,
                        "unit": "mg"
                    },
                    "VITA_RAE": {
                        "label": "Vitamin A",
                        "quantity": 788.7532835401701,
                        "unit": "µg"
                    },
                    "VITC": {
                        "label": "Vitamin C",
                        "quantity": 116.27327042337814,
                        "unit": "mg"
                    },
                    "THIA": {
                        "label": "Thiamin (B1)",
                        "quantity": 0.7462624095748845,
                        "unit": "mg"
                    },
                    "RIBF": {
                        "label": "Riboflavin (B2)",
                        "quantity": 1.2105396014477634,
                        "unit": "mg"
                    },
                    "NIA": {
                        "label": "Niacin (B3)",
                        "quantity": 25.319215353136855,
                        "unit": "mg"
                    },
                    "VITB6A": {
                        "label": "Vitamin B6",
                        "quantity": 2.3587430157768265,
                        "unit": "mg"
                    },
                    "FOLDFE": {
                        "label": "Folate equivalent (total)",
                        "quantity": 214.93937872521587,
                        "unit": "µg"
                    },
                    "FOLFD": {
                        "label": "Folate (food)",
                        "quantity": 214.93937872521587,
                        "unit": "µg"
                    },
                    "FOLAC": {
                        "label": "Folic acid",
                        "quantity": 0.0,
                        "unit": "µg"
                    },
                    "VITB12": {
                        "label": "Vitamin B12",
                        "quantity": 1.8342742859526138,
                        "unit": "µg"
                    },
                    "VITD": {
                        "label": "Vitamin D",
                        "quantity": 3.522259047940805,
                        "unit": "µg"
                    },
                    "TOCPHA": {
                        "label": "Vitamin E",
                        "quantity": 85.94918716101077,
                        "unit": "mg"
                    },
                    "VITK1": {
                        "label": "Vitamin K",
                        "quantity": 174.94019497025636,
                        "unit": "µg"
                    },
                    "WATER": {
                        "label": "Water",
                        "quantity": 1159.744187752241,
                        "unit": "g"
                    }
                },
                "totalDaily": {
                    "ENERC_KCAL": {
                        "label": "Energy",
                        "quantity": 204.5769572961478,
                        "unit": "%"
                    },
                    "FAT": {
                        "label": "Fat",
                        "quantity": 539.2584034113892,
                        "unit": "%"
                    },
                    "FASAT": {
                        "label": "Saturated",
                        "quantity": 302.98224856924946,
                        "unit": "%"
                    },
                    "CHOCDF": {
                        "label": "Carbs",
                        "quantity": 58.62680211701581,
                        "unit": "%"
                    },
                    "FIBTG": {
                        "label": "Fiber",
                        "quantity": 115.01222258241904,
                        "unit": "%"
                    },
                    "PROCNT": {
                        "label": "Protein",
                        "quantity": 159.1210948810214,
                        "unit": "%"
                    },
                    "CHOLE": {
                        "label": "Cholesterol",
                        "quantity": 112.70711581387393,
                        "unit": "%"
                    },
                    "NA": {
                        "label": "Sodium",
                        "quantity": 172.3937966887695,
                        "unit": "%"
                    },
                    "CA": {
                        "label": "Calcium",
                        "quantity": 82.60243066817146,
                        "unit": "%"
                    },
                    "MG": {
                        "label": "Magnesium",
                        "quantity": 89.81933883479255,
                        "unit": "%"
                    },
                    "K": {
                        "label": "Potassium",
                        "quantity": 66.37223856946093,
                        "unit": "%"
                    },
                    "FE": {
                        "label": "Iron",
                        "quantity": 59.53608771089743,
                        "unit": "%"
                    },
                    "ZN": {
                        "label": "Zinc",
                        "quantity": 90.25706239079749,
                        "unit": "%"
                    },
                    "P": {
                        "label": "Phosphorus",
                        "quantity": 250.84251941513136,
                        "unit": "%"
                    },
                    "VITA_RAE": {
                        "label": "Vitamin A",
                        "quantity": 87.63925372668557,
                        "unit": "%"
                    },
                    "VITC": {
                        "label": "Vitamin C",
                        "quantity": 129.19252269264237,
                        "unit": "%"
                    },
                    "THIA": {
                        "label": "Thiamin (B1)",
                        "quantity": 62.188534131240374,
                        "unit": "%"
                    },
                    "RIBF": {
                        "label": "Riboflavin (B2)",
                        "quantity": 93.11843088059719,
                        "unit": "%"
                    },
                    "NIA": {
                        "label": "Niacin (B3)",
                        "quantity": 158.24509595710535,
                        "unit": "%"
                    },
                    "VITB6A": {
                        "label": "Vitamin B6",
                        "quantity": 181.44177044437126,
                        "unit": "%"
                    },
                    "FOLDFE": {
                        "label": "Folate equivalent (total)",
                        "quantity": 53.73484468130397,
                        "unit": "%"
                    },
                    "VITB12": {
                        "label": "Vitamin B12",
                        "quantity": 76.42809524802557,
                        "unit": "%"
                    },
                    "VITD": {
                        "label": "Vitamin D",
                        "quantity": 23.481726986272033,
                        "unit": "%"
                    },
                    "TOCPHA": {
                        "label": "Vitamin E",
                        "quantity": 572.9945810734051,
                        "unit": "%"
                    },
                    "VITK1": {
                        "label": "Vitamin K",
                        "quantity": 145.78349580854695,
                        "unit": "%"
                    }
                },
                "digest": [
                    {
                        "label": "Fat",
                        "tag": "FAT",
                        "schemaOrgTag": "fatContent",
                        "total": 350.51796221740295,
                        "hasRDI": True,
                        "daily": 539.2584034113892,
                        "unit": "g",
                        "sub": [
                            {
                                "label": "Saturated",
                                "tag": "FASAT",
                                "schemaOrgTag": "saturatedFatContent",
                                "total": 60.59644971384989,
                                "hasRDI": True,
                                "daily": 302.98224856924946,
                                "unit": "g"
                            },
                            {
                                "label": "Trans",
                                "tag": "FATRN",
                                "schemaOrgTag": "transFatContent",
                                "total": 2.028731570414454,
                                "hasRDI": False,
                                "daily": 0.0,
                                "unit": "g"
                            },
                            {
                                "label": "Monounsaturated",
                                "tag": "FAMS",
                                "schemaOrgTag": '',
                                "total": 76.50357986420461,
                                "hasRDI": False,
                                "daily": 0.0,
                                "unit": "g"
                            },
                            {
                                "label": "Polyunsaturated",
                                "tag": "FAPU",
                                "schemaOrgTag": '',
                                "total": 187.94800246456123,
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
                        "total": 175.88040635104744,
                        "hasRDI": True,
                        "daily": 58.62680211701581,
                        "unit": "g",
                        "sub": [
                            {
                                "label": "Carbs (net)",
                                "tag": "CHOCDF.net",
                                "schemaOrgTag": '',
                                "total": 147.12735070544267,
                                "hasRDI": False,
                                "daily": 0.0,
                                "unit": "g"
                            },
                            {
                                "label": "Fiber",
                                "tag": "FIBTG",
                                "schemaOrgTag": "fiberContent",
                                "total": 28.75305564560476,
                                "hasRDI": True,
                                "daily": 115.01222258241904,
                                "unit": "g"
                            },
                            {
                                "label": "Sugars",
                                "tag": "SUGAR",
                                "schemaOrgTag": "sugarContent",
                                "total": 32.27607219343178,
                                "hasRDI": False,
                                "daily": 0.0,
                                "unit": "g"
                            },
                            {
                                "label": "Sugars, added",
                                "tag": "SUGAR.added",
                                "schemaOrgTag": '',
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
                        "total": 79.5605474405107,
                        "hasRDI": True,
                        "daily": 159.1210948810214,
                        "unit": "g"
                    },
                    {
                        "label": "Cholesterol",
                        "tag": "CHOLE",
                        "schemaOrgTag": "cholesterolContent",
                        "total": 338.12134744162177,
                        "hasRDI": True,
                        "daily": 112.70711581387393,
                        "unit": "mg"
                    },
                    {
                        "label": "Sodium",
                        "tag": "NA",
                        "schemaOrgTag": "sodiumContent",
                        "total": 4137.451120530468,
                        "hasRDI": True,
                        "daily": 172.3937966887695,
                        "unit": "mg"
                    },
                    {
                        "label": "Calcium",
                        "tag": "CA",
                        "schemaOrgTag": '',
                        "total": 826.0243066817147,
                        "hasRDI": True,
                        "daily": 82.60243066817146,
                        "unit": "mg"
                    },
                    {
                        "label": "Magnesium",
                        "tag": "MG",
                        "schemaOrgTag": '',
                        "total": 377.2412231061287,
                        "hasRDI": True,
                        "daily": 89.81933883479255,
                        "unit": "mg"
                    },
                    {
                        "label": "Potassium",
                        "tag": "K",
                        "schemaOrgTag": '',
                        "total": 3119.495212764664,
                        "hasRDI": True,
                        "daily": 66.37223856946093,
                        "unit": "mg"
                    },
                    {
                        "label": "Iron",
                        "tag": "FE",
                        "schemaOrgTag": '',
                        "total": 10.716495787961536,
                        "hasRDI": True,
                        "daily": 59.53608771089743,
                        "unit": "mg"
                    },
                    {
                        "label": "Zinc",
                        "tag": "ZN",
                        "schemaOrgTag": '',
                        "total": 9.928276862987722,
                        "hasRDI": True,
                        "daily": 90.25706239079749,
                        "unit": "mg"
                    },
                    {
                        "label": "Phosphorus",
                        "tag": "P",
                        "schemaOrgTag": '',
                        "total": 1755.8976359059197,
                        "hasRDI": True,
                        "daily": 250.84251941513136,
                        "unit": "mg"
                    },
                    {
                        "label": "Vitamin A",
                        "tag": "VITA_RAE",
                        "schemaOrgTag": '',
                        "total": 788.7532835401701,
                        "hasRDI": True,
                        "daily": 87.63925372668557,
                        "unit": "µg"
                    },
                    {
                        "label": "Vitamin C",
                        "tag": "VITC",
                        "schemaOrgTag": '',
                        "total": 116.27327042337814,
                        "hasRDI": True,
                        "daily": 129.19252269264237,
                        "unit": "mg"
                    },
                    {
                        "label": "Thiamin (B1)",
                        "tag": "THIA",
                        "schemaOrgTag": '',
                        "total": 0.7462624095748845,
                        "hasRDI": True,
                        "daily": 62.188534131240374,
                        "unit": "mg"
                    },
                    {
                        "label": "Riboflavin (B2)",
                        "tag": "RIBF",
                        "schemaOrgTag": '',
                        "total": 1.2105396014477634,
                        "hasRDI": True,
                        "daily": 93.11843088059719,
                        "unit": "mg"
                    },
                    {
                        "label": "Niacin (B3)",
                        "tag": "NIA",
                        "schemaOrgTag": '',
                        "total": 25.319215353136855,
                        "hasRDI": True,
                        "daily": 158.24509595710535,
                        "unit": "mg"
                    },
                    {
                        "label": "Vitamin B6",
                        "tag": "VITB6A",
                        "schemaOrgTag": '',
                        "total": 2.3587430157768265,
                        "hasRDI": True,
                        "daily": 181.44177044437126,
                        "unit": "mg"
                    },
                    {
                        "label": "Folate equivalent (total)",
                        "tag": "FOLDFE",
                        "schemaOrgTag": '',
                        "total": 214.93937872521587,
                        "hasRDI": True,
                        "daily": 53.73484468130397,
                        "unit": "µg"
                    },
                    {
                        "label": "Folate (food)",
                        "tag": "FOLFD",
                        "schemaOrgTag": '',
                        "total": 214.93937872521587,
                        "hasRDI": False,
                        "daily": 0.0,
                        "unit": "µg"
                    },
                    {
                        "label": "Folic acid",
                        "tag": "FOLAC",
                        "schemaOrgTag": '',
                        "total": 0.0,
                        "hasRDI": False,
                        "daily": 0.0,
                        "unit": "µg"
                    },
                    {
                        "label": "Vitamin B12",
                        "tag": "VITB12",
                        "schemaOrgTag": '',
                        "total": 1.8342742859526138,
                        "hasRDI": True,
                        "daily": 76.42809524802557,
                        "unit": "µg"
                    },
                    {
                        "label": "Vitamin D",
                        "tag": "VITD",
                        "schemaOrgTag": '',
                        "total": 3.522259047940805,
                        "hasRDI": True,
                        "daily": 23.481726986272033,
                        "unit": "µg"
                    },
                    {
                        "label": "Vitamin E",
                        "tag": "TOCPHA",
                        "schemaOrgTag": '',
                        "total": 85.94918716101077,
                        "hasRDI": True,
                        "daily": 572.9945810734051,
                        "unit": "mg"
                    },
                    {
                        "label": "Vitamin K",
                        "tag": "VITK1",
                        "schemaOrgTag": '',
                        "total": 174.94019497025636,
                        "hasRDI": True,
                        "daily": 145.78349580854695,
                        "unit": "µg"
                    },
                    {
                        "label": "Sugar alcohols",
                        "tag": "Sugar.alcohol",
                        "schemaOrgTag": '',
                        "total": 0.0,
                        "hasRDI": False,
                        "daily": 0.0,
                        "unit": "g"
                    },
                    {
                        "label": "Water",
                        "tag": "WATER",
                        "schemaOrgTag": '',
                        "total": 1159.744187752241,
                        "hasRDI": False,
                        "daily": 0.0,
                        "unit": "g"
                    }
                ]
            },
            "_links": {
                "self": {
                    "title": "Self",
                    "href": "https://api.edamam.com/api/recipes/v2/d7092856ef9cff30acd0d4ccefa317c3?type=public&app_id=e909afd5&app_key=34e59dda7e1bffb92e49c416e9449e1d"
                }
            }
        },
        {
            "recipe": {
                "uri": "http://www.edamam.com/ontologies/edamam.owl#recipe_92e98a8664c5d7aa2a3fcd4a5369adec",
                "label": "Salad Tacos",
                "image": "https://edamam-product-images.s3.amazonaws.com/web-img/453/453b12b11b3fa1832288c818d5b754df.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLWVhc3QtMSJIMEYCIQCP2Gbt%2ByPQIVKV%2FafgML7WXbkOusL9fCs6d1le6dFKYAIhAJcnuEh%2B1NzOso38QgGaVBwaVQAMxyMJATg%2FR%2Fl0jl96KsEFCJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMMTg3MDE3MTUwOTg2IgydADkJdybnmhdEGwQqlQUNCCJJEzulouVCRRPPDPN9Ik9nmgPZk%2Fam6u04CTug5FWfzto4W1y6mlAuXr3EHPB%2FvTcZ%2BmAkgcS5%2FRfKsviGgYg1PBDbKvJFWJigqXNb6jHaHO3eyZnXpof0Qk2PachTFyGGF7upzvEiKr6BGB6DtCoEGe3wCd0iFSMS%2Ft8LIlICGGYaaCvWq9TXeaXkel5jju8XxawzfW0OY8ad1NODjiJJ%2FJ02goRzRa3HwZdXj0P4%2FwwiBHg8BMnsBu5XvhNCt9Gz%2Bxp9cZIC8TMv%2FY8rOvepaH28zVl5BjLGle3tn5syTeLiH6OS68I4OndB2qqeqZqdi9cu6zb1H0y8aKh8r8IIaHqXhP6jBXwOxUN8uimNrMJnaDPxNdvFPuR5yx8UApiuserTd1b1ZIBFiBJ6lavYUBrkLW%2B7bZIJltsNTSxF2GTKFWoXHKGf3%2FXYj%2FniRUh%2BB3xUXrXh8PzVKChkdfuCxirnj5UG2XCrj22%2BBJG8S8UHiExHaIwt01Nel6V7Y0IlXWvwqK8YEx%2FHOI%2FewXERfrnIQDCsrQyC7qTLL3HndUW2Ke8ib2iC%2BPgaP6xDqkqdlhOSojQHG4rfwcyVOFOzeauzAO7Rc77mb0rCUJdMckP6nKiD7nrtjlZXznFmYhCvjmWQF2l06Jl7xQsr%2BjkGAeoXo9X%2FiC11ZTNfxOVIe3LWWkRvMwGWvgvtgF4ZEDGaLXgsbO4I8%2FpSmGD4ox9ZWDfX%2BtTURCyBYVXqYpQ4TpgMhHqAtTUr4TNc7GRLVbfi1xqZNQDt1Sfdzh3Xq88dOJyKsyUs7rcFuuxoNyxvqstWVaAyRglOH1n%2BpV0xA7%2FKEHa%2F8%2FzH6uaXeIp3eLJN1%2BGlAQc1sP2jehPHqGi5Lc7YMOKk8akGOrABqEMeyIMA72vRUvaZqcs7N77uX3kDw2%2BTfyF8pS8HYdR1%2BEU1ekEPGlPPLyTo0NFmbmMa4urw%2B19eIvlGSnFjiSeee%2F%2BeotdKLVnDgZ5aNxOYivkgUqjazWNTWX1qdv7Jq7GWrNDLwjZiU5zLvpcjSyzLyGAVIo8pW14m4aC3jppuzjKpasygGK2%2Bf%2BmxisMAkIdRRS5aXW9PY%2FuwiBnL3qiZT5RtAdamISZZM9jUAWY%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231028T003610Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFPXEGMX3T%2F20231028%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=b56e1105ab54f75fedcd9943668a5aec5480cac4bd9a2b3d1e482cc87882b5be",
                "images": {
                    "THUMBNAIL": {
                        "url": "https://edamam-product-images.s3.amazonaws.com/web-img/453/453b12b11b3fa1832288c818d5b754df-s.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLWVhc3QtMSJIMEYCIQCP2Gbt%2ByPQIVKV%2FafgML7WXbkOusL9fCs6d1le6dFKYAIhAJcnuEh%2B1NzOso38QgGaVBwaVQAMxyMJATg%2FR%2Fl0jl96KsEFCJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMMTg3MDE3MTUwOTg2IgydADkJdybnmhdEGwQqlQUNCCJJEzulouVCRRPPDPN9Ik9nmgPZk%2Fam6u04CTug5FWfzto4W1y6mlAuXr3EHPB%2FvTcZ%2BmAkgcS5%2FRfKsviGgYg1PBDbKvJFWJigqXNb6jHaHO3eyZnXpof0Qk2PachTFyGGF7upzvEiKr6BGB6DtCoEGe3wCd0iFSMS%2Ft8LIlICGGYaaCvWq9TXeaXkel5jju8XxawzfW0OY8ad1NODjiJJ%2FJ02goRzRa3HwZdXj0P4%2FwwiBHg8BMnsBu5XvhNCt9Gz%2Bxp9cZIC8TMv%2FY8rOvepaH28zVl5BjLGle3tn5syTeLiH6OS68I4OndB2qqeqZqdi9cu6zb1H0y8aKh8r8IIaHqXhP6jBXwOxUN8uimNrMJnaDPxNdvFPuR5yx8UApiuserTd1b1ZIBFiBJ6lavYUBrkLW%2B7bZIJltsNTSxF2GTKFWoXHKGf3%2FXYj%2FniRUh%2BB3xUXrXh8PzVKChkdfuCxirnj5UG2XCrj22%2BBJG8S8UHiExHaIwt01Nel6V7Y0IlXWvwqK8YEx%2FHOI%2FewXERfrnIQDCsrQyC7qTLL3HndUW2Ke8ib2iC%2BPgaP6xDqkqdlhOSojQHG4rfwcyVOFOzeauzAO7Rc77mb0rCUJdMckP6nKiD7nrtjlZXznFmYhCvjmWQF2l06Jl7xQsr%2BjkGAeoXo9X%2FiC11ZTNfxOVIe3LWWkRvMwGWvgvtgF4ZEDGaLXgsbO4I8%2FpSmGD4ox9ZWDfX%2BtTURCyBYVXqYpQ4TpgMhHqAtTUr4TNc7GRLVbfi1xqZNQDt1Sfdzh3Xq88dOJyKsyUs7rcFuuxoNyxvqstWVaAyRglOH1n%2BpV0xA7%2FKEHa%2F8%2FzH6uaXeIp3eLJN1%2BGlAQc1sP2jehPHqGi5Lc7YMOKk8akGOrABqEMeyIMA72vRUvaZqcs7N77uX3kDw2%2BTfyF8pS8HYdR1%2BEU1ekEPGlPPLyTo0NFmbmMa4urw%2B19eIvlGSnFjiSeee%2F%2BeotdKLVnDgZ5aNxOYivkgUqjazWNTWX1qdv7Jq7GWrNDLwjZiU5zLvpcjSyzLyGAVIo8pW14m4aC3jppuzjKpasygGK2%2Bf%2BmxisMAkIdRRS5aXW9PY%2FuwiBnL3qiZT5RtAdamISZZM9jUAWY%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231028T003610Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFPXEGMX3T%2F20231028%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=fcbfdefcce005c3fa4af97917ce7747652fddc37ea350a4568fac55699e70531",
                        "width": 100,
                        "height": 100
                    },
                    "SMALL": {
                        "url": "https://edamam-product-images.s3.amazonaws.com/web-img/453/453b12b11b3fa1832288c818d5b754df-m.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLWVhc3QtMSJIMEYCIQCP2Gbt%2ByPQIVKV%2FafgML7WXbkOusL9fCs6d1le6dFKYAIhAJcnuEh%2B1NzOso38QgGaVBwaVQAMxyMJATg%2FR%2Fl0jl96KsEFCJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMMTg3MDE3MTUwOTg2IgydADkJdybnmhdEGwQqlQUNCCJJEzulouVCRRPPDPN9Ik9nmgPZk%2Fam6u04CTug5FWfzto4W1y6mlAuXr3EHPB%2FvTcZ%2BmAkgcS5%2FRfKsviGgYg1PBDbKvJFWJigqXNb6jHaHO3eyZnXpof0Qk2PachTFyGGF7upzvEiKr6BGB6DtCoEGe3wCd0iFSMS%2Ft8LIlICGGYaaCvWq9TXeaXkel5jju8XxawzfW0OY8ad1NODjiJJ%2FJ02goRzRa3HwZdXj0P4%2FwwiBHg8BMnsBu5XvhNCt9Gz%2Bxp9cZIC8TMv%2FY8rOvepaH28zVl5BjLGle3tn5syTeLiH6OS68I4OndB2qqeqZqdi9cu6zb1H0y8aKh8r8IIaHqXhP6jBXwOxUN8uimNrMJnaDPxNdvFPuR5yx8UApiuserTd1b1ZIBFiBJ6lavYUBrkLW%2B7bZIJltsNTSxF2GTKFWoXHKGf3%2FXYj%2FniRUh%2BB3xUXrXh8PzVKChkdfuCxirnj5UG2XCrj22%2BBJG8S8UHiExHaIwt01Nel6V7Y0IlXWvwqK8YEx%2FHOI%2FewXERfrnIQDCsrQyC7qTLL3HndUW2Ke8ib2iC%2BPgaP6xDqkqdlhOSojQHG4rfwcyVOFOzeauzAO7Rc77mb0rCUJdMckP6nKiD7nrtjlZXznFmYhCvjmWQF2l06Jl7xQsr%2BjkGAeoXo9X%2FiC11ZTNfxOVIe3LWWkRvMwGWvgvtgF4ZEDGaLXgsbO4I8%2FpSmGD4ox9ZWDfX%2BtTURCyBYVXqYpQ4TpgMhHqAtTUr4TNc7GRLVbfi1xqZNQDt1Sfdzh3Xq88dOJyKsyUs7rcFuuxoNyxvqstWVaAyRglOH1n%2BpV0xA7%2FKEHa%2F8%2FzH6uaXeIp3eLJN1%2BGlAQc1sP2jehPHqGi5Lc7YMOKk8akGOrABqEMeyIMA72vRUvaZqcs7N77uX3kDw2%2BTfyF8pS8HYdR1%2BEU1ekEPGlPPLyTo0NFmbmMa4urw%2B19eIvlGSnFjiSeee%2F%2BeotdKLVnDgZ5aNxOYivkgUqjazWNTWX1qdv7Jq7GWrNDLwjZiU5zLvpcjSyzLyGAVIo8pW14m4aC3jppuzjKpasygGK2%2Bf%2BmxisMAkIdRRS5aXW9PY%2FuwiBnL3qiZT5RtAdamISZZM9jUAWY%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231028T003610Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFPXEGMX3T%2F20231028%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=baee55036cf3bc0a833e3e222bb4e5bf5dff9db02545cf82164788c4d2be34bc",
                        "width": 200,
                        "height": 200
                    },
                    "REGULAR": {
                        "url": "https://edamam-product-images.s3.amazonaws.com/web-img/453/453b12b11b3fa1832288c818d5b754df.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLWVhc3QtMSJIMEYCIQCP2Gbt%2ByPQIVKV%2FafgML7WXbkOusL9fCs6d1le6dFKYAIhAJcnuEh%2B1NzOso38QgGaVBwaVQAMxyMJATg%2FR%2Fl0jl96KsEFCJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMMTg3MDE3MTUwOTg2IgydADkJdybnmhdEGwQqlQUNCCJJEzulouVCRRPPDPN9Ik9nmgPZk%2Fam6u04CTug5FWfzto4W1y6mlAuXr3EHPB%2FvTcZ%2BmAkgcS5%2FRfKsviGgYg1PBDbKvJFWJigqXNb6jHaHO3eyZnXpof0Qk2PachTFyGGF7upzvEiKr6BGB6DtCoEGe3wCd0iFSMS%2Ft8LIlICGGYaaCvWq9TXeaXkel5jju8XxawzfW0OY8ad1NODjiJJ%2FJ02goRzRa3HwZdXj0P4%2FwwiBHg8BMnsBu5XvhNCt9Gz%2Bxp9cZIC8TMv%2FY8rOvepaH28zVl5BjLGle3tn5syTeLiH6OS68I4OndB2qqeqZqdi9cu6zb1H0y8aKh8r8IIaHqXhP6jBXwOxUN8uimNrMJnaDPxNdvFPuR5yx8UApiuserTd1b1ZIBFiBJ6lavYUBrkLW%2B7bZIJltsNTSxF2GTKFWoXHKGf3%2FXYj%2FniRUh%2BB3xUXrXh8PzVKChkdfuCxirnj5UG2XCrj22%2BBJG8S8UHiExHaIwt01Nel6V7Y0IlXWvwqK8YEx%2FHOI%2FewXERfrnIQDCsrQyC7qTLL3HndUW2Ke8ib2iC%2BPgaP6xDqkqdlhOSojQHG4rfwcyVOFOzeauzAO7Rc77mb0rCUJdMckP6nKiD7nrtjlZXznFmYhCvjmWQF2l06Jl7xQsr%2BjkGAeoXo9X%2FiC11ZTNfxOVIe3LWWkRvMwGWvgvtgF4ZEDGaLXgsbO4I8%2FpSmGD4ox9ZWDfX%2BtTURCyBYVXqYpQ4TpgMhHqAtTUr4TNc7GRLVbfi1xqZNQDt1Sfdzh3Xq88dOJyKsyUs7rcFuuxoNyxvqstWVaAyRglOH1n%2BpV0xA7%2FKEHa%2F8%2FzH6uaXeIp3eLJN1%2BGlAQc1sP2jehPHqGi5Lc7YMOKk8akGOrABqEMeyIMA72vRUvaZqcs7N77uX3kDw2%2BTfyF8pS8HYdR1%2BEU1ekEPGlPPLyTo0NFmbmMa4urw%2B19eIvlGSnFjiSeee%2F%2BeotdKLVnDgZ5aNxOYivkgUqjazWNTWX1qdv7Jq7GWrNDLwjZiU5zLvpcjSyzLyGAVIo8pW14m4aC3jppuzjKpasygGK2%2Bf%2BmxisMAkIdRRS5aXW9PY%2FuwiBnL3qiZT5RtAdamISZZM9jUAWY%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231028T003610Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFPXEGMX3T%2F20231028%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=b56e1105ab54f75fedcd9943668a5aec5480cac4bd9a2b3d1e482cc87882b5be",
                        "width": 300,
                        "height": 300
                    },
                    "LARGE": {
                        "url": "https://edamam-product-images.s3.amazonaws.com/web-img/453/453b12b11b3fa1832288c818d5b754df-l.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLWVhc3QtMSJIMEYCIQCP2Gbt%2ByPQIVKV%2FafgML7WXbkOusL9fCs6d1le6dFKYAIhAJcnuEh%2B1NzOso38QgGaVBwaVQAMxyMJATg%2FR%2Fl0jl96KsEFCJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMMTg3MDE3MTUwOTg2IgydADkJdybnmhdEGwQqlQUNCCJJEzulouVCRRPPDPN9Ik9nmgPZk%2Fam6u04CTug5FWfzto4W1y6mlAuXr3EHPB%2FvTcZ%2BmAkgcS5%2FRfKsviGgYg1PBDbKvJFWJigqXNb6jHaHO3eyZnXpof0Qk2PachTFyGGF7upzvEiKr6BGB6DtCoEGe3wCd0iFSMS%2Ft8LIlICGGYaaCvWq9TXeaXkel5jju8XxawzfW0OY8ad1NODjiJJ%2FJ02goRzRa3HwZdXj0P4%2FwwiBHg8BMnsBu5XvhNCt9Gz%2Bxp9cZIC8TMv%2FY8rOvepaH28zVl5BjLGle3tn5syTeLiH6OS68I4OndB2qqeqZqdi9cu6zb1H0y8aKh8r8IIaHqXhP6jBXwOxUN8uimNrMJnaDPxNdvFPuR5yx8UApiuserTd1b1ZIBFiBJ6lavYUBrkLW%2B7bZIJltsNTSxF2GTKFWoXHKGf3%2FXYj%2FniRUh%2BB3xUXrXh8PzVKChkdfuCxirnj5UG2XCrj22%2BBJG8S8UHiExHaIwt01Nel6V7Y0IlXWvwqK8YEx%2FHOI%2FewXERfrnIQDCsrQyC7qTLL3HndUW2Ke8ib2iC%2BPgaP6xDqkqdlhOSojQHG4rfwcyVOFOzeauzAO7Rc77mb0rCUJdMckP6nKiD7nrtjlZXznFmYhCvjmWQF2l06Jl7xQsr%2BjkGAeoXo9X%2FiC11ZTNfxOVIe3LWWkRvMwGWvgvtgF4ZEDGaLXgsbO4I8%2FpSmGD4ox9ZWDfX%2BtTURCyBYVXqYpQ4TpgMhHqAtTUr4TNc7GRLVbfi1xqZNQDt1Sfdzh3Xq88dOJyKsyUs7rcFuuxoNyxvqstWVaAyRglOH1n%2BpV0xA7%2FKEHa%2F8%2FzH6uaXeIp3eLJN1%2BGlAQc1sP2jehPHqGi5Lc7YMOKk8akGOrABqEMeyIMA72vRUvaZqcs7N77uX3kDw2%2BTfyF8pS8HYdR1%2BEU1ekEPGlPPLyTo0NFmbmMa4urw%2B19eIvlGSnFjiSeee%2F%2BeotdKLVnDgZ5aNxOYivkgUqjazWNTWX1qdv7Jq7GWrNDLwjZiU5zLvpcjSyzLyGAVIo8pW14m4aC3jppuzjKpasygGK2%2Bf%2BmxisMAkIdRRS5aXW9PY%2FuwiBnL3qiZT5RtAdamISZZM9jUAWY%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231028T003610Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFPXEGMX3T%2F20231028%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=4d022c3b5a2864b1d78d503213a814662e2384a2c2187a4b8c97c45c6384aa13",
                        "width": 600,
                        "height": 600
                    }
                },
                "source": "Pioneer Woman",
                "url": "http://thepioneerwoman.com/cooking/2013/01/salad-tacos/",
                "shareAs": "http://www.edamam.com/recipe/salad-tacos-92e98a8664c5d7aa2a3fcd4a5369adec/tacos",
                "yield": 8.0,
                "dietLabels": [],
                "healthLabels": [
                    "Peanut-Free",
                    "Tree-Nut-Free",
                    "Soy-Free",
                    "Fish-Free",
                    "Shellfish-Free",
                    "Pork-Free",
                    "Crustacean-Free",
                    "Celery-Free",
                    "Sesame-Free",
                    "Lupine-Free",
                    "Mollusk-Free",
                    "Alcohol-Free",
                    "Sulfite-Free"
                ],
                "cautions": [
                    "Eggs",
                    "Milk",
                    "Sulfites",
                    "FODMAP"
                ],
                "ingredientLines": [
                    "16 whole Taco Shells",
                    "2 pounds Ground Beef",
                    "3 Tablespoons Taco Seasoning",
                    "1 can (4 Ounce) Tomato Paste",
                    "Salt To Taste",
                    "1 can (14.5 Ounce) Beans (kidney, Pinto, Chili), Undrained",
                    "1/2 cup Hot Water",
                    "1 head Green Leaf Lettuce, Sliced Very Thin",
                    "1 cup Grape Tomatoes, Halved (or Diced Regular Tomatoes)",
                    "1 cup Grated Cheese (cheddar, Jack, Or Cheddar/jack)",
                    "1/4 cup Mayonnaise",
                    "1/4 cup Sour Cream",
                    "1/4 cup Salsa",
                    "1 Tablespoon Ranch Dressing Mix (optional)",
                    "Extra Hot Sauce (optional)",
                    "Crushed Tortilla Chips (optional)"
                ],
                "ingredients": [
                    {
                        "text": "16 whole Taco Shells",
                        "quantity": 16.0,
                        "measure": "<unit>",
                        "food": "Taco Shells",
                        "weight": 203.2,
                        "foodCategory": "quick breads and pastries",
                        "foodId": "food_amx6njaaa4q9lsaz4k98faejx12a",
                        "image": "https://www.edamam.com/food-img/def/def506222dc404affdfbf7b7133a34c6.jpg"
                    },
                    {
                        "text": "2 pounds Ground Beef",
                        "quantity": 2.0,
                        "measure": "pound",
                        "food": "Ground Beef",
                        "weight": 907.18474,
                        "foodCategory": "meats",
                        "foodId": "food_boq91pbbhklr6sb0d9sbybzgklkm",
                        "image": "https://www.edamam.com/food-img/cfa/cfae8f9276eaf8f0d9349ba662744a0c.jpg"
                    },
                    {
                        "text": "3 Tablespoons Taco Seasoning",
                        "quantity": 3.0,
                        "measure": "tablespoon",
                        "food": "Taco Seasoning",
                        "weight": 25.649999998265343,
                        "foodCategory": "Condiments and sauces",
                        "foodId": "food_boffkg3ap17ef6a47lzm6b655i8w",
                        "image": "https://www.edamam.com/food-img/b3d/b3d804a544f099eabb941f255c1618a6.jpg"
                    },
                    {
                        "text": "1 can (4 Ounce) Tomato Paste",
                        "quantity": 4.0,
                        "measure": "ounce",
                        "food": "Tomato Paste",
                        "weight": 113.3980925,
                        "foodCategory": "canned vegetables",
                        "foodId": "food_auu2atfal07b6gbd1a5wsawy7u0s",
                        "image": "https://www.edamam.com/food-img/aef/aef4e029118da71388e526086506053a.jpg"
                    },
                    {
                        "text": "Salt To Taste",
                        "quantity": 0.0,
                        "measure": '',
                        "food": "Salt",
                        "weight": 13.55697021636459,
                        "foodCategory": "Condiments and sauces",
                        "foodId": "food_btxz81db72hwbra2pncvebzzzum9",
                        "image": "https://www.edamam.com/food-img/694/6943ea510918c6025795e8dc6e6eaaeb.jpg"
                    },
                    {
                        "text": "1 can (14.5 Ounce) Beans (kidney, Pinto, Chili), Undrained",
                        "quantity": 14.5,
                        "measure": "ounce",
                        "food": "Beans",
                        "weight": 411.0680853125,
                        "foodCategory": "plant-based protein",
                        "foodId": "food_bggwvu5a6s0gniamjy6r1aoknilo",
                        "image": "https://www.edamam.com/food-img/a39/a39102018ed39c6008134e0570af8a6c.jpg"
                    },
                    {
                        "text": "1/2 cup Hot Water",
                        "quantity": 0.5,
                        "measure": "cup",
                        "food": "Water",
                        "weight": 118.29411825,
                        "foodCategory": "water",
                        "foodId": "food_a99vzubbk1ayrsad318rvbzr3dh0",
                        "image": "https://www.edamam.com/food-img/5dd/5dd9d1361847b2ca53c4b19a8f92627e.jpg"
                    },
                    {
                        "text": "1 head Green Leaf Lettuce, Sliced Very Thin",
                        "quantity": 1.0,
                        "measure": "leaf",
                        "food": "Lettuce",
                        "weight": 5.0,
                        "foodCategory": "vegetables",
                        "foodId": "food_bf5fxtkbc9alwoajuvsi7amonr5w",
                        "image": "https://www.edamam.com/food-img/719/71996625d0cb47e197093ecd52c97dc2.jpg"
                    },
                    {
                        "text": "1 cup Grape Tomatoes, Halved (or Diced Regular Tomatoes)",
                        "quantity": 1.0,
                        "measure": "cup",
                        "food": "Grape Tomatoes",
                        "weight": 149.0,
                        "foodCategory": "vegetables",
                        "foodId": "food_b14rghgav9zzw5a0a3j9daj3xhpf",
                        "image": "https://www.edamam.com/food-img/23e/23e727a14f1035bdc2733bb0477efbd2.jpg"
                    },
                    {
                        "text": "1 cup Grated Cheese (cheddar, Jack, Or Cheddar/jack)",
                        "quantity": 1.0,
                        "measure": "cup",
                        "food": "Cheese",
                        "weight": 132.0,
                        "foodCategory": "Cheese",
                        "foodId": "food_bhppgmha1u27voagb8eptbp9g376",
                        "image": "https://www.edamam.com/food-img/bcd/bcd94dde1fcde1475b5bf0540f821c5d.jpg"
                    },
                    {
                        "text": "1/4 cup Mayonnaise",
                        "quantity": 0.25,
                        "measure": "cup",
                        "food": "Mayonnaise",
                        "weight": 57.75,
                        "foodCategory": "condiments and sauces",
                        "foodId": "food_bu8t61zaplle7dbrzk81dbygq0qj",
                        "image": "https://www.edamam.com/food-img/577/577308a0422357885c94cc9b5f1f1862.jpg"
                    },
                    {
                        "text": "1/4 cup Sour Cream",
                        "quantity": 0.25,
                        "measure": "cup",
                        "food": "Sour Cream",
                        "weight": 57.5,
                        "foodCategory": "Dairy",
                        "foodId": "food_adp9fcubzl3lr7bcvzn3rbfiiiwq",
                        "image": "https://www.edamam.com/food-img/f9d/f9d6183267b041b0aff9a10b89c9c15f.jpg"
                    },
                    {
                        "text": "1/4 cup Salsa",
                        "quantity": 0.25,
                        "measure": "cup",
                        "food": "Salsa",
                        "weight": 64.75,
                        "foodCategory": "canned soup",
                        "foodId": "food_b0t3obfawlm5k2b6erxscacez35u",
                        "image": "https://www.edamam.com/food-img/995/995d0f166754a0475c181b9c156fec43.jpg"
                    },
                    {
                        "text": "1 Tablespoon Ranch Dressing Mix (optional)",
                        "quantity": 1.0,
                        "measure": "tablespoon",
                        "food": "Dressing Mix",
                        "weight": 14.7,
                        "foodCategory": "Condiments and sauces",
                        "foodId": "food_a083urbbhn7fvnbf8jzhwb4n31co",
                        "image": "https://www.edamam.com/food-img/039/039ba0b2a516252cbd57fd484924f4c2.jpg"
                    },
                    {
                        "text": "Extra Hot Sauce (optional)",
                        "quantity": 0.0,
                        "measure": '',
                        "food": "Hot Sauce",
                        "weight": 0.0,
                        "foodCategory": "canned soup",
                        "foodId": "food_a6201h1bu1m0tfbrvis6ma6nvhzv",
                        "image": "https://www.edamam.com/food-img/946/946c38a4c278da4361d2615d653d685a.jpg"
                    },
                    {
                        "text": "Crushed Tortilla Chips (optional)",
                        "quantity": 0.0,
                        "measure": '',
                        "food": "Tortilla Chips",
                        "weight": 0.0,
                        "foodCategory": "savory snacks",
                        "foodId": "food_bkxl9s9bpcxmenbef89qbbofifnr",
                        "image": "https://www.edamam.com/food-img/24e/24eea039cad825c1745263674e9879df.jpg"
                    }
                ],
                "calories": 5050.289792700665,
                "totalCO2Emissions": 96384.40496148235,
                "co2EmissionsClass": "G",
                "totalWeight": 2259.495036060765,
                "totalTime": 0.0,
                "cuisineType": [
                    "mexican"
                ],
                "mealType": [
                    "lunch/dinner"
                ],
                "dishType": [
                    "salad"
                ],
                "totalNutrients": {
                    "ENERC_KCAL": {
                        "label": "Energy",
                        "quantity": 5050.289792700665,
                        "unit": "kcal"
                    },
                    "FAT": {
                        "label": "Fat",
                        "quantity": 331.63199148215625,
                        "unit": "g"
                    },
                    "FASAT": {
                        "label": "Saturated",
                        "quantity": 121.71999926763127,
                        "unit": "g"
                    },
                    "FATRN": {
                        "label": "Trans",
                        "quantity": 11.511983932000001,
                        "unit": "g"
                    },
                    "FAMS": {
                        "label": "Monounsaturated",
                        "quantity": 121.73375823330313,
                        "unit": "g"
                    },
                    "FAPU": {
                        "label": "Polyunsaturated",
                        "quantity": 47.04861420740938,
                        "unit": "g"
                    },
                    "CHOCDF": {
                        "label": "Carbs",
                        "quantity": 271.3454633769939,
                        "unit": "g"
                    },
                    "CHOCDF.net": {
                        "label": "Carbohydrates (net)",
                        "quantity": 226.86577348972463,
                        "unit": "g"
                    },
                    "FIBTG": {
                        "label": "Fiber",
                        "quantity": 44.47968988726929,
                        "unit": "g"
                    },
                    "SUGAR": {
                        "label": "Sugars",
                        "quantity": 31.201750113718912,
                        "unit": "g"
                    },
                    "PROCNT": {
                        "label": "Protein",
                        "quantity": 239.00724586960945,
                        "unit": "g"
                    },
                    "CHOLE": {
                        "label": "Cholesterol",
                        "quantity": 841.0776654000002,
                        "unit": "mg"
                    },
                    "NA": {
                        "label": "Sodium",
                        "quantity": 7087.603113817604,
                        "unit": "mg"
                    },
                    "CA": {
                        "label": "Calcium",
                        "quantity": 1743.3240923256249,
                        "unit": "mg"
                    },
                    "MG": {
                        "label": "Magnesium",
                        "quantity": 649.915769341875,
                        "unit": "mg"
                    },
                    "K": {
                        "label": "Potassium",
                        "quantity": 6913.740063251403,
                        "unit": "mg"
                    },
                    "FE": {
                        "label": "Iron",
                        "quantity": 39.50277286321885,
                        "unit": "mg"
                    },
                    "ZN": {
                        "label": "Zinc",
                        "quantity": 51.915552082075,
                        "unit": "mg"
                    },
                    "P": {
                        "label": "Phosphorus",
                        "quantity": 3079.400763609375,
                        "unit": "mg"
                    },
                    "VITA_RAE": {
                        "label": "Vitamin A",
                        "quantity": 726.7084399,
                        "unit": "µg"
                    },
                    "VITC": {
                        "label": "Vitamin C",
                        "quantity": 47.1799322575,
                        "unit": "mg"
                    },
                    "THIA": {
                        "label": "Thiamin (B1)",
                        "quantity": 1.4227041556000002,
                        "unit": "mg"
                    },
                    "RIBF": {
                        "label": "Riboflavin (B2)",
                        "quantity": 2.574780230490625,
                        "unit": "mg"
                    },
                    "NIA": {
                        "label": "Niacin (B3)",
                        "quantity": 47.866426763703146,
                        "unit": "mg"
                    },
                    "VITB6A": {
                        "label": "Vitamin B6",
                        "quantity": 4.250128653984375,
                        "unit": "mg"
                    },
                    "FOLDFE": {
                        "label": "Folate equivalent (total)",
                        "quantity": 584.7049583531251,
                        "unit": "µg"
                    },
                    "FOLFD": {
                        "label": "Folate (food)",
                        "quantity": 505.456958353125,
                        "unit": "µg"
                    },
                    "FOLAC": {
                        "label": "Folic acid",
                        "quantity": 48.768,
                        "unit": "µg"
                    },
                    "VITB12": {
                        "label": "Vitamin B12",
                        "quantity": 20.986503436000007,
                        "unit": "µg"
                    },
                    "VITD": {
                        "label": "Vitamin D",
                        "quantity": 1.6991847400000002,
                        "unit": "µg"
                    },
                    "TOCPHA": {
                        "label": "Vitamin E",
                        "quantity": 14.249619909468754,
                        "unit": "mg"
                    },
                    "VITK1": {
                        "label": "Vitamin K",
                        "quantity": 90.57063233906251,
                        "unit": "µg"
                    },
                    "WATER": {
                        "label": "Water",
                        "quantity": 1368.0024039832138,
                        "unit": "g"
                    }
                },
                "totalDaily": {
                    "ENERC_KCAL": {
                        "label": "Energy",
                        "quantity": 252.51448963503327,
                        "unit": "%"
                    },
                    "FAT": {
                        "label": "Fat",
                        "quantity": 510.2030638187019,
                        "unit": "%"
                    },
                    "FASAT": {
                        "label": "Saturated",
                        "quantity": 608.5999963381563,
                        "unit": "%"
                    },
                    "CHOCDF": {
                        "label": "Carbs",
                        "quantity": 90.4484877923313,
                        "unit": "%"
                    },
                    "FIBTG": {
                        "label": "Fiber",
                        "quantity": 177.91875954907715,
                        "unit": "%"
                    },
                    "PROCNT": {
                        "label": "Protein",
                        "quantity": 478.01449173921884,
                        "unit": "%"
                    },
                    "CHOLE": {
                        "label": "Cholesterol",
                        "quantity": 280.3592218000001,
                        "unit": "%"
                    },
                    "NA": {
                        "label": "Sodium",
                        "quantity": 295.31679640906685,
                        "unit": "%"
                    },
                    "CA": {
                        "label": "Calcium",
                        "quantity": 174.3324092325625,
                        "unit": "%"
                    },
                    "MG": {
                        "label": "Magnesium",
                        "quantity": 154.74184984330358,
                        "unit": "%"
                    },
                    "K": {
                        "label": "Potassium",
                        "quantity": 147.1008524096043,
                        "unit": "%"
                    },
                    "FE": {
                        "label": "Iron",
                        "quantity": 219.45984924010475,
                        "unit": "%"
                    },
                    "ZN": {
                        "label": "Zinc",
                        "quantity": 471.9595643825,
                        "unit": "%"
                    },
                    "P": {
                        "label": "Phosphorus",
                        "quantity": 439.91439480133926,
                        "unit": "%"
                    },
                    "VITA_RAE": {
                        "label": "Vitamin A",
                        "quantity": 80.74538221111112,
                        "unit": "%"
                    },
                    "VITC": {
                        "label": "Vitamin C",
                        "quantity": 52.42214695277777,
                        "unit": "%"
                    },
                    "THIA": {
                        "label": "Thiamin (B1)",
                        "quantity": 118.55867963333337,
                        "unit": "%"
                    },
                    "RIBF": {
                        "label": "Riboflavin (B2)",
                        "quantity": 198.06001773004806,
                        "unit": "%"
                    },
                    "NIA": {
                        "label": "Niacin (B3)",
                        "quantity": 299.1651672731447,
                        "unit": "%"
                    },
                    "VITB6A": {
                        "label": "Vitamin B6",
                        "quantity": 326.93297338341347,
                        "unit": "%"
                    },
                    "FOLDFE": {
                        "label": "Folate equivalent (total)",
                        "quantity": 146.17623958828128,
                        "unit": "%"
                    },
                    "VITB12": {
                        "label": "Vitamin B12",
                        "quantity": 874.437643166667,
                        "unit": "%"
                    },
                    "VITD": {
                        "label": "Vitamin D",
                        "quantity": 11.327898266666669,
                        "unit": "%"
                    },
                    "TOCPHA": {
                        "label": "Vitamin E",
                        "quantity": 94.99746606312503,
                        "unit": "%"
                    },
                    "VITK1": {
                        "label": "Vitamin K",
                        "quantity": 75.47552694921875,
                        "unit": "%"
                    }
                },
                "digest": [
                    {
                        "label": "Fat",
                        "tag": "FAT",
                        "schemaOrgTag": "fatContent",
                        "total": 331.63199148215625,
                        "hasRDI": True,
                        "daily": 510.2030638187019,
                        "unit": "g",
                        "sub": [
                            {
                                "label": "Saturated",
                                "tag": "FASAT",
                                "schemaOrgTag": "saturatedFatContent",
                                "total": 121.71999926763127,
                                "hasRDI": True,
                                "daily": 608.5999963381563,
                                "unit": "g"
                            },
                            {
                                "label": "Trans",
                                "tag": "FATRN",
                                "schemaOrgTag": "transFatContent",
                                "total": 11.511983932000001,
                                "hasRDI": False,
                                "daily": 0.0,
                                "unit": "g"
                            },
                            {
                                "label": "Monounsaturated",
                                "tag": "FAMS",
                                "schemaOrgTag": '',
                                "total": 121.73375823330313,
                                "hasRDI": False,
                                "daily": 0.0,
                                "unit": "g"
                            },
                            {
                                "label": "Polyunsaturated",
                                "tag": "FAPU",
                                "schemaOrgTag": '',
                                "total": 47.04861420740938,
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
                        "total": 271.3454633769939,
                        "hasRDI": True,
                        "daily": 90.4484877923313,
                        "unit": "g",
                        "sub": [
                            {
                                "label": "Carbs (net)",
                                "tag": "CHOCDF.net",
                                "schemaOrgTag": '',
                                "total": 226.86577348972463,
                                "hasRDI": False,
                                "daily": 0.0,
                                "unit": "g"
                            },
                            {
                                "label": "Fiber",
                                "tag": "FIBTG",
                                "schemaOrgTag": "fiberContent",
                                "total": 44.47968988726929,
                                "hasRDI": True,
                                "daily": 177.91875954907715,
                                "unit": "g"
                            },
                            {
                                "label": "Sugars",
                                "tag": "SUGAR",
                                "schemaOrgTag": "sugarContent",
                                "total": 31.201750113718912,
                                "hasRDI": False,
                                "daily": 0.0,
                                "unit": "g"
                            },
                            {
                                "label": "Sugars, added",
                                "tag": "SUGAR.added",
                                "schemaOrgTag": '',
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
                        "total": 239.00724586960945,
                        "hasRDI": True,
                        "daily": 478.01449173921884,
                        "unit": "g"
                    },
                    {
                        "label": "Cholesterol",
                        "tag": "CHOLE",
                        "schemaOrgTag": "cholesterolContent",
                        "total": 841.0776654000002,
                        "hasRDI": True,
                        "daily": 280.3592218000001,
                        "unit": "mg"
                    },
                    {
                        "label": "Sodium",
                        "tag": "NA",
                        "schemaOrgTag": "sodiumContent",
                        "total": 7087.603113817604,
                        "hasRDI": True,
                        "daily": 295.31679640906685,
                        "unit": "mg"
                    },
                    {
                        "label": "Calcium",
                        "tag": "CA",
                        "schemaOrgTag": '',
                        "total": 1743.3240923256249,
                        "hasRDI": True,
                        "daily": 174.3324092325625,
                        "unit": "mg"
                    },
                    {
                        "label": "Magnesium",
                        "tag": "MG",
                        "schemaOrgTag": '',
                        "total": 649.915769341875,
                        "hasRDI": True,
                        "daily": 154.74184984330358,
                        "unit": "mg"
                    },
                    {
                        "label": "Potassium",
                        "tag": "K",
                        "schemaOrgTag": '',
                        "total": 6913.740063251403,
                        "hasRDI": True,
                        "daily": 147.1008524096043,
                        "unit": "mg"
                    },
                    {
                        "label": "Iron",
                        "tag": "FE",
                        "schemaOrgTag": '',
                        "total": 39.50277286321885,
                        "hasRDI": True,
                        "daily": 219.45984924010475,
                        "unit": "mg"
                    },
                    {
                        "label": "Zinc",
                        "tag": "ZN",
                        "schemaOrgTag": '',
                        "total": 51.915552082075,
                        "hasRDI": True,
                        "daily": 471.9595643825,
                        "unit": "mg"
                    },
                    {
                        "label": "Phosphorus",
                        "tag": "P",
                        "schemaOrgTag": '',
                        "total": 3079.400763609375,
                        "hasRDI": True,
                        "daily": 439.91439480133926,
                        "unit": "mg"
                    },
                    {
                        "label": "Vitamin A",
                        "tag": "VITA_RAE",
                        "schemaOrgTag": '',
                        "total": 726.7084399,
                        "hasRDI": True,
                        "daily": 80.74538221111112,
                        "unit": "µg"
                    },
                    {
                        "label": "Vitamin C",
                        "tag": "VITC",
                        "schemaOrgTag": '',
                        "total": 47.1799322575,
                        "hasRDI": True,
                        "daily": 52.42214695277777,
                        "unit": "mg"
                    },
                    {
                        "label": "Thiamin (B1)",
                        "tag": "THIA",
                        "schemaOrgTag": '',
                        "total": 1.4227041556000002,
                        "hasRDI": True,
                        "daily": 118.55867963333337,
                        "unit": "mg"
                    },
                    {
                        "label": "Riboflavin (B2)",
                        "tag": "RIBF",
                        "schemaOrgTag": '',
                        "total": 2.574780230490625,
                        "hasRDI": True,
                        "daily": 198.06001773004806,
                        "unit": "mg"
                    },
                    {
                        "label": "Niacin (B3)",
                        "tag": "NIA",
                        "schemaOrgTag": '',
                        "total": 47.866426763703146,
                        "hasRDI": True,
                        "daily": 299.1651672731447,
                        "unit": "mg"
                    },
                    {
                        "label": "Vitamin B6",
                        "tag": "VITB6A",
                        "schemaOrgTag": '',
                        "total": 4.250128653984375,
                        "hasRDI": True,
                        "daily": 326.93297338341347,
                        "unit": "mg"
                    },
                    {
                        "label": "Folate equivalent (total)",
                        "tag": "FOLDFE",
                        "schemaOrgTag": '',
                        "total": 584.7049583531251,
                        "hasRDI": True,
                        "daily": 146.17623958828128,
                        "unit": "µg"
                    },
                    {
                        "label": "Folate (food)",
                        "tag": "FOLFD",
                        "schemaOrgTag": '',
                        "total": 505.456958353125,
                        "hasRDI": False,
                        "daily": 0.0,
                        "unit": "µg"
                    },
                    {
                        "label": "Folic acid",
                        "tag": "FOLAC",
                        "schemaOrgTag": '',
                        "total": 48.768,
                        "hasRDI": False,
                        "daily": 0.0,
                        "unit": "µg"
                    },
                    {
                        "label": "Vitamin B12",
                        "tag": "VITB12",
                        "schemaOrgTag": '',
                        "total": 20.986503436000007,
                        "hasRDI": True,
                        "daily": 874.437643166667,
                        "unit": "µg"
                    },
                    {
                        "label": "Vitamin D",
                        "tag": "VITD",
                        "schemaOrgTag": '',
                        "total": 1.6991847400000002,
                        "hasRDI": True,
                        "daily": 11.327898266666669,
                        "unit": "µg"
                    },
                    {
                        "label": "Vitamin E",
                        "tag": "TOCPHA",
                        "schemaOrgTag": '',
                        "total": 14.249619909468754,
                        "hasRDI": True,
                        "daily": 94.99746606312503,
                        "unit": "mg"
                    },
                    {
                        "label": "Vitamin K",
                        "tag": "VITK1",
                        "schemaOrgTag": '',
                        "total": 90.57063233906251,
                        "hasRDI": True,
                        "daily": 75.47552694921875,
                        "unit": "µg"
                    },
                    {
                        "label": "Sugar alcohols",
                        "tag": "Sugar.alcohol",
                        "schemaOrgTag": '',
                        "total": 0.0,
                        "hasRDI": False,
                        "daily": 0.0,
                        "unit": "g"
                    },
                    {
                        "label": "Water",
                        "tag": "WATER",
                        "schemaOrgTag": '',
                        "total": 1368.0024039832138,
                        "hasRDI": False,
                        "daily": 0.0,
                        "unit": "g"
                    }
                ]
            },
            "_links": {
                "self": {
                    "title": "Self",
                    "href": "https://api.edamam.com/api/recipes/v2/92e98a8664c5d7aa2a3fcd4a5369adec?type=public&app_id=e909afd5&app_key=34e59dda7e1bffb92e49c416e9449e1d"
                }
            }
        },
        {
            "recipe": {
                "uri": "http://www.edamam.com/ontologies/edamam.owl#recipe_ae05c505b65174b75d829825035b3d2c",
                "label": "Black Bean Tacos",
                "image": "https://edamam-product-images.s3.amazonaws.com/web-img/e69/e690cade9500b8ac7037094dd103dce1.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLWVhc3QtMSJIMEYCIQCP2Gbt%2ByPQIVKV%2FafgML7WXbkOusL9fCs6d1le6dFKYAIhAJcnuEh%2B1NzOso38QgGaVBwaVQAMxyMJATg%2FR%2Fl0jl96KsEFCJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMMTg3MDE3MTUwOTg2IgydADkJdybnmhdEGwQqlQUNCCJJEzulouVCRRPPDPN9Ik9nmgPZk%2Fam6u04CTug5FWfzto4W1y6mlAuXr3EHPB%2FvTcZ%2BmAkgcS5%2FRfKsviGgYg1PBDbKvJFWJigqXNb6jHaHO3eyZnXpof0Qk2PachTFyGGF7upzvEiKr6BGB6DtCoEGe3wCd0iFSMS%2Ft8LIlICGGYaaCvWq9TXeaXkel5jju8XxawzfW0OY8ad1NODjiJJ%2FJ02goRzRa3HwZdXj0P4%2FwwiBHg8BMnsBu5XvhNCt9Gz%2Bxp9cZIC8TMv%2FY8rOvepaH28zVl5BjLGle3tn5syTeLiH6OS68I4OndB2qqeqZqdi9cu6zb1H0y8aKh8r8IIaHqXhP6jBXwOxUN8uimNrMJnaDPxNdvFPuR5yx8UApiuserTd1b1ZIBFiBJ6lavYUBrkLW%2B7bZIJltsNTSxF2GTKFWoXHKGf3%2FXYj%2FniRUh%2BB3xUXrXh8PzVKChkdfuCxirnj5UG2XCrj22%2BBJG8S8UHiExHaIwt01Nel6V7Y0IlXWvwqK8YEx%2FHOI%2FewXERfrnIQDCsrQyC7qTLL3HndUW2Ke8ib2iC%2BPgaP6xDqkqdlhOSojQHG4rfwcyVOFOzeauzAO7Rc77mb0rCUJdMckP6nKiD7nrtjlZXznFmYhCvjmWQF2l06Jl7xQsr%2BjkGAeoXo9X%2FiC11ZTNfxOVIe3LWWkRvMwGWvgvtgF4ZEDGaLXgsbO4I8%2FpSmGD4ox9ZWDfX%2BtTURCyBYVXqYpQ4TpgMhHqAtTUr4TNc7GRLVbfi1xqZNQDt1Sfdzh3Xq88dOJyKsyUs7rcFuuxoNyxvqstWVaAyRglOH1n%2BpV0xA7%2FKEHa%2F8%2FzH6uaXeIp3eLJN1%2BGlAQc1sP2jehPHqGi5Lc7YMOKk8akGOrABqEMeyIMA72vRUvaZqcs7N77uX3kDw2%2BTfyF8pS8HYdR1%2BEU1ekEPGlPPLyTo0NFmbmMa4urw%2B19eIvlGSnFjiSeee%2F%2BeotdKLVnDgZ5aNxOYivkgUqjazWNTWX1qdv7Jq7GWrNDLwjZiU5zLvpcjSyzLyGAVIo8pW14m4aC3jppuzjKpasygGK2%2Bf%2BmxisMAkIdRRS5aXW9PY%2FuwiBnL3qiZT5RtAdamISZZM9jUAWY%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231028T003610Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFPXEGMX3T%2F20231028%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=d3423278143c401a79844463136cf62c12ab635e393562a972534cbb0c88c4b0",
                "images": {
                    "THUMBNAIL": {
                        "url": "https://edamam-product-images.s3.amazonaws.com/web-img/e69/e690cade9500b8ac7037094dd103dce1-s.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLWVhc3QtMSJIMEYCIQCP2Gbt%2ByPQIVKV%2FafgML7WXbkOusL9fCs6d1le6dFKYAIhAJcnuEh%2B1NzOso38QgGaVBwaVQAMxyMJATg%2FR%2Fl0jl96KsEFCJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMMTg3MDE3MTUwOTg2IgydADkJdybnmhdEGwQqlQUNCCJJEzulouVCRRPPDPN9Ik9nmgPZk%2Fam6u04CTug5FWfzto4W1y6mlAuXr3EHPB%2FvTcZ%2BmAkgcS5%2FRfKsviGgYg1PBDbKvJFWJigqXNb6jHaHO3eyZnXpof0Qk2PachTFyGGF7upzvEiKr6BGB6DtCoEGe3wCd0iFSMS%2Ft8LIlICGGYaaCvWq9TXeaXkel5jju8XxawzfW0OY8ad1NODjiJJ%2FJ02goRzRa3HwZdXj0P4%2FwwiBHg8BMnsBu5XvhNCt9Gz%2Bxp9cZIC8TMv%2FY8rOvepaH28zVl5BjLGle3tn5syTeLiH6OS68I4OndB2qqeqZqdi9cu6zb1H0y8aKh8r8IIaHqXhP6jBXwOxUN8uimNrMJnaDPxNdvFPuR5yx8UApiuserTd1b1ZIBFiBJ6lavYUBrkLW%2B7bZIJltsNTSxF2GTKFWoXHKGf3%2FXYj%2FniRUh%2BB3xUXrXh8PzVKChkdfuCxirnj5UG2XCrj22%2BBJG8S8UHiExHaIwt01Nel6V7Y0IlXWvwqK8YEx%2FHOI%2FewXERfrnIQDCsrQyC7qTLL3HndUW2Ke8ib2iC%2BPgaP6xDqkqdlhOSojQHG4rfwcyVOFOzeauzAO7Rc77mb0rCUJdMckP6nKiD7nrtjlZXznFmYhCvjmWQF2l06Jl7xQsr%2BjkGAeoXo9X%2FiC11ZTNfxOVIe3LWWkRvMwGWvgvtgF4ZEDGaLXgsbO4I8%2FpSmGD4ox9ZWDfX%2BtTURCyBYVXqYpQ4TpgMhHqAtTUr4TNc7GRLVbfi1xqZNQDt1Sfdzh3Xq88dOJyKsyUs7rcFuuxoNyxvqstWVaAyRglOH1n%2BpV0xA7%2FKEHa%2F8%2FzH6uaXeIp3eLJN1%2BGlAQc1sP2jehPHqGi5Lc7YMOKk8akGOrABqEMeyIMA72vRUvaZqcs7N77uX3kDw2%2BTfyF8pS8HYdR1%2BEU1ekEPGlPPLyTo0NFmbmMa4urw%2B19eIvlGSnFjiSeee%2F%2BeotdKLVnDgZ5aNxOYivkgUqjazWNTWX1qdv7Jq7GWrNDLwjZiU5zLvpcjSyzLyGAVIo8pW14m4aC3jppuzjKpasygGK2%2Bf%2BmxisMAkIdRRS5aXW9PY%2FuwiBnL3qiZT5RtAdamISZZM9jUAWY%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231028T003610Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFPXEGMX3T%2F20231028%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=685d82b0aca1e9e4a9d59529d6138ee554dc96f6b01bc36be8661bbdb7703d90",
                        "width": 100,
                        "height": 100
                    },
                    "SMALL": {
                        "url": "https://edamam-product-images.s3.amazonaws.com/web-img/e69/e690cade9500b8ac7037094dd103dce1-m.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLWVhc3QtMSJIMEYCIQCP2Gbt%2ByPQIVKV%2FafgML7WXbkOusL9fCs6d1le6dFKYAIhAJcnuEh%2B1NzOso38QgGaVBwaVQAMxyMJATg%2FR%2Fl0jl96KsEFCJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMMTg3MDE3MTUwOTg2IgydADkJdybnmhdEGwQqlQUNCCJJEzulouVCRRPPDPN9Ik9nmgPZk%2Fam6u04CTug5FWfzto4W1y6mlAuXr3EHPB%2FvTcZ%2BmAkgcS5%2FRfKsviGgYg1PBDbKvJFWJigqXNb6jHaHO3eyZnXpof0Qk2PachTFyGGF7upzvEiKr6BGB6DtCoEGe3wCd0iFSMS%2Ft8LIlICGGYaaCvWq9TXeaXkel5jju8XxawzfW0OY8ad1NODjiJJ%2FJ02goRzRa3HwZdXj0P4%2FwwiBHg8BMnsBu5XvhNCt9Gz%2Bxp9cZIC8TMv%2FY8rOvepaH28zVl5BjLGle3tn5syTeLiH6OS68I4OndB2qqeqZqdi9cu6zb1H0y8aKh8r8IIaHqXhP6jBXwOxUN8uimNrMJnaDPxNdvFPuR5yx8UApiuserTd1b1ZIBFiBJ6lavYUBrkLW%2B7bZIJltsNTSxF2GTKFWoXHKGf3%2FXYj%2FniRUh%2BB3xUXrXh8PzVKChkdfuCxirnj5UG2XCrj22%2BBJG8S8UHiExHaIwt01Nel6V7Y0IlXWvwqK8YEx%2FHOI%2FewXERfrnIQDCsrQyC7qTLL3HndUW2Ke8ib2iC%2BPgaP6xDqkqdlhOSojQHG4rfwcyVOFOzeauzAO7Rc77mb0rCUJdMckP6nKiD7nrtjlZXznFmYhCvjmWQF2l06Jl7xQsr%2BjkGAeoXo9X%2FiC11ZTNfxOVIe3LWWkRvMwGWvgvtgF4ZEDGaLXgsbO4I8%2FpSmGD4ox9ZWDfX%2BtTURCyBYVXqYpQ4TpgMhHqAtTUr4TNc7GRLVbfi1xqZNQDt1Sfdzh3Xq88dOJyKsyUs7rcFuuxoNyxvqstWVaAyRglOH1n%2BpV0xA7%2FKEHa%2F8%2FzH6uaXeIp3eLJN1%2BGlAQc1sP2jehPHqGi5Lc7YMOKk8akGOrABqEMeyIMA72vRUvaZqcs7N77uX3kDw2%2BTfyF8pS8HYdR1%2BEU1ekEPGlPPLyTo0NFmbmMa4urw%2B19eIvlGSnFjiSeee%2F%2BeotdKLVnDgZ5aNxOYivkgUqjazWNTWX1qdv7Jq7GWrNDLwjZiU5zLvpcjSyzLyGAVIo8pW14m4aC3jppuzjKpasygGK2%2Bf%2BmxisMAkIdRRS5aXW9PY%2FuwiBnL3qiZT5RtAdamISZZM9jUAWY%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231028T003610Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFPXEGMX3T%2F20231028%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=24508c2bec25790a1037acaa7cd8456f3ff98648f229bb04f1a2c75c0d4350ae",
                        "width": 200,
                        "height": 200
                    },
                    "REGULAR": {
                        "url": "https://edamam-product-images.s3.amazonaws.com/web-img/e69/e690cade9500b8ac7037094dd103dce1.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLWVhc3QtMSJIMEYCIQCP2Gbt%2ByPQIVKV%2FafgML7WXbkOusL9fCs6d1le6dFKYAIhAJcnuEh%2B1NzOso38QgGaVBwaVQAMxyMJATg%2FR%2Fl0jl96KsEFCJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMMTg3MDE3MTUwOTg2IgydADkJdybnmhdEGwQqlQUNCCJJEzulouVCRRPPDPN9Ik9nmgPZk%2Fam6u04CTug5FWfzto4W1y6mlAuXr3EHPB%2FvTcZ%2BmAkgcS5%2FRfKsviGgYg1PBDbKvJFWJigqXNb6jHaHO3eyZnXpof0Qk2PachTFyGGF7upzvEiKr6BGB6DtCoEGe3wCd0iFSMS%2Ft8LIlICGGYaaCvWq9TXeaXkel5jju8XxawzfW0OY8ad1NODjiJJ%2FJ02goRzRa3HwZdXj0P4%2FwwiBHg8BMnsBu5XvhNCt9Gz%2Bxp9cZIC8TMv%2FY8rOvepaH28zVl5BjLGle3tn5syTeLiH6OS68I4OndB2qqeqZqdi9cu6zb1H0y8aKh8r8IIaHqXhP6jBXwOxUN8uimNrMJnaDPxNdvFPuR5yx8UApiuserTd1b1ZIBFiBJ6lavYUBrkLW%2B7bZIJltsNTSxF2GTKFWoXHKGf3%2FXYj%2FniRUh%2BB3xUXrXh8PzVKChkdfuCxirnj5UG2XCrj22%2BBJG8S8UHiExHaIwt01Nel6V7Y0IlXWvwqK8YEx%2FHOI%2FewXERfrnIQDCsrQyC7qTLL3HndUW2Ke8ib2iC%2BPgaP6xDqkqdlhOSojQHG4rfwcyVOFOzeauzAO7Rc77mb0rCUJdMckP6nKiD7nrtjlZXznFmYhCvjmWQF2l06Jl7xQsr%2BjkGAeoXo9X%2FiC11ZTNfxOVIe3LWWkRvMwGWvgvtgF4ZEDGaLXgsbO4I8%2FpSmGD4ox9ZWDfX%2BtTURCyBYVXqYpQ4TpgMhHqAtTUr4TNc7GRLVbfi1xqZNQDt1Sfdzh3Xq88dOJyKsyUs7rcFuuxoNyxvqstWVaAyRglOH1n%2BpV0xA7%2FKEHa%2F8%2FzH6uaXeIp3eLJN1%2BGlAQc1sP2jehPHqGi5Lc7YMOKk8akGOrABqEMeyIMA72vRUvaZqcs7N77uX3kDw2%2BTfyF8pS8HYdR1%2BEU1ekEPGlPPLyTo0NFmbmMa4urw%2B19eIvlGSnFjiSeee%2F%2BeotdKLVnDgZ5aNxOYivkgUqjazWNTWX1qdv7Jq7GWrNDLwjZiU5zLvpcjSyzLyGAVIo8pW14m4aC3jppuzjKpasygGK2%2Bf%2BmxisMAkIdRRS5aXW9PY%2FuwiBnL3qiZT5RtAdamISZZM9jUAWY%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231028T003610Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFPXEGMX3T%2F20231028%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=d3423278143c401a79844463136cf62c12ab635e393562a972534cbb0c88c4b0",
                        "width": 300,
                        "height": 300
                    },
                    "LARGE": {
                        "url": "https://edamam-product-images.s3.amazonaws.com/web-img/e69/e690cade9500b8ac7037094dd103dce1-l.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLWVhc3QtMSJIMEYCIQCP2Gbt%2ByPQIVKV%2FafgML7WXbkOusL9fCs6d1le6dFKYAIhAJcnuEh%2B1NzOso38QgGaVBwaVQAMxyMJATg%2FR%2Fl0jl96KsEFCJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMMTg3MDE3MTUwOTg2IgydADkJdybnmhdEGwQqlQUNCCJJEzulouVCRRPPDPN9Ik9nmgPZk%2Fam6u04CTug5FWfzto4W1y6mlAuXr3EHPB%2FvTcZ%2BmAkgcS5%2FRfKsviGgYg1PBDbKvJFWJigqXNb6jHaHO3eyZnXpof0Qk2PachTFyGGF7upzvEiKr6BGB6DtCoEGe3wCd0iFSMS%2Ft8LIlICGGYaaCvWq9TXeaXkel5jju8XxawzfW0OY8ad1NODjiJJ%2FJ02goRzRa3HwZdXj0P4%2FwwiBHg8BMnsBu5XvhNCt9Gz%2Bxp9cZIC8TMv%2FY8rOvepaH28zVl5BjLGle3tn5syTeLiH6OS68I4OndB2qqeqZqdi9cu6zb1H0y8aKh8r8IIaHqXhP6jBXwOxUN8uimNrMJnaDPxNdvFPuR5yx8UApiuserTd1b1ZIBFiBJ6lavYUBrkLW%2B7bZIJltsNTSxF2GTKFWoXHKGf3%2FXYj%2FniRUh%2BB3xUXrXh8PzVKChkdfuCxirnj5UG2XCrj22%2BBJG8S8UHiExHaIwt01Nel6V7Y0IlXWvwqK8YEx%2FHOI%2FewXERfrnIQDCsrQyC7qTLL3HndUW2Ke8ib2iC%2BPgaP6xDqkqdlhOSojQHG4rfwcyVOFOzeauzAO7Rc77mb0rCUJdMckP6nKiD7nrtjlZXznFmYhCvjmWQF2l06Jl7xQsr%2BjkGAeoXo9X%2FiC11ZTNfxOVIe3LWWkRvMwGWvgvtgF4ZEDGaLXgsbO4I8%2FpSmGD4ox9ZWDfX%2BtTURCyBYVXqYpQ4TpgMhHqAtTUr4TNc7GRLVbfi1xqZNQDt1Sfdzh3Xq88dOJyKsyUs7rcFuuxoNyxvqstWVaAyRglOH1n%2BpV0xA7%2FKEHa%2F8%2FzH6uaXeIp3eLJN1%2BGlAQc1sP2jehPHqGi5Lc7YMOKk8akGOrABqEMeyIMA72vRUvaZqcs7N77uX3kDw2%2BTfyF8pS8HYdR1%2BEU1ekEPGlPPLyTo0NFmbmMa4urw%2B19eIvlGSnFjiSeee%2F%2BeotdKLVnDgZ5aNxOYivkgUqjazWNTWX1qdv7Jq7GWrNDLwjZiU5zLvpcjSyzLyGAVIo8pW14m4aC3jppuzjKpasygGK2%2Bf%2BmxisMAkIdRRS5aXW9PY%2FuwiBnL3qiZT5RtAdamISZZM9jUAWY%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231028T003610Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFPXEGMX3T%2F20231028%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=640ddb57d4f37c8a46972897ef828d8006581e3b8361016045011d9ec0631f2b",
                        "width": 600,
                        "height": 600
                    }
                },
                "source": "EatingWell",
                "url": "http://www.eatingwell.com/recipe/263545/black-bean-tacos/",
                "shareAs": "http://www.edamam.com/recipe/black-bean-tacos-ae05c505b65174b75d829825035b3d2c/tacos",
                "yield": 4.0,
                "dietLabels": [
                    "Balanced",
                    "High-Fiber"
                ],
                "healthLabels": [
                    "Sugar-Conscious",
                    "Vegetarian",
                    "Pescatarian",
                    "Mediterranean",
                    "Egg-Free",
                    "Peanut-Free",
                    "Tree-Nut-Free",
                    "Soy-Free",
                    "Fish-Free",
                    "Shellfish-Free",
                    "Pork-Free",
                    "Red-Meat-Free",
                    "Crustacean-Free",
                    "Celery-Free",
                    "Mustard-Free",
                    "Sesame-Free",
                    "Lupine-Free",
                    "Mollusk-Free",
                    "Alcohol-Free",
                    "Sulfite-Free",
                    "Kosher",
                    "Immuno-Supportive"
                ],
                "cautions": [
                    "Eggs",
                    "Milk",
                    "Sulfites"
                ],
                "ingredientLines": [
                    "2 (15 ounce) cans black beans, rinsed",
                    "1 teaspoon ground cumin",
                    "½ teaspoon garlic powder",
                    "8 hard taco shells",
                    "¾ cup shredded Mexican cheese blend"
                ],
                "ingredients": [
                    {
                        "text": "2 (15 ounce) cans black beans, rinsed",
                        "quantity": 30.0,
                        "measure": "ounce",
                        "food": "black beans",
                        "weight": 850.48569375,
                        "foodCategory": "plant-based protein",
                        "foodId": "food_bazzo85azdbkmsb56nu4ra5rphoe",
                        "image": "https://www.edamam.com/food-img/850/8505bc3d47bbc820b69d532202f61ce1.jpg"
                    },
                    {
                        "text": "1 teaspoon ground cumin",
                        "quantity": 1.0,
                        "measure": "teaspoon",
                        "food": "cumin",
                        "weight": 2.1,
                        "foodCategory": "Condiments and sauces",
                        "foodId": "food_a8jjbx4biqndasapojdb5by3e92e",
                        "image": "https://www.edamam.com/food-img/07e/07e2a4eb77ce46591033846504817d35.jpg"
                    },
                    {
                        "text": "½ teaspoon garlic powder",
                        "quantity": 0.5,
                        "measure": "teaspoon",
                        "food": "garlic powder",
                        "weight": 1.55,
                        "foodCategory": "Condiments and sauces",
                        "foodId": "food_boq94r1a036492bdup9u1beyph0l",
                        "image": "https://www.edamam.com/food-img/5c3/5c3db1d5a1a16b1f0a74796f74dd5985.jpg"
                    },
                    {
                        "text": "8 hard taco shells",
                        "quantity": 8.0,
                        "measure": "<unit>",
                        "food": "taco shells",
                        "weight": 101.6,
                        "foodCategory": "quick breads and pastries",
                        "foodId": "food_amx6njaaa4q9lsaz4k98faejx12a",
                        "image": "https://www.edamam.com/food-img/def/def506222dc404affdfbf7b7133a34c6.jpg"
                    },
                    {
                        "text": "¾ cup shredded Mexican cheese blend",
                        "quantity": 0.75,
                        "measure": "cup",
                        "food": "cheese",
                        "weight": 99.0,
                        "foodCategory": "Cheese",
                        "foodId": "food_bhppgmha1u27voagb8eptbp9g376",
                        "image": "https://www.edamam.com/food-img/bcd/bcd94dde1fcde1475b5bf0540f821c5d.jpg"
                    }
                ],
                "calories": 1669.5334813124998,
                "totalCO2Emissions": 3062.736259168294,
                "co2EmissionsClass": "E",
                "totalWeight": 1054.7356937499999,
                "totalTime": 25.0,
                "cuisineType": [
                    "mexican"
                ],
                "mealType": [
                    "lunch/dinner"
                ],
                "dishType": [
                    "salad"
                ],
                "totalNutrients": {
                    "ENERC_KCAL": {
                        "label": "Energy",
                        "quantity": 1669.5334813124998,
                        "unit": "kcal"
                    },
                    "FAT": {
                        "label": "Fat",
                        "quantity": 58.061823511875005,
                        "unit": "g"
                    },
                    "FASAT": {
                        "label": "Saturated",
                        "quantity": 26.5986637703125,
                        "unit": "g"
                    },
                    "FATRN": {
                        "label": "Trans",
                        "quantity": 0.174752,
                        "unit": "g"
                    },
                    "FAMS": {
                        "label": "Monounsaturated",
                        "quantity": 16.8555439234375,
                        "unit": "g"
                    },
                    "FAPU": {
                        "label": "Polyunsaturated",
                        "quantity": 7.655326117187499,
                        "unit": "g"
                    },
                    "CHOCDF": {
                        "label": "Carbs",
                        "quantity": 211.08797516250002,
                        "unit": "g"
                    },
                    "CHOCDF.net": {
                        "label": "Carbohydrates (net)",
                        "quantity": 145.23726229375,
                        "unit": "g"
                    },
                    "FIBTG": {
                        "label": "Fiber",
                        "quantity": 65.85071286875,
                        "unit": "g"
                    },
                    "SUGAR": {
                        "label": "Sugars",
                        "quantity": 4.040232095625,
                        "unit": "g"
                    },
                    "PROCNT": {
                        "label": "Protein",
                        "quantity": 81.09894733312501,
                        "unit": "g"
                    },
                    "CHOLE": {
                        "label": "Cholesterol",
                        "quantity": 98.01,
                        "unit": "mg"
                    },
                    "NA": {
                        "label": "Sodium",
                        "quantity": 2153.782257375,
                        "unit": "mg"
                    },
                    "CA": {
                        "label": "Calcium",
                        "quantity": 1122.9454928124999,
                        "unit": "mg"
                    },
                    "MG": {
                        "label": "Magnesium",
                        "quantity": 417.6074928124999,
                        "unit": "mg"
                    },
                    "K": {
                        "label": "Potassium",
                        "quantity": 2985.46693675,
                        "unit": "mg"
                    },
                    "FE": {
                        "label": "Iron",
                        "quantity": 19.446043181249998,
                        "unit": "mg"
                    },
                    "ZN": {
                        "label": "Zinc",
                        "quantity": 9.97912774625,
                        "unit": "mg"
                    },
                    "P": {
                        "label": "Phosphorus",
                        "quantity": 1622.5985492500001,
                        "unit": "mg"
                    },
                    "VITA_RAE": {
                        "label": "Vitamin A",
                        "quantity": 335.99,
                        "unit": "µg"
                    },
                    "VITC": {
                        "label": "Vitamin C",
                        "quantity": 23.14341373125,
                        "unit": "mg"
                    },
                    "THIA": {
                        "label": "Thiamin (B1)",
                        "quantity": 1.4587764712500002,
                        "unit": "mg"
                    },
                    "RIBF": {
                        "label": "Riboflavin (B2)",
                        "quantity": 1.5346353324999997,
                        "unit": "mg"
                    },
                    "NIA": {
                        "label": "Niacin (B3)",
                        "quantity": 7.33985930125,
                        "unit": "mg"
                    },
                    "VITB6A": {
                        "label": "Vitamin B6",
                        "quantity": 0.7740651315625,
                        "unit": "mg"
                    },
                    "FOLDFE": {
                        "label": "Folate equivalent (total)",
                        "quantity": 632.8247731875001,
                        "unit": "µg"
                    },
                    "FOLFD": {
                        "label": "Folate (food)",
                        "quantity": 593.2007731875001,
                        "unit": "µg"
                    },
                    "FOLAC": {
                        "label": "Folic acid",
                        "quantity": 24.384,
                        "unit": "µg"
                    },
                    "VITB12": {
                        "label": "Vitamin B12",
                        "quantity": 1.089,
                        "unit": "µg"
                    },
                    "VITD": {
                        "label": "Vitamin D",
                        "quantity": 0.594,
                        "unit": "µg"
                    },
                    "TOCPHA": {
                        "label": "Vitamin E",
                        "quantity": 6.75726630125,
                        "unit": "mg"
                    },
                    "VITK1": {
                        "label": "Vitamin K",
                        "quantity": 30.79437095625,
                        "unit": "µg"
                    },
                    "WATER": {
                        "label": "Water",
                        "quantity": 686.1708194749999,
                        "unit": "g"
                    }
                },
                "totalDaily": {
                    "ENERC_KCAL": {
                        "label": "Energy",
                        "quantity": 83.47667406562499,
                        "unit": "%"
                    },
                    "FAT": {
                        "label": "Fat",
                        "quantity": 89.32588232596156,
                        "unit": "%"
                    },
                    "FASAT": {
                        "label": "Saturated",
                        "quantity": 132.9933188515625,
                        "unit": "%"
                    },
                    "CHOCDF": {
                        "label": "Carbs",
                        "quantity": 70.3626583875,
                        "unit": "%"
                    },
                    "FIBTG": {
                        "label": "Fiber",
                        "quantity": 263.402851475,
                        "unit": "%"
                    },
                    "PROCNT": {
                        "label": "Protein",
                        "quantity": 162.19789466625002,
                        "unit": "%"
                    },
                    "CHOLE": {
                        "label": "Cholesterol",
                        "quantity": 32.67,
                        "unit": "%"
                    },
                    "NA": {
                        "label": "Sodium",
                        "quantity": 89.740927390625,
                        "unit": "%"
                    },
                    "CA": {
                        "label": "Calcium",
                        "quantity": 112.29454928124999,
                        "unit": "%"
                    },
                    "MG": {
                        "label": "Magnesium",
                        "quantity": 99.4303554315476,
                        "unit": "%"
                    },
                    "K": {
                        "label": "Potassium",
                        "quantity": 63.52057312234042,
                        "unit": "%"
                    },
                    "FE": {
                        "label": "Iron",
                        "quantity": 108.03357322916665,
                        "unit": "%"
                    },
                    "ZN": {
                        "label": "Zinc",
                        "quantity": 90.71934314772729,
                        "unit": "%"
                    },
                    "P": {
                        "label": "Phosphorus",
                        "quantity": 231.79979275000002,
                        "unit": "%"
                    },
                    "VITA_RAE": {
                        "label": "Vitamin A",
                        "quantity": 37.33222222222222,
                        "unit": "%"
                    },
                    "VITC": {
                        "label": "Vitamin C",
                        "quantity": 25.71490414583333,
                        "unit": "%"
                    },
                    "THIA": {
                        "label": "Thiamin (B1)",
                        "quantity": 121.56470593750001,
                        "unit": "%"
                    },
                    "RIBF": {
                        "label": "Riboflavin (B2)",
                        "quantity": 118.0488717307692,
                        "unit": "%"
                    },
                    "NIA": {
                        "label": "Niacin (B3)",
                        "quantity": 45.8741206328125,
                        "unit": "%"
                    },
                    "VITB6A": {
                        "label": "Vitamin B6",
                        "quantity": 59.54347165865384,
                        "unit": "%"
                    },
                    "FOLDFE": {
                        "label": "Folate equivalent (total)",
                        "quantity": 158.20619329687503,
                        "unit": "%"
                    },
                    "VITB12": {
                        "label": "Vitamin B12",
                        "quantity": 45.375,
                        "unit": "%"
                    },
                    "VITD": {
                        "label": "Vitamin D",
                        "quantity": 3.96,
                        "unit": "%"
                    },
                    "TOCPHA": {
                        "label": "Vitamin E",
                        "quantity": 45.04844200833333,
                        "unit": "%"
                    },
                    "VITK1": {
                        "label": "Vitamin K",
                        "quantity": 25.661975796875,
                        "unit": "%"
                    }
                },
                "digest": [
                    {
                        "label": "Fat",
                        "tag": "FAT",
                        "schemaOrgTag": "fatContent",
                        "total": 58.061823511875005,
                        "hasRDI": True,
                        "daily": 89.32588232596156,
                        "unit": "g",
                        "sub": [
                            {
                                "label": "Saturated",
                                "tag": "FASAT",
                                "schemaOrgTag": "saturatedFatContent",
                                "total": 26.5986637703125,
                                "hasRDI": True,
                                "daily": 132.9933188515625,
                                "unit": "g"
                            },
                            {
                                "label": "Trans",
                                "tag": "FATRN",
                                "schemaOrgTag": "transFatContent",
                                "total": 0.174752,
                                "hasRDI": False,
                                "daily": 0.0,
                                "unit": "g"
                            },
                            {
                                "label": "Monounsaturated",
                                "tag": "FAMS",
                                "schemaOrgTag": '',
                                "total": 16.8555439234375,
                                "hasRDI": False,
                                "daily": 0.0,
                                "unit": "g"
                            },
                            {
                                "label": "Polyunsaturated",
                                "tag": "FAPU",
                                "schemaOrgTag": '',
                                "total": 7.655326117187499,
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
                        "total": 211.08797516250002,
                        "hasRDI": True,
                        "daily": 70.3626583875,
                        "unit": "g",
                        "sub": [
                            {
                                "label": "Carbs (net)",
                                "tag": "CHOCDF.net",
                                "schemaOrgTag": '',
                                "total": 145.23726229375,
                                "hasRDI": False,
                                "daily": 0.0,
                                "unit": "g"
                            },
                            {
                                "label": "Fiber",
                                "tag": "FIBTG",
                                "schemaOrgTag": "fiberContent",
                                "total": 65.85071286875,
                                "hasRDI": True,
                                "daily": 263.402851475,
                                "unit": "g"
                            },
                            {
                                "label": "Sugars",
                                "tag": "SUGAR",
                                "schemaOrgTag": "sugarContent",
                                "total": 4.040232095625,
                                "hasRDI": False,
                                "daily": 0.0,
                                "unit": "g"
                            },
                            {
                                "label": "Sugars, added",
                                "tag": "SUGAR.added",
                                "schemaOrgTag": '',
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
                        "total": 81.09894733312501,
                        "hasRDI": True,
                        "daily": 162.19789466625002,
                        "unit": "g"
                    },
                    {
                        "label": "Cholesterol",
                        "tag": "CHOLE",
                        "schemaOrgTag": "cholesterolContent",
                        "total": 98.01,
                        "hasRDI": True,
                        "daily": 32.67,
                        "unit": "mg"
                    },
                    {
                        "label": "Sodium",
                        "tag": "NA",
                        "schemaOrgTag": "sodiumContent",
                        "total": 2153.782257375,
                        "hasRDI": True,
                        "daily": 89.740927390625,
                        "unit": "mg"
                    },
                    {
                        "label": "Calcium",
                        "tag": "CA",
                        "schemaOrgTag": '',
                        "total": 1122.9454928124999,
                        "hasRDI": True,
                        "daily": 112.29454928124999,
                        "unit": "mg"
                    },
                    {
                        "label": "Magnesium",
                        "tag": "MG",
                        "schemaOrgTag": '',
                        "total": 417.6074928124999,
                        "hasRDI": True,
                        "daily": 99.4303554315476,
                        "unit": "mg"
                    },
                    {
                        "label": "Potassium",
                        "tag": "K",
                        "schemaOrgTag": '',
                        "total": 2985.46693675,
                        "hasRDI": True,
                        "daily": 63.52057312234042,
                        "unit": "mg"
                    },
                    {
                        "label": "Iron",
                        "tag": "FE",
                        "schemaOrgTag": '',
                        "total": 19.446043181249998,
                        "hasRDI": True,
                        "daily": 108.03357322916665,
                        "unit": "mg"
                    },
                    {
                        "label": "Zinc",
                        "tag": "ZN",
                        "schemaOrgTag": '',
                        "total": 9.97912774625,
                        "hasRDI": True,
                        "daily": 90.71934314772729,
                        "unit": "mg"
                    },
                    {
                        "label": "Phosphorus",
                        "tag": "P",
                        "schemaOrgTag": '',
                        "total": 1622.5985492500001,
                        "hasRDI": True,
                        "daily": 231.79979275000002,
                        "unit": "mg"
                    },
                    {
                        "label": "Vitamin A",
                        "tag": "VITA_RAE",
                        "schemaOrgTag": '',
                        "total": 335.99,
                        "hasRDI": True,
                        "daily": 37.33222222222222,
                        "unit": "µg"
                    },
                    {
                        "label": "Vitamin C",
                        "tag": "VITC",
                        "schemaOrgTag": '',
                        "total": 23.14341373125,
                        "hasRDI": True,
                        "daily": 25.71490414583333,
                        "unit": "mg"
                    },
                    {
                        "label": "Thiamin (B1)",
                        "tag": "THIA",
                        "schemaOrgTag": '',
                        "total": 1.4587764712500002,
                        "hasRDI": True,
                        "daily": 121.56470593750001,
                        "unit": "mg"
                    },
                    {
                        "label": "Riboflavin (B2)",
                        "tag": "RIBF",
                        "schemaOrgTag": '',
                        "total": 1.5346353324999997,
                        "hasRDI": True,
                        "daily": 118.0488717307692,
                        "unit": "mg"
                    },
                    {
                        "label": "Niacin (B3)",
                        "tag": "NIA",
                        "schemaOrgTag": '',
                        "total": 7.33985930125,
                        "hasRDI": True,
                        "daily": 45.8741206328125,
                        "unit": "mg"
                    },
                    {
                        "label": "Vitamin B6",
                        "tag": "VITB6A",
                        "schemaOrgTag": '',
                        "total": 0.7740651315625,
                        "hasRDI": True,
                        "daily": 59.54347165865384,
                        "unit": "mg"
                    },
                    {
                        "label": "Folate equivalent (total)",
                        "tag": "FOLDFE",
                        "schemaOrgTag": '',
                        "total": 632.8247731875001,
                        "hasRDI": True,
                        "daily": 158.20619329687503,
                        "unit": "µg"
                    },
                    {
                        "label": "Folate (food)",
                        "tag": "FOLFD",
                        "schemaOrgTag": '',
                        "total": 593.2007731875001,
                        "hasRDI": False,
                        "daily": 0.0,
                        "unit": "µg"
                    },
                    {
                        "label": "Folic acid",
                        "tag": "FOLAC",
                        "schemaOrgTag": '',
                        "total": 24.384,
                        "hasRDI": False,
                        "daily": 0.0,
                        "unit": "µg"
                    },
                    {
                        "label": "Vitamin B12",
                        "tag": "VITB12",
                        "schemaOrgTag": '',
                        "total": 1.089,
                        "hasRDI": True,
                        "daily": 45.375,
                        "unit": "µg"
                    },
                    {
                        "label": "Vitamin D",
                        "tag": "VITD",
                        "schemaOrgTag": '',
                        "total": 0.594,
                        "hasRDI": True,
                        "daily": 3.96,
                        "unit": "µg"
                    },
                    {
                        "label": "Vitamin E",
                        "tag": "TOCPHA",
                        "schemaOrgTag": '',
                        "total": 6.75726630125,
                        "hasRDI": True,
                        "daily": 45.04844200833333,
                        "unit": "mg"
                    },
                    {
                        "label": "Vitamin K",
                        "tag": "VITK1",
                        "schemaOrgTag": '',
                        "total": 30.79437095625,
                        "hasRDI": True,
                        "daily": 25.661975796875,
                        "unit": "µg"
                    },
                    {
                        "label": "Sugar alcohols",
                        "tag": "Sugar.alcohol",
                        "schemaOrgTag": '',
                        "total": 0.0,
                        "hasRDI": False,
                        "daily": 0.0,
                        "unit": "g"
                    },
                    {
                        "label": "Water",
                        "tag": "WATER",
                        "schemaOrgTag": '',
                        "total": 686.1708194749999,
                        "hasRDI": False,
                        "daily": 0.0,
                        "unit": "g"
                    }
                ]
            },
            "_links": {
                "self": {
                    "title": "Self",
                    "href": "https://api.edamam.com/api/recipes/v2/ae05c505b65174b75d829825035b3d2c?type=public&app_id=e909afd5&app_key=34e59dda7e1bffb92e49c416e9449e1d"
                }
            }
        },
        {
            "recipe": {
                "uri": "http://www.edamam.com/ontologies/edamam.owl#recipe_6055b587f0ebc2d4ecea6e0d02f11f6a",
                "label": "Grilled Shrimp Tacos with Poblano-Corn Salsa",
                "image": "https://edamam-product-images.s3.amazonaws.com/web-img/1dc/1dc7fc9f02c27c1c227ded6bdb16b501.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLWVhc3QtMSJIMEYCIQCP2Gbt%2ByPQIVKV%2FafgML7WXbkOusL9fCs6d1le6dFKYAIhAJcnuEh%2B1NzOso38QgGaVBwaVQAMxyMJATg%2FR%2Fl0jl96KsEFCJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMMTg3MDE3MTUwOTg2IgydADkJdybnmhdEGwQqlQUNCCJJEzulouVCRRPPDPN9Ik9nmgPZk%2Fam6u04CTug5FWfzto4W1y6mlAuXr3EHPB%2FvTcZ%2BmAkgcS5%2FRfKsviGgYg1PBDbKvJFWJigqXNb6jHaHO3eyZnXpof0Qk2PachTFyGGF7upzvEiKr6BGB6DtCoEGe3wCd0iFSMS%2Ft8LIlICGGYaaCvWq9TXeaXkel5jju8XxawzfW0OY8ad1NODjiJJ%2FJ02goRzRa3HwZdXj0P4%2FwwiBHg8BMnsBu5XvhNCt9Gz%2Bxp9cZIC8TMv%2FY8rOvepaH28zVl5BjLGle3tn5syTeLiH6OS68I4OndB2qqeqZqdi9cu6zb1H0y8aKh8r8IIaHqXhP6jBXwOxUN8uimNrMJnaDPxNdvFPuR5yx8UApiuserTd1b1ZIBFiBJ6lavYUBrkLW%2B7bZIJltsNTSxF2GTKFWoXHKGf3%2FXYj%2FniRUh%2BB3xUXrXh8PzVKChkdfuCxirnj5UG2XCrj22%2BBJG8S8UHiExHaIwt01Nel6V7Y0IlXWvwqK8YEx%2FHOI%2FewXERfrnIQDCsrQyC7qTLL3HndUW2Ke8ib2iC%2BPgaP6xDqkqdlhOSojQHG4rfwcyVOFOzeauzAO7Rc77mb0rCUJdMckP6nKiD7nrtjlZXznFmYhCvjmWQF2l06Jl7xQsr%2BjkGAeoXo9X%2FiC11ZTNfxOVIe3LWWkRvMwGWvgvtgF4ZEDGaLXgsbO4I8%2FpSmGD4ox9ZWDfX%2BtTURCyBYVXqYpQ4TpgMhHqAtTUr4TNc7GRLVbfi1xqZNQDt1Sfdzh3Xq88dOJyKsyUs7rcFuuxoNyxvqstWVaAyRglOH1n%2BpV0xA7%2FKEHa%2F8%2FzH6uaXeIp3eLJN1%2BGlAQc1sP2jehPHqGi5Lc7YMOKk8akGOrABqEMeyIMA72vRUvaZqcs7N77uX3kDw2%2BTfyF8pS8HYdR1%2BEU1ekEPGlPPLyTo0NFmbmMa4urw%2B19eIvlGSnFjiSeee%2F%2BeotdKLVnDgZ5aNxOYivkgUqjazWNTWX1qdv7Jq7GWrNDLwjZiU5zLvpcjSyzLyGAVIo8pW14m4aC3jppuzjKpasygGK2%2Bf%2BmxisMAkIdRRS5aXW9PY%2FuwiBnL3qiZT5RtAdamISZZM9jUAWY%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231028T003610Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFPXEGMX3T%2F20231028%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=cee22c772eee0bcbfb1542345894597fb47ee9a2c78dd8a2f58f6b29d78b1e39",
                "images": {
                    "THUMBNAIL": {
                        "url": "https://edamam-product-images.s3.amazonaws.com/web-img/1dc/1dc7fc9f02c27c1c227ded6bdb16b501-s.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLWVhc3QtMSJIMEYCIQCP2Gbt%2ByPQIVKV%2FafgML7WXbkOusL9fCs6d1le6dFKYAIhAJcnuEh%2B1NzOso38QgGaVBwaVQAMxyMJATg%2FR%2Fl0jl96KsEFCJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMMTg3MDE3MTUwOTg2IgydADkJdybnmhdEGwQqlQUNCCJJEzulouVCRRPPDPN9Ik9nmgPZk%2Fam6u04CTug5FWfzto4W1y6mlAuXr3EHPB%2FvTcZ%2BmAkgcS5%2FRfKsviGgYg1PBDbKvJFWJigqXNb6jHaHO3eyZnXpof0Qk2PachTFyGGF7upzvEiKr6BGB6DtCoEGe3wCd0iFSMS%2Ft8LIlICGGYaaCvWq9TXeaXkel5jju8XxawzfW0OY8ad1NODjiJJ%2FJ02goRzRa3HwZdXj0P4%2FwwiBHg8BMnsBu5XvhNCt9Gz%2Bxp9cZIC8TMv%2FY8rOvepaH28zVl5BjLGle3tn5syTeLiH6OS68I4OndB2qqeqZqdi9cu6zb1H0y8aKh8r8IIaHqXhP6jBXwOxUN8uimNrMJnaDPxNdvFPuR5yx8UApiuserTd1b1ZIBFiBJ6lavYUBrkLW%2B7bZIJltsNTSxF2GTKFWoXHKGf3%2FXYj%2FniRUh%2BB3xUXrXh8PzVKChkdfuCxirnj5UG2XCrj22%2BBJG8S8UHiExHaIwt01Nel6V7Y0IlXWvwqK8YEx%2FHOI%2FewXERfrnIQDCsrQyC7qTLL3HndUW2Ke8ib2iC%2BPgaP6xDqkqdlhOSojQHG4rfwcyVOFOzeauzAO7Rc77mb0rCUJdMckP6nKiD7nrtjlZXznFmYhCvjmWQF2l06Jl7xQsr%2BjkGAeoXo9X%2FiC11ZTNfxOVIe3LWWkRvMwGWvgvtgF4ZEDGaLXgsbO4I8%2FpSmGD4ox9ZWDfX%2BtTURCyBYVXqYpQ4TpgMhHqAtTUr4TNc7GRLVbfi1xqZNQDt1Sfdzh3Xq88dOJyKsyUs7rcFuuxoNyxvqstWVaAyRglOH1n%2BpV0xA7%2FKEHa%2F8%2FzH6uaXeIp3eLJN1%2BGlAQc1sP2jehPHqGi5Lc7YMOKk8akGOrABqEMeyIMA72vRUvaZqcs7N77uX3kDw2%2BTfyF8pS8HYdR1%2BEU1ekEPGlPPLyTo0NFmbmMa4urw%2B19eIvlGSnFjiSeee%2F%2BeotdKLVnDgZ5aNxOYivkgUqjazWNTWX1qdv7Jq7GWrNDLwjZiU5zLvpcjSyzLyGAVIo8pW14m4aC3jppuzjKpasygGK2%2Bf%2BmxisMAkIdRRS5aXW9PY%2FuwiBnL3qiZT5RtAdamISZZM9jUAWY%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231028T003610Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFPXEGMX3T%2F20231028%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=a4efee37e41a1954f78b2bd52fc184c6b9458a88d4cc98975224e39a1896ba39",
                        "width": 100,
                        "height": 100
                    },
                    "SMALL": {
                        "url": "https://edamam-product-images.s3.amazonaws.com/web-img/1dc/1dc7fc9f02c27c1c227ded6bdb16b501-m.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLWVhc3QtMSJIMEYCIQCP2Gbt%2ByPQIVKV%2FafgML7WXbkOusL9fCs6d1le6dFKYAIhAJcnuEh%2B1NzOso38QgGaVBwaVQAMxyMJATg%2FR%2Fl0jl96KsEFCJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMMTg3MDE3MTUwOTg2IgydADkJdybnmhdEGwQqlQUNCCJJEzulouVCRRPPDPN9Ik9nmgPZk%2Fam6u04CTug5FWfzto4W1y6mlAuXr3EHPB%2FvTcZ%2BmAkgcS5%2FRfKsviGgYg1PBDbKvJFWJigqXNb6jHaHO3eyZnXpof0Qk2PachTFyGGF7upzvEiKr6BGB6DtCoEGe3wCd0iFSMS%2Ft8LIlICGGYaaCvWq9TXeaXkel5jju8XxawzfW0OY8ad1NODjiJJ%2FJ02goRzRa3HwZdXj0P4%2FwwiBHg8BMnsBu5XvhNCt9Gz%2Bxp9cZIC8TMv%2FY8rOvepaH28zVl5BjLGle3tn5syTeLiH6OS68I4OndB2qqeqZqdi9cu6zb1H0y8aKh8r8IIaHqXhP6jBXwOxUN8uimNrMJnaDPxNdvFPuR5yx8UApiuserTd1b1ZIBFiBJ6lavYUBrkLW%2B7bZIJltsNTSxF2GTKFWoXHKGf3%2FXYj%2FniRUh%2BB3xUXrXh8PzVKChkdfuCxirnj5UG2XCrj22%2BBJG8S8UHiExHaIwt01Nel6V7Y0IlXWvwqK8YEx%2FHOI%2FewXERfrnIQDCsrQyC7qTLL3HndUW2Ke8ib2iC%2BPgaP6xDqkqdlhOSojQHG4rfwcyVOFOzeauzAO7Rc77mb0rCUJdMckP6nKiD7nrtjlZXznFmYhCvjmWQF2l06Jl7xQsr%2BjkGAeoXo9X%2FiC11ZTNfxOVIe3LWWkRvMwGWvgvtgF4ZEDGaLXgsbO4I8%2FpSmGD4ox9ZWDfX%2BtTURCyBYVXqYpQ4TpgMhHqAtTUr4TNc7GRLVbfi1xqZNQDt1Sfdzh3Xq88dOJyKsyUs7rcFuuxoNyxvqstWVaAyRglOH1n%2BpV0xA7%2FKEHa%2F8%2FzH6uaXeIp3eLJN1%2BGlAQc1sP2jehPHqGi5Lc7YMOKk8akGOrABqEMeyIMA72vRUvaZqcs7N77uX3kDw2%2BTfyF8pS8HYdR1%2BEU1ekEPGlPPLyTo0NFmbmMa4urw%2B19eIvlGSnFjiSeee%2F%2BeotdKLVnDgZ5aNxOYivkgUqjazWNTWX1qdv7Jq7GWrNDLwjZiU5zLvpcjSyzLyGAVIo8pW14m4aC3jppuzjKpasygGK2%2Bf%2BmxisMAkIdRRS5aXW9PY%2FuwiBnL3qiZT5RtAdamISZZM9jUAWY%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231028T003610Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFPXEGMX3T%2F20231028%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=06749b38cf1717229dc60bcd311e27edebf5e773beeb29aada78b5b08da21cd9",
                        "width": 200,
                        "height": 200
                    },
                    "REGULAR": {
                        "url": "https://edamam-product-images.s3.amazonaws.com/web-img/1dc/1dc7fc9f02c27c1c227ded6bdb16b501.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLWVhc3QtMSJIMEYCIQCP2Gbt%2ByPQIVKV%2FafgML7WXbkOusL9fCs6d1le6dFKYAIhAJcnuEh%2B1NzOso38QgGaVBwaVQAMxyMJATg%2FR%2Fl0jl96KsEFCJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMMTg3MDE3MTUwOTg2IgydADkJdybnmhdEGwQqlQUNCCJJEzulouVCRRPPDPN9Ik9nmgPZk%2Fam6u04CTug5FWfzto4W1y6mlAuXr3EHPB%2FvTcZ%2BmAkgcS5%2FRfKsviGgYg1PBDbKvJFWJigqXNb6jHaHO3eyZnXpof0Qk2PachTFyGGF7upzvEiKr6BGB6DtCoEGe3wCd0iFSMS%2Ft8LIlICGGYaaCvWq9TXeaXkel5jju8XxawzfW0OY8ad1NODjiJJ%2FJ02goRzRa3HwZdXj0P4%2FwwiBHg8BMnsBu5XvhNCt9Gz%2Bxp9cZIC8TMv%2FY8rOvepaH28zVl5BjLGle3tn5syTeLiH6OS68I4OndB2qqeqZqdi9cu6zb1H0y8aKh8r8IIaHqXhP6jBXwOxUN8uimNrMJnaDPxNdvFPuR5yx8UApiuserTd1b1ZIBFiBJ6lavYUBrkLW%2B7bZIJltsNTSxF2GTKFWoXHKGf3%2FXYj%2FniRUh%2BB3xUXrXh8PzVKChkdfuCxirnj5UG2XCrj22%2BBJG8S8UHiExHaIwt01Nel6V7Y0IlXWvwqK8YEx%2FHOI%2FewXERfrnIQDCsrQyC7qTLL3HndUW2Ke8ib2iC%2BPgaP6xDqkqdlhOSojQHG4rfwcyVOFOzeauzAO7Rc77mb0rCUJdMckP6nKiD7nrtjlZXznFmYhCvjmWQF2l06Jl7xQsr%2BjkGAeoXo9X%2FiC11ZTNfxOVIe3LWWkRvMwGWvgvtgF4ZEDGaLXgsbO4I8%2FpSmGD4ox9ZWDfX%2BtTURCyBYVXqYpQ4TpgMhHqAtTUr4TNc7GRLVbfi1xqZNQDt1Sfdzh3Xq88dOJyKsyUs7rcFuuxoNyxvqstWVaAyRglOH1n%2BpV0xA7%2FKEHa%2F8%2FzH6uaXeIp3eLJN1%2BGlAQc1sP2jehPHqGi5Lc7YMOKk8akGOrABqEMeyIMA72vRUvaZqcs7N77uX3kDw2%2BTfyF8pS8HYdR1%2BEU1ekEPGlPPLyTo0NFmbmMa4urw%2B19eIvlGSnFjiSeee%2F%2BeotdKLVnDgZ5aNxOYivkgUqjazWNTWX1qdv7Jq7GWrNDLwjZiU5zLvpcjSyzLyGAVIo8pW14m4aC3jppuzjKpasygGK2%2Bf%2BmxisMAkIdRRS5aXW9PY%2FuwiBnL3qiZT5RtAdamISZZM9jUAWY%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231028T003610Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFPXEGMX3T%2F20231028%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=cee22c772eee0bcbfb1542345894597fb47ee9a2c78dd8a2f58f6b29d78b1e39",
                        "width": 300,
                        "height": 300
                    }
                },
                "source": "PBS Food",
                "url": "http://www.pbs.org/food/recipes/grilled-shrimp-tacos-with-poblano-corn-salsa/",
                "shareAs": "http://www.edamam.com/recipe/grilled-shrimp-tacos-with-poblano-corn-salsa-6055b587f0ebc2d4ecea6e0d02f11f6a/tacos",
                "yield": 4.0,
                "dietLabels": [
                    "High-Fiber"
                ],
                "healthLabels": [
                    "Pescatarian",
                    "Dairy-Free",
                    "Egg-Free",
                    "Peanut-Free",
                    "Tree-Nut-Free",
                    "Soy-Free",
                    "Pork-Free",
                    "Red-Meat-Free",
                    "Celery-Free",
                    "Mustard-Free",
                    "Sesame-Free",
                    "Lupine-Free",
                    "Mollusk-Free",
                    "Alcohol-Free",
                    "Sulfite-Free"
                ],
                "cautions": [
                    "Eggs",
                    "Milk",
                    "Sulfites"
                ],
                "ingredientLines": [
                    "Salsa:",
                    "1 ear corn, husked",
                    "6 scallions, white and light green parts only (about 5 inches)",
                    "1 poblano chile",
                    "1 cup cherry tomatoes, halved",
                    "1 large (or 2 small) haas avocado",
                    "1 small bunch cilantro, minced",
                    "Juice of two small limes",
                    "1 clove garlic, minced",
                    "1./2 salt",
                    "1 t olive oil",
                    "Tacos:",
                    "1 lb shrimp",
                    "1 package corn tortillas"
                ],
                "ingredients": [
                    {
                        "text": "1 ear corn, husked",
                        "quantity": 1.0,
                        "measure": "ear",
                        "food": "corn",
                        "weight": 102.0,
                        "foodCategory": "vegetables",
                        "foodId": "food_b4wvre6b14mmkpaa22d8ybup8q51",
                        "image": "https://www.edamam.com/food-img/eb5/eb5e11afb9f697720b2de2e0e0e27d8d.jpg"
                    },
                    {
                        "text": "6 scallions, white and light green parts only (about 5 inches)",
                        "quantity": 6.0,
                        "measure": "<unit>",
                        "food": "scallions",
                        "weight": 83.33333333333334,
                        "foodCategory": "vegetables",
                        "foodId": "food_bknlkyzbuzo27pb11whr4bttkuy6",
                        "image": "https://www.edamam.com/food-img/b89/b89986ed6aa466285bdd99bac34b3c46.jpg"
                    },
                    {
                        "text": "1 poblano chile",
                        "quantity": 1.0,
                        "measure": "<unit>",
                        "food": "chile",
                        "weight": 45.0,
                        "foodCategory": "vegetables",
                        "foodId": "food_a6g98mqatzj7vca6ms3bnbzqxf3s",
                        "image": "https://www.edamam.com/food-img/469/469213672957a242638e20c27e3e8acd.jpeg"
                    },
                    {
                        "text": "1 cup cherry tomatoes, halved",
                        "quantity": 1.0,
                        "measure": "cup",
                        "food": "cherry tomatoes",
                        "weight": 175.0,
                        "foodCategory": "vegetables",
                        "foodId": "food_a30b0hpbvavginafe0tocbf6ymje",
                        "image": "https://www.edamam.com/food-img/23e/23e727a14f1035bdc2733bb0477efbd2.jpg"
                    },
                    {
                        "text": "1 large (or 2 small) haas avocado",
                        "quantity": 1.0,
                        "measure": "<unit>",
                        "food": "haas avocado",
                        "weight": 201.0,
                        "foodCategory": "fruit",
                        "foodId": "food_b0yuze4b1g3afpanijno5abtiu28",
                        "image": "https://www.edamam.com/food-img/984/984a707ea8e9c6bf5f6498970a9e6d9d.jpg"
                    },
                    {
                        "text": "1 small bunch cilantro, minced",
                        "quantity": 1.0,
                        "measure": "bunch",
                        "food": "cilantro",
                        "weight": 30.0,
                        "foodCategory": "vegetables",
                        "foodId": "food_alhzhuwb4lc7jnb5s6f02by60bzp",
                        "image": "https://www.edamam.com/food-img/d57/d57e375b6ff99a90c7ee2b1990a1af36.jpg"
                    },
                    {
                        "text": "Juice of two small limes",
                        "quantity": 2.0,
                        "measure": "<unit>",
                        "food": "limes",
                        "weight": 100.5,
                        "foodCategory": "fruit",
                        "foodId": "food_av58muyb8kg92fbk0g8g8aui5knv",
                        "image": "https://www.edamam.com/food-img/48a/48a123c9576647c4ada6a41df5eeb22a.jpg"
                    },
                    {
                        "text": "1 clove garlic, minced",
                        "quantity": 1.0,
                        "measure": "clove",
                        "food": "garlic",
                        "weight": 3.0,
                        "foodCategory": "vegetables",
                        "foodId": "food_avtcmx6bgjv1jvay6s6stan8dnyp",
                        "image": "https://www.edamam.com/food-img/6ee/6ee142951f48aaf94f4312409f8d133d.jpg"
                    },
                    {
                        "text": "1./2 salt",
                        "quantity": 0.0,
                        "measure": '',
                        "food": "salt",
                        "weight": 7.33155422,
                        "foodCategory": "Condiments and sauces",
                        "foodId": "food_btxz81db72hwbra2pncvebzzzum9",
                        "image": "https://www.edamam.com/food-img/694/6943ea510918c6025795e8dc6e6eaaeb.jpg"
                    },
                    {
                        "text": "1 t olive oil",
                        "quantity": 1.0,
                        "measure": "teaspoon",
                        "food": "olive oil",
                        "weight": 4.5,
                        "foodCategory": "Oils",
                        "foodId": "food_b1d1icuad3iktrbqby0hiagafaz7",
                        "image": "https://www.edamam.com/food-img/4d6/4d651eaa8a353647746290c7a9b29d84.jpg"
                    },
                    {
                        "text": "1 lb shrimp",
                        "quantity": 1.0,
                        "measure": "pound",
                        "food": "shrimp",
                        "weight": 453.59237,
                        "foodCategory": "seafood",
                        "foodId": "food_bjap0xzbf5x6s3azkpwtfb14i25u",
                        "image": "https://www.edamam.com/food-img/4df/4df0fd62e878ed84b387b9e3ab48f2dc.jpg"
                    },
                    {
                        "text": "1 package corn tortillas",
                        "quantity": 1.0,
                        "measure": "<unit>",
                        "food": "corn tortillas",
                        "weight": 24.0,
                        "foodCategory": "quick breads and pastries",
                        "foodId": "food_bhw0b95agm97s0abfignnb8fsvb3",
                        "image": "https://www.edamam.com/food-img/b8a/b8ad23dcc06f2324f944e47eb579d644.jpg"
                    }
                ],
                "calories": 1004.6601811666668,
                "totalCO2Emissions": 13044.262345105268,
                "co2EmissionsClass": "G",
                "totalWeight": 1227.6449701656898,
                "totalTime": 348.0,
                "cuisineType": [
                    "mexican"
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
                        "quantity": 1004.6601811666668,
                        "unit": "kcal"
                    },
                    "FAT": {
                        "label": "Fat",
                        "quantity": 39.49965442033333,
                        "unit": "g"
                    },
                    "FASAT": {
                        "label": "Saturated",
                        "quantity": 5.924194960366666,
                        "unit": "g"
                    },
                    "FATRN": {
                        "label": "Trans",
                        "quantity": 0.018143694800000002,
                        "unit": "g"
                    },
                    "FAMS": {
                        "label": "Monounsaturated",
                        "quantity": 24.169284438200005,
                        "unit": "g"
                    },
                    "FAPU": {
                        "label": "Polyunsaturated",
                        "quantity": 6.046912069066666,
                        "unit": "g"
                    },
                    "CHOCDF": {
                        "label": "Carbs",
                        "quantity": 76.45846666666668,
                        "unit": "g"
                    },
                    "CHOCDF.net": {
                        "label": "Carbohydrates (net)",
                        "quantity": 50.78080000000001,
                        "unit": "g"
                    },
                    "FIBTG": {
                        "label": "Fiber",
                        "quantity": 25.677666666666667,
                        "unit": "g"
                    },
                    "SUGAR": {
                        "label": "Sugars",
                        "quantity": 18.84161666666667,
                        "unit": "g"
                    },
                    "PROCNT": {
                        "label": "Protein",
                        "quantity": 105.33526637000001,
                        "unit": "g"
                    },
                    "CHOLE": {
                        "label": "Cholesterol",
                        "quantity": 730.2837157000001,
                        "unit": "mg"
                    },
                    "NA": {
                        "label": "Sodium",
                        "quantity": 2841.5637845876,
                        "unit": "mg"
                    },
                    "CA": {
                        "label": "Calcium",
                        "quantity": 479.8117408397656,
                        "unit": "mg"
                    },
                    "MG": {
                        "label": "Magnesium",
                        "quantity": 332.97118883499024,
                        "unit": "mg"
                    },
                    "K": {
                        "label": "Potassium",
                        "quantity": 3553.3663981465893,
                        "unit": "mg"
                    },
                    "FE": {
                        "label": "Iron",
                        "quantity": 7.68818723788011,
                        "unit": "mg"
                    },
                    "ZN": {
                        "label": "Zinc",
                        "quantity": 9.188707024832357,
                        "unit": "mg"
                    },
                    "P": {
                        "label": "Phosphorus",
                        "quantity": 1370.6110051333333,
                        "unit": "mg"
                    },
                    "VITA_RAE": {
                        "label": "Vitamin A",
                        "quantity": 263.12666666666667,
                        "unit": "µg"
                    },
                    "VITC": {
                        "label": "Vitamin C",
                        "quantity": 169.75916666666666,
                        "unit": "mg"
                    },
                    "THIA": {
                        "label": "Thiamin (B1)",
                        "quantity": 0.5145633333333334,
                        "unit": "mg"
                    },
                    "RIBF": {
                        "label": "Riboflavin (B2)",
                        "quantity": 0.5436166666666666,
                        "unit": "mg"
                    },
                    "NIA": {
                        "label": "Niacin (B3)",
                        "quantity": 8.2528,
                        "unit": "mg"
                    },
                    "VITB6A": {
                        "label": "Vitamin B6",
                        "quantity": 1.2076383333333331,
                        "unit": "mg"
                    },
                    "FOLDFE": {
                        "label": "Folate equivalent (total)",
                        "quantity": 323.5133333333334,
                        "unit": "µg"
                    },
                    "FOLFD": {
                        "label": "Folate (food)",
                        "quantity": 323.5133333333334,
                        "unit": "µg"
                    },
                    "FOLAC": {
                        "label": "Folic acid",
                        "quantity": 0.0,
                        "unit": "µg"
                    },
                    "VITB12": {
                        "label": "Vitamin B12",
                        "quantity": 0.0,
                        "unit": "µg"
                    },
                    "VITD": {
                        "label": "Vitamin D",
                        "quantity": 0.0,
                        "unit": "µg"
                    },
                    "TOCPHA": {
                        "label": "Vitamin E",
                        "quantity": 7.6346333333333325,
                        "unit": "mg"
                    },
                    "VITK1": {
                        "label": "Vitamin K",
                        "quantity": 331.5040000000001,
                        "unit": "µg"
                    },
                    "WATER": {
                        "label": "Water",
                        "quantity": 989.2636899469982,
                        "unit": "g"
                    }
                },
                "totalDaily": {
                    "ENERC_KCAL": {
                        "label": "Energy",
                        "quantity": 50.23300905833334,
                        "unit": "%"
                    },
                    "FAT": {
                        "label": "Fat",
                        "quantity": 60.76869910820512,
                        "unit": "%"
                    },
                    "FASAT": {
                        "label": "Saturated",
                        "quantity": 29.62097480183333,
                        "unit": "%"
                    },
                    "CHOCDF": {
                        "label": "Carbs",
                        "quantity": 25.48615555555556,
                        "unit": "%"
                    },
                    "FIBTG": {
                        "label": "Fiber",
                        "quantity": 102.71066666666667,
                        "unit": "%"
                    },
                    "PROCNT": {
                        "label": "Protein",
                        "quantity": 210.67053274000003,
                        "unit": "%"
                    },
                    "CHOLE": {
                        "label": "Cholesterol",
                        "quantity": 243.4279052333334,
                        "unit": "%"
                    },
                    "NA": {
                        "label": "Sodium",
                        "quantity": 118.39849102448332,
                        "unit": "%"
                    },
                    "CA": {
                        "label": "Calcium",
                        "quantity": 47.98117408397656,
                        "unit": "%"
                    },
                    "MG": {
                        "label": "Magnesium",
                        "quantity": 79.27885448452149,
                        "unit": "%"
                    },
                    "K": {
                        "label": "Potassium",
                        "quantity": 75.60354038609763,
                        "unit": "%"
                    },
                    "FE": {
                        "label": "Iron",
                        "quantity": 42.71215132155617,
                        "unit": "%"
                    },
                    "ZN": {
                        "label": "Zinc",
                        "quantity": 83.5337002257487,
                        "unit": "%"
                    },
                    "P": {
                        "label": "Phosphorus",
                        "quantity": 195.80157216190477,
                        "unit": "%"
                    },
                    "VITA_RAE": {
                        "label": "Vitamin A",
                        "quantity": 29.2362962962963,
                        "unit": "%"
                    },
                    "VITC": {
                        "label": "Vitamin C",
                        "quantity": 188.62129629629626,
                        "unit": "%"
                    },
                    "THIA": {
                        "label": "Thiamin (B1)",
                        "quantity": 42.880277777777785,
                        "unit": "%"
                    },
                    "RIBF": {
                        "label": "Riboflavin (B2)",
                        "quantity": 41.81666666666666,
                        "unit": "%"
                    },
                    "NIA": {
                        "label": "Niacin (B3)",
                        "quantity": 51.580000000000005,
                        "unit": "%"
                    },
                    "VITB6A": {
                        "label": "Vitamin B6",
                        "quantity": 92.8952564102564,
                        "unit": "%"
                    },
                    "FOLDFE": {
                        "label": "Folate equivalent (total)",
                        "quantity": 80.87833333333334,
                        "unit": "%"
                    },
                    "VITB12": {
                        "label": "Vitamin B12",
                        "quantity": 0.0,
                        "unit": "%"
                    },
                    "VITD": {
                        "label": "Vitamin D",
                        "quantity": 0.0,
                        "unit": "%"
                    },
                    "TOCPHA": {
                        "label": "Vitamin E",
                        "quantity": 50.89755555555555,
                        "unit": "%"
                    },
                    "VITK1": {
                        "label": "Vitamin K",
                        "quantity": 276.2533333333334,
                        "unit": "%"
                    }
                },
                "digest": [
                    {
                        "label": "Fat",
                        "tag": "FAT",
                        "schemaOrgTag": "fatContent",
                        "total": 39.49965442033333,
                        "hasRDI": True,
                        "daily": 60.76869910820512,
                        "unit": "g",
                        "sub": [
                            {
                                "label": "Saturated",
                                "tag": "FASAT",
                                "schemaOrgTag": "saturatedFatContent",
                                "total": 5.924194960366666,
                                "hasRDI": True,
                                "daily": 29.62097480183333,
                                "unit": "g"
                            },
                            {
                                "label": "Trans",
                                "tag": "FATRN",
                                "schemaOrgTag": "transFatContent",
                                "total": 0.018143694800000002,
                                "hasRDI": False,
                                "daily": 0.0,
                                "unit": "g"
                            },
                            {
                                "label": "Monounsaturated",
                                "tag": "FAMS",
                                "schemaOrgTag": '',
                                "total": 24.169284438200005,
                                "hasRDI": False,
                                "daily": 0.0,
                                "unit": "g"
                            },
                            {
                                "label": "Polyunsaturated",
                                "tag": "FAPU",
                                "schemaOrgTag": '',
                                "total": 6.046912069066666,
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
                        "total": 76.45846666666668,
                        "hasRDI": True,
                        "daily": 25.48615555555556,
                        "unit": "g",
                        "sub": [
                            {
                                "label": "Carbs (net)",
                                "tag": "CHOCDF.net",
                                "schemaOrgTag": '',
                                "total": 50.78080000000001,
                                "hasRDI": False,
                                "daily": 0.0,
                                "unit": "g"
                            },
                            {
                                "label": "Fiber",
                                "tag": "FIBTG",
                                "schemaOrgTag": "fiberContent",
                                "total": 25.677666666666667,
                                "hasRDI": True,
                                "daily": 102.71066666666667,
                                "unit": "g"
                            },
                            {
                                "label": "Sugars",
                                "tag": "SUGAR",
                                "schemaOrgTag": "sugarContent",
                                "total": 18.84161666666667,
                                "hasRDI": False,
                                "daily": 0.0,
                                "unit": "g"
                            },
                            {
                                "label": "Sugars, added",
                                "tag": "SUGAR.added",
                                "schemaOrgTag": '',
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
                        "total": 105.33526637000001,
                        "hasRDI": True,
                        "daily": 210.67053274000003,
                        "unit": "g"
                    },
                    {
                        "label": "Cholesterol",
                        "tag": "CHOLE",
                        "schemaOrgTag": "cholesterolContent",
                        "total": 730.2837157000001,
                        "hasRDI": True,
                        "daily": 243.4279052333334,
                        "unit": "mg"
                    },
                    {
                        "label": "Sodium",
                        "tag": "NA",
                        "schemaOrgTag": "sodiumContent",
                        "total": 2841.5637845876,
                        "hasRDI": True,
                        "daily": 118.39849102448332,
                        "unit": "mg"
                    },
                    {
                        "label": "Calcium",
                        "tag": "CA",
                        "schemaOrgTag": '',
                        "total": 479.8117408397656,
                        "hasRDI": True,
                        "daily": 47.98117408397656,
                        "unit": "mg"
                    },
                    {
                        "label": "Magnesium",
                        "tag": "MG",
                        "schemaOrgTag": '',
                        "total": 332.97118883499024,
                        "hasRDI": True,
                        "daily": 79.27885448452149,
                        "unit": "mg"
                    },
                    {
                        "label": "Potassium",
                        "tag": "K",
                        "schemaOrgTag": '',
                        "total": 3553.3663981465893,
                        "hasRDI": True,
                        "daily": 75.60354038609763,
                        "unit": "mg"
                    },
                    {
                        "label": "Iron",
                        "tag": "FE",
                        "schemaOrgTag": '',
                        "total": 7.68818723788011,
                        "hasRDI": True,
                        "daily": 42.71215132155617,
                        "unit": "mg"
                    },
                    {
                        "label": "Zinc",
                        "tag": "ZN",
                        "schemaOrgTag": '',
                        "total": 9.188707024832357,
                        "hasRDI": True,
                        "daily": 83.5337002257487,
                        "unit": "mg"
                    },
                    {
                        "label": "Phosphorus",
                        "tag": "P",
                        "schemaOrgTag": '',
                        "total": 1370.6110051333333,
                        "hasRDI": True,
                        "daily": 195.80157216190477,
                        "unit": "mg"
                    },
                    {
                        "label": "Vitamin A",
                        "tag": "VITA_RAE",
                        "schemaOrgTag": '',
                        "total": 263.12666666666667,
                        "hasRDI": True,
                        "daily": 29.2362962962963,
                        "unit": "µg"
                    },
                    {
                        "label": "Vitamin C",
                        "tag": "VITC",
                        "schemaOrgTag": '',
                        "total": 169.75916666666666,
                        "hasRDI": True,
                        "daily": 188.62129629629626,
                        "unit": "mg"
                    },
                    {
                        "label": "Thiamin (B1)",
                        "tag": "THIA",
                        "schemaOrgTag": '',
                        "total": 0.5145633333333334,
                        "hasRDI": True,
                        "daily": 42.880277777777785,
                        "unit": "mg"
                    },
                    {
                        "label": "Riboflavin (B2)",
                        "tag": "RIBF",
                        "schemaOrgTag": '',
                        "total": 0.5436166666666666,
                        "hasRDI": True,
                        "daily": 41.81666666666666,
                        "unit": "mg"
                    },
                    {
                        "label": "Niacin (B3)",
                        "tag": "NIA",
                        "schemaOrgTag": '',
                        "total": 8.2528,
                        "hasRDI": True,
                        "daily": 51.580000000000005,
                        "unit": "mg"
                    },
                    {
                        "label": "Vitamin B6",
                        "tag": "VITB6A",
                        "schemaOrgTag": '',
                        "total": 1.2076383333333331,
                        "hasRDI": True,
                        "daily": 92.8952564102564,
                        "unit": "mg"
                    },
                    {
                        "label": "Folate equivalent (total)",
                        "tag": "FOLDFE",
                        "schemaOrgTag": '',
                        "total": 323.5133333333334,
                        "hasRDI": True,
                        "daily": 80.87833333333334,
                        "unit": "µg"
                    },
                    {
                        "label": "Folate (food)",
                        "tag": "FOLFD",
                        "schemaOrgTag": '',
                        "total": 323.5133333333334,
                        "hasRDI": False,
                        "daily": 0.0,
                        "unit": "µg"
                    },
                    {
                        "label": "Folic acid",
                        "tag": "FOLAC",
                        "schemaOrgTag": '',
                        "total": 0.0,
                        "hasRDI": False,
                        "daily": 0.0,
                        "unit": "µg"
                    },
                    {
                        "label": "Vitamin B12",
                        "tag": "VITB12",
                        "schemaOrgTag": '',
                        "total": 0.0,
                        "hasRDI": True,
                        "daily": 0.0,
                        "unit": "µg"
                    },
                    {
                        "label": "Vitamin D",
                        "tag": "VITD",
                        "schemaOrgTag": '',
                        "total": 0.0,
                        "hasRDI": True,
                        "daily": 0.0,
                        "unit": "µg"
                    },
                    {
                        "label": "Vitamin E",
                        "tag": "TOCPHA",
                        "schemaOrgTag": '',
                        "total": 7.6346333333333325,
                        "hasRDI": True,
                        "daily": 50.89755555555555,
                        "unit": "mg"
                    },
                    {
                        "label": "Vitamin K",
                        "tag": "VITK1",
                        "schemaOrgTag": '',
                        "total": 331.5040000000001,
                        "hasRDI": True,
                        "daily": 276.2533333333334,
                        "unit": "µg"
                    },
                    {
                        "label": "Sugar alcohols",
                        "tag": "Sugar.alcohol",
                        "schemaOrgTag": '',
                        "total": 0.0,
                        "hasRDI": False,
                        "daily": 0.0,
                        "unit": "g"
                    },
                    {
                        "label": "Water",
                        "tag": "WATER",
                        "schemaOrgTag": '',
                        "total": 989.2636899469982,
                        "hasRDI": False,
                        "daily": 0.0,
                        "unit": "g"
                    }
                ]
            },
            "_links": {
                "self": {
                    "title": "Self",
                    "href": "https://api.edamam.com/api/recipes/v2/6055b587f0ebc2d4ecea6e0d02f11f6a?type=public&app_id=e909afd5&app_key=34e59dda7e1bffb92e49c416e9449e1d"
                }
            }
        },
        {
            "recipe": {
                "uri": "http://www.edamam.com/ontologies/edamam.owl#recipe_66b2a1e54bdb227504a8e091877a08e8",
                "label": "Chicken Tacos",
                "image": "https://edamam-product-images.s3.amazonaws.com/web-img/371/3710a81fe4b9d12b302b08a2eaf4d387.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLWVhc3QtMSJIMEYCIQCP2Gbt%2ByPQIVKV%2FafgML7WXbkOusL9fCs6d1le6dFKYAIhAJcnuEh%2B1NzOso38QgGaVBwaVQAMxyMJATg%2FR%2Fl0jl96KsEFCJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMMTg3MDE3MTUwOTg2IgydADkJdybnmhdEGwQqlQUNCCJJEzulouVCRRPPDPN9Ik9nmgPZk%2Fam6u04CTug5FWfzto4W1y6mlAuXr3EHPB%2FvTcZ%2BmAkgcS5%2FRfKsviGgYg1PBDbKvJFWJigqXNb6jHaHO3eyZnXpof0Qk2PachTFyGGF7upzvEiKr6BGB6DtCoEGe3wCd0iFSMS%2Ft8LIlICGGYaaCvWq9TXeaXkel5jju8XxawzfW0OY8ad1NODjiJJ%2FJ02goRzRa3HwZdXj0P4%2FwwiBHg8BMnsBu5XvhNCt9Gz%2Bxp9cZIC8TMv%2FY8rOvepaH28zVl5BjLGle3tn5syTeLiH6OS68I4OndB2qqeqZqdi9cu6zb1H0y8aKh8r8IIaHqXhP6jBXwOxUN8uimNrMJnaDPxNdvFPuR5yx8UApiuserTd1b1ZIBFiBJ6lavYUBrkLW%2B7bZIJltsNTSxF2GTKFWoXHKGf3%2FXYj%2FniRUh%2BB3xUXrXh8PzVKChkdfuCxirnj5UG2XCrj22%2BBJG8S8UHiExHaIwt01Nel6V7Y0IlXWvwqK8YEx%2FHOI%2FewXERfrnIQDCsrQyC7qTLL3HndUW2Ke8ib2iC%2BPgaP6xDqkqdlhOSojQHG4rfwcyVOFOzeauzAO7Rc77mb0rCUJdMckP6nKiD7nrtjlZXznFmYhCvjmWQF2l06Jl7xQsr%2BjkGAeoXo9X%2FiC11ZTNfxOVIe3LWWkRvMwGWvgvtgF4ZEDGaLXgsbO4I8%2FpSmGD4ox9ZWDfX%2BtTURCyBYVXqYpQ4TpgMhHqAtTUr4TNc7GRLVbfi1xqZNQDt1Sfdzh3Xq88dOJyKsyUs7rcFuuxoNyxvqstWVaAyRglOH1n%2BpV0xA7%2FKEHa%2F8%2FzH6uaXeIp3eLJN1%2BGlAQc1sP2jehPHqGi5Lc7YMOKk8akGOrABqEMeyIMA72vRUvaZqcs7N77uX3kDw2%2BTfyF8pS8HYdR1%2BEU1ekEPGlPPLyTo0NFmbmMa4urw%2B19eIvlGSnFjiSeee%2F%2BeotdKLVnDgZ5aNxOYivkgUqjazWNTWX1qdv7Jq7GWrNDLwjZiU5zLvpcjSyzLyGAVIo8pW14m4aC3jppuzjKpasygGK2%2Bf%2BmxisMAkIdRRS5aXW9PY%2FuwiBnL3qiZT5RtAdamISZZM9jUAWY%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231028T003610Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFPXEGMX3T%2F20231028%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=52640bb04caddd2271d407c1cce110fed98a162e61f5df0e656bb51c83822f39",
                "images": {
                    "THUMBNAIL": {
                        "url": "https://edamam-product-images.s3.amazonaws.com/web-img/371/3710a81fe4b9d12b302b08a2eaf4d387-s.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLWVhc3QtMSJIMEYCIQCP2Gbt%2ByPQIVKV%2FafgML7WXbkOusL9fCs6d1le6dFKYAIhAJcnuEh%2B1NzOso38QgGaVBwaVQAMxyMJATg%2FR%2Fl0jl96KsEFCJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMMTg3MDE3MTUwOTg2IgydADkJdybnmhdEGwQqlQUNCCJJEzulouVCRRPPDPN9Ik9nmgPZk%2Fam6u04CTug5FWfzto4W1y6mlAuXr3EHPB%2FvTcZ%2BmAkgcS5%2FRfKsviGgYg1PBDbKvJFWJigqXNb6jHaHO3eyZnXpof0Qk2PachTFyGGF7upzvEiKr6BGB6DtCoEGe3wCd0iFSMS%2Ft8LIlICGGYaaCvWq9TXeaXkel5jju8XxawzfW0OY8ad1NODjiJJ%2FJ02goRzRa3HwZdXj0P4%2FwwiBHg8BMnsBu5XvhNCt9Gz%2Bxp9cZIC8TMv%2FY8rOvepaH28zVl5BjLGle3tn5syTeLiH6OS68I4OndB2qqeqZqdi9cu6zb1H0y8aKh8r8IIaHqXhP6jBXwOxUN8uimNrMJnaDPxNdvFPuR5yx8UApiuserTd1b1ZIBFiBJ6lavYUBrkLW%2B7bZIJltsNTSxF2GTKFWoXHKGf3%2FXYj%2FniRUh%2BB3xUXrXh8PzVKChkdfuCxirnj5UG2XCrj22%2BBJG8S8UHiExHaIwt01Nel6V7Y0IlXWvwqK8YEx%2FHOI%2FewXERfrnIQDCsrQyC7qTLL3HndUW2Ke8ib2iC%2BPgaP6xDqkqdlhOSojQHG4rfwcyVOFOzeauzAO7Rc77mb0rCUJdMckP6nKiD7nrtjlZXznFmYhCvjmWQF2l06Jl7xQsr%2BjkGAeoXo9X%2FiC11ZTNfxOVIe3LWWkRvMwGWvgvtgF4ZEDGaLXgsbO4I8%2FpSmGD4ox9ZWDfX%2BtTURCyBYVXqYpQ4TpgMhHqAtTUr4TNc7GRLVbfi1xqZNQDt1Sfdzh3Xq88dOJyKsyUs7rcFuuxoNyxvqstWVaAyRglOH1n%2BpV0xA7%2FKEHa%2F8%2FzH6uaXeIp3eLJN1%2BGlAQc1sP2jehPHqGi5Lc7YMOKk8akGOrABqEMeyIMA72vRUvaZqcs7N77uX3kDw2%2BTfyF8pS8HYdR1%2BEU1ekEPGlPPLyTo0NFmbmMa4urw%2B19eIvlGSnFjiSeee%2F%2BeotdKLVnDgZ5aNxOYivkgUqjazWNTWX1qdv7Jq7GWrNDLwjZiU5zLvpcjSyzLyGAVIo8pW14m4aC3jppuzjKpasygGK2%2Bf%2BmxisMAkIdRRS5aXW9PY%2FuwiBnL3qiZT5RtAdamISZZM9jUAWY%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231028T003610Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFPXEGMX3T%2F20231028%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=7ca770457eaa539acc6ca3aefec6b1e84ce027c680de7df4af76bc5c5ea67abc",
                        "width": 100,
                        "height": 100
                    },
                    "SMALL": {
                        "url": "https://edamam-product-images.s3.amazonaws.com/web-img/371/3710a81fe4b9d12b302b08a2eaf4d387-m.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLWVhc3QtMSJIMEYCIQCP2Gbt%2ByPQIVKV%2FafgML7WXbkOusL9fCs6d1le6dFKYAIhAJcnuEh%2B1NzOso38QgGaVBwaVQAMxyMJATg%2FR%2Fl0jl96KsEFCJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMMTg3MDE3MTUwOTg2IgydADkJdybnmhdEGwQqlQUNCCJJEzulouVCRRPPDPN9Ik9nmgPZk%2Fam6u04CTug5FWfzto4W1y6mlAuXr3EHPB%2FvTcZ%2BmAkgcS5%2FRfKsviGgYg1PBDbKvJFWJigqXNb6jHaHO3eyZnXpof0Qk2PachTFyGGF7upzvEiKr6BGB6DtCoEGe3wCd0iFSMS%2Ft8LIlICGGYaaCvWq9TXeaXkel5jju8XxawzfW0OY8ad1NODjiJJ%2FJ02goRzRa3HwZdXj0P4%2FwwiBHg8BMnsBu5XvhNCt9Gz%2Bxp9cZIC8TMv%2FY8rOvepaH28zVl5BjLGle3tn5syTeLiH6OS68I4OndB2qqeqZqdi9cu6zb1H0y8aKh8r8IIaHqXhP6jBXwOxUN8uimNrMJnaDPxNdvFPuR5yx8UApiuserTd1b1ZIBFiBJ6lavYUBrkLW%2B7bZIJltsNTSxF2GTKFWoXHKGf3%2FXYj%2FniRUh%2BB3xUXrXh8PzVKChkdfuCxirnj5UG2XCrj22%2BBJG8S8UHiExHaIwt01Nel6V7Y0IlXWvwqK8YEx%2FHOI%2FewXERfrnIQDCsrQyC7qTLL3HndUW2Ke8ib2iC%2BPgaP6xDqkqdlhOSojQHG4rfwcyVOFOzeauzAO7Rc77mb0rCUJdMckP6nKiD7nrtjlZXznFmYhCvjmWQF2l06Jl7xQsr%2BjkGAeoXo9X%2FiC11ZTNfxOVIe3LWWkRvMwGWvgvtgF4ZEDGaLXgsbO4I8%2FpSmGD4ox9ZWDfX%2BtTURCyBYVXqYpQ4TpgMhHqAtTUr4TNc7GRLVbfi1xqZNQDt1Sfdzh3Xq88dOJyKsyUs7rcFuuxoNyxvqstWVaAyRglOH1n%2BpV0xA7%2FKEHa%2F8%2FzH6uaXeIp3eLJN1%2BGlAQc1sP2jehPHqGi5Lc7YMOKk8akGOrABqEMeyIMA72vRUvaZqcs7N77uX3kDw2%2BTfyF8pS8HYdR1%2BEU1ekEPGlPPLyTo0NFmbmMa4urw%2B19eIvlGSnFjiSeee%2F%2BeotdKLVnDgZ5aNxOYivkgUqjazWNTWX1qdv7Jq7GWrNDLwjZiU5zLvpcjSyzLyGAVIo8pW14m4aC3jppuzjKpasygGK2%2Bf%2BmxisMAkIdRRS5aXW9PY%2FuwiBnL3qiZT5RtAdamISZZM9jUAWY%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231028T003610Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFPXEGMX3T%2F20231028%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=c94826d60b9781f05863694f01e205e899da94cc501f2d321428c97a1904ba19",
                        "width": 200,
                        "height": 200
                    },
                    "REGULAR": {
                        "url": "https://edamam-product-images.s3.amazonaws.com/web-img/371/3710a81fe4b9d12b302b08a2eaf4d387.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLWVhc3QtMSJIMEYCIQCP2Gbt%2ByPQIVKV%2FafgML7WXbkOusL9fCs6d1le6dFKYAIhAJcnuEh%2B1NzOso38QgGaVBwaVQAMxyMJATg%2FR%2Fl0jl96KsEFCJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMMTg3MDE3MTUwOTg2IgydADkJdybnmhdEGwQqlQUNCCJJEzulouVCRRPPDPN9Ik9nmgPZk%2Fam6u04CTug5FWfzto4W1y6mlAuXr3EHPB%2FvTcZ%2BmAkgcS5%2FRfKsviGgYg1PBDbKvJFWJigqXNb6jHaHO3eyZnXpof0Qk2PachTFyGGF7upzvEiKr6BGB6DtCoEGe3wCd0iFSMS%2Ft8LIlICGGYaaCvWq9TXeaXkel5jju8XxawzfW0OY8ad1NODjiJJ%2FJ02goRzRa3HwZdXj0P4%2FwwiBHg8BMnsBu5XvhNCt9Gz%2Bxp9cZIC8TMv%2FY8rOvepaH28zVl5BjLGle3tn5syTeLiH6OS68I4OndB2qqeqZqdi9cu6zb1H0y8aKh8r8IIaHqXhP6jBXwOxUN8uimNrMJnaDPxNdvFPuR5yx8UApiuserTd1b1ZIBFiBJ6lavYUBrkLW%2B7bZIJltsNTSxF2GTKFWoXHKGf3%2FXYj%2FniRUh%2BB3xUXrXh8PzVKChkdfuCxirnj5UG2XCrj22%2BBJG8S8UHiExHaIwt01Nel6V7Y0IlXWvwqK8YEx%2FHOI%2FewXERfrnIQDCsrQyC7qTLL3HndUW2Ke8ib2iC%2BPgaP6xDqkqdlhOSojQHG4rfwcyVOFOzeauzAO7Rc77mb0rCUJdMckP6nKiD7nrtjlZXznFmYhCvjmWQF2l06Jl7xQsr%2BjkGAeoXo9X%2FiC11ZTNfxOVIe3LWWkRvMwGWvgvtgF4ZEDGaLXgsbO4I8%2FpSmGD4ox9ZWDfX%2BtTURCyBYVXqYpQ4TpgMhHqAtTUr4TNc7GRLVbfi1xqZNQDt1Sfdzh3Xq88dOJyKsyUs7rcFuuxoNyxvqstWVaAyRglOH1n%2BpV0xA7%2FKEHa%2F8%2FzH6uaXeIp3eLJN1%2BGlAQc1sP2jehPHqGi5Lc7YMOKk8akGOrABqEMeyIMA72vRUvaZqcs7N77uX3kDw2%2BTfyF8pS8HYdR1%2BEU1ekEPGlPPLyTo0NFmbmMa4urw%2B19eIvlGSnFjiSeee%2F%2BeotdKLVnDgZ5aNxOYivkgUqjazWNTWX1qdv7Jq7GWrNDLwjZiU5zLvpcjSyzLyGAVIo8pW14m4aC3jppuzjKpasygGK2%2Bf%2BmxisMAkIdRRS5aXW9PY%2FuwiBnL3qiZT5RtAdamISZZM9jUAWY%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231028T003610Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFPXEGMX3T%2F20231028%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=52640bb04caddd2271d407c1cce110fed98a162e61f5df0e656bb51c83822f39",
                        "width": 300,
                        "height": 300
                    },
                    "LARGE": {
                        "url": "https://edamam-product-images.s3.amazonaws.com/web-img/371/3710a81fe4b9d12b302b08a2eaf4d387-l.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLWVhc3QtMSJIMEYCIQCP2Gbt%2ByPQIVKV%2FafgML7WXbkOusL9fCs6d1le6dFKYAIhAJcnuEh%2B1NzOso38QgGaVBwaVQAMxyMJATg%2FR%2Fl0jl96KsEFCJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMMTg3MDE3MTUwOTg2IgydADkJdybnmhdEGwQqlQUNCCJJEzulouVCRRPPDPN9Ik9nmgPZk%2Fam6u04CTug5FWfzto4W1y6mlAuXr3EHPB%2FvTcZ%2BmAkgcS5%2FRfKsviGgYg1PBDbKvJFWJigqXNb6jHaHO3eyZnXpof0Qk2PachTFyGGF7upzvEiKr6BGB6DtCoEGe3wCd0iFSMS%2Ft8LIlICGGYaaCvWq9TXeaXkel5jju8XxawzfW0OY8ad1NODjiJJ%2FJ02goRzRa3HwZdXj0P4%2FwwiBHg8BMnsBu5XvhNCt9Gz%2Bxp9cZIC8TMv%2FY8rOvepaH28zVl5BjLGle3tn5syTeLiH6OS68I4OndB2qqeqZqdi9cu6zb1H0y8aKh8r8IIaHqXhP6jBXwOxUN8uimNrMJnaDPxNdvFPuR5yx8UApiuserTd1b1ZIBFiBJ6lavYUBrkLW%2B7bZIJltsNTSxF2GTKFWoXHKGf3%2FXYj%2FniRUh%2BB3xUXrXh8PzVKChkdfuCxirnj5UG2XCrj22%2BBJG8S8UHiExHaIwt01Nel6V7Y0IlXWvwqK8YEx%2FHOI%2FewXERfrnIQDCsrQyC7qTLL3HndUW2Ke8ib2iC%2BPgaP6xDqkqdlhOSojQHG4rfwcyVOFOzeauzAO7Rc77mb0rCUJdMckP6nKiD7nrtjlZXznFmYhCvjmWQF2l06Jl7xQsr%2BjkGAeoXo9X%2FiC11ZTNfxOVIe3LWWkRvMwGWvgvtgF4ZEDGaLXgsbO4I8%2FpSmGD4ox9ZWDfX%2BtTURCyBYVXqYpQ4TpgMhHqAtTUr4TNc7GRLVbfi1xqZNQDt1Sfdzh3Xq88dOJyKsyUs7rcFuuxoNyxvqstWVaAyRglOH1n%2BpV0xA7%2FKEHa%2F8%2FzH6uaXeIp3eLJN1%2BGlAQc1sP2jehPHqGi5Lc7YMOKk8akGOrABqEMeyIMA72vRUvaZqcs7N77uX3kDw2%2BTfyF8pS8HYdR1%2BEU1ekEPGlPPLyTo0NFmbmMa4urw%2B19eIvlGSnFjiSeee%2F%2BeotdKLVnDgZ5aNxOYivkgUqjazWNTWX1qdv7Jq7GWrNDLwjZiU5zLvpcjSyzLyGAVIo8pW14m4aC3jppuzjKpasygGK2%2Bf%2BmxisMAkIdRRS5aXW9PY%2FuwiBnL3qiZT5RtAdamISZZM9jUAWY%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231028T003610Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFPXEGMX3T%2F20231028%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=d31e2e60f42329c8973dd759e2a94ca977604c2d9776f3f3c6c873cc776db03d",
                        "width": 600,
                        "height": 600
                    }
                },
                "source": "Real Simple",
                "url": "http://www.realsimple.com/food-recipes/browse-all-recipes/chicken-tacos-10000001132654/index.html",
                "shareAs": "http://www.edamam.com/recipe/chicken-tacos-66b2a1e54bdb227504a8e091877a08e8/tacos",
                "yield": 14.0,
                "dietLabels": [
                    "Low-Carb"
                ],
                "healthLabels": [
                    "Sugar-Conscious",
                    "Keto-Friendly",
                    "Egg-Free",
                    "Peanut-Free",
                    "Tree-Nut-Free",
                    "Soy-Free",
                    "Fish-Free",
                    "Shellfish-Free",
                    "Pork-Free",
                    "Red-Meat-Free",
                    "Crustacean-Free",
                    "Celery-Free",
                    "Mustard-Free",
                    "Sesame-Free",
                    "Lupine-Free",
                    "Mollusk-Free",
                    "Alcohol-Free",
                    "Sulfite-Free"
                ],
                "cautions": [
                    "Eggs",
                    "Milk",
                    "Sulfites"
                ],
                "ingredientLines": [
                    "1 store-bought rotisserie chicken",
                    "2 cups store-bought red or green salsa",
                    "8 taco shells",
                    "1 cup (4 ounces) grated Cheddar or Monterey Jack cheese",
                    "8 sprigs fresh cilantro (optional)",
                    "1/2 cup sour cream",
                    "1 avocado, chopped",
                    "1 lime, quartered"
                ],
                "ingredients": [
                    {
                        "text": "1 store-bought rotisserie chicken",
                        "quantity": 1.0,
                        "measure": "<unit>",
                        "food": "chicken",
                        "weight": 1200.0,
                        "foodCategory": "Poultry",
                        "foodId": "food_bmyxrshbfao9s1amjrvhoauob6mo",
                        "image": "https://www.edamam.com/food-img/d33/d338229d774a743f7858f6764e095878.jpg"
                    },
                    {
                        "text": "2 cups store-bought red or green salsa",
                        "quantity": 2.0,
                        "measure": "cup",
                        "food": "salsa",
                        "weight": 518.0,
                        "foodCategory": "canned soup",
                        "foodId": "food_b0t3obfawlm5k2b6erxscacez35u",
                        "image": "https://www.edamam.com/food-img/995/995d0f166754a0475c181b9c156fec43.jpg"
                    },
                    {
                        "text": "8 taco shells",
                        "quantity": 8.0,
                        "measure": "<unit>",
                        "food": "taco shells",
                        "weight": 101.6,
                        "foodCategory": "quick breads and pastries",
                        "foodId": "food_amx6njaaa4q9lsaz4k98faejx12a",
                        "image": "https://www.edamam.com/food-img/def/def506222dc404affdfbf7b7133a34c6.jpg"
                    },
                    {
                        "text": "1 cup (4 ounces) grated Cheddar or Monterey Jack cheese",
                        "quantity": 4.0,
                        "measure": "ounce",
                        "food": "Jack cheese",
                        "weight": 113.3980925,
                        "foodCategory": "Cheese",
                        "foodId": "food_atp17pta7d5it2a80ct13ard6aj3",
                        "image": "https://www.edamam.com/food-img/590/59062b9f8d57ebc7d831b7b7c231f726.jpg"
                    },
                    {
                        "text": "8 sprigs fresh cilantro (optional)",
                        "quantity": 8.0,
                        "measure": "sprig",
                        "food": "cilantro",
                        "weight": 17.77777777777778,
                        "foodCategory": "vegetables",
                        "foodId": "food_alhzhuwb4lc7jnb5s6f02by60bzp",
                        "image": "https://www.edamam.com/food-img/d57/d57e375b6ff99a90c7ee2b1990a1af36.jpg"
                    },
                    {
                        "text": "1/2 cup sour cream",
                        "quantity": 0.5,
                        "measure": "cup",
                        "food": "sour cream",
                        "weight": 115.0,
                        "foodCategory": "Dairy",
                        "foodId": "food_adp9fcubzl3lr7bcvzn3rbfiiiwq",
                        "image": "https://www.edamam.com/food-img/f9d/f9d6183267b041b0aff9a10b89c9c15f.jpg"
                    },
                    {
                        "text": "1 avocado, chopped",
                        "quantity": 1.0,
                        "measure": "<unit>",
                        "food": "avocado",
                        "weight": 201.0,
                        "foodCategory": "fruit",
                        "foodId": "food_b0yuze4b1g3afpanijno5abtiu28",
                        "image": "https://www.edamam.com/food-img/984/984a707ea8e9c6bf5f6498970a9e6d9d.jpg"
                    },
                    {
                        "text": "1 lime, quartered",
                        "quantity": 1.0,
                        "measure": "<unit>",
                        "food": "lime",
                        "weight": 67.0,
                        "foodCategory": "fruit",
                        "foodId": "food_av58muyb8kg92fbk0g8g8aui5knv",
                        "image": "https://www.edamam.com/food-img/48a/48a123c9576647c4ada6a41df5eeb22a.jpg"
                    }
                ],
                "calories": 4210.299773913889,
                "totalCO2Emissions": 18786.525115566666,
                "co2EmissionsClass": "F",
                "totalWeight": 2333.775870277778,
                "totalTime": 0.0,
                "cuisineType": [
                    "mexican"
                ],
                "mealType": [
                    "lunch/dinner"
                ],
                "dishType": [
                    "sandwiches"
                ],
                "totalNutrients": {
                    "ENERC_KCAL": {
                        "label": "Energy",
                        "quantity": 4210.299773913889,
                        "unit": "kcal"
                    },
                    "FAT": {
                        "label": "Fat",
                        "quantity": 290.67246647194446,
                        "unit": "g"
                    },
                    "FASAT": {
                        "label": "Saturated",
                        "quantity": 96.61494455638889,
                        "unit": "g"
                    },
                    "FATRN": {
                        "label": "Trans",
                        "quantity": 2.2541520000000004,
                        "unit": "g"
                    },
                    "FAMS": {
                        "label": "Monounsaturated",
                        "quantity": 116.98473198263889,
                        "unit": "g"
                    },
                    "FAPU": {
                        "label": "Polyunsaturated",
                        "quantity": 50.39364996268611,
                        "unit": "g"
                    },
                    "CHOCDF": {
                        "label": "Carbs",
                        "quantity": 129.83955147344446,
                        "unit": "g"
                    },
                    "CHOCDF.net": {
                        "label": "Carbohydrates (net)",
                        "quantity": 97.34957369566668,
                        "unit": "g"
                    },
                    "FIBTG": {
                        "label": "Fiber",
                        "quantity": 32.48997777777778,
                        "unit": "g"
                    },
                    "SUGAR": {
                        "label": "Sugars",
                        "quantity": 29.397857129166674,
                        "unit": "g"
                    },
                    "PROCNT": {
                        "label": "Protein",
                        "quantity": 273.0423593291667,
                        "unit": "g"
                    },
                    "CHOLE": {
                        "label": "Cholesterol",
                        "quantity": 1068.774302325,
                        "unit": "mg"
                    },
                    "NA": {
                        "label": "Sodium",
                        "quantity": 5591.790332777778,
                        "unit": "mg"
                    },
                    "CA": {
                        "label": "Calcium",
                        "quantity": 1409.240881161111,
                        "unit": "mg"
                    },
                    "MG": {
                        "label": "Magnesium",
                        "quantity": 511.07770719722225,
                        "unit": "mg"
                    },
                    "K": {
                        "label": "Potassium",
                        "quantity": 5298.610677147222,
                        "unit": "mg"
                    },
                    "FE": {
                        "label": "Iron",
                        "quantity": 17.36097293266667,
                        "unit": "mg"
                    },
                    "ZN": {
                        "label": "Zinc",
                        "quantity": 23.518591663888888,
                        "unit": "mg"
                    },
                    "P": {
                        "label": "Phosphorus",
                        "quantity": 2887.6688640333336,
                        "unit": "mg"
                    },
                    "VITA_RAE": {
                        "label": "Vitamin A",
                        "quantity": 1054.605334261111,
                        "unit": "µg"
                    },
                    "VITC": {
                        "label": "Vitamin C",
                        "quantity": 74.474,
                        "unit": "mg"
                    },
                    "THIA": {
                        "label": "Thiamin (B1)",
                        "quantity": 1.3170868249861112,
                        "unit": "mg"
                    },
                    "RIBF": {
                        "label": "Riboflavin (B2)",
                        "quantity": 2.6259925607499994,
                        "unit": "mg"
                    },
                    "NIA": {
                        "label": "Niacin (B3)",
                        "quantity": 93.18726355935831,
                        "unit": "mg"
                    },
                    "VITB6A": {
                        "label": "Vitamin B6",
                        "quantity": 6.0058113819638885,
                        "unit": "mg"
                    },
                    "FOLDFE": {
                        "label": "Folate equivalent (total)",
                        "quantity": 385.5838788722223,
                        "unit": "µg"
                    },
                    "FOLFD": {
                        "label": "Folate (food)",
                        "quantity": 345.95987887222225,
                        "unit": "µg"
                    },
                    "FOLAC": {
                        "label": "Folic acid",
                        "quantity": 24.384,
                        "unit": "µg"
                    },
                    "VITB12": {
                        "label": "Vitamin B12",
                        "quantity": 4.9027041677500005,
                        "unit": "µg"
                    },
                    "VITD": {
                        "label": "Vitamin D",
                        "quantity": 3.0803885550000003,
                        "unit": "µg"
                    },
                    "TOCPHA": {
                        "label": "Vitamin E",
                        "quantity": 16.415819484944446,
                        "unit": "mg"
                    },
                    "VITK1": {
                        "label": "Vitamin K",
                        "quantity": 151.2946634236111,
                        "unit": "µg"
                    },
                    "WATER": {
                        "label": "Water",
                        "quantity": 1614.3187290361113,
                        "unit": "g"
                    }
                },
                "totalDaily": {
                    "ENERC_KCAL": {
                        "label": "Energy",
                        "quantity": 210.51498869569446,
                        "unit": "%"
                    },
                    "FAT": {
                        "label": "Fat",
                        "quantity": 447.18840995683763,
                        "unit": "%"
                    },
                    "FASAT": {
                        "label": "Saturated",
                        "quantity": 483.07472278194444,
                        "unit": "%"
                    },
                    "CHOCDF": {
                        "label": "Carbs",
                        "quantity": 43.27985049114815,
                        "unit": "%"
                    },
                    "FIBTG": {
                        "label": "Fiber",
                        "quantity": 129.95991111111113,
                        "unit": "%"
                    },
                    "PROCNT": {
                        "label": "Protein",
                        "quantity": 546.0847186583334,
                        "unit": "%"
                    },
                    "CHOLE": {
                        "label": "Cholesterol",
                        "quantity": 356.258100775,
                        "unit": "%"
                    },
                    "NA": {
                        "label": "Sodium",
                        "quantity": 232.9912638657407,
                        "unit": "%"
                    },
                    "CA": {
                        "label": "Calcium",
                        "quantity": 140.92408811611108,
                        "unit": "%"
                    },
                    "MG": {
                        "label": "Magnesium",
                        "quantity": 121.68516838029102,
                        "unit": "%"
                    },
                    "K": {
                        "label": "Potassium",
                        "quantity": 112.73639738611112,
                        "unit": "%"
                    },
                    "FE": {
                        "label": "Iron",
                        "quantity": 96.44984962592594,
                        "unit": "%"
                    },
                    "ZN": {
                        "label": "Zinc",
                        "quantity": 213.80537876262625,
                        "unit": "%"
                    },
                    "P": {
                        "label": "Phosphorus",
                        "quantity": 412.52412343333333,
                        "unit": "%"
                    },
                    "VITA_RAE": {
                        "label": "Vitamin A",
                        "quantity": 117.17837047345678,
                        "unit": "%"
                    },
                    "VITC": {
                        "label": "Vitamin C",
                        "quantity": 82.7488888888889,
                        "unit": "%"
                    },
                    "THIA": {
                        "label": "Thiamin (B1)",
                        "quantity": 109.75723541550927,
                        "unit": "%"
                    },
                    "RIBF": {
                        "label": "Riboflavin (B2)",
                        "quantity": 201.99942774999997,
                        "unit": "%"
                    },
                    "NIA": {
                        "label": "Niacin (B3)",
                        "quantity": 582.4203972459894,
                        "unit": "%"
                    },
                    "VITB6A": {
                        "label": "Vitamin B6",
                        "quantity": 461.9854909202991,
                        "unit": "%"
                    },
                    "FOLDFE": {
                        "label": "Folate equivalent (total)",
                        "quantity": 96.39596971805557,
                        "unit": "%"
                    },
                    "VITB12": {
                        "label": "Vitamin B12",
                        "quantity": 204.2793403229167,
                        "unit": "%"
                    },
                    "VITD": {
                        "label": "Vitamin D",
                        "quantity": 20.5359237,
                        "unit": "%"
                    },
                    "TOCPHA": {
                        "label": "Vitamin E",
                        "quantity": 109.4387965662963,
                        "unit": "%"
                    },
                    "VITK1": {
                        "label": "Vitamin K",
                        "quantity": 126.07888618634257,
                        "unit": "%"
                    }
                },
                "digest": [
                    {
                        "label": "Fat",
                        "tag": "FAT",
                        "schemaOrgTag": "fatContent",
                        "total": 290.67246647194446,
                        "hasRDI": True,
                        "daily": 447.18840995683763,
                        "unit": "g",
                        "sub": [
                            {
                                "label": "Saturated",
                                "tag": "FASAT",
                                "schemaOrgTag": "saturatedFatContent",
                                "total": 96.61494455638889,
                                "hasRDI": True,
                                "daily": 483.07472278194444,
                                "unit": "g"
                            },
                            {
                                "label": "Trans",
                                "tag": "FATRN",
                                "schemaOrgTag": "transFatContent",
                                "total": 2.2541520000000004,
                                "hasRDI": False,
                                "daily": 0.0,
                                "unit": "g"
                            },
                            {
                                "label": "Monounsaturated",
                                "tag": "FAMS",
                                "schemaOrgTag": '',
                                "total": 116.98473198263889,
                                "hasRDI": False,
                                "daily": 0.0,
                                "unit": "g"
                            },
                            {
                                "label": "Polyunsaturated",
                                "tag": "FAPU",
                                "schemaOrgTag": '',
                                "total": 50.39364996268611,
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
                        "total": 129.83955147344446,
                        "hasRDI": True,
                        "daily": 43.27985049114815,
                        "unit": "g",
                        "sub": [
                            {
                                "label": "Carbs (net)",
                                "tag": "CHOCDF.net",
                                "schemaOrgTag": '',
                                "total": 97.34957369566668,
                                "hasRDI": False,
                                "daily": 0.0,
                                "unit": "g"
                            },
                            {
                                "label": "Fiber",
                                "tag": "FIBTG",
                                "schemaOrgTag": "fiberContent",
                                "total": 32.48997777777778,
                                "hasRDI": True,
                                "daily": 129.95991111111113,
                                "unit": "g"
                            },
                            {
                                "label": "Sugars",
                                "tag": "SUGAR",
                                "schemaOrgTag": "sugarContent",
                                "total": 29.397857129166674,
                                "hasRDI": False,
                                "daily": 0.0,
                                "unit": "g"
                            },
                            {
                                "label": "Sugars, added",
                                "tag": "SUGAR.added",
                                "schemaOrgTag": '',
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
                        "total": 273.0423593291667,
                        "hasRDI": True,
                        "daily": 546.0847186583334,
                        "unit": "g"
                    },
                    {
                        "label": "Cholesterol",
                        "tag": "CHOLE",
                        "schemaOrgTag": "cholesterolContent",
                        "total": 1068.774302325,
                        "hasRDI": True,
                        "daily": 356.258100775,
                        "unit": "mg"
                    },
                    {
                        "label": "Sodium",
                        "tag": "NA",
                        "schemaOrgTag": "sodiumContent",
                        "total": 5591.790332777778,
                        "hasRDI": True,
                        "daily": 232.9912638657407,
                        "unit": "mg"
                    },
                    {
                        "label": "Calcium",
                        "tag": "CA",
                        "schemaOrgTag": '',
                        "total": 1409.240881161111,
                        "hasRDI": True,
                        "daily": 140.92408811611108,
                        "unit": "mg"
                    },
                    {
                        "label": "Magnesium",
                        "tag": "MG",
                        "schemaOrgTag": '',
                        "total": 511.07770719722225,
                        "hasRDI": True,
                        "daily": 121.68516838029102,
                        "unit": "mg"
                    },
                    {
                        "label": "Potassium",
                        "tag": "K",
                        "schemaOrgTag": '',
                        "total": 5298.610677147222,
                        "hasRDI": True,
                        "daily": 112.73639738611112,
                        "unit": "mg"
                    },
                    {
                        "label": "Iron",
                        "tag": "FE",
                        "schemaOrgTag": '',
                        "total": 17.36097293266667,
                        "hasRDI": True,
                        "daily": 96.44984962592594,
                        "unit": "mg"
                    },
                    {
                        "label": "Zinc",
                        "tag": "ZN",
                        "schemaOrgTag": '',
                        "total": 23.518591663888888,
                        "hasRDI": True,
                        "daily": 213.80537876262625,
                        "unit": "mg"
                    },
                    {
                        "label": "Phosphorus",
                        "tag": "P",
                        "schemaOrgTag": '',
                        "total": 2887.6688640333336,
                        "hasRDI": True,
                        "daily": 412.52412343333333,
                        "unit": "mg"
                    },
                    {
                        "label": "Vitamin A",
                        "tag": "VITA_RAE",
                        "schemaOrgTag": '',
                        "total": 1054.605334261111,
                        "hasRDI": True,
                        "daily": 117.17837047345678,
                        "unit": "µg"
                    },
                    {
                        "label": "Vitamin C",
                        "tag": "VITC",
                        "schemaOrgTag": '',
                        "total": 74.474,
                        "hasRDI": True,
                        "daily": 82.7488888888889,
                        "unit": "mg"
                    },
                    {
                        "label": "Thiamin (B1)",
                        "tag": "THIA",
                        "schemaOrgTag": '',
                        "total": 1.3170868249861112,
                        "hasRDI": True,
                        "daily": 109.75723541550927,
                        "unit": "mg"
                    },
                    {
                        "label": "Riboflavin (B2)",
                        "tag": "RIBF",
                        "schemaOrgTag": '',
                        "total": 2.6259925607499994,
                        "hasRDI": True,
                        "daily": 201.99942774999997,
                        "unit": "mg"
                    },
                    {
                        "label": "Niacin (B3)",
                        "tag": "NIA",
                        "schemaOrgTag": '',
                        "total": 93.18726355935831,
                        "hasRDI": True,
                        "daily": 582.4203972459894,
                        "unit": "mg"
                    },
                    {
                        "label": "Vitamin B6",
                        "tag": "VITB6A",
                        "schemaOrgTag": '',
                        "total": 6.0058113819638885,
                        "hasRDI": True,
                        "daily": 461.9854909202991,
                        "unit": "mg"
                    },
                    {
                        "label": "Folate equivalent (total)",
                        "tag": "FOLDFE",
                        "schemaOrgTag": '',
                        "total": 385.5838788722223,
                        "hasRDI": True,
                        "daily": 96.39596971805557,
                        "unit": "µg"
                    },
                    {
                        "label": "Folate (food)",
                        "tag": "FOLFD",
                        "schemaOrgTag": '',
                        "total": 345.95987887222225,
                        "hasRDI": False,
                        "daily": 0.0,
                        "unit": "µg"
                    },
                    {
                        "label": "Folic acid",
                        "tag": "FOLAC",
                        "schemaOrgTag": '',
                        "total": 24.384,
                        "hasRDI": False,
                        "daily": 0.0,
                        "unit": "µg"
                    },
                    {
                        "label": "Vitamin B12",
                        "tag": "VITB12",
                        "schemaOrgTag": '',
                        "total": 4.9027041677500005,
                        "hasRDI": True,
                        "daily": 204.2793403229167,
                        "unit": "µg"
                    },
                    {
                        "label": "Vitamin D",
                        "tag": "VITD",
                        "schemaOrgTag": '',
                        "total": 3.0803885550000003,
                        "hasRDI": True,
                        "daily": 20.5359237,
                        "unit": "µg"
                    },
                    {
                        "label": "Vitamin E",
                        "tag": "TOCPHA",
                        "schemaOrgTag": '',
                        "total": 16.415819484944446,
                        "hasRDI": True,
                        "daily": 109.4387965662963,
                        "unit": "mg"
                    },
                    {
                        "label": "Vitamin K",
                        "tag": "VITK1",
                        "schemaOrgTag": '',
                        "total": 151.2946634236111,
                        "hasRDI": True,
                        "daily": 126.07888618634257,
                        "unit": "µg"
                    },
                    {
                        "label": "Sugar alcohols",
                        "tag": "Sugar.alcohol",
                        "schemaOrgTag": '',
                        "total": 0.0,
                        "hasRDI": False,
                        "daily": 0.0,
                        "unit": "g"
                    },
                    {
                        "label": "Water",
                        "tag": "WATER",
                        "schemaOrgTag": '',
                        "total": 1614.3187290361113,
                        "hasRDI": False,
                        "daily": 0.0,
                        "unit": "g"
                    }
                ]
            },
            "_links": {
                "self": {
                    "title": "Self",
                    "href": "https://api.edamam.com/api/recipes/v2/66b2a1e54bdb227504a8e091877a08e8?type=public&app_id=e909afd5&app_key=34e59dda7e1bffb92e49c416e9449e1d"
                }
            }
        },
        {
            "recipe": {
                "uri": "http://www.edamam.com/ontologies/edamam.owl#recipe_8cc770d62c36aa8b1a956696966d39c9",
                "label": "Choco Tacos",
                "image": "https://edamam-product-images.s3.amazonaws.com/web-img/55f/55f86e4b0332364c9aa156ef7765553b.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLWVhc3QtMSJIMEYCIQCP2Gbt%2ByPQIVKV%2FafgML7WXbkOusL9fCs6d1le6dFKYAIhAJcnuEh%2B1NzOso38QgGaVBwaVQAMxyMJATg%2FR%2Fl0jl96KsEFCJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMMTg3MDE3MTUwOTg2IgydADkJdybnmhdEGwQqlQUNCCJJEzulouVCRRPPDPN9Ik9nmgPZk%2Fam6u04CTug5FWfzto4W1y6mlAuXr3EHPB%2FvTcZ%2BmAkgcS5%2FRfKsviGgYg1PBDbKvJFWJigqXNb6jHaHO3eyZnXpof0Qk2PachTFyGGF7upzvEiKr6BGB6DtCoEGe3wCd0iFSMS%2Ft8LIlICGGYaaCvWq9TXeaXkel5jju8XxawzfW0OY8ad1NODjiJJ%2FJ02goRzRa3HwZdXj0P4%2FwwiBHg8BMnsBu5XvhNCt9Gz%2Bxp9cZIC8TMv%2FY8rOvepaH28zVl5BjLGle3tn5syTeLiH6OS68I4OndB2qqeqZqdi9cu6zb1H0y8aKh8r8IIaHqXhP6jBXwOxUN8uimNrMJnaDPxNdvFPuR5yx8UApiuserTd1b1ZIBFiBJ6lavYUBrkLW%2B7bZIJltsNTSxF2GTKFWoXHKGf3%2FXYj%2FniRUh%2BB3xUXrXh8PzVKChkdfuCxirnj5UG2XCrj22%2BBJG8S8UHiExHaIwt01Nel6V7Y0IlXWvwqK8YEx%2FHOI%2FewXERfrnIQDCsrQyC7qTLL3HndUW2Ke8ib2iC%2BPgaP6xDqkqdlhOSojQHG4rfwcyVOFOzeauzAO7Rc77mb0rCUJdMckP6nKiD7nrtjlZXznFmYhCvjmWQF2l06Jl7xQsr%2BjkGAeoXo9X%2FiC11ZTNfxOVIe3LWWkRvMwGWvgvtgF4ZEDGaLXgsbO4I8%2FpSmGD4ox9ZWDfX%2BtTURCyBYVXqYpQ4TpgMhHqAtTUr4TNc7GRLVbfi1xqZNQDt1Sfdzh3Xq88dOJyKsyUs7rcFuuxoNyxvqstWVaAyRglOH1n%2BpV0xA7%2FKEHa%2F8%2FzH6uaXeIp3eLJN1%2BGlAQc1sP2jehPHqGi5Lc7YMOKk8akGOrABqEMeyIMA72vRUvaZqcs7N77uX3kDw2%2BTfyF8pS8HYdR1%2BEU1ekEPGlPPLyTo0NFmbmMa4urw%2B19eIvlGSnFjiSeee%2F%2BeotdKLVnDgZ5aNxOYivkgUqjazWNTWX1qdv7Jq7GWrNDLwjZiU5zLvpcjSyzLyGAVIo8pW14m4aC3jppuzjKpasygGK2%2Bf%2BmxisMAkIdRRS5aXW9PY%2FuwiBnL3qiZT5RtAdamISZZM9jUAWY%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231028T003610Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFPXEGMX3T%2F20231028%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=ce4101288da352dadb7efaea4a72df1529fbc6e68290d3e625702d246098e8d5",
                "images": {
                    "THUMBNAIL": {
                        "url": "https://edamam-product-images.s3.amazonaws.com/web-img/55f/55f86e4b0332364c9aa156ef7765553b-s.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLWVhc3QtMSJIMEYCIQCP2Gbt%2ByPQIVKV%2FafgML7WXbkOusL9fCs6d1le6dFKYAIhAJcnuEh%2B1NzOso38QgGaVBwaVQAMxyMJATg%2FR%2Fl0jl96KsEFCJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMMTg3MDE3MTUwOTg2IgydADkJdybnmhdEGwQqlQUNCCJJEzulouVCRRPPDPN9Ik9nmgPZk%2Fam6u04CTug5FWfzto4W1y6mlAuXr3EHPB%2FvTcZ%2BmAkgcS5%2FRfKsviGgYg1PBDbKvJFWJigqXNb6jHaHO3eyZnXpof0Qk2PachTFyGGF7upzvEiKr6BGB6DtCoEGe3wCd0iFSMS%2Ft8LIlICGGYaaCvWq9TXeaXkel5jju8XxawzfW0OY8ad1NODjiJJ%2FJ02goRzRa3HwZdXj0P4%2FwwiBHg8BMnsBu5XvhNCt9Gz%2Bxp9cZIC8TMv%2FY8rOvepaH28zVl5BjLGle3tn5syTeLiH6OS68I4OndB2qqeqZqdi9cu6zb1H0y8aKh8r8IIaHqXhP6jBXwOxUN8uimNrMJnaDPxNdvFPuR5yx8UApiuserTd1b1ZIBFiBJ6lavYUBrkLW%2B7bZIJltsNTSxF2GTKFWoXHKGf3%2FXYj%2FniRUh%2BB3xUXrXh8PzVKChkdfuCxirnj5UG2XCrj22%2BBJG8S8UHiExHaIwt01Nel6V7Y0IlXWvwqK8YEx%2FHOI%2FewXERfrnIQDCsrQyC7qTLL3HndUW2Ke8ib2iC%2BPgaP6xDqkqdlhOSojQHG4rfwcyVOFOzeauzAO7Rc77mb0rCUJdMckP6nKiD7nrtjlZXznFmYhCvjmWQF2l06Jl7xQsr%2BjkGAeoXo9X%2FiC11ZTNfxOVIe3LWWkRvMwGWvgvtgF4ZEDGaLXgsbO4I8%2FpSmGD4ox9ZWDfX%2BtTURCyBYVXqYpQ4TpgMhHqAtTUr4TNc7GRLVbfi1xqZNQDt1Sfdzh3Xq88dOJyKsyUs7rcFuuxoNyxvqstWVaAyRglOH1n%2BpV0xA7%2FKEHa%2F8%2FzH6uaXeIp3eLJN1%2BGlAQc1sP2jehPHqGi5Lc7YMOKk8akGOrABqEMeyIMA72vRUvaZqcs7N77uX3kDw2%2BTfyF8pS8HYdR1%2BEU1ekEPGlPPLyTo0NFmbmMa4urw%2B19eIvlGSnFjiSeee%2F%2BeotdKLVnDgZ5aNxOYivkgUqjazWNTWX1qdv7Jq7GWrNDLwjZiU5zLvpcjSyzLyGAVIo8pW14m4aC3jppuzjKpasygGK2%2Bf%2BmxisMAkIdRRS5aXW9PY%2FuwiBnL3qiZT5RtAdamISZZM9jUAWY%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231028T003610Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFPXEGMX3T%2F20231028%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=d0f1f5a50011d6e7b351e4cf616166c18c4a697da0d993d63a0e95d0771005e7",
                        "width": 100,
                        "height": 100
                    },
                    "SMALL": {
                        "url": "https://edamam-product-images.s3.amazonaws.com/web-img/55f/55f86e4b0332364c9aa156ef7765553b-m.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLWVhc3QtMSJIMEYCIQCP2Gbt%2ByPQIVKV%2FafgML7WXbkOusL9fCs6d1le6dFKYAIhAJcnuEh%2B1NzOso38QgGaVBwaVQAMxyMJATg%2FR%2Fl0jl96KsEFCJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMMTg3MDE3MTUwOTg2IgydADkJdybnmhdEGwQqlQUNCCJJEzulouVCRRPPDPN9Ik9nmgPZk%2Fam6u04CTug5FWfzto4W1y6mlAuXr3EHPB%2FvTcZ%2BmAkgcS5%2FRfKsviGgYg1PBDbKvJFWJigqXNb6jHaHO3eyZnXpof0Qk2PachTFyGGF7upzvEiKr6BGB6DtCoEGe3wCd0iFSMS%2Ft8LIlICGGYaaCvWq9TXeaXkel5jju8XxawzfW0OY8ad1NODjiJJ%2FJ02goRzRa3HwZdXj0P4%2FwwiBHg8BMnsBu5XvhNCt9Gz%2Bxp9cZIC8TMv%2FY8rOvepaH28zVl5BjLGle3tn5syTeLiH6OS68I4OndB2qqeqZqdi9cu6zb1H0y8aKh8r8IIaHqXhP6jBXwOxUN8uimNrMJnaDPxNdvFPuR5yx8UApiuserTd1b1ZIBFiBJ6lavYUBrkLW%2B7bZIJltsNTSxF2GTKFWoXHKGf3%2FXYj%2FniRUh%2BB3xUXrXh8PzVKChkdfuCxirnj5UG2XCrj22%2BBJG8S8UHiExHaIwt01Nel6V7Y0IlXWvwqK8YEx%2FHOI%2FewXERfrnIQDCsrQyC7qTLL3HndUW2Ke8ib2iC%2BPgaP6xDqkqdlhOSojQHG4rfwcyVOFOzeauzAO7Rc77mb0rCUJdMckP6nKiD7nrtjlZXznFmYhCvjmWQF2l06Jl7xQsr%2BjkGAeoXo9X%2FiC11ZTNfxOVIe3LWWkRvMwGWvgvtgF4ZEDGaLXgsbO4I8%2FpSmGD4ox9ZWDfX%2BtTURCyBYVXqYpQ4TpgMhHqAtTUr4TNc7GRLVbfi1xqZNQDt1Sfdzh3Xq88dOJyKsyUs7rcFuuxoNyxvqstWVaAyRglOH1n%2BpV0xA7%2FKEHa%2F8%2FzH6uaXeIp3eLJN1%2BGlAQc1sP2jehPHqGi5Lc7YMOKk8akGOrABqEMeyIMA72vRUvaZqcs7N77uX3kDw2%2BTfyF8pS8HYdR1%2BEU1ekEPGlPPLyTo0NFmbmMa4urw%2B19eIvlGSnFjiSeee%2F%2BeotdKLVnDgZ5aNxOYivkgUqjazWNTWX1qdv7Jq7GWrNDLwjZiU5zLvpcjSyzLyGAVIo8pW14m4aC3jppuzjKpasygGK2%2Bf%2BmxisMAkIdRRS5aXW9PY%2FuwiBnL3qiZT5RtAdamISZZM9jUAWY%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231028T003610Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFPXEGMX3T%2F20231028%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=d393da14ece38daeaa7d25670a72ff846d1285d8a5159e1d73a25bb211a3d056",
                        "width": 200,
                        "height": 200
                    },
                    "REGULAR": {
                        "url": "https://edamam-product-images.s3.amazonaws.com/web-img/55f/55f86e4b0332364c9aa156ef7765553b.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLWVhc3QtMSJIMEYCIQCP2Gbt%2ByPQIVKV%2FafgML7WXbkOusL9fCs6d1le6dFKYAIhAJcnuEh%2B1NzOso38QgGaVBwaVQAMxyMJATg%2FR%2Fl0jl96KsEFCJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMMTg3MDE3MTUwOTg2IgydADkJdybnmhdEGwQqlQUNCCJJEzulouVCRRPPDPN9Ik9nmgPZk%2Fam6u04CTug5FWfzto4W1y6mlAuXr3EHPB%2FvTcZ%2BmAkgcS5%2FRfKsviGgYg1PBDbKvJFWJigqXNb6jHaHO3eyZnXpof0Qk2PachTFyGGF7upzvEiKr6BGB6DtCoEGe3wCd0iFSMS%2Ft8LIlICGGYaaCvWq9TXeaXkel5jju8XxawzfW0OY8ad1NODjiJJ%2FJ02goRzRa3HwZdXj0P4%2FwwiBHg8BMnsBu5XvhNCt9Gz%2Bxp9cZIC8TMv%2FY8rOvepaH28zVl5BjLGle3tn5syTeLiH6OS68I4OndB2qqeqZqdi9cu6zb1H0y8aKh8r8IIaHqXhP6jBXwOxUN8uimNrMJnaDPxNdvFPuR5yx8UApiuserTd1b1ZIBFiBJ6lavYUBrkLW%2B7bZIJltsNTSxF2GTKFWoXHKGf3%2FXYj%2FniRUh%2BB3xUXrXh8PzVKChkdfuCxirnj5UG2XCrj22%2BBJG8S8UHiExHaIwt01Nel6V7Y0IlXWvwqK8YEx%2FHOI%2FewXERfrnIQDCsrQyC7qTLL3HndUW2Ke8ib2iC%2BPgaP6xDqkqdlhOSojQHG4rfwcyVOFOzeauzAO7Rc77mb0rCUJdMckP6nKiD7nrtjlZXznFmYhCvjmWQF2l06Jl7xQsr%2BjkGAeoXo9X%2FiC11ZTNfxOVIe3LWWkRvMwGWvgvtgF4ZEDGaLXgsbO4I8%2FpSmGD4ox9ZWDfX%2BtTURCyBYVXqYpQ4TpgMhHqAtTUr4TNc7GRLVbfi1xqZNQDt1Sfdzh3Xq88dOJyKsyUs7rcFuuxoNyxvqstWVaAyRglOH1n%2BpV0xA7%2FKEHa%2F8%2FzH6uaXeIp3eLJN1%2BGlAQc1sP2jehPHqGi5Lc7YMOKk8akGOrABqEMeyIMA72vRUvaZqcs7N77uX3kDw2%2BTfyF8pS8HYdR1%2BEU1ekEPGlPPLyTo0NFmbmMa4urw%2B19eIvlGSnFjiSeee%2F%2BeotdKLVnDgZ5aNxOYivkgUqjazWNTWX1qdv7Jq7GWrNDLwjZiU5zLvpcjSyzLyGAVIo8pW14m4aC3jppuzjKpasygGK2%2Bf%2BmxisMAkIdRRS5aXW9PY%2FuwiBnL3qiZT5RtAdamISZZM9jUAWY%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231028T003610Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFPXEGMX3T%2F20231028%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=ce4101288da352dadb7efaea4a72df1529fbc6e68290d3e625702d246098e8d5",
                        "width": 300,
                        "height": 300
                    },
                    "LARGE": {
                        "url": "https://edamam-product-images.s3.amazonaws.com/web-img/55f/55f86e4b0332364c9aa156ef7765553b-l.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLWVhc3QtMSJIMEYCIQCP2Gbt%2ByPQIVKV%2FafgML7WXbkOusL9fCs6d1le6dFKYAIhAJcnuEh%2B1NzOso38QgGaVBwaVQAMxyMJATg%2FR%2Fl0jl96KsEFCJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMMTg3MDE3MTUwOTg2IgydADkJdybnmhdEGwQqlQUNCCJJEzulouVCRRPPDPN9Ik9nmgPZk%2Fam6u04CTug5FWfzto4W1y6mlAuXr3EHPB%2FvTcZ%2BmAkgcS5%2FRfKsviGgYg1PBDbKvJFWJigqXNb6jHaHO3eyZnXpof0Qk2PachTFyGGF7upzvEiKr6BGB6DtCoEGe3wCd0iFSMS%2Ft8LIlICGGYaaCvWq9TXeaXkel5jju8XxawzfW0OY8ad1NODjiJJ%2FJ02goRzRa3HwZdXj0P4%2FwwiBHg8BMnsBu5XvhNCt9Gz%2Bxp9cZIC8TMv%2FY8rOvepaH28zVl5BjLGle3tn5syTeLiH6OS68I4OndB2qqeqZqdi9cu6zb1H0y8aKh8r8IIaHqXhP6jBXwOxUN8uimNrMJnaDPxNdvFPuR5yx8UApiuserTd1b1ZIBFiBJ6lavYUBrkLW%2B7bZIJltsNTSxF2GTKFWoXHKGf3%2FXYj%2FniRUh%2BB3xUXrXh8PzVKChkdfuCxirnj5UG2XCrj22%2BBJG8S8UHiExHaIwt01Nel6V7Y0IlXWvwqK8YEx%2FHOI%2FewXERfrnIQDCsrQyC7qTLL3HndUW2Ke8ib2iC%2BPgaP6xDqkqdlhOSojQHG4rfwcyVOFOzeauzAO7Rc77mb0rCUJdMckP6nKiD7nrtjlZXznFmYhCvjmWQF2l06Jl7xQsr%2BjkGAeoXo9X%2FiC11ZTNfxOVIe3LWWkRvMwGWvgvtgF4ZEDGaLXgsbO4I8%2FpSmGD4ox9ZWDfX%2BtTURCyBYVXqYpQ4TpgMhHqAtTUr4TNc7GRLVbfi1xqZNQDt1Sfdzh3Xq88dOJyKsyUs7rcFuuxoNyxvqstWVaAyRglOH1n%2BpV0xA7%2FKEHa%2F8%2FzH6uaXeIp3eLJN1%2BGlAQc1sP2jehPHqGi5Lc7YMOKk8akGOrABqEMeyIMA72vRUvaZqcs7N77uX3kDw2%2BTfyF8pS8HYdR1%2BEU1ekEPGlPPLyTo0NFmbmMa4urw%2B19eIvlGSnFjiSeee%2F%2BeotdKLVnDgZ5aNxOYivkgUqjazWNTWX1qdv7Jq7GWrNDLwjZiU5zLvpcjSyzLyGAVIo8pW14m4aC3jppuzjKpasygGK2%2Bf%2BmxisMAkIdRRS5aXW9PY%2FuwiBnL3qiZT5RtAdamISZZM9jUAWY%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231028T003610Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFPXEGMX3T%2F20231028%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=e4e5ce0927bed32a8bc51e7ce0090dc189653dada3ed05489dd2630b66898ee3",
                        "width": 600,
                        "height": 600
                    }
                },
                "source": "Food52",
                "url": "https://food52.com/recipes/28771-choco-tacos",
                "shareAs": "http://www.edamam.com/recipe/choco-tacos-8cc770d62c36aa8b1a956696966d39c9/tacos",
                "yield": 8.0,
                "dietLabels": [
                    "Low-Sodium"
                ],
                "healthLabels": [
                    "Vegetarian",
                    "Pescatarian",
                    "Soy-Free",
                    "Fish-Free",
                    "Shellfish-Free",
                    "Pork-Free",
                    "Red-Meat-Free",
                    "Crustacean-Free",
                    "Celery-Free",
                    "Mustard-Free",
                    "Sesame-Free",
                    "Lupine-Free",
                    "Mollusk-Free",
                    "Alcohol-Free",
                    "Kosher"
                ],
                "cautions": [
                    "Tree-Nuts",
                    "Sulfites"
                ],
                "ingredientLines": [
                    "2/3 cup all-purpose flour",
                    "1/2 cup sugar",
                    "1/8 teaspoon kosher salt",
                    "2 tablespoons unsalted butter, plus more for greasing the pan",
                    "1/4 cup milk",
                    "1/4 teaspoon almond extract",
                    "1/2 teaspoon vanilla extract",
                    "2 large egg whites",
                    "10 ounces dark chocolate chips",
                    "3 tablespoons coconut oil",
                    "4 to 6 cups ice cream (original Choco Tacos have fudge-swirled vanilla ice cream, but feel free to use any flavor)",
                    "1/2 cup crushed nuts, plus any other desired toppings like sprinkles"
                ],
                "ingredients": [
                    {
                        "text": "2/3 cup all-purpose flour",
                        "quantity": 0.6666666666666666,
                        "measure": "cup",
                        "food": "all-purpose flour",
                        "weight": 83.33333333333333,
                        "foodCategory": "grains",
                        "foodId": "food_ar3x97tbq9o9p6b6gzwj0am0c81l",
                        "image": "https://www.edamam.com/food-img/368/368077bbcab62f862a8c766a56ea5dd1.jpg"
                    },
                    {
                        "text": "1/2 cup sugar",
                        "quantity": 0.5,
                        "measure": "cup",
                        "food": "sugar",
                        "weight": 100.0,
                        "foodCategory": "sugars",
                        "foodId": "food_axi2ijobrk819yb0adceobnhm1c2",
                        "image": "https://www.edamam.com/food-img/ecb/ecb3f5aaed96d0188c21b8369be07765.jpg"
                    },
                    {
                        "text": "1/8 teaspoon kosher salt",
                        "quantity": 0.125,
                        "measure": "teaspoon",
                        "food": "kosher salt",
                        "weight": 0.6067708333641094,
                        "foodCategory": "Condiments and sauces",
                        "foodId": "food_a1vgrj1bs8rd1majvmd9ubz8ttkg",
                        "image": "https://www.edamam.com/food-img/694/6943ea510918c6025795e8dc6e6eaaeb.jpg"
                    },
                    {
                        "text": "2 tablespoons unsalted butter, plus more for greasing the pan",
                        "quantity": 2.0,
                        "measure": "tablespoon",
                        "food": "unsalted butter",
                        "weight": 28.4,
                        "foodCategory": "Dairy",
                        "foodId": "food_awz3iefajbk1fwahq9logahmgltj",
                        "image": "https://www.edamam.com/food-img/713/71397239b670d88c04faa8d05035cab4.jpg"
                    },
                    {
                        "text": "1/4 cup milk",
                        "quantity": 0.25,
                        "measure": "cup",
                        "food": "milk",
                        "weight": 61.0,
                        "foodCategory": "Milk",
                        "foodId": "food_b49rs1kaw0jktabzkg2vvanvvsis",
                        "image": "https://www.edamam.com/food-img/7c9/7c9962acf83654a8d98ea6a2ade93735.jpg"
                    },
                    {
                        "text": "1/4 teaspoon almond extract",
                        "quantity": 0.25,
                        "measure": "teaspoon",
                        "food": "almond extract",
                        "weight": 1.05,
                        "foodCategory": "Condiments and sauces",
                        "foodId": "food_akzcb47a1rd7udato049aak1z46h",
                        "image": "https://www.edamam.com/food-img/90f/90f910b0bf82750d4f6528263e014cca.jpg"
                    },
                    {
                        "text": "1/2 teaspoon vanilla extract",
                        "quantity": 0.5,
                        "measure": "teaspoon",
                        "food": "vanilla extract",
                        "weight": 2.1,
                        "foodCategory": "Condiments and sauces",
                        "foodId": "food_bh1wvnqaw3q7ciascfoygaabax2a",
                        "image": "https://www.edamam.com/food-img/90f/90f910b0bf82750d4f6528263e014cca.jpg"
                    },
                    {
                        "text": "2 large egg whites",
                        "quantity": 2.0,
                        "measure": "<unit>",
                        "food": "egg whites",
                        "weight": 66.0,
                        "foodCategory": "Eggs",
                        "foodId": "food_a7hurbpb20zs42bnwg2p8bca3ihs",
                        "image": "https://www.edamam.com/food-img/b30/b304a020501418f9a63cf7f9359bc99d.jpg"
                    },
                    {
                        "text": "10 ounces dark chocolate chips",
                        "quantity": 10.0,
                        "measure": "ounce",
                        "food": "dark chocolate chips",
                        "weight": 283.49523125,
                        "foodCategory": "chocolate",
                        "foodId": "food_afwurvlasugs4ibig02xbblph5bn",
                        "image": "https://www.edamam.com/food-img/3cf/3cf0e13350f43392dc13c07d27ad145d.jpg"
                    },
                    {
                        "text": "3 tablespoons coconut oil",
                        "quantity": 3.0,
                        "measure": "tablespoon",
                        "food": "coconut oil",
                        "weight": 40.8,
                        "foodCategory": "Oils",
                        "foodId": "food_b40ubq8a0enoidbcr1tmfbwgs6aw",
                        "image": "https://www.edamam.com/food-img/3c9/3c97284c57e76e16093d51572b558be8.jpg"
                    },
                    {
                        "text": "4 to 6 cups ice cream (original Choco Tacos have fudge-swirled vanilla ice cream, but feel free to use any flavor)",
                        "quantity": 5.0,
                        "measure": "cup",
                        "food": "ice cream",
                        "weight": 660.0,
                        "foodCategory": "frozen treats",
                        "foodId": "food_bsg87una16tr8waipd66na9drm1k",
                        "image": "https://www.edamam.com/food-img/1be/1be43587dc55730fc761aedf4f3df090.jpg"
                    },
                    {
                        "text": "1/2 cup crushed nuts, plus any other desired toppings like sprinkles",
                        "quantity": 0.5,
                        "measure": "cup",
                        "food": "sprinkles",
                        "weight": 100.0,
                        "foodCategory": "sugars",
                        "foodId": "food_bu3p27mbly89p6b42fcifalyxdcj",
                        "image": "https://www.edamam.com/food-img/ecb/ecb3f5aaed96d0188c21b8369be07765.jpg"
                    }
                ],
                "calories": 4787.000816208333,
                "totalCO2Emissions": 17612.548557465387,
                "co2EmissionsClass": "F",
                "totalWeight": 1426.7853354166973,
                "totalTime": 0.0,
                "cuisineType": [
                    "mexican"
                ],
                "mealType": [
                    "lunch/dinner"
                ],
                "dishType": [
                    "sandwiches"
                ],
                "totalNutrients": {
                    "ENERC_KCAL": {
                        "label": "Energy",
                        "quantity": 4787.000816208333,
                        "unit": "kcal"
                    },
                    "FAT": {
                        "label": "Fat",
                        "quantity": 259.74742517916667,
                        "unit": "g"
                    },
                    "FASAT": {
                        "label": "Saturated",
                        "quantity": 163.53641332291667,
                        "unit": "g"
                    },
                    "FATRN": {
                        "label": "Trans",
                        "quantity": 0.096472569375,
                        "unit": "g"
                    },
                    "FAMS": {
                        "label": "Monounsaturated",
                        "quantity": 65.6857646,
                        "unit": "g"
                    },
                    "FAPU": {
                        "label": "Polyunsaturated",
                        "quantity": 8.566922580416668,
                        "unit": "g"
                    },
                    "CHOCDF": {
                        "label": "Carbs",
                        "quantity": 553.2913844770833,
                        "unit": "g"
                    },
                    "CHOCDF.net": {
                        "label": "Carbohydrates (net)",
                        "quantity": 515.5204042708333,
                        "unit": "g"
                    },
                    "FIBTG": {
                        "label": "Fiber",
                        "quantity": 37.770980206249995,
                        "unit": "g"
                    },
                    "SUGAR": {
                        "label": "Sugars",
                        "quantity": 411.7468955,
                        "unit": "g"
                    },
                    "SUGAR.added": {
                        "label": "Sugars, added",
                        "quantity": 407.5588555,
                        "unit": "g"
                    },
                    "PROCNT": {
                        "label": "Protein",
                        "quantity": 63.12640184770834,
                        "unit": "g"
                    },
                    "CHOLE": {
                        "label": "Cholesterol",
                        "quantity": 366.06485693750005,
                        "unit": "mg"
                    },
                    "NA": {
                        "label": "Sodium",
                        "quantity": 962.9902962619411,
                        "unit": "mg"
                    },
                    "CA": {
                        "label": "Calcium",
                        "quantity": 1147.5176438125075,
                        "unit": "mg"
                    },
                    "MG": {
                        "label": "Magnesium",
                        "quantity": 771.414528291667,
                        "unit": "mg"
                    },
                    "K": {
                        "label": "Potassium",
                        "quantity": 3633.184111770836,
                        "unit": "mg"
                    },
                    "FE": {
                        "label": "Iron",
                        "quantity": 38.39956152916677,
                        "unit": "mg"
                    },
                    "ZN": {
                        "label": "Zinc",
                        "quantity": 14.824317258541697,
                        "unit": "mg"
                    },
                    "P": {
                        "label": "Phosphorus",
                        "quantity": 1724.3103122500002,
                        "unit": "mg"
                    },
                    "VITA_RAE": {
                        "label": "Vitamin A",
                        "quantity": 1006.7859046250001,
                        "unit": "µg"
                    },
                    "VITC": {
                        "label": "Vitamin C",
                        "quantity": 3.96,
                        "unit": "mg"
                    },
                    "THIA": {
                        "label": "Thiamin (B1)",
                        "quantity": 1.0536215452916666,
                        "unit": "mg"
                    },
                    "RIBF": {
                        "label": "Riboflavin (B2)",
                        "quantity": 2.6602714470416666,
                        "unit": "mg"
                    },
                    "NIA": {
                        "label": "Niacin (B3)",
                        "quantity": 8.807872094791666,
                        "unit": "mg"
                    },
                    "VITB6A": {
                        "label": "Vitamin B6",
                        "quantity": 0.4881258545416667,
                        "unit": "mg"
                    },
                    "FOLDFE": {
                        "label": "Folate equivalent (total)",
                        "quantity": 282.042,
                        "unit": "µg"
                    },
                    "FOLFD": {
                        "label": "Folate (food)",
                        "quantity": 63.708666666666666,
                        "unit": "µg"
                    },
                    "FOLAC": {
                        "label": "Folic acid",
                        "quantity": 128.33333333333331,
                        "unit": "µg"
                    },
                    "VITB12": {
                        "label": "Vitamin B12",
                        "quantity": 3.7499666475000004,
                        "unit": "µg"
                    },
                    "VITD": {
                        "label": "Vitamin D",
                        "quantity": 2.1130000000000004,
                        "unit": "µg"
                    },
                    "TOCPHA": {
                        "label": "Vitamin E",
                        "quantity": 4.590748531041667,
                        "unit": "mg"
                    },
                    "VITK1": {
                        "label": "Vitamin K",
                        "quantity": 25.34095188125,
                        "unit": "µg"
                    },
                    "WATER": {
                        "label": "Water",
                        "quantity": 534.2687048764584,
                        "unit": "g"
                    }
                },
                "totalDaily": {
                    "ENERC_KCAL": {
                        "label": "Energy",
                        "quantity": 239.35004081041666,
                        "unit": "%"
                    },
                    "FAT": {
                        "label": "Fat",
                        "quantity": 399.6114233525641,
                        "unit": "%"
                    },
                    "FASAT": {
                        "label": "Saturated",
                        "quantity": 817.6820666145834,
                        "unit": "%"
                    },
                    "CHOCDF": {
                        "label": "Carbs",
                        "quantity": 184.43046149236108,
                        "unit": "%"
                    },
                    "FIBTG": {
                        "label": "Fiber",
                        "quantity": 151.08392082499998,
                        "unit": "%"
                    },
                    "PROCNT": {
                        "label": "Protein",
                        "quantity": 126.25280369541667,
                        "unit": "%"
                    },
                    "CHOLE": {
                        "label": "Cholesterol",
                        "quantity": 122.02161897916669,
                        "unit": "%"
                    },
                    "NA": {
                        "label": "Sodium",
                        "quantity": 40.12459567758088,
                        "unit": "%"
                    },
                    "CA": {
                        "label": "Calcium",
                        "quantity": 114.75176438125075,
                        "unit": "%"
                    },
                    "MG": {
                        "label": "Magnesium",
                        "quantity": 183.6701257837302,
                        "unit": "%"
                    },
                    "K": {
                        "label": "Potassium",
                        "quantity": 77.30178961214546,
                        "unit": "%"
                    },
                    "FE": {
                        "label": "Iron",
                        "quantity": 213.33089738425983,
                        "unit": "%"
                    },
                    "ZN": {
                        "label": "Zinc",
                        "quantity": 134.76652053219723,
                        "unit": "%"
                    },
                    "P": {
                        "label": "Phosphorus",
                        "quantity": 246.33004460714287,
                        "unit": "%"
                    },
                    "VITA_RAE": {
                        "label": "Vitamin A",
                        "quantity": 111.8651005138889,
                        "unit": "%"
                    },
                    "VITC": {
                        "label": "Vitamin C",
                        "quantity": 4.4,
                        "unit": "%"
                    },
                    "THIA": {
                        "label": "Thiamin (B1)",
                        "quantity": 87.80179544097221,
                        "unit": "%"
                    },
                    "RIBF": {
                        "label": "Riboflavin (B2)",
                        "quantity": 204.6362651570513,
                        "unit": "%"
                    },
                    "NIA": {
                        "label": "Niacin (B3)",
                        "quantity": 55.04920059244791,
                        "unit": "%"
                    },
                    "VITB6A": {
                        "label": "Vitamin B6",
                        "quantity": 37.54814265705128,
                        "unit": "%"
                    },
                    "FOLDFE": {
                        "label": "Folate equivalent (total)",
                        "quantity": 70.5105,
                        "unit": "%"
                    },
                    "VITB12": {
                        "label": "Vitamin B12",
                        "quantity": 156.24861031250003,
                        "unit": "%"
                    },
                    "VITD": {
                        "label": "Vitamin D",
                        "quantity": 14.08666666666667,
                        "unit": "%"
                    },
                    "TOCPHA": {
                        "label": "Vitamin E",
                        "quantity": 30.604990206944446,
                        "unit": "%"
                    },
                    "VITK1": {
                        "label": "Vitamin K",
                        "quantity": 21.117459901041666,
                        "unit": "%"
                    }
                },
                "digest": [
                    {
                        "label": "Fat",
                        "tag": "FAT",
                        "schemaOrgTag": "fatContent",
                        "total": 259.74742517916667,
                        "hasRDI": True,
                        "daily": 399.6114233525641,
                        "unit": "g",
                        "sub": [
                            {
                                "label": "Saturated",
                                "tag": "FASAT",
                                "schemaOrgTag": "saturatedFatContent",
                                "total": 163.53641332291667,
                                "hasRDI": True,
                                "daily": 817.6820666145834,
                                "unit": "g"
                            },
                            {
                                "label": "Trans",
                                "tag": "FATRN",
                                "schemaOrgTag": "transFatContent",
                                "total": 0.096472569375,
                                "hasRDI": False,
                                "daily": 0.0,
                                "unit": "g"
                            },
                            {
                                "label": "Monounsaturated",
                                "tag": "FAMS",
                                "schemaOrgTag": '',
                                "total": 65.6857646,
                                "hasRDI": False,
                                "daily": 0.0,
                                "unit": "g"
                            },
                            {
                                "label": "Polyunsaturated",
                                "tag": "FAPU",
                                "schemaOrgTag": '',
                                "total": 8.566922580416668,
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
                        "total": 553.2913844770833,
                        "hasRDI": True,
                        "daily": 184.43046149236108,
                        "unit": "g",
                        "sub": [
                            {
                                "label": "Carbs (net)",
                                "tag": "CHOCDF.net",
                                "schemaOrgTag": '',
                                "total": 515.5204042708333,
                                "hasRDI": False,
                                "daily": 0.0,
                                "unit": "g"
                            },
                            {
                                "label": "Fiber",
                                "tag": "FIBTG",
                                "schemaOrgTag": "fiberContent",
                                "total": 37.770980206249995,
                                "hasRDI": True,
                                "daily": 151.08392082499998,
                                "unit": "g"
                            },
                            {
                                "label": "Sugars",
                                "tag": "SUGAR",
                                "schemaOrgTag": "sugarContent",
                                "total": 411.7468955,
                                "hasRDI": False,
                                "daily": 0.0,
                                "unit": "g"
                            },
                            {
                                "label": "Sugars, added",
                                "tag": "SUGAR.added",
                                "schemaOrgTag": '',
                                "total": 407.5588555,
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
                        "total": 63.12640184770834,
                        "hasRDI": True,
                        "daily": 126.25280369541667,
                        "unit": "g"
                    },
                    {
                        "label": "Cholesterol",
                        "tag": "CHOLE",
                        "schemaOrgTag": "cholesterolContent",
                        "total": 366.06485693750005,
                        "hasRDI": True,
                        "daily": 122.02161897916669,
                        "unit": "mg"
                    },
                    {
                        "label": "Sodium",
                        "tag": "NA",
                        "schemaOrgTag": "sodiumContent",
                        "total": 962.9902962619411,
                        "hasRDI": True,
                        "daily": 40.12459567758088,
                        "unit": "mg"
                    },
                    {
                        "label": "Calcium",
                        "tag": "CA",
                        "schemaOrgTag": '',
                        "total": 1147.5176438125075,
                        "hasRDI": True,
                        "daily": 114.75176438125075,
                        "unit": "mg"
                    },
                    {
                        "label": "Magnesium",
                        "tag": "MG",
                        "schemaOrgTag": '',
                        "total": 771.414528291667,
                        "hasRDI": True,
                        "daily": 183.6701257837302,
                        "unit": "mg"
                    },
                    {
                        "label": "Potassium",
                        "tag": "K",
                        "schemaOrgTag": '',
                        "total": 3633.184111770836,
                        "hasRDI": True,
                        "daily": 77.30178961214546,
                        "unit": "mg"
                    },
                    {
                        "label": "Iron",
                        "tag": "FE",
                        "schemaOrgTag": '',
                        "total": 38.39956152916677,
                        "hasRDI": True,
                        "daily": 213.33089738425983,
                        "unit": "mg"
                    },
                    {
                        "label": "Zinc",
                        "tag": "ZN",
                        "schemaOrgTag": '',
                        "total": 14.824317258541697,
                        "hasRDI": True,
                        "daily": 134.76652053219723,
                        "unit": "mg"
                    },
                    {
                        "label": "Phosphorus",
                        "tag": "P",
                        "schemaOrgTag": '',
                        "total": 1724.3103122500002,
                        "hasRDI": True,
                        "daily": 246.33004460714287,
                        "unit": "mg"
                    },
                    {
                        "label": "Vitamin A",
                        "tag": "VITA_RAE",
                        "schemaOrgTag": '',
                        "total": 1006.7859046250001,
                        "hasRDI": True,
                        "daily": 111.8651005138889,
                        "unit": "µg"
                    },
                    {
                        "label": "Vitamin C",
                        "tag": "VITC",
                        "schemaOrgTag": '',
                        "total": 3.96,
                        "hasRDI": True,
                        "daily": 4.4,
                        "unit": "mg"
                    },
                    {
                        "label": "Thiamin (B1)",
                        "tag": "THIA",
                        "schemaOrgTag": '',
                        "total": 1.0536215452916666,
                        "hasRDI": True,
                        "daily": 87.80179544097221,
                        "unit": "mg"
                    },
                    {
                        "label": "Riboflavin (B2)",
                        "tag": "RIBF",
                        "schemaOrgTag": '',
                        "total": 2.6602714470416666,
                        "hasRDI": True,
                        "daily": 204.6362651570513,
                        "unit": "mg"
                    },
                    {
                        "label": "Niacin (B3)",
                        "tag": "NIA",
                        "schemaOrgTag": '',
                        "total": 8.807872094791666,
                        "hasRDI": True,
                        "daily": 55.04920059244791,
                        "unit": "mg"
                    },
                    {
                        "label": "Vitamin B6",
                        "tag": "VITB6A",
                        "schemaOrgTag": '',
                        "total": 0.4881258545416667,
                        "hasRDI": True,
                        "daily": 37.54814265705128,
                        "unit": "mg"
                    },
                    {
                        "label": "Folate equivalent (total)",
                        "tag": "FOLDFE",
                        "schemaOrgTag": '',
                        "total": 282.042,
                        "hasRDI": True,
                        "daily": 70.5105,
                        "unit": "µg"
                    },
                    {
                        "label": "Folate (food)",
                        "tag": "FOLFD",
                        "schemaOrgTag": '',
                        "total": 63.708666666666666,
                        "hasRDI": False,
                        "daily": 0.0,
                        "unit": "µg"
                    },
                    {
                        "label": "Folic acid",
                        "tag": "FOLAC",
                        "schemaOrgTag": '',
                        "total": 128.33333333333331,
                        "hasRDI": False,
                        "daily": 0.0,
                        "unit": "µg"
                    },
                    {
                        "label": "Vitamin B12",
                        "tag": "VITB12",
                        "schemaOrgTag": '',
                        "total": 3.7499666475000004,
                        "hasRDI": True,
                        "daily": 156.24861031250003,
                        "unit": "µg"
                    },
                    {
                        "label": "Vitamin D",
                        "tag": "VITD",
                        "schemaOrgTag": '',
                        "total": 2.1130000000000004,
                        "hasRDI": True,
                        "daily": 14.08666666666667,
                        "unit": "µg"
                    },
                    {
                        "label": "Vitamin E",
                        "tag": "TOCPHA",
                        "schemaOrgTag": '',
                        "total": 4.590748531041667,
                        "hasRDI": True,
                        "daily": 30.604990206944446,
                        "unit": "mg"
                    },
                    {
                        "label": "Vitamin K",
                        "tag": "VITK1",
                        "schemaOrgTag": '',
                        "total": 25.34095188125,
                        "hasRDI": True,
                        "daily": 21.117459901041666,
                        "unit": "µg"
                    },
                    {
                        "label": "Sugar alcohols",
                        "tag": "Sugar.alcohol",
                        "schemaOrgTag": '',
                        "total": 0.0,
                        "hasRDI": False,
                        "daily": 0.0,
                        "unit": "g"
                    },
                    {
                        "label": "Water",
                        "tag": "WATER",
                        "schemaOrgTag": '',
                        "total": 534.2687048764584,
                        "hasRDI": False,
                        "daily": 0.0,
                        "unit": "g"
                    }
                ]
            },
            "_links": {
                "self": {
                    "title": "Self",
                    "href": "https://api.edamam.com/api/recipes/v2/8cc770d62c36aa8b1a956696966d39c9?type=public&app_id=e909afd5&app_key=34e59dda7e1bffb92e49c416e9449e1d"
                }
            }
        },
        {
            "recipe": {
                "uri": "http://www.edamam.com/ontologies/edamam.owl#recipe_e96c729fd52df87738cf5d4faf40a792",
                "label": "Chorizo and Potato Tacos with Avocado Salsa Verde",
                "image": "https://edamam-product-images.s3.amazonaws.com/web-img/211/2115ff1e77dcf4dd65034b1adb9443a8.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLWVhc3QtMSJIMEYCIQCP2Gbt%2ByPQIVKV%2FafgML7WXbkOusL9fCs6d1le6dFKYAIhAJcnuEh%2B1NzOso38QgGaVBwaVQAMxyMJATg%2FR%2Fl0jl96KsEFCJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMMTg3MDE3MTUwOTg2IgydADkJdybnmhdEGwQqlQUNCCJJEzulouVCRRPPDPN9Ik9nmgPZk%2Fam6u04CTug5FWfzto4W1y6mlAuXr3EHPB%2FvTcZ%2BmAkgcS5%2FRfKsviGgYg1PBDbKvJFWJigqXNb6jHaHO3eyZnXpof0Qk2PachTFyGGF7upzvEiKr6BGB6DtCoEGe3wCd0iFSMS%2Ft8LIlICGGYaaCvWq9TXeaXkel5jju8XxawzfW0OY8ad1NODjiJJ%2FJ02goRzRa3HwZdXj0P4%2FwwiBHg8BMnsBu5XvhNCt9Gz%2Bxp9cZIC8TMv%2FY8rOvepaH28zVl5BjLGle3tn5syTeLiH6OS68I4OndB2qqeqZqdi9cu6zb1H0y8aKh8r8IIaHqXhP6jBXwOxUN8uimNrMJnaDPxNdvFPuR5yx8UApiuserTd1b1ZIBFiBJ6lavYUBrkLW%2B7bZIJltsNTSxF2GTKFWoXHKGf3%2FXYj%2FniRUh%2BB3xUXrXh8PzVKChkdfuCxirnj5UG2XCrj22%2BBJG8S8UHiExHaIwt01Nel6V7Y0IlXWvwqK8YEx%2FHOI%2FewXERfrnIQDCsrQyC7qTLL3HndUW2Ke8ib2iC%2BPgaP6xDqkqdlhOSojQHG4rfwcyVOFOzeauzAO7Rc77mb0rCUJdMckP6nKiD7nrtjlZXznFmYhCvjmWQF2l06Jl7xQsr%2BjkGAeoXo9X%2FiC11ZTNfxOVIe3LWWkRvMwGWvgvtgF4ZEDGaLXgsbO4I8%2FpSmGD4ox9ZWDfX%2BtTURCyBYVXqYpQ4TpgMhHqAtTUr4TNc7GRLVbfi1xqZNQDt1Sfdzh3Xq88dOJyKsyUs7rcFuuxoNyxvqstWVaAyRglOH1n%2BpV0xA7%2FKEHa%2F8%2FzH6uaXeIp3eLJN1%2BGlAQc1sP2jehPHqGi5Lc7YMOKk8akGOrABqEMeyIMA72vRUvaZqcs7N77uX3kDw2%2BTfyF8pS8HYdR1%2BEU1ekEPGlPPLyTo0NFmbmMa4urw%2B19eIvlGSnFjiSeee%2F%2BeotdKLVnDgZ5aNxOYivkgUqjazWNTWX1qdv7Jq7GWrNDLwjZiU5zLvpcjSyzLyGAVIo8pW14m4aC3jppuzjKpasygGK2%2Bf%2BmxisMAkIdRRS5aXW9PY%2FuwiBnL3qiZT5RtAdamISZZM9jUAWY%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231028T003610Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFPXEGMX3T%2F20231028%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=4ebd5a474188172c68824255034c3472f71137a830b1e3df488d164d85a6f5fd",
                "images": {
                    "THUMBNAIL": {
                        "url": "https://edamam-product-images.s3.amazonaws.com/web-img/211/2115ff1e77dcf4dd65034b1adb9443a8-s.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLWVhc3QtMSJIMEYCIQCP2Gbt%2ByPQIVKV%2FafgML7WXbkOusL9fCs6d1le6dFKYAIhAJcnuEh%2B1NzOso38QgGaVBwaVQAMxyMJATg%2FR%2Fl0jl96KsEFCJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMMTg3MDE3MTUwOTg2IgydADkJdybnmhdEGwQqlQUNCCJJEzulouVCRRPPDPN9Ik9nmgPZk%2Fam6u04CTug5FWfzto4W1y6mlAuXr3EHPB%2FvTcZ%2BmAkgcS5%2FRfKsviGgYg1PBDbKvJFWJigqXNb6jHaHO3eyZnXpof0Qk2PachTFyGGF7upzvEiKr6BGB6DtCoEGe3wCd0iFSMS%2Ft8LIlICGGYaaCvWq9TXeaXkel5jju8XxawzfW0OY8ad1NODjiJJ%2FJ02goRzRa3HwZdXj0P4%2FwwiBHg8BMnsBu5XvhNCt9Gz%2Bxp9cZIC8TMv%2FY8rOvepaH28zVl5BjLGle3tn5syTeLiH6OS68I4OndB2qqeqZqdi9cu6zb1H0y8aKh8r8IIaHqXhP6jBXwOxUN8uimNrMJnaDPxNdvFPuR5yx8UApiuserTd1b1ZIBFiBJ6lavYUBrkLW%2B7bZIJltsNTSxF2GTKFWoXHKGf3%2FXYj%2FniRUh%2BB3xUXrXh8PzVKChkdfuCxirnj5UG2XCrj22%2BBJG8S8UHiExHaIwt01Nel6V7Y0IlXWvwqK8YEx%2FHOI%2FewXERfrnIQDCsrQyC7qTLL3HndUW2Ke8ib2iC%2BPgaP6xDqkqdlhOSojQHG4rfwcyVOFOzeauzAO7Rc77mb0rCUJdMckP6nKiD7nrtjlZXznFmYhCvjmWQF2l06Jl7xQsr%2BjkGAeoXo9X%2FiC11ZTNfxOVIe3LWWkRvMwGWvgvtgF4ZEDGaLXgsbO4I8%2FpSmGD4ox9ZWDfX%2BtTURCyBYVXqYpQ4TpgMhHqAtTUr4TNc7GRLVbfi1xqZNQDt1Sfdzh3Xq88dOJyKsyUs7rcFuuxoNyxvqstWVaAyRglOH1n%2BpV0xA7%2FKEHa%2F8%2FzH6uaXeIp3eLJN1%2BGlAQc1sP2jehPHqGi5Lc7YMOKk8akGOrABqEMeyIMA72vRUvaZqcs7N77uX3kDw2%2BTfyF8pS8HYdR1%2BEU1ekEPGlPPLyTo0NFmbmMa4urw%2B19eIvlGSnFjiSeee%2F%2BeotdKLVnDgZ5aNxOYivkgUqjazWNTWX1qdv7Jq7GWrNDLwjZiU5zLvpcjSyzLyGAVIo8pW14m4aC3jppuzjKpasygGK2%2Bf%2BmxisMAkIdRRS5aXW9PY%2FuwiBnL3qiZT5RtAdamISZZM9jUAWY%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231028T003610Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFPXEGMX3T%2F20231028%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=4a03252ed19a44964d0f13970f465d215ada32013f931ec10f496bdcb15f521f",
                        "width": 100,
                        "height": 100
                    },
                    "SMALL": {
                        "url": "https://edamam-product-images.s3.amazonaws.com/web-img/211/2115ff1e77dcf4dd65034b1adb9443a8-m.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLWVhc3QtMSJIMEYCIQCP2Gbt%2ByPQIVKV%2FafgML7WXbkOusL9fCs6d1le6dFKYAIhAJcnuEh%2B1NzOso38QgGaVBwaVQAMxyMJATg%2FR%2Fl0jl96KsEFCJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMMTg3MDE3MTUwOTg2IgydADkJdybnmhdEGwQqlQUNCCJJEzulouVCRRPPDPN9Ik9nmgPZk%2Fam6u04CTug5FWfzto4W1y6mlAuXr3EHPB%2FvTcZ%2BmAkgcS5%2FRfKsviGgYg1PBDbKvJFWJigqXNb6jHaHO3eyZnXpof0Qk2PachTFyGGF7upzvEiKr6BGB6DtCoEGe3wCd0iFSMS%2Ft8LIlICGGYaaCvWq9TXeaXkel5jju8XxawzfW0OY8ad1NODjiJJ%2FJ02goRzRa3HwZdXj0P4%2FwwiBHg8BMnsBu5XvhNCt9Gz%2Bxp9cZIC8TMv%2FY8rOvepaH28zVl5BjLGle3tn5syTeLiH6OS68I4OndB2qqeqZqdi9cu6zb1H0y8aKh8r8IIaHqXhP6jBXwOxUN8uimNrMJnaDPxNdvFPuR5yx8UApiuserTd1b1ZIBFiBJ6lavYUBrkLW%2B7bZIJltsNTSxF2GTKFWoXHKGf3%2FXYj%2FniRUh%2BB3xUXrXh8PzVKChkdfuCxirnj5UG2XCrj22%2BBJG8S8UHiExHaIwt01Nel6V7Y0IlXWvwqK8YEx%2FHOI%2FewXERfrnIQDCsrQyC7qTLL3HndUW2Ke8ib2iC%2BPgaP6xDqkqdlhOSojQHG4rfwcyVOFOzeauzAO7Rc77mb0rCUJdMckP6nKiD7nrtjlZXznFmYhCvjmWQF2l06Jl7xQsr%2BjkGAeoXo9X%2FiC11ZTNfxOVIe3LWWkRvMwGWvgvtgF4ZEDGaLXgsbO4I8%2FpSmGD4ox9ZWDfX%2BtTURCyBYVXqYpQ4TpgMhHqAtTUr4TNc7GRLVbfi1xqZNQDt1Sfdzh3Xq88dOJyKsyUs7rcFuuxoNyxvqstWVaAyRglOH1n%2BpV0xA7%2FKEHa%2F8%2FzH6uaXeIp3eLJN1%2BGlAQc1sP2jehPHqGi5Lc7YMOKk8akGOrABqEMeyIMA72vRUvaZqcs7N77uX3kDw2%2BTfyF8pS8HYdR1%2BEU1ekEPGlPPLyTo0NFmbmMa4urw%2B19eIvlGSnFjiSeee%2F%2BeotdKLVnDgZ5aNxOYivkgUqjazWNTWX1qdv7Jq7GWrNDLwjZiU5zLvpcjSyzLyGAVIo8pW14m4aC3jppuzjKpasygGK2%2Bf%2BmxisMAkIdRRS5aXW9PY%2FuwiBnL3qiZT5RtAdamISZZM9jUAWY%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231028T003610Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFPXEGMX3T%2F20231028%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=ab025cd2aa89b6ac0950e928b2b9fc38721730152435fc03f0cafaedea7838e5",
                        "width": 200,
                        "height": 200
                    },
                    "REGULAR": {
                        "url": "https://edamam-product-images.s3.amazonaws.com/web-img/211/2115ff1e77dcf4dd65034b1adb9443a8.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLWVhc3QtMSJIMEYCIQCP2Gbt%2ByPQIVKV%2FafgML7WXbkOusL9fCs6d1le6dFKYAIhAJcnuEh%2B1NzOso38QgGaVBwaVQAMxyMJATg%2FR%2Fl0jl96KsEFCJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMMTg3MDE3MTUwOTg2IgydADkJdybnmhdEGwQqlQUNCCJJEzulouVCRRPPDPN9Ik9nmgPZk%2Fam6u04CTug5FWfzto4W1y6mlAuXr3EHPB%2FvTcZ%2BmAkgcS5%2FRfKsviGgYg1PBDbKvJFWJigqXNb6jHaHO3eyZnXpof0Qk2PachTFyGGF7upzvEiKr6BGB6DtCoEGe3wCd0iFSMS%2Ft8LIlICGGYaaCvWq9TXeaXkel5jju8XxawzfW0OY8ad1NODjiJJ%2FJ02goRzRa3HwZdXj0P4%2FwwiBHg8BMnsBu5XvhNCt9Gz%2Bxp9cZIC8TMv%2FY8rOvepaH28zVl5BjLGle3tn5syTeLiH6OS68I4OndB2qqeqZqdi9cu6zb1H0y8aKh8r8IIaHqXhP6jBXwOxUN8uimNrMJnaDPxNdvFPuR5yx8UApiuserTd1b1ZIBFiBJ6lavYUBrkLW%2B7bZIJltsNTSxF2GTKFWoXHKGf3%2FXYj%2FniRUh%2BB3xUXrXh8PzVKChkdfuCxirnj5UG2XCrj22%2BBJG8S8UHiExHaIwt01Nel6V7Y0IlXWvwqK8YEx%2FHOI%2FewXERfrnIQDCsrQyC7qTLL3HndUW2Ke8ib2iC%2BPgaP6xDqkqdlhOSojQHG4rfwcyVOFOzeauzAO7Rc77mb0rCUJdMckP6nKiD7nrtjlZXznFmYhCvjmWQF2l06Jl7xQsr%2BjkGAeoXo9X%2FiC11ZTNfxOVIe3LWWkRvMwGWvgvtgF4ZEDGaLXgsbO4I8%2FpSmGD4ox9ZWDfX%2BtTURCyBYVXqYpQ4TpgMhHqAtTUr4TNc7GRLVbfi1xqZNQDt1Sfdzh3Xq88dOJyKsyUs7rcFuuxoNyxvqstWVaAyRglOH1n%2BpV0xA7%2FKEHa%2F8%2FzH6uaXeIp3eLJN1%2BGlAQc1sP2jehPHqGi5Lc7YMOKk8akGOrABqEMeyIMA72vRUvaZqcs7N77uX3kDw2%2BTfyF8pS8HYdR1%2BEU1ekEPGlPPLyTo0NFmbmMa4urw%2B19eIvlGSnFjiSeee%2F%2BeotdKLVnDgZ5aNxOYivkgUqjazWNTWX1qdv7Jq7GWrNDLwjZiU5zLvpcjSyzLyGAVIo8pW14m4aC3jppuzjKpasygGK2%2Bf%2BmxisMAkIdRRS5aXW9PY%2FuwiBnL3qiZT5RtAdamISZZM9jUAWY%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231028T003610Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFPXEGMX3T%2F20231028%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=4ebd5a474188172c68824255034c3472f71137a830b1e3df488d164d85a6f5fd",
                        "width": 300,
                        "height": 300
                    },
                    "LARGE": {
                        "url": "https://edamam-product-images.s3.amazonaws.com/web-img/211/2115ff1e77dcf4dd65034b1adb9443a8-l.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLWVhc3QtMSJIMEYCIQCP2Gbt%2ByPQIVKV%2FafgML7WXbkOusL9fCs6d1le6dFKYAIhAJcnuEh%2B1NzOso38QgGaVBwaVQAMxyMJATg%2FR%2Fl0jl96KsEFCJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMMTg3MDE3MTUwOTg2IgydADkJdybnmhdEGwQqlQUNCCJJEzulouVCRRPPDPN9Ik9nmgPZk%2Fam6u04CTug5FWfzto4W1y6mlAuXr3EHPB%2FvTcZ%2BmAkgcS5%2FRfKsviGgYg1PBDbKvJFWJigqXNb6jHaHO3eyZnXpof0Qk2PachTFyGGF7upzvEiKr6BGB6DtCoEGe3wCd0iFSMS%2Ft8LIlICGGYaaCvWq9TXeaXkel5jju8XxawzfW0OY8ad1NODjiJJ%2FJ02goRzRa3HwZdXj0P4%2FwwiBHg8BMnsBu5XvhNCt9Gz%2Bxp9cZIC8TMv%2FY8rOvepaH28zVl5BjLGle3tn5syTeLiH6OS68I4OndB2qqeqZqdi9cu6zb1H0y8aKh8r8IIaHqXhP6jBXwOxUN8uimNrMJnaDPxNdvFPuR5yx8UApiuserTd1b1ZIBFiBJ6lavYUBrkLW%2B7bZIJltsNTSxF2GTKFWoXHKGf3%2FXYj%2FniRUh%2BB3xUXrXh8PzVKChkdfuCxirnj5UG2XCrj22%2BBJG8S8UHiExHaIwt01Nel6V7Y0IlXWvwqK8YEx%2FHOI%2FewXERfrnIQDCsrQyC7qTLL3HndUW2Ke8ib2iC%2BPgaP6xDqkqdlhOSojQHG4rfwcyVOFOzeauzAO7Rc77mb0rCUJdMckP6nKiD7nrtjlZXznFmYhCvjmWQF2l06Jl7xQsr%2BjkGAeoXo9X%2FiC11ZTNfxOVIe3LWWkRvMwGWvgvtgF4ZEDGaLXgsbO4I8%2FpSmGD4ox9ZWDfX%2BtTURCyBYVXqYpQ4TpgMhHqAtTUr4TNc7GRLVbfi1xqZNQDt1Sfdzh3Xq88dOJyKsyUs7rcFuuxoNyxvqstWVaAyRglOH1n%2BpV0xA7%2FKEHa%2F8%2FzH6uaXeIp3eLJN1%2BGlAQc1sP2jehPHqGi5Lc7YMOKk8akGOrABqEMeyIMA72vRUvaZqcs7N77uX3kDw2%2BTfyF8pS8HYdR1%2BEU1ekEPGlPPLyTo0NFmbmMa4urw%2B19eIvlGSnFjiSeee%2F%2BeotdKLVnDgZ5aNxOYivkgUqjazWNTWX1qdv7Jq7GWrNDLwjZiU5zLvpcjSyzLyGAVIo8pW14m4aC3jppuzjKpasygGK2%2Bf%2BmxisMAkIdRRS5aXW9PY%2FuwiBnL3qiZT5RtAdamISZZM9jUAWY%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231028T003610Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFPXEGMX3T%2F20231028%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=3d975c88cb32f5aaccc4dc4d4c6d3ed1ed9f21aca2a14b6f270e74752b65d72e",
                        "width": 600,
                        "height": 600
                    }
                },
                "source": "Closet Cooking",
                "url": "https://www.closetcooking.com/chorizo-and-potato-tacos-with-avocado/",
                "shareAs": "http://www.edamam.com/recipe/chorizo-and-potato-tacos-with-avocado-salsa-verde-e96c729fd52df87738cf5d4faf40a792/tacos",
                "yield": 4.0,
                "dietLabels": [
                    "High-Fiber"
                ],
                "healthLabels": [
                    "Dairy-Free",
                    "Egg-Free",
                    "Peanut-Free",
                    "Tree-Nut-Free",
                    "Soy-Free",
                    "Fish-Free",
                    "Shellfish-Free",
                    "Crustacean-Free",
                    "Celery-Free",
                    "Mustard-Free",
                    "Sesame-Free",
                    "Lupine-Free",
                    "Mollusk-Free",
                    "Alcohol-Free",
                    "Sulfite-Free"
                ],
                "cautions": [
                    "Eggs",
                    "Milk",
                    "Sulfites"
                ],
                "ingredientLines": [
                    "1 cup salsa verde",
                    "1/2 avocado",
                    "For the tacos:",
                    "1 tablespoon oil (or bacon grease!)",
                    "1 pound potatoes",
                    "1 pound fresh Mexican style chorizo sausage, casing removed",
                    "1 onion, diced",
                    "3 cloves garlic, chopped",
                    "salt and pepper to taste",
                    "12 small corn tortillas, warmed",
                    "1 onion, diced",
                    "1 cup cilantro"
                ],
                "ingredients": [
                    {
                        "text": "1 cup salsa verde",
                        "quantity": 1.0,
                        "measure": "cup",
                        "food": "salsa verde",
                        "weight": 240.00000000405768,
                        "foodCategory": "condiments and sauces",
                        "foodId": "food_ax6tfr7a1hlbwpbkyaytlbkxaub2",
                        "image": "https://www.edamam.com/food-img/205/205d9e349c3b7e60d4886c5ab4e27a92.jpg"
                    },
                    {
                        "text": "1/2 avocado",
                        "quantity": 0.5,
                        "measure": "<unit>",
                        "food": "avocado",
                        "weight": 100.5,
                        "foodCategory": "fruit",
                        "foodId": "food_b0yuze4b1g3afpanijno5abtiu28",
                        "image": "https://www.edamam.com/food-img/984/984a707ea8e9c6bf5f6498970a9e6d9d.jpg"
                    },
                    {
                        "text": "1 tablespoon oil (or bacon grease!)",
                        "quantity": 1.0,
                        "measure": "tablespoon",
                        "food": "oil",
                        "weight": 14.0,
                        "foodCategory": "Oils",
                        "foodId": "food_bk9p9aaavhvoq4bqsnprobpsiuxs",
                        "image": "https://www.edamam.com/food-img/07e/07e106ab3536d57428e5c46d009038f8.jpg"
                    },
                    {
                        "text": "1 pound potatoes",
                        "quantity": 1.0,
                        "measure": "pound",
                        "food": "potatoes",
                        "weight": 453.59237,
                        "foodCategory": "vegetables",
                        "foodId": "food_abiw5baauresjmb6xpap2bg3otzu",
                        "image": "https://www.edamam.com/food-img/651/6512e82417bce15c2899630c1a2799df.jpg"
                    },
                    {
                        "text": "1 pound fresh Mexican style chorizo sausage, casing removed",
                        "quantity": 1.0,
                        "measure": "pound",
                        "food": "chorizo",
                        "weight": 453.59237,
                        "foodCategory": "Cured meats",
                        "foodId": "food_a011ctbbqlxv1ebqtemvla9v6mpa",
                        "image": "https://www.edamam.com/food-img/c01/c0139ae7ad8a0334a23365b6284a5819.jpg"
                    },
                    {
                        "text": "1 onion, diced",
                        "quantity": 1.0,
                        "measure": "<unit>",
                        "food": "onion",
                        "weight": 125.0,
                        "foodCategory": "vegetables",
                        "foodId": "food_bmrvi4ob4binw9a5m7l07amlfcoy",
                        "image": "https://www.edamam.com/food-img/205/205e6bf2399b85d34741892ef91cc603.jpg"
                    },
                    {
                        "text": "3 cloves garlic, chopped",
                        "quantity": 3.0,
                        "measure": "clove",
                        "food": "garlic",
                        "weight": 9.0,
                        "foodCategory": "vegetables",
                        "foodId": "food_avtcmx6bgjv1jvay6s6stan8dnyp",
                        "image": "https://www.edamam.com/food-img/6ee/6ee142951f48aaf94f4312409f8d133d.jpg"
                    },
                    {
                        "text": "salt and pepper to taste",
                        "quantity": 0.0,
                        "measure": '',
                        "food": "salt",
                        "weight": 10.948108440024347,
                        "foodCategory": "Condiments and sauces",
                        "foodId": "food_btxz81db72hwbra2pncvebzzzum9",
                        "image": "https://www.edamam.com/food-img/694/6943ea510918c6025795e8dc6e6eaaeb.jpg"
                    },
                    {
                        "text": "salt and pepper to taste",
                        "quantity": 0.0,
                        "measure": '',
                        "food": "pepper",
                        "weight": 5.474054220012174,
                        "foodCategory": "Condiments and sauces",
                        "foodId": "food_b6ywzluaaxv02wad7s1r9ag4py89",
                        "image": "https://www.edamam.com/food-img/c6e/c6e5c3bd8d3bc15175d9766971a4d1b2.jpg"
                    },
                    {
                        "text": "12 small corn tortillas, warmed",
                        "quantity": 12.0,
                        "measure": "<unit>",
                        "food": "corn tortillas",
                        "weight": 288.0,
                        "foodCategory": "quick breads and pastries",
                        "foodId": "food_bhw0b95agm97s0abfignnb8fsvb3",
                        "image": "https://www.edamam.com/food-img/b8a/b8ad23dcc06f2324f944e47eb579d644.jpg"
                    },
                    {
                        "text": "1 onion, diced",
                        "quantity": 1.0,
                        "measure": "<unit>",
                        "food": "onion",
                        "weight": 125.0,
                        "foodCategory": "vegetables",
                        "foodId": "food_bmrvi4ob4binw9a5m7l07amlfcoy",
                        "image": "https://www.edamam.com/food-img/205/205e6bf2399b85d34741892ef91cc603.jpg"
                    },
                    {
                        "text": "1 cup cilantro",
                        "quantity": 1.0,
                        "measure": "cup",
                        "food": "cilantro",
                        "weight": 16.0,
                        "foodCategory": "vegetables",
                        "foodId": "food_alhzhuwb4lc7jnb5s6f02by60bzp",
                        "image": "https://www.edamam.com/food-img/d57/d57e375b6ff99a90c7ee2b1990a1af36.jpg"
                    }
                ],
                "calories": 2826.3294161937724,
                "totalCO2Emissions": 6687.46211360718,
                "co2EmissionsClass": "F",
                "totalWeight": 1830.15879422407,
                "totalTime": 0.0,
                "cuisineType": [
                    "mexican"
                ],
                "mealType": [
                    "lunch/dinner"
                ],
                "dishType": [
                    "sandwiches"
                ],
                "totalNutrients": {
                    "ENERC_KCAL": {
                        "label": "Energy",
                        "quantity": 2826.3294161937724,
                        "unit": "kcal"
                    },
                    "FAT": {
                        "label": "Fat",
                        "quantity": 153.93407217060852,
                        "unit": "g"
                    },
                    "FASAT": {
                        "label": "Saturated",
                        "quantity": 43.78937126615818,
                        "unit": "g"
                    },
                    "FATRN": {
                        "label": "Trans",
                        "quantity": 0.6132186151000001,
                        "unit": "g"
                    },
                    "FAMS": {
                        "label": "Monounsaturated",
                        "quantity": 68.91176632808589,
                        "unit": "g"
                    },
                    "FAPU": {
                        "label": "Polyunsaturated",
                        "quantity": 29.673621766515723,
                        "unit": "g"
                    },
                    "CHOCDF": {
                        "label": "Carbs",
                        "quantity": 279.2287010370659,
                        "unit": "g"
                    },
                    "CHOCDF.net": {
                        "label": "Carbohydrates (net)",
                        "quantity": 233.99382554932572,
                        "unit": "g"
                    },
                    "FIBTG": {
                        "label": "Fiber",
                        "quantity": 45.234875487740176,
                        "unit": "g"
                    },
                    "SUGAR": {
                        "label": "Sugars",
                        "quantity": 26.181391381150092,
                        "unit": "g"
                    },
                    "PROCNT": {
                        "label": "Protein",
                        "quantity": 96.35770754392712,
                        "unit": "g"
                    },
                    "CHOLE": {
                        "label": "Cholesterol",
                        "quantity": 285.7631931,
                        "unit": "mg"
                    },
                    "NA": {
                        "label": "Sodium",
                        "quantity": 5932.543228680765,
                        "unit": "mg"
                    },
                    "CA": {
                        "label": "Calcium",
                        "quantity": 516.3136948950191,
                        "unit": "mg"
                    },
                    "MG": {
                        "label": "Magnesium",
                        "quantity": 517.9203518169918,
                        "unit": "mg"
                    },
                    "K": {
                        "label": "Potassium",
                        "quantity": 5526.791993236672,
                        "unit": "mg"
                    },
                    "FE": {
                        "label": "Iron",
                        "quantity": 17.217631278789558,
                        "unit": "mg"
                    },
                    "ZN": {
                        "label": "Zinc",
                        "quantity": 14.67167017122829,
                        "unit": "mg"
                    },
                    "P": {
                        "label": "Phosphorus",
                        "quantity": 2091.979287869283,
                        "unit": "mg"
                    },
                    "VITA_RAE": {
                        "label": "Vitamin A",
                        "quantity": 88.83299463984963,
                        "unit": "µg"
                    },
                    "VITC": {
                        "label": "Vitamin C",
                        "quantity": 154.5556968904991,
                        "unit": "mg"
                    },
                    "THIA": {
                        "label": "Thiamin (B1)",
                        "quantity": 1.90443300415948,
                        "unit": "mg"
                    },
                    "RIBF": {
                        "label": "Riboflavin (B2)",
                        "quantity": 2.068709202997483,
                        "unit": "mg"
                    },
                    "NIA": {
                        "label": "Niacin (B3)",
                        "quantity": 40.169285979173885,
                        "unit": "mg"
                    },
                    "VITB6A": {
                        "label": "Vitamin B6",
                        "quantity": 4.311023878483604,
                        "unit": "mg"
                    },
                    "FOLDFE": {
                        "label": "Folate equivalent (total)",
                        "quantity": 241.6644447177267,
                        "unit": "µg"
                    },
                    "FOLFD": {
                        "label": "Folate (food)",
                        "quantity": 241.6644447177267,
                        "unit": "µg"
                    },
                    "FOLAC": {
                        "label": "Folic acid",
                        "quantity": 0.0,
                        "unit": "µg"
                    },
                    "VITB12": {
                        "label": "Vitamin B12",
                        "quantity": 9.071847400000001,
                        "unit": "µg"
                    },
                    "VITD": {
                        "label": "Vitamin D",
                        "quantity": 6.80388555,
                        "unit": "µg"
                    },
                    "TOCPHA": {
                        "label": "Vitamin E",
                        "quantity": 7.926142614905577,
                        "unit": "mg"
                    },
                    "VITK1": {
                        "label": "Vitamin K",
                        "quantity": 132.52929632137182,
                        "unit": "µg"
                    },
                    "WATER": {
                        "label": "Water",
                        "quantity": 1271.8320325811333,
                        "unit": "g"
                    }
                },
                "totalDaily": {
                    "ENERC_KCAL": {
                        "label": "Energy",
                        "quantity": 141.3164708096886,
                        "unit": "%"
                    },
                    "FAT": {
                        "label": "Fat",
                        "quantity": 236.82164949324388,
                        "unit": "%"
                    },
                    "FASAT": {
                        "label": "Saturated",
                        "quantity": 218.9468563307909,
                        "unit": "%"
                    },
                    "CHOCDF": {
                        "label": "Carbs",
                        "quantity": 93.07623367902195,
                        "unit": "%"
                    },
                    "FIBTG": {
                        "label": "Fiber",
                        "quantity": 180.9395019509607,
                        "unit": "%"
                    },
                    "PROCNT": {
                        "label": "Protein",
                        "quantity": 192.71541508785424,
                        "unit": "%"
                    },
                    "CHOLE": {
                        "label": "Cholesterol",
                        "quantity": 95.25439770000001,
                        "unit": "%"
                    },
                    "NA": {
                        "label": "Sodium",
                        "quantity": 247.18930119503187,
                        "unit": "%"
                    },
                    "CA": {
                        "label": "Calcium",
                        "quantity": 51.631369489501914,
                        "unit": "%"
                    },
                    "MG": {
                        "label": "Magnesium",
                        "quantity": 123.31436948023615,
                        "unit": "%"
                    },
                    "K": {
                        "label": "Potassium",
                        "quantity": 117.59131900503557,
                        "unit": "%"
                    },
                    "FE": {
                        "label": "Iron",
                        "quantity": 95.65350710438643,
                        "unit": "%"
                    },
                    "ZN": {
                        "label": "Zinc",
                        "quantity": 133.378819738439,
                        "unit": "%"
                    },
                    "P": {
                        "label": "Phosphorus",
                        "quantity": 298.8541839813261,
                        "unit": "%"
                    },
                    "VITA_RAE": {
                        "label": "Vitamin A",
                        "quantity": 9.870332737761071,
                        "unit": "%"
                    },
                    "VITC": {
                        "label": "Vitamin C",
                        "quantity": 171.72855210055454,
                        "unit": "%"
                    },
                    "THIA": {
                        "label": "Thiamin (B1)",
                        "quantity": 158.70275034662333,
                        "unit": "%"
                    },
                    "RIBF": {
                        "label": "Riboflavin (B2)",
                        "quantity": 159.13147715365253,
                        "unit": "%"
                    },
                    "NIA": {
                        "label": "Niacin (B3)",
                        "quantity": 251.0580373698368,
                        "unit": "%"
                    },
                    "VITB6A": {
                        "label": "Vitamin B6",
                        "quantity": 331.61722142181566,
                        "unit": "%"
                    },
                    "FOLDFE": {
                        "label": "Folate equivalent (total)",
                        "quantity": 60.416111179431674,
                        "unit": "%"
                    },
                    "VITB12": {
                        "label": "Vitamin B12",
                        "quantity": 377.99364166666675,
                        "unit": "%"
                    },
                    "VITD": {
                        "label": "Vitamin D",
                        "quantity": 45.359237,
                        "unit": "%"
                    },
                    "TOCPHA": {
                        "label": "Vitamin E",
                        "quantity": 52.840950766037174,
                        "unit": "%"
                    },
                    "VITK1": {
                        "label": "Vitamin K",
                        "quantity": 110.44108026780985,
                        "unit": "%"
                    }
                },
                "digest": [
                    {
                        "label": "Fat",
                        "tag": "FAT",
                        "schemaOrgTag": "fatContent",
                        "total": 153.93407217060852,
                        "hasRDI": True,
                        "daily": 236.82164949324388,
                        "unit": "g",
                        "sub": [
                            {
                                "label": "Saturated",
                                "tag": "FASAT",
                                "schemaOrgTag": "saturatedFatContent",
                                "total": 43.78937126615818,
                                "hasRDI": True,
                                "daily": 218.9468563307909,
                                "unit": "g"
                            },
                            {
                                "label": "Trans",
                                "tag": "FATRN",
                                "schemaOrgTag": "transFatContent",
                                "total": 0.6132186151000001,
                                "hasRDI": False,
                                "daily": 0.0,
                                "unit": "g"
                            },
                            {
                                "label": "Monounsaturated",
                                "tag": "FAMS",
                                "schemaOrgTag": '',
                                "total": 68.91176632808589,
                                "hasRDI": False,
                                "daily": 0.0,
                                "unit": "g"
                            },
                            {
                                "label": "Polyunsaturated",
                                "tag": "FAPU",
                                "schemaOrgTag": '',
                                "total": 29.673621766515723,
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
                        "total": 279.2287010370659,
                        "hasRDI": True,
                        "daily": 93.07623367902195,
                        "unit": "g",
                        "sub": [
                            {
                                "label": "Carbs (net)",
                                "tag": "CHOCDF.net",
                                "schemaOrgTag": '',
                                "total": 233.99382554932572,
                                "hasRDI": False,
                                "daily": 0.0,
                                "unit": "g"
                            },
                            {
                                "label": "Fiber",
                                "tag": "FIBTG",
                                "schemaOrgTag": "fiberContent",
                                "total": 45.234875487740176,
                                "hasRDI": True,
                                "daily": 180.9395019509607,
                                "unit": "g"
                            },
                            {
                                "label": "Sugars",
                                "tag": "SUGAR",
                                "schemaOrgTag": "sugarContent",
                                "total": 26.181391381150092,
                                "hasRDI": False,
                                "daily": 0.0,
                                "unit": "g"
                            },
                            {
                                "label": "Sugars, added",
                                "tag": "SUGAR.added",
                                "schemaOrgTag": '',
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
                        "total": 96.35770754392712,
                        "hasRDI": True,
                        "daily": 192.71541508785424,
                        "unit": "g"
                    },
                    {
                        "label": "Cholesterol",
                        "tag": "CHOLE",
                        "schemaOrgTag": "cholesterolContent",
                        "total": 285.7631931,
                        "hasRDI": True,
                        "daily": 95.25439770000001,
                        "unit": "mg"
                    },
                    {
                        "label": "Sodium",
                        "tag": "NA",
                        "schemaOrgTag": "sodiumContent",
                        "total": 5932.543228680765,
                        "hasRDI": True,
                        "daily": 247.18930119503187,
                        "unit": "mg"
                    },
                    {
                        "label": "Calcium",
                        "tag": "CA",
                        "schemaOrgTag": '',
                        "total": 516.3136948950191,
                        "hasRDI": True,
                        "daily": 51.631369489501914,
                        "unit": "mg"
                    },
                    {
                        "label": "Magnesium",
                        "tag": "MG",
                        "schemaOrgTag": '',
                        "total": 517.9203518169918,
                        "hasRDI": True,
                        "daily": 123.31436948023615,
                        "unit": "mg"
                    },
                    {
                        "label": "Potassium",
                        "tag": "K",
                        "schemaOrgTag": '',
                        "total": 5526.791993236672,
                        "hasRDI": True,
                        "daily": 117.59131900503557,
                        "unit": "mg"
                    },
                    {
                        "label": "Iron",
                        "tag": "FE",
                        "schemaOrgTag": '',
                        "total": 17.217631278789558,
                        "hasRDI": True,
                        "daily": 95.65350710438643,
                        "unit": "mg"
                    },
                    {
                        "label": "Zinc",
                        "tag": "ZN",
                        "schemaOrgTag": '',
                        "total": 14.67167017122829,
                        "hasRDI": True,
                        "daily": 133.378819738439,
                        "unit": "mg"
                    },
                    {
                        "label": "Phosphorus",
                        "tag": "P",
                        "schemaOrgTag": '',
                        "total": 2091.979287869283,
                        "hasRDI": True,
                        "daily": 298.8541839813261,
                        "unit": "mg"
                    },
                    {
                        "label": "Vitamin A",
                        "tag": "VITA_RAE",
                        "schemaOrgTag": '',
                        "total": 88.83299463984963,
                        "hasRDI": True,
                        "daily": 9.870332737761071,
                        "unit": "µg"
                    },
                    {
                        "label": "Vitamin C",
                        "tag": "VITC",
                        "schemaOrgTag": '',
                        "total": 154.5556968904991,
                        "hasRDI": True,
                        "daily": 171.72855210055454,
                        "unit": "mg"
                    },
                    {
                        "label": "Thiamin (B1)",
                        "tag": "THIA",
                        "schemaOrgTag": '',
                        "total": 1.90443300415948,
                        "hasRDI": True,
                        "daily": 158.70275034662333,
                        "unit": "mg"
                    },
                    {
                        "label": "Riboflavin (B2)",
                        "tag": "RIBF",
                        "schemaOrgTag": '',
                        "total": 2.068709202997483,
                        "hasRDI": True,
                        "daily": 159.13147715365253,
                        "unit": "mg"
                    },
                    {
                        "label": "Niacin (B3)",
                        "tag": "NIA",
                        "schemaOrgTag": '',
                        "total": 40.169285979173885,
                        "hasRDI": True,
                        "daily": 251.0580373698368,
                        "unit": "mg"
                    },
                    {
                        "label": "Vitamin B6",
                        "tag": "VITB6A",
                        "schemaOrgTag": '',
                        "total": 4.311023878483604,
                        "hasRDI": True,
                        "daily": 331.61722142181566,
                        "unit": "mg"
                    },
                    {
                        "label": "Folate equivalent (total)",
                        "tag": "FOLDFE",
                        "schemaOrgTag": '',
                        "total": 241.6644447177267,
                        "hasRDI": True,
                        "daily": 60.416111179431674,
                        "unit": "µg"
                    },
                    {
                        "label": "Folate (food)",
                        "tag": "FOLFD",
                        "schemaOrgTag": '',
                        "total": 241.6644447177267,
                        "hasRDI": False,
                        "daily": 0.0,
                        "unit": "µg"
                    },
                    {
                        "label": "Folic acid",
                        "tag": "FOLAC",
                        "schemaOrgTag": '',
                        "total": 0.0,
                        "hasRDI": False,
                        "daily": 0.0,
                        "unit": "µg"
                    },
                    {
                        "label": "Vitamin B12",
                        "tag": "VITB12",
                        "schemaOrgTag": '',
                        "total": 9.071847400000001,
                        "hasRDI": True,
                        "daily": 377.99364166666675,
                        "unit": "µg"
                    },
                    {
                        "label": "Vitamin D",
                        "tag": "VITD",
                        "schemaOrgTag": '',
                        "total": 6.80388555,
                        "hasRDI": True,
                        "daily": 45.359237,
                        "unit": "µg"
                    },
                    {
                        "label": "Vitamin E",
                        "tag": "TOCPHA",
                        "schemaOrgTag": '',
                        "total": 7.926142614905577,
                        "hasRDI": True,
                        "daily": 52.840950766037174,
                        "unit": "mg"
                    },
                    {
                        "label": "Vitamin K",
                        "tag": "VITK1",
                        "schemaOrgTag": '',
                        "total": 132.52929632137182,
                        "hasRDI": True,
                        "daily": 110.44108026780985,
                        "unit": "µg"
                    },
                    {
                        "label": "Sugar alcohols",
                        "tag": "Sugar.alcohol",
                        "schemaOrgTag": '',
                        "total": 0.0,
                        "hasRDI": False,
                        "daily": 0.0,
                        "unit": "g"
                    },
                    {
                        "label": "Water",
                        "tag": "WATER",
                        "schemaOrgTag": '',
                        "total": 1271.8320325811333,
                        "hasRDI": False,
                        "daily": 0.0,
                        "unit": "g"
                    }
                ]
            },
            "_links": {
                "self": {
                    "title": "Self",
                    "href": "https://api.edamam.com/api/recipes/v2/e96c729fd52df87738cf5d4faf40a792?type=public&app_id=e909afd5&app_key=34e59dda7e1bffb92e49c416e9449e1d"
                }
            }
        },
        {
            "recipe": {
                "uri": "http://www.edamam.com/ontologies/edamam.owl#recipe_d9a81a6c7c04afa4705c9a627d31dba9",
                "label": "Puerco Enchilado Tacos",
                "image": "https://edamam-product-images.s3.amazonaws.com/web-img/d58/d58aaab56240e36ece1f3733f6fe4548.jpeg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLWVhc3QtMSJIMEYCIQCP2Gbt%2ByPQIVKV%2FafgML7WXbkOusL9fCs6d1le6dFKYAIhAJcnuEh%2B1NzOso38QgGaVBwaVQAMxyMJATg%2FR%2Fl0jl96KsEFCJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMMTg3MDE3MTUwOTg2IgydADkJdybnmhdEGwQqlQUNCCJJEzulouVCRRPPDPN9Ik9nmgPZk%2Fam6u04CTug5FWfzto4W1y6mlAuXr3EHPB%2FvTcZ%2BmAkgcS5%2FRfKsviGgYg1PBDbKvJFWJigqXNb6jHaHO3eyZnXpof0Qk2PachTFyGGF7upzvEiKr6BGB6DtCoEGe3wCd0iFSMS%2Ft8LIlICGGYaaCvWq9TXeaXkel5jju8XxawzfW0OY8ad1NODjiJJ%2FJ02goRzRa3HwZdXj0P4%2FwwiBHg8BMnsBu5XvhNCt9Gz%2Bxp9cZIC8TMv%2FY8rOvepaH28zVl5BjLGle3tn5syTeLiH6OS68I4OndB2qqeqZqdi9cu6zb1H0y8aKh8r8IIaHqXhP6jBXwOxUN8uimNrMJnaDPxNdvFPuR5yx8UApiuserTd1b1ZIBFiBJ6lavYUBrkLW%2B7bZIJltsNTSxF2GTKFWoXHKGf3%2FXYj%2FniRUh%2BB3xUXrXh8PzVKChkdfuCxirnj5UG2XCrj22%2BBJG8S8UHiExHaIwt01Nel6V7Y0IlXWvwqK8YEx%2FHOI%2FewXERfrnIQDCsrQyC7qTLL3HndUW2Ke8ib2iC%2BPgaP6xDqkqdlhOSojQHG4rfwcyVOFOzeauzAO7Rc77mb0rCUJdMckP6nKiD7nrtjlZXznFmYhCvjmWQF2l06Jl7xQsr%2BjkGAeoXo9X%2FiC11ZTNfxOVIe3LWWkRvMwGWvgvtgF4ZEDGaLXgsbO4I8%2FpSmGD4ox9ZWDfX%2BtTURCyBYVXqYpQ4TpgMhHqAtTUr4TNc7GRLVbfi1xqZNQDt1Sfdzh3Xq88dOJyKsyUs7rcFuuxoNyxvqstWVaAyRglOH1n%2BpV0xA7%2FKEHa%2F8%2FzH6uaXeIp3eLJN1%2BGlAQc1sP2jehPHqGi5Lc7YMOKk8akGOrABqEMeyIMA72vRUvaZqcs7N77uX3kDw2%2BTfyF8pS8HYdR1%2BEU1ekEPGlPPLyTo0NFmbmMa4urw%2B19eIvlGSnFjiSeee%2F%2BeotdKLVnDgZ5aNxOYivkgUqjazWNTWX1qdv7Jq7GWrNDLwjZiU5zLvpcjSyzLyGAVIo8pW14m4aC3jppuzjKpasygGK2%2Bf%2BmxisMAkIdRRS5aXW9PY%2FuwiBnL3qiZT5RtAdamISZZM9jUAWY%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231028T003610Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFPXEGMX3T%2F20231028%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=265bf645f982a3df149515757480116dcc8ceeb8b178ced9c5081ef7346329af",
                "images": {
                    "THUMBNAIL": {
                        "url": "https://edamam-product-images.s3.amazonaws.com/web-img/d58/d58aaab56240e36ece1f3733f6fe4548-s.jpeg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLWVhc3QtMSJIMEYCIQCP2Gbt%2ByPQIVKV%2FafgML7WXbkOusL9fCs6d1le6dFKYAIhAJcnuEh%2B1NzOso38QgGaVBwaVQAMxyMJATg%2FR%2Fl0jl96KsEFCJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMMTg3MDE3MTUwOTg2IgydADkJdybnmhdEGwQqlQUNCCJJEzulouVCRRPPDPN9Ik9nmgPZk%2Fam6u04CTug5FWfzto4W1y6mlAuXr3EHPB%2FvTcZ%2BmAkgcS5%2FRfKsviGgYg1PBDbKvJFWJigqXNb6jHaHO3eyZnXpof0Qk2PachTFyGGF7upzvEiKr6BGB6DtCoEGe3wCd0iFSMS%2Ft8LIlICGGYaaCvWq9TXeaXkel5jju8XxawzfW0OY8ad1NODjiJJ%2FJ02goRzRa3HwZdXj0P4%2FwwiBHg8BMnsBu5XvhNCt9Gz%2Bxp9cZIC8TMv%2FY8rOvepaH28zVl5BjLGle3tn5syTeLiH6OS68I4OndB2qqeqZqdi9cu6zb1H0y8aKh8r8IIaHqXhP6jBXwOxUN8uimNrMJnaDPxNdvFPuR5yx8UApiuserTd1b1ZIBFiBJ6lavYUBrkLW%2B7bZIJltsNTSxF2GTKFWoXHKGf3%2FXYj%2FniRUh%2BB3xUXrXh8PzVKChkdfuCxirnj5UG2XCrj22%2BBJG8S8UHiExHaIwt01Nel6V7Y0IlXWvwqK8YEx%2FHOI%2FewXERfrnIQDCsrQyC7qTLL3HndUW2Ke8ib2iC%2BPgaP6xDqkqdlhOSojQHG4rfwcyVOFOzeauzAO7Rc77mb0rCUJdMckP6nKiD7nrtjlZXznFmYhCvjmWQF2l06Jl7xQsr%2BjkGAeoXo9X%2FiC11ZTNfxOVIe3LWWkRvMwGWvgvtgF4ZEDGaLXgsbO4I8%2FpSmGD4ox9ZWDfX%2BtTURCyBYVXqYpQ4TpgMhHqAtTUr4TNc7GRLVbfi1xqZNQDt1Sfdzh3Xq88dOJyKsyUs7rcFuuxoNyxvqstWVaAyRglOH1n%2BpV0xA7%2FKEHa%2F8%2FzH6uaXeIp3eLJN1%2BGlAQc1sP2jehPHqGi5Lc7YMOKk8akGOrABqEMeyIMA72vRUvaZqcs7N77uX3kDw2%2BTfyF8pS8HYdR1%2BEU1ekEPGlPPLyTo0NFmbmMa4urw%2B19eIvlGSnFjiSeee%2F%2BeotdKLVnDgZ5aNxOYivkgUqjazWNTWX1qdv7Jq7GWrNDLwjZiU5zLvpcjSyzLyGAVIo8pW14m4aC3jppuzjKpasygGK2%2Bf%2BmxisMAkIdRRS5aXW9PY%2FuwiBnL3qiZT5RtAdamISZZM9jUAWY%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231028T003610Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFPXEGMX3T%2F20231028%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=d0192a830241dfa0eb5670ff4d7e6e3adb9331229ae63ad3463587e799dd61b6",
                        "width": 100,
                        "height": 100
                    },
                    "SMALL": {
                        "url": "https://edamam-product-images.s3.amazonaws.com/web-img/d58/d58aaab56240e36ece1f3733f6fe4548-m.jpeg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLWVhc3QtMSJIMEYCIQCP2Gbt%2ByPQIVKV%2FafgML7WXbkOusL9fCs6d1le6dFKYAIhAJcnuEh%2B1NzOso38QgGaVBwaVQAMxyMJATg%2FR%2Fl0jl96KsEFCJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMMTg3MDE3MTUwOTg2IgydADkJdybnmhdEGwQqlQUNCCJJEzulouVCRRPPDPN9Ik9nmgPZk%2Fam6u04CTug5FWfzto4W1y6mlAuXr3EHPB%2FvTcZ%2BmAkgcS5%2FRfKsviGgYg1PBDbKvJFWJigqXNb6jHaHO3eyZnXpof0Qk2PachTFyGGF7upzvEiKr6BGB6DtCoEGe3wCd0iFSMS%2Ft8LIlICGGYaaCvWq9TXeaXkel5jju8XxawzfW0OY8ad1NODjiJJ%2FJ02goRzRa3HwZdXj0P4%2FwwiBHg8BMnsBu5XvhNCt9Gz%2Bxp9cZIC8TMv%2FY8rOvepaH28zVl5BjLGle3tn5syTeLiH6OS68I4OndB2qqeqZqdi9cu6zb1H0y8aKh8r8IIaHqXhP6jBXwOxUN8uimNrMJnaDPxNdvFPuR5yx8UApiuserTd1b1ZIBFiBJ6lavYUBrkLW%2B7bZIJltsNTSxF2GTKFWoXHKGf3%2FXYj%2FniRUh%2BB3xUXrXh8PzVKChkdfuCxirnj5UG2XCrj22%2BBJG8S8UHiExHaIwt01Nel6V7Y0IlXWvwqK8YEx%2FHOI%2FewXERfrnIQDCsrQyC7qTLL3HndUW2Ke8ib2iC%2BPgaP6xDqkqdlhOSojQHG4rfwcyVOFOzeauzAO7Rc77mb0rCUJdMckP6nKiD7nrtjlZXznFmYhCvjmWQF2l06Jl7xQsr%2BjkGAeoXo9X%2FiC11ZTNfxOVIe3LWWkRvMwGWvgvtgF4ZEDGaLXgsbO4I8%2FpSmGD4ox9ZWDfX%2BtTURCyBYVXqYpQ4TpgMhHqAtTUr4TNc7GRLVbfi1xqZNQDt1Sfdzh3Xq88dOJyKsyUs7rcFuuxoNyxvqstWVaAyRglOH1n%2BpV0xA7%2FKEHa%2F8%2FzH6uaXeIp3eLJN1%2BGlAQc1sP2jehPHqGi5Lc7YMOKk8akGOrABqEMeyIMA72vRUvaZqcs7N77uX3kDw2%2BTfyF8pS8HYdR1%2BEU1ekEPGlPPLyTo0NFmbmMa4urw%2B19eIvlGSnFjiSeee%2F%2BeotdKLVnDgZ5aNxOYivkgUqjazWNTWX1qdv7Jq7GWrNDLwjZiU5zLvpcjSyzLyGAVIo8pW14m4aC3jppuzjKpasygGK2%2Bf%2BmxisMAkIdRRS5aXW9PY%2FuwiBnL3qiZT5RtAdamISZZM9jUAWY%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231028T003610Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFPXEGMX3T%2F20231028%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=fa4370a958b95a54a92f7c1052a3cc11afdfd46a433f0d410c9f03aacfca8088",
                        "width": 200,
                        "height": 200
                    },
                    "REGULAR": {
                        "url": "https://edamam-product-images.s3.amazonaws.com/web-img/d58/d58aaab56240e36ece1f3733f6fe4548.jpeg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLWVhc3QtMSJIMEYCIQCP2Gbt%2ByPQIVKV%2FafgML7WXbkOusL9fCs6d1le6dFKYAIhAJcnuEh%2B1NzOso38QgGaVBwaVQAMxyMJATg%2FR%2Fl0jl96KsEFCJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMMTg3MDE3MTUwOTg2IgydADkJdybnmhdEGwQqlQUNCCJJEzulouVCRRPPDPN9Ik9nmgPZk%2Fam6u04CTug5FWfzto4W1y6mlAuXr3EHPB%2FvTcZ%2BmAkgcS5%2FRfKsviGgYg1PBDbKvJFWJigqXNb6jHaHO3eyZnXpof0Qk2PachTFyGGF7upzvEiKr6BGB6DtCoEGe3wCd0iFSMS%2Ft8LIlICGGYaaCvWq9TXeaXkel5jju8XxawzfW0OY8ad1NODjiJJ%2FJ02goRzRa3HwZdXj0P4%2FwwiBHg8BMnsBu5XvhNCt9Gz%2Bxp9cZIC8TMv%2FY8rOvepaH28zVl5BjLGle3tn5syTeLiH6OS68I4OndB2qqeqZqdi9cu6zb1H0y8aKh8r8IIaHqXhP6jBXwOxUN8uimNrMJnaDPxNdvFPuR5yx8UApiuserTd1b1ZIBFiBJ6lavYUBrkLW%2B7bZIJltsNTSxF2GTKFWoXHKGf3%2FXYj%2FniRUh%2BB3xUXrXh8PzVKChkdfuCxirnj5UG2XCrj22%2BBJG8S8UHiExHaIwt01Nel6V7Y0IlXWvwqK8YEx%2FHOI%2FewXERfrnIQDCsrQyC7qTLL3HndUW2Ke8ib2iC%2BPgaP6xDqkqdlhOSojQHG4rfwcyVOFOzeauzAO7Rc77mb0rCUJdMckP6nKiD7nrtjlZXznFmYhCvjmWQF2l06Jl7xQsr%2BjkGAeoXo9X%2FiC11ZTNfxOVIe3LWWkRvMwGWvgvtgF4ZEDGaLXgsbO4I8%2FpSmGD4ox9ZWDfX%2BtTURCyBYVXqYpQ4TpgMhHqAtTUr4TNc7GRLVbfi1xqZNQDt1Sfdzh3Xq88dOJyKsyUs7rcFuuxoNyxvqstWVaAyRglOH1n%2BpV0xA7%2FKEHa%2F8%2FzH6uaXeIp3eLJN1%2BGlAQc1sP2jehPHqGi5Lc7YMOKk8akGOrABqEMeyIMA72vRUvaZqcs7N77uX3kDw2%2BTfyF8pS8HYdR1%2BEU1ekEPGlPPLyTo0NFmbmMa4urw%2B19eIvlGSnFjiSeee%2F%2BeotdKLVnDgZ5aNxOYivkgUqjazWNTWX1qdv7Jq7GWrNDLwjZiU5zLvpcjSyzLyGAVIo8pW14m4aC3jppuzjKpasygGK2%2Bf%2BmxisMAkIdRRS5aXW9PY%2FuwiBnL3qiZT5RtAdamISZZM9jUAWY%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231028T003610Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFPXEGMX3T%2F20231028%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=265bf645f982a3df149515757480116dcc8ceeb8b178ced9c5081ef7346329af",
                        "width": 300,
                        "height": 300
                    }
                },
                "source": "Food Network",
                "url": "https://www.foodnetwork.com/recipes/marcela-valladolid/puerco-enchilado-tacos-3363775",
                "shareAs": "http://www.edamam.com/recipe/puerco-enchilado-tacos-d9a81a6c7c04afa4705c9a627d31dba9/tacos",
                "yield": 6.0,
                "dietLabels": [],
                "healthLabels": [
                    "Dairy-Free",
                    "Egg-Free",
                    "Peanut-Free",
                    "Tree-Nut-Free",
                    "Soy-Free",
                    "Fish-Free",
                    "Shellfish-Free",
                    "Crustacean-Free",
                    "Celery-Free",
                    "Mustard-Free",
                    "Sesame-Free",
                    "Lupine-Free",
                    "Mollusk-Free",
                    "Alcohol-Free",
                    "Sulfite-Free"
                ],
                "cautions": [
                    "Eggs",
                    "Milk",
                    "Sulfites"
                ],
                "ingredientLines": [
                    "2 tablespoons vegetable oil",
                    "4 cloves garlic",
                    "1 small white onion, roughly chopped",
                    "Salt",
                    "8 dried guajillo chile peppers, seeded",
                    "1 small Roma tomato, quartered",
                    "1 bay leaf",
                    "For the tacos:",
                    "3 tablespoons vegetable oil",
                    "1 russet potato, peeled and cut into 1-inch cubes",
                    "1 1/2 pounds boneless pork butt, cut into 1-inch cubes",
                    "Freshly ground pepper",
                    "1 1/2 cups beef broth",
                    "Corn tortillas, warmed, for serving",
                    "Fresh cilantro and diced white onion and radishes, for topping"
                ],
                "ingredients": [
                    {
                        "text": "2 tablespoons vegetable oil",
                        "quantity": 2.0,
                        "measure": "tablespoon",
                        "food": "vegetable oil",
                        "weight": 28.0,
                        "foodCategory": "Oils",
                        "foodId": "food_bt1mzi2ah2sfg8bv7no1qai83w8s",
                        "image": "https://www.edamam.com/food-img/6e5/6e51a63a6300a8ea1b4c4cc68dfaba33.jpg"
                    },
                    {
                        "text": "4 cloves garlic",
                        "quantity": 4.0,
                        "measure": "clove",
                        "food": "garlic",
                        "weight": 12.0,
                        "foodCategory": "vegetables",
                        "foodId": "food_avtcmx6bgjv1jvay6s6stan8dnyp",
                        "image": "https://www.edamam.com/food-img/6ee/6ee142951f48aaf94f4312409f8d133d.jpg"
                    },
                    {
                        "text": "1 small white onion, roughly chopped",
                        "quantity": 1.0,
                        "measure": "<unit>",
                        "food": "white onion",
                        "weight": 70.0,
                        "foodCategory": "vegetables",
                        "foodId": "food_bmrvi4ob4binw9a5m7l07amlfcoy",
                        "image": "https://www.edamam.com/food-img/205/205e6bf2399b85d34741892ef91cc603.jpg"
                    },
                    {
                        "text": "Salt",
                        "quantity": 0.0,
                        "measure": '',
                        "food": "Salt",
                        "weight": 9.074664663333333,
                        "foodCategory": "Condiments and sauces",
                        "foodId": "food_btxz81db72hwbra2pncvebzzzum9",
                        "image": "https://www.edamam.com/food-img/694/6943ea510918c6025795e8dc6e6eaaeb.jpg"
                    },
                    {
                        "text": "8 dried guajillo chile peppers, seeded",
                        "quantity": 8.0,
                        "measure": "pepper",
                        "food": "dried guajillo chile",
                        "weight": 4.0,
                        "foodCategory": "vegetables",
                        "foodId": "food_blhbqv7bbrfga8aw67rq2b0df6x5",
                        "image": "https://www.edamam.com/food-img/6cb/6cb8e4510251a322178f6e191b3a7b1b.jpeg"
                    },
                    {
                        "text": "1 small Roma tomato, quartered",
                        "quantity": 1.0,
                        "measure": "<unit>",
                        "food": "Roma tomato",
                        "weight": 46.5,
                        "foodCategory": "vegetables",
                        "foodId": "food_ab8jymba5i5xv3apgymg7a90bxb5",
                        "image": "https://www.edamam.com/food-img/23e/23e727a14f1035bdc2733bb0477efbd2.jpg"
                    },
                    {
                        "text": "1 bay leaf",
                        "quantity": 1.0,
                        "measure": "<unit>",
                        "food": "bay leaf",
                        "weight": 0.6,
                        "foodCategory": "Condiments and sauces",
                        "foodId": "food_asx39x4ayja4jab6ivj6zayvkblo",
                        "image": "https://www.edamam.com/food-img/0f9/0f9f5f95df173e9ffaaff2977bef88f3.jpg"
                    },
                    {
                        "text": "3 tablespoons vegetable oil",
                        "quantity": 3.0,
                        "measure": "tablespoon",
                        "food": "vegetable oil",
                        "weight": 42.0,
                        "foodCategory": "Oils",
                        "foodId": "food_bt1mzi2ah2sfg8bv7no1qai83w8s",
                        "image": "https://www.edamam.com/food-img/6e5/6e51a63a6300a8ea1b4c4cc68dfaba33.jpg"
                    },
                    {
                        "text": "1 russet potato, peeled and cut into 1-inch cubes",
                        "quantity": 1.0,
                        "measure": "<unit>",
                        "food": "russet potato",
                        "weight": 244.95555555555552,
                        "foodCategory": "vegetables",
                        "foodId": "food_brsjy86bq09pzgbmr4ri8bnohrf7",
                        "image": "https://www.edamam.com/food-img/71b/71b3756ecfd3d1efa075874377038b67.jpg"
                    },
                    {
                        "text": "1 1/2 pounds boneless pork butt, cut into 1-inch cubes",
                        "quantity": 1.5,
                        "measure": "pound",
                        "food": "pork butt",
                        "weight": 680.388555,
                        "foodCategory": "meats",
                        "foodId": "food_acjul5rb7atkmmb6qcu4ta4mksoi",
                        "image": "https://www.edamam.com/food-img/f38/f38e947daeeae074141b73e0c9d1cc93.jpg"
                    },
                    {
                        "text": "Freshly ground pepper",
                        "quantity": 0.0,
                        "measure": '',
                        "food": "pepper",
                        "weight": 4.537332331666667,
                        "foodCategory": "Condiments and sauces",
                        "foodId": "food_b6ywzluaaxv02wad7s1r9ag4py89",
                        "image": "https://www.edamam.com/food-img/c6e/c6e5c3bd8d3bc15175d9766971a4d1b2.jpg"
                    },
                    {
                        "text": "1 1/2 cups beef broth",
                        "quantity": 1.5,
                        "measure": "cup",
                        "food": "beef broth",
                        "weight": 360.0,
                        "foodCategory": "canned soup",
                        "foodId": "food_bxd832fblxgfaibgn0zk0b6dg6dh",
                        "image": "https://www.edamam.com/food-img/428/4284513ddbf46e51f0f33566c0d61715.jpg"
                    },
                    {
                        "text": "Corn tortillas, warmed, for serving",
                        "quantity": 1.0,
                        "measure": "serving",
                        "food": "Corn tortillas",
                        "weight": 24.0,
                        "foodCategory": "quick breads and pastries",
                        "foodId": "food_bhw0b95agm97s0abfignnb8fsvb3",
                        "image": "https://www.edamam.com/food-img/b8a/b8ad23dcc06f2324f944e47eb579d644.jpg"
                    },
                    {
                        "text": "Fresh cilantro and diced white onion and radishes, for topping",
                        "quantity": 0.0,
                        "measure": '',
                        "food": "cilantro",
                        "weight": 15.124441105555556,
                        "foodCategory": "vegetables",
                        "foodId": "food_alhzhuwb4lc7jnb5s6f02by60bzp",
                        "image": "https://www.edamam.com/food-img/d57/d57e375b6ff99a90c7ee2b1990a1af36.jpg"
                    },
                    {
                        "text": "Fresh cilantro and diced white onion and radishes, for topping",
                        "quantity": 0.0,
                        "measure": '',
                        "food": "white onion",
                        "weight": 0.0,
                        "foodCategory": "vegetables",
                        "foodId": "food_bmrvi4ob4binw9a5m7l07amlfcoy",
                        "image": "https://www.edamam.com/food-img/205/205e6bf2399b85d34741892ef91cc603.jpg"
                    },
                    {
                        "text": "Fresh cilantro and diced white onion and radishes, for topping",
                        "quantity": 0.0,
                        "measure": '',
                        "food": "radishes",
                        "weight": 0.0,
                        "foodCategory": "vegetables",
                        "foodId": "food_bs6xkukbtd85e7b2lh5zfazpe45y",
                        "image": "https://www.edamam.com/food-img/ad7/ad78f4315cdba1dc26ccef0d7dba464b.jpg"
                    }
                ],
                "calories": 2260.91292679565,
                "totalCO2Emissions": 44820.1555364165,
                "co2EmissionsClass": "G",
                "totalWeight": 1538.2738970994913,
                "totalTime": 120.0,
                "cuisineType": [
                    "mexican"
                ],
                "mealType": [
                    "lunch/dinner"
                ],
                "dishType": [
                    "sandwiches"
                ],
                "totalNutrients": {
                    "ENERC_KCAL": {
                        "label": "Energy",
                        "quantity": 2260.91292679565,
                        "unit": "kcal"
                    },
                    "FAT": {
                        "label": "Fat",
                        "quantity": 156.30426939220567,
                        "unit": "g"
                    },
                    "FASAT": {
                        "label": "Saturated",
                        "quantity": 34.61679692810938,
                        "unit": "g"
                    },
                    "FATRN": {
                        "label": "Trans",
                        "quantity": 1.31934683825,
                        "unit": "g"
                    },
                    "FAMS": {
                        "label": "Monounsaturated",
                        "quantity": 86.30254092558238,
                        "unit": "g"
                    },
                    "FAPU": {
                        "label": "Polyunsaturated",
                        "quantity": 23.588995122001148,
                        "unit": "g"
                    },
                    "CHOCDF": {
                        "label": "Carbs",
                        "quantity": 78.3847652363961,
                        "unit": "g"
                    },
                    "CHOCDF.net": {
                        "label": "Carbohydrates (net)",
                        "quantity": 68.81111358330666,
                        "unit": "g"
                    },
                    "FIBTG": {
                        "label": "Fiber",
                        "quantity": 9.573651653089444,
                        "unit": "g"
                    },
                    "SUGAR": {
                        "label": "Sugars",
                        "quantity": 9.789496008985445,
                        "unit": "g"
                    },
                    "PROCNT": {
                        "label": "Protein",
                        "quantity": 135.29575061693055,
                        "unit": "g"
                    },
                    "CHOLE": {
                        "label": "Cholesterol",
                        "quantity": 421.8409041,
                        "unit": "mg"
                    },
                    "NA": {
                        "label": "Sodium",
                        "quantity": 3562.8815911075253,
                        "unit": "mg"
                    },
                    "CA": {
                        "label": "Calcium",
                        "quantity": 269.934471937839,
                        "unit": "mg"
                    },
                    "MG": {
                        "label": "Magnesium",
                        "quantity": 266.0053618834394,
                        "unit": "mg"
                    },
                    "K": {
                        "label": "Potassium",
                        "quantity": 4373.877570786315,
                        "unit": "mg"
                    },
                    "FE": {
                        "label": "Iron",
                        "quantity": 12.6989516140031,
                        "unit": "mg"
                    },
                    "ZN": {
                        "label": "Zinc",
                        "quantity": 23.196811933992436,
                        "unit": "mg"
                    },
                    "P": {
                        "label": "Phosphorus",
                        "quantity": 1685.7105268702553,
                        "unit": "mg"
                    },
                    "VITA_RAE": {
                        "label": "Vitamin A",
                        "quantity": 139.98621735527223,
                        "unit": "µg"
                    },
                    "VITC": {
                        "label": "Vitamin C",
                        "quantity": 34.87556576516666,
                        "unit": "mg"
                    },
                    "THIA": {
                        "label": "Thiamin (B1)",
                        "quantity": 3.9719767360144775,
                        "unit": "mg"
                    },
                    "RIBF": {
                        "label": "Riboflavin (B2)",
                        "quantity": 2.949936725271333,
                        "unit": "mg"
                    },
                    "NIA": {
                        "label": "Niacin (B3)",
                        "quantity": 35.91502939463045,
                        "unit": "mg"
                    },
                    "VITB6A": {
                        "label": "Vitamin B6",
                        "quantity": 4.750924098299095,
                        "unit": "mg"
                    },
                    "FOLDFE": {
                        "label": "Folate equivalent (total)",
                        "quantity": 76.59727775960555,
                        "unit": "µg"
                    },
                    "FOLFD": {
                        "label": "Folate (food)",
                        "quantity": 76.59727775960555,
                        "unit": "µg"
                    },
                    "FOLAC": {
                        "label": "Folic acid",
                        "quantity": 0.0,
                        "unit": "µg"
                    },
                    "VITB12": {
                        "label": "Vitamin B12",
                        "quantity": 6.1915358505,
                        "unit": "µg"
                    },
                    "VITD": {
                        "label": "Vitamin D",
                        "quantity": 4.762719885,
                        "unit": "µg"
                    },
                    "TOCPHA": {
                        "label": "Vitamin E",
                        "quantity": 17.710149660443783,
                        "unit": "mg"
                    },
                    "VITK1": {
                        "label": "Vitamin K",
                        "quantity": 67.57369245115555,
                        "unit": "µg"
                    },
                    "WATER": {
                        "label": "Water",
                        "quantity": 1147.8073239936607,
                        "unit": "g"
                    }
                },
                "totalDaily": {
                    "ENERC_KCAL": {
                        "label": "Energy",
                        "quantity": 113.0456463397825,
                        "unit": "%"
                    },
                    "FAT": {
                        "label": "Fat",
                        "quantity": 240.46810675723947,
                        "unit": "%"
                    },
                    "FASAT": {
                        "label": "Saturated",
                        "quantity": 173.0839846405469,
                        "unit": "%"
                    },
                    "CHOCDF": {
                        "label": "Carbs",
                        "quantity": 26.128255078798702,
                        "unit": "%"
                    },
                    "FIBTG": {
                        "label": "Fiber",
                        "quantity": 38.294606612357775,
                        "unit": "%"
                    },
                    "PROCNT": {
                        "label": "Protein",
                        "quantity": 270.5915012338611,
                        "unit": "%"
                    },
                    "CHOLE": {
                        "label": "Cholesterol",
                        "quantity": 140.61363469999998,
                        "unit": "%"
                    },
                    "NA": {
                        "label": "Sodium",
                        "quantity": 148.4533996294802,
                        "unit": "%"
                    },
                    "CA": {
                        "label": "Calcium",
                        "quantity": 26.9934471937839,
                        "unit": "%"
                    },
                    "MG": {
                        "label": "Magnesium",
                        "quantity": 63.33460997224747,
                        "unit": "%"
                    },
                    "K": {
                        "label": "Potassium",
                        "quantity": 93.06122491034712,
                        "unit": "%"
                    },
                    "FE": {
                        "label": "Iron",
                        "quantity": 70.54973118890611,
                        "unit": "%"
                    },
                    "ZN": {
                        "label": "Zinc",
                        "quantity": 210.8801084908403,
                        "unit": "%"
                    },
                    "P": {
                        "label": "Phosphorus",
                        "quantity": 240.81578955289362,
                        "unit": "%"
                    },
                    "VITA_RAE": {
                        "label": "Vitamin A",
                        "quantity": 15.554024150585803,
                        "unit": "%"
                    },
                    "VITC": {
                        "label": "Vitamin C",
                        "quantity": 38.75062862796296,
                        "unit": "%"
                    },
                    "THIA": {
                        "label": "Thiamin (B1)",
                        "quantity": 330.99806133453984,
                        "unit": "%"
                    },
                    "RIBF": {
                        "label": "Riboflavin (B2)",
                        "quantity": 226.91820963625636,
                        "unit": "%"
                    },
                    "NIA": {
                        "label": "Niacin (B3)",
                        "quantity": 224.46893371644032,
                        "unit": "%"
                    },
                    "VITB6A": {
                        "label": "Vitamin B6",
                        "quantity": 365.4556998691611,
                        "unit": "%"
                    },
                    "FOLDFE": {
                        "label": "Folate equivalent (total)",
                        "quantity": 19.149319439901387,
                        "unit": "%"
                    },
                    "VITB12": {
                        "label": "Vitamin B12",
                        "quantity": 257.98066043750003,
                        "unit": "%"
                    },
                    "VITD": {
                        "label": "Vitamin D",
                        "quantity": 31.751465900000003,
                        "unit": "%"
                    },
                    "TOCPHA": {
                        "label": "Vitamin E",
                        "quantity": 118.06766440295856,
                        "unit": "%"
                    },
                    "VITK1": {
                        "label": "Vitamin K",
                        "quantity": 56.31141037596296,
                        "unit": "%"
                    }
                },
                "digest": [
                    {
                        "label": "Fat",
                        "tag": "FAT",
                        "schemaOrgTag": "fatContent",
                        "total": 156.30426939220567,
                        "hasRDI": True,
                        "daily": 240.46810675723947,
                        "unit": "g",
                        "sub": [
                            {
                                "label": "Saturated",
                                "tag": "FASAT",
                                "schemaOrgTag": "saturatedFatContent",
                                "total": 34.61679692810938,
                                "hasRDI": True,
                                "daily": 173.0839846405469,
                                "unit": "g"
                            },
                            {
                                "label": "Trans",
                                "tag": "FATRN",
                                "schemaOrgTag": "transFatContent",
                                "total": 1.31934683825,
                                "hasRDI": False,
                                "daily": 0.0,
                                "unit": "g"
                            },
                            {
                                "label": "Monounsaturated",
                                "tag": "FAMS",
                                "schemaOrgTag": '',
                                "total": 86.30254092558238,
                                "hasRDI": False,
                                "daily": 0.0,
                                "unit": "g"
                            },
                            {
                                "label": "Polyunsaturated",
                                "tag": "FAPU",
                                "schemaOrgTag": '',
                                "total": 23.588995122001148,
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
                        "total": 78.3847652363961,
                        "hasRDI": True,
                        "daily": 26.128255078798702,
                        "unit": "g",
                        "sub": [
                            {
                                "label": "Carbs (net)",
                                "tag": "CHOCDF.net",
                                "schemaOrgTag": '',
                                "total": 68.81111358330666,
                                "hasRDI": False,
                                "daily": 0.0,
                                "unit": "g"
                            },
                            {
                                "label": "Fiber",
                                "tag": "FIBTG",
                                "schemaOrgTag": "fiberContent",
                                "total": 9.573651653089444,
                                "hasRDI": True,
                                "daily": 38.294606612357775,
                                "unit": "g"
                            },
                            {
                                "label": "Sugars",
                                "tag": "SUGAR",
                                "schemaOrgTag": "sugarContent",
                                "total": 9.789496008985445,
                                "hasRDI": False,
                                "daily": 0.0,
                                "unit": "g"
                            },
                            {
                                "label": "Sugars, added",
                                "tag": "SUGAR.added",
                                "schemaOrgTag": '',
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
                        "total": 135.29575061693055,
                        "hasRDI": True,
                        "daily": 270.5915012338611,
                        "unit": "g"
                    },
                    {
                        "label": "Cholesterol",
                        "tag": "CHOLE",
                        "schemaOrgTag": "cholesterolContent",
                        "total": 421.8409041,
                        "hasRDI": True,
                        "daily": 140.61363469999998,
                        "unit": "mg"
                    },
                    {
                        "label": "Sodium",
                        "tag": "NA",
                        "schemaOrgTag": "sodiumContent",
                        "total": 3562.8815911075253,
                        "hasRDI": True,
                        "daily": 148.4533996294802,
                        "unit": "mg"
                    },
                    {
                        "label": "Calcium",
                        "tag": "CA",
                        "schemaOrgTag": '',
                        "total": 269.934471937839,
                        "hasRDI": True,
                        "daily": 26.9934471937839,
                        "unit": "mg"
                    },
                    {
                        "label": "Magnesium",
                        "tag": "MG",
                        "schemaOrgTag": '',
                        "total": 266.0053618834394,
                        "hasRDI": True,
                        "daily": 63.33460997224747,
                        "unit": "mg"
                    },
                    {
                        "label": "Potassium",
                        "tag": "K",
                        "schemaOrgTag": '',
                        "total": 4373.877570786315,
                        "hasRDI": True,
                        "daily": 93.06122491034712,
                        "unit": "mg"
                    },
                    {
                        "label": "Iron",
                        "tag": "FE",
                        "schemaOrgTag": '',
                        "total": 12.6989516140031,
                        "hasRDI": True,
                        "daily": 70.54973118890611,
                        "unit": "mg"
                    },
                    {
                        "label": "Zinc",
                        "tag": "ZN",
                        "schemaOrgTag": '',
                        "total": 23.196811933992436,
                        "hasRDI": True,
                        "daily": 210.8801084908403,
                        "unit": "mg"
                    },
                    {
                        "label": "Phosphorus",
                        "tag": "P",
                        "schemaOrgTag": '',
                        "total": 1685.7105268702553,
                        "hasRDI": True,
                        "daily": 240.81578955289362,
                        "unit": "mg"
                    },
                    {
                        "label": "Vitamin A",
                        "tag": "VITA_RAE",
                        "schemaOrgTag": '',
                        "total": 139.98621735527223,
                        "hasRDI": True,
                        "daily": 15.554024150585803,
                        "unit": "µg"
                    },
                    {
                        "label": "Vitamin C",
                        "tag": "VITC",
                        "schemaOrgTag": '',
                        "total": 34.87556576516666,
                        "hasRDI": True,
                        "daily": 38.75062862796296,
                        "unit": "mg"
                    },
                    {
                        "label": "Thiamin (B1)",
                        "tag": "THIA",
                        "schemaOrgTag": '',
                        "total": 3.9719767360144775,
                        "hasRDI": True,
                        "daily": 330.99806133453984,
                        "unit": "mg"
                    },
                    {
                        "label": "Riboflavin (B2)",
                        "tag": "RIBF",
                        "schemaOrgTag": '',
                        "total": 2.949936725271333,
                        "hasRDI": True,
                        "daily": 226.91820963625636,
                        "unit": "mg"
                    },
                    {
                        "label": "Niacin (B3)",
                        "tag": "NIA",
                        "schemaOrgTag": '',
                        "total": 35.91502939463045,
                        "hasRDI": True,
                        "daily": 224.46893371644032,
                        "unit": "mg"
                    },
                    {
                        "label": "Vitamin B6",
                        "tag": "VITB6A",
                        "schemaOrgTag": '',
                        "total": 4.750924098299095,
                        "hasRDI": True,
                        "daily": 365.4556998691611,
                        "unit": "mg"
                    },
                    {
                        "label": "Folate equivalent (total)",
                        "tag": "FOLDFE",
                        "schemaOrgTag": '',
                        "total": 76.59727775960555,
                        "hasRDI": True,
                        "daily": 19.149319439901387,
                        "unit": "µg"
                    },
                    {
                        "label": "Folate (food)",
                        "tag": "FOLFD",
                        "schemaOrgTag": '',
                        "total": 76.59727775960555,
                        "hasRDI": False,
                        "daily": 0.0,
                        "unit": "µg"
                    },
                    {
                        "label": "Folic acid",
                        "tag": "FOLAC",
                        "schemaOrgTag": '',
                        "total": 0.0,
                        "hasRDI": False,
                        "daily": 0.0,
                        "unit": "µg"
                    },
                    {
                        "label": "Vitamin B12",
                        "tag": "VITB12",
                        "schemaOrgTag": '',
                        "total": 6.1915358505,
                        "hasRDI": True,
                        "daily": 257.98066043750003,
                        "unit": "µg"
                    },
                    {
                        "label": "Vitamin D",
                        "tag": "VITD",
                        "schemaOrgTag": '',
                        "total": 4.762719885,
                        "hasRDI": True,
                        "daily": 31.751465900000003,
                        "unit": "µg"
                    },
                    {
                        "label": "Vitamin E",
                        "tag": "TOCPHA",
                        "schemaOrgTag": '',
                        "total": 17.710149660443783,
                        "hasRDI": True,
                        "daily": 118.06766440295856,
                        "unit": "mg"
                    },
                    {
                        "label": "Vitamin K",
                        "tag": "VITK1",
                        "schemaOrgTag": '',
                        "total": 67.57369245115555,
                        "hasRDI": True,
                        "daily": 56.31141037596296,
                        "unit": "µg"
                    },
                    {
                        "label": "Sugar alcohols",
                        "tag": "Sugar.alcohol",
                        "schemaOrgTag": '',
                        "total": 0.0,
                        "hasRDI": False,
                        "daily": 0.0,
                        "unit": "g"
                    },
                    {
                        "label": "Water",
                        "tag": "WATER",
                        "schemaOrgTag": '',
                        "total": 1147.8073239936607,
                        "hasRDI": False,
                        "daily": 0.0,
                        "unit": "g"
                    }
                ]
            },
            "_links": {
                "self": {
                    "title": "Self",
                    "href": "https://api.edamam.com/api/recipes/v2/d9a81a6c7c04afa4705c9a627d31dba9?type=public&app_id=e909afd5&app_key=34e59dda7e1bffb92e49c416e9449e1d"
                }
            }
        },
        {
            "recipe": {
                "uri": "http://www.edamam.com/ontologies/edamam.owl#recipe_6b11398feaa404a407ae7de9f2a08905",
                "label": "Soft and Crunchy Tacos",
                "image": "https://edamam-product-images.s3.amazonaws.com/web-img/624/624b1e8f654fcc8f39eb2b5c1d4f196c.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLWVhc3QtMSJIMEYCIQCP2Gbt%2ByPQIVKV%2FafgML7WXbkOusL9fCs6d1le6dFKYAIhAJcnuEh%2B1NzOso38QgGaVBwaVQAMxyMJATg%2FR%2Fl0jl96KsEFCJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMMTg3MDE3MTUwOTg2IgydADkJdybnmhdEGwQqlQUNCCJJEzulouVCRRPPDPN9Ik9nmgPZk%2Fam6u04CTug5FWfzto4W1y6mlAuXr3EHPB%2FvTcZ%2BmAkgcS5%2FRfKsviGgYg1PBDbKvJFWJigqXNb6jHaHO3eyZnXpof0Qk2PachTFyGGF7upzvEiKr6BGB6DtCoEGe3wCd0iFSMS%2Ft8LIlICGGYaaCvWq9TXeaXkel5jju8XxawzfW0OY8ad1NODjiJJ%2FJ02goRzRa3HwZdXj0P4%2FwwiBHg8BMnsBu5XvhNCt9Gz%2Bxp9cZIC8TMv%2FY8rOvepaH28zVl5BjLGle3tn5syTeLiH6OS68I4OndB2qqeqZqdi9cu6zb1H0y8aKh8r8IIaHqXhP6jBXwOxUN8uimNrMJnaDPxNdvFPuR5yx8UApiuserTd1b1ZIBFiBJ6lavYUBrkLW%2B7bZIJltsNTSxF2GTKFWoXHKGf3%2FXYj%2FniRUh%2BB3xUXrXh8PzVKChkdfuCxirnj5UG2XCrj22%2BBJG8S8UHiExHaIwt01Nel6V7Y0IlXWvwqK8YEx%2FHOI%2FewXERfrnIQDCsrQyC7qTLL3HndUW2Ke8ib2iC%2BPgaP6xDqkqdlhOSojQHG4rfwcyVOFOzeauzAO7Rc77mb0rCUJdMckP6nKiD7nrtjlZXznFmYhCvjmWQF2l06Jl7xQsr%2BjkGAeoXo9X%2FiC11ZTNfxOVIe3LWWkRvMwGWvgvtgF4ZEDGaLXgsbO4I8%2FpSmGD4ox9ZWDfX%2BtTURCyBYVXqYpQ4TpgMhHqAtTUr4TNc7GRLVbfi1xqZNQDt1Sfdzh3Xq88dOJyKsyUs7rcFuuxoNyxvqstWVaAyRglOH1n%2BpV0xA7%2FKEHa%2F8%2FzH6uaXeIp3eLJN1%2BGlAQc1sP2jehPHqGi5Lc7YMOKk8akGOrABqEMeyIMA72vRUvaZqcs7N77uX3kDw2%2BTfyF8pS8HYdR1%2BEU1ekEPGlPPLyTo0NFmbmMa4urw%2B19eIvlGSnFjiSeee%2F%2BeotdKLVnDgZ5aNxOYivkgUqjazWNTWX1qdv7Jq7GWrNDLwjZiU5zLvpcjSyzLyGAVIo8pW14m4aC3jppuzjKpasygGK2%2Bf%2BmxisMAkIdRRS5aXW9PY%2FuwiBnL3qiZT5RtAdamISZZM9jUAWY%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231028T003610Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFPXEGMX3T%2F20231028%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=29d89bd895f188005a603f51e54db456801593d3112a2e09ae8f5c83409ca5e7",
                "images": {
                    "THUMBNAIL": {
                        "url": "https://edamam-product-images.s3.amazonaws.com/web-img/624/624b1e8f654fcc8f39eb2b5c1d4f196c-s.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLWVhc3QtMSJIMEYCIQCP2Gbt%2ByPQIVKV%2FafgML7WXbkOusL9fCs6d1le6dFKYAIhAJcnuEh%2B1NzOso38QgGaVBwaVQAMxyMJATg%2FR%2Fl0jl96KsEFCJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMMTg3MDE3MTUwOTg2IgydADkJdybnmhdEGwQqlQUNCCJJEzulouVCRRPPDPN9Ik9nmgPZk%2Fam6u04CTug5FWfzto4W1y6mlAuXr3EHPB%2FvTcZ%2BmAkgcS5%2FRfKsviGgYg1PBDbKvJFWJigqXNb6jHaHO3eyZnXpof0Qk2PachTFyGGF7upzvEiKr6BGB6DtCoEGe3wCd0iFSMS%2Ft8LIlICGGYaaCvWq9TXeaXkel5jju8XxawzfW0OY8ad1NODjiJJ%2FJ02goRzRa3HwZdXj0P4%2FwwiBHg8BMnsBu5XvhNCt9Gz%2Bxp9cZIC8TMv%2FY8rOvepaH28zVl5BjLGle3tn5syTeLiH6OS68I4OndB2qqeqZqdi9cu6zb1H0y8aKh8r8IIaHqXhP6jBXwOxUN8uimNrMJnaDPxNdvFPuR5yx8UApiuserTd1b1ZIBFiBJ6lavYUBrkLW%2B7bZIJltsNTSxF2GTKFWoXHKGf3%2FXYj%2FniRUh%2BB3xUXrXh8PzVKChkdfuCxirnj5UG2XCrj22%2BBJG8S8UHiExHaIwt01Nel6V7Y0IlXWvwqK8YEx%2FHOI%2FewXERfrnIQDCsrQyC7qTLL3HndUW2Ke8ib2iC%2BPgaP6xDqkqdlhOSojQHG4rfwcyVOFOzeauzAO7Rc77mb0rCUJdMckP6nKiD7nrtjlZXznFmYhCvjmWQF2l06Jl7xQsr%2BjkGAeoXo9X%2FiC11ZTNfxOVIe3LWWkRvMwGWvgvtgF4ZEDGaLXgsbO4I8%2FpSmGD4ox9ZWDfX%2BtTURCyBYVXqYpQ4TpgMhHqAtTUr4TNc7GRLVbfi1xqZNQDt1Sfdzh3Xq88dOJyKsyUs7rcFuuxoNyxvqstWVaAyRglOH1n%2BpV0xA7%2FKEHa%2F8%2FzH6uaXeIp3eLJN1%2BGlAQc1sP2jehPHqGi5Lc7YMOKk8akGOrABqEMeyIMA72vRUvaZqcs7N77uX3kDw2%2BTfyF8pS8HYdR1%2BEU1ekEPGlPPLyTo0NFmbmMa4urw%2B19eIvlGSnFjiSeee%2F%2BeotdKLVnDgZ5aNxOYivkgUqjazWNTWX1qdv7Jq7GWrNDLwjZiU5zLvpcjSyzLyGAVIo8pW14m4aC3jppuzjKpasygGK2%2Bf%2BmxisMAkIdRRS5aXW9PY%2FuwiBnL3qiZT5RtAdamISZZM9jUAWY%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231028T003610Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFPXEGMX3T%2F20231028%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=727ffd07b822b1c433844757930c7f8fc43039d1d5605ee0fd0a94437d1a37d8",
                        "width": 100,
                        "height": 100
                    },
                    "SMALL": {
                        "url": "https://edamam-product-images.s3.amazonaws.com/web-img/624/624b1e8f654fcc8f39eb2b5c1d4f196c-m.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLWVhc3QtMSJIMEYCIQCP2Gbt%2ByPQIVKV%2FafgML7WXbkOusL9fCs6d1le6dFKYAIhAJcnuEh%2B1NzOso38QgGaVBwaVQAMxyMJATg%2FR%2Fl0jl96KsEFCJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMMTg3MDE3MTUwOTg2IgydADkJdybnmhdEGwQqlQUNCCJJEzulouVCRRPPDPN9Ik9nmgPZk%2Fam6u04CTug5FWfzto4W1y6mlAuXr3EHPB%2FvTcZ%2BmAkgcS5%2FRfKsviGgYg1PBDbKvJFWJigqXNb6jHaHO3eyZnXpof0Qk2PachTFyGGF7upzvEiKr6BGB6DtCoEGe3wCd0iFSMS%2Ft8LIlICGGYaaCvWq9TXeaXkel5jju8XxawzfW0OY8ad1NODjiJJ%2FJ02goRzRa3HwZdXj0P4%2FwwiBHg8BMnsBu5XvhNCt9Gz%2Bxp9cZIC8TMv%2FY8rOvepaH28zVl5BjLGle3tn5syTeLiH6OS68I4OndB2qqeqZqdi9cu6zb1H0y8aKh8r8IIaHqXhP6jBXwOxUN8uimNrMJnaDPxNdvFPuR5yx8UApiuserTd1b1ZIBFiBJ6lavYUBrkLW%2B7bZIJltsNTSxF2GTKFWoXHKGf3%2FXYj%2FniRUh%2BB3xUXrXh8PzVKChkdfuCxirnj5UG2XCrj22%2BBJG8S8UHiExHaIwt01Nel6V7Y0IlXWvwqK8YEx%2FHOI%2FewXERfrnIQDCsrQyC7qTLL3HndUW2Ke8ib2iC%2BPgaP6xDqkqdlhOSojQHG4rfwcyVOFOzeauzAO7Rc77mb0rCUJdMckP6nKiD7nrtjlZXznFmYhCvjmWQF2l06Jl7xQsr%2BjkGAeoXo9X%2FiC11ZTNfxOVIe3LWWkRvMwGWvgvtgF4ZEDGaLXgsbO4I8%2FpSmGD4ox9ZWDfX%2BtTURCyBYVXqYpQ4TpgMhHqAtTUr4TNc7GRLVbfi1xqZNQDt1Sfdzh3Xq88dOJyKsyUs7rcFuuxoNyxvqstWVaAyRglOH1n%2BpV0xA7%2FKEHa%2F8%2FzH6uaXeIp3eLJN1%2BGlAQc1sP2jehPHqGi5Lc7YMOKk8akGOrABqEMeyIMA72vRUvaZqcs7N77uX3kDw2%2BTfyF8pS8HYdR1%2BEU1ekEPGlPPLyTo0NFmbmMa4urw%2B19eIvlGSnFjiSeee%2F%2BeotdKLVnDgZ5aNxOYivkgUqjazWNTWX1qdv7Jq7GWrNDLwjZiU5zLvpcjSyzLyGAVIo8pW14m4aC3jppuzjKpasygGK2%2Bf%2BmxisMAkIdRRS5aXW9PY%2FuwiBnL3qiZT5RtAdamISZZM9jUAWY%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231028T003610Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFPXEGMX3T%2F20231028%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=d08b4f2b2d3be4e079db1114f41039f5e209e6012738f07c729ee64bf5c64ec3",
                        "width": 200,
                        "height": 200
                    },
                    "REGULAR": {
                        "url": "https://edamam-product-images.s3.amazonaws.com/web-img/624/624b1e8f654fcc8f39eb2b5c1d4f196c.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLWVhc3QtMSJIMEYCIQCP2Gbt%2ByPQIVKV%2FafgML7WXbkOusL9fCs6d1le6dFKYAIhAJcnuEh%2B1NzOso38QgGaVBwaVQAMxyMJATg%2FR%2Fl0jl96KsEFCJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMMTg3MDE3MTUwOTg2IgydADkJdybnmhdEGwQqlQUNCCJJEzulouVCRRPPDPN9Ik9nmgPZk%2Fam6u04CTug5FWfzto4W1y6mlAuXr3EHPB%2FvTcZ%2BmAkgcS5%2FRfKsviGgYg1PBDbKvJFWJigqXNb6jHaHO3eyZnXpof0Qk2PachTFyGGF7upzvEiKr6BGB6DtCoEGe3wCd0iFSMS%2Ft8LIlICGGYaaCvWq9TXeaXkel5jju8XxawzfW0OY8ad1NODjiJJ%2FJ02goRzRa3HwZdXj0P4%2FwwiBHg8BMnsBu5XvhNCt9Gz%2Bxp9cZIC8TMv%2FY8rOvepaH28zVl5BjLGle3tn5syTeLiH6OS68I4OndB2qqeqZqdi9cu6zb1H0y8aKh8r8IIaHqXhP6jBXwOxUN8uimNrMJnaDPxNdvFPuR5yx8UApiuserTd1b1ZIBFiBJ6lavYUBrkLW%2B7bZIJltsNTSxF2GTKFWoXHKGf3%2FXYj%2FniRUh%2BB3xUXrXh8PzVKChkdfuCxirnj5UG2XCrj22%2BBJG8S8UHiExHaIwt01Nel6V7Y0IlXWvwqK8YEx%2FHOI%2FewXERfrnIQDCsrQyC7qTLL3HndUW2Ke8ib2iC%2BPgaP6xDqkqdlhOSojQHG4rfwcyVOFOzeauzAO7Rc77mb0rCUJdMckP6nKiD7nrtjlZXznFmYhCvjmWQF2l06Jl7xQsr%2BjkGAeoXo9X%2FiC11ZTNfxOVIe3LWWkRvMwGWvgvtgF4ZEDGaLXgsbO4I8%2FpSmGD4ox9ZWDfX%2BtTURCyBYVXqYpQ4TpgMhHqAtTUr4TNc7GRLVbfi1xqZNQDt1Sfdzh3Xq88dOJyKsyUs7rcFuuxoNyxvqstWVaAyRglOH1n%2BpV0xA7%2FKEHa%2F8%2FzH6uaXeIp3eLJN1%2BGlAQc1sP2jehPHqGi5Lc7YMOKk8akGOrABqEMeyIMA72vRUvaZqcs7N77uX3kDw2%2BTfyF8pS8HYdR1%2BEU1ekEPGlPPLyTo0NFmbmMa4urw%2B19eIvlGSnFjiSeee%2F%2BeotdKLVnDgZ5aNxOYivkgUqjazWNTWX1qdv7Jq7GWrNDLwjZiU5zLvpcjSyzLyGAVIo8pW14m4aC3jppuzjKpasygGK2%2Bf%2BmxisMAkIdRRS5aXW9PY%2FuwiBnL3qiZT5RtAdamISZZM9jUAWY%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231028T003610Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFPXEGMX3T%2F20231028%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=29d89bd895f188005a603f51e54db456801593d3112a2e09ae8f5c83409ca5e7",
                        "width": 300,
                        "height": 300
                    }
                },
                "source": "Delish",
                "url": "http://www.delish.com/cooking/recipe-ideas/recipes/a32784/soft-crunchy-tacos-120913/",
                "shareAs": "http://www.edamam.com/recipe/soft-and-crunchy-tacos-6b11398feaa404a407ae7de9f2a08905/tacos",
                "yield": 4.0,
                "dietLabels": [
                    "High-Fiber"
                ],
                "healthLabels": [
                    "Egg-Free",
                    "Peanut-Free",
                    "Tree-Nut-Free",
                    "Soy-Free",
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
                    "Sulfite-Free"
                ],
                "cautions": [
                    "Eggs",
                    "Milk",
                    "Sulfites"
                ],
                "ingredientLines": [
                    "8 taco shells",
                    "8 soft-taco or fajita-size flour tortillas",
                    "1 c. bagged shredded Cheddar cheese",
                    "1 lb. lean ground beef",
                    "1 pkt (11⁄4 oz) taco seasoning mix",
                    "1 c. Shredded romaine lettuce",
                    "1 c. bottled taco sauce",
                    "¼ c. Chopped red onion"
                ],
                "ingredients": [
                    {
                        "text": "8 taco shells",
                        "quantity": 8.0,
                        "measure": "<unit>",
                        "food": "taco shells",
                        "weight": 101.6,
                        "foodCategory": "quick breads and pastries",
                        "foodId": "food_amx6njaaa4q9lsaz4k98faejx12a",
                        "image": "https://www.edamam.com/food-img/def/def506222dc404affdfbf7b7133a34c6.jpg"
                    },
                    {
                        "text": "8 soft-taco or fajita-size flour tortillas",
                        "quantity": 8.0,
                        "measure": "<unit>",
                        "food": "flour tortillas",
                        "weight": 392.0,
                        "foodCategory": "bread, rolls and tortillas",
                        "foodId": "food_a9ql6pdb639bs5b2nlvbob3w0mlj",
                        "image": "https://www.edamam.com/food-img/357/357e415685787e6d6844e8d08c1b1586.jpg"
                    },
                    {
                        "text": "1 c. bagged shredded Cheddar cheese",
                        "quantity": 1.0,
                        "measure": "cup",
                        "food": "Cheddar cheese",
                        "weight": 113.0,
                        "foodCategory": "Cheese",
                        "foodId": "food_bhppgmha1u27voagb8eptbp9g376",
                        "image": "https://www.edamam.com/food-img/bcd/bcd94dde1fcde1475b5bf0540f821c5d.jpg"
                    },
                    {
                        "text": "1 lb. lean ground beef",
                        "quantity": 1.0,
                        "measure": "pound",
                        "food": "ground beef",
                        "weight": 453.59237,
                        "foodCategory": "meats",
                        "foodId": "food_boq91pbbhklr6sb0d9sbybzgklkm",
                        "image": "https://www.edamam.com/food-img/cfa/cfae8f9276eaf8f0d9349ba662744a0c.jpg"
                    },
                    {
                        "text": "1 pkt (11⁄4 oz) taco seasoning mix",
                        "quantity": 2.75,
                        "measure": "ounce",
                        "food": "taco seasoning",
                        "weight": 77.96118859375001,
                        "foodCategory": "Condiments and sauces",
                        "foodId": "food_boffkg3ap17ef6a47lzm6b655i8w",
                        "image": "https://www.edamam.com/food-img/b3d/b3d804a544f099eabb941f255c1618a6.jpg"
                    },
                    {
                        "text": "1 c. Shredded romaine lettuce",
                        "quantity": 1.0,
                        "measure": "cup",
                        "food": "romaine lettuce",
                        "weight": 47.0,
                        "foodCategory": "vegetables",
                        "foodId": "food_bfmb5cybk1o247bmrmry4a6jvp60",
                        "image": "https://www.edamam.com/food-img/79e/79e8dd0ee229cbc32171ec362ce93a37.jpg"
                    },
                    {
                        "text": "1 c. bottled taco sauce",
                        "quantity": 1.0,
                        "measure": "cup",
                        "food": "taco sauce",
                        "weight": 128.0000000021641,
                        "foodCategory": "canned soup",
                        "foodId": "food_av2o4efb0hdsrrb2voz89b1qj44e",
                        "image": "https://www.edamam.com/food-img/ec4/ec454f6c2231ba1dce2397400be19183.jpg"
                    },
                    {
                        "text": "¼ c. Chopped red onion",
                        "quantity": 0.25,
                        "measure": "cup",
                        "food": "red onion",
                        "weight": 40.0,
                        "foodCategory": "vegetables",
                        "foodId": "food_bmrvi4ob4binw9a5m7l07amlfcoy",
                        "image": "https://www.edamam.com/food-img/205/205e6bf2399b85d34741892ef91cc603.jpg"
                    }
                ],
                "calories": 3562.395647072416,
                "totalCO2Emissions": 48950.51039755922,
                "co2EmissionsClass": "G",
                "totalWeight": 1353.153558595914,
                "totalTime": 12.0,
                "cuisineType": [
                    "mexican"
                ],
                "mealType": [
                    "lunch/dinner"
                ],
                "dishType": [
                    "sandwiches"
                ],
                "totalNutrients": {
                    "ENERC_KCAL": {
                        "label": "Energy",
                        "quantity": 3562.395647072416,
                        "unit": "kcal"
                    },
                    "FAT": {
                        "label": "Fat",
                        "quantity": 180.390874,
                        "unit": "g"
                    },
                    "FASAT": {
                        "label": "Saturated",
                        "quantity": 67.770431646,
                        "unit": "g"
                    },
                    "FATRN": {
                        "label": "Trans",
                        "quantity": 5.582021966,
                        "unit": "g"
                    },
                    "FAMS": {
                        "label": "Monounsaturated",
                        "quantity": 72.71150474500001,
                        "unit": "g"
                    },
                    "FAPU": {
                        "label": "Polyunsaturated",
                        "quantity": 17.525676247699995,
                        "unit": "g"
                    },
                    "CHOCDF": {
                        "label": "Carbs",
                        "quantity": 320.07988938451024,
                        "unit": "g"
                    },
                    "CHOCDF.net": {
                        "label": "Carbohydrates (net)",
                        "quantity": 291.8288513015415,
                        "unit": "g"
                    },
                    "FIBTG": {
                        "label": "Fiber",
                        "quantity": 28.251038082968755,
                        "unit": "g"
                    },
                    "SUGAR": {
                        "label": "Sugars",
                        "quantity": 31.168708368260262,
                        "unit": "g"
                    },
                    "PROCNT": {
                        "label": "Protein",
                        "quantity": 146.33300112671878,
                        "unit": "g"
                    },
                    "CHOLE": {
                        "label": "Cholesterol",
                        "quantity": 433.92058270000007,
                        "unit": "mg"
                    },
                    "NA": {
                        "label": "Sodium",
                        "quantity": 10693.650542963527,
                        "unit": "mg"
                    },
                    "CA": {
                        "label": "Calcium",
                        "quantity": 1649.2166266000002,
                        "unit": "mg"
                    },
                    "MG": {
                        "label": "Magnesium",
                        "quantity": 284.8487029,
                        "unit": "mg"
                    },
                    "K": {
                        "label": "Potassium",
                        "quantity": 3020.7372849375006,
                        "unit": "mg"
                    },
                    "FE": {
                        "label": "Iron",
                        "quantity": 29.79163755675,
                        "unit": "mg"
                    },
                    "ZN": {
                        "label": "Zinc",
                        "quantity": 27.119621066000004,
                        "unit": "mg"
                    },
                    "P": {
                        "label": "Phosphorus",
                        "quantity": 2328.2139446,
                        "unit": "mg"
                    },
                    "VITA_RAE": {
                        "label": "Vitamin A",
                        "quantity": 604.8896948000001,
                        "unit": "µg"
                    },
                    "VITC": {
                        "label": "Vitamin C",
                        "quantity": 4.840000000000001,
                        "unit": "mg"
                    },
                    "THIA": {
                        "label": "Thiamin (B1)",
                        "quantity": 2.4085507191000004,
                        "unit": "mg"
                    },
                    "RIBF": {
                        "label": "Riboflavin (B2)",
                        "quantity": 1.7782144786999998,
                        "unit": "mg"
                    },
                    "NIA": {
                        "label": "Niacin (B3)",
                        "quantity": 37.771857251,
                        "unit": "mg"
                    },
                    "VITB6A": {
                        "label": "Vitamin B6",
                        "quantity": 1.9384713551000003,
                        "unit": "mg"
                    },
                    "FOLDFE": {
                        "label": "Folate equivalent (total)",
                        "quantity": 957.1014659,
                        "unit": "µg"
                    },
                    "FOLFD": {
                        "label": "Folate (food)",
                        "quantity": 254.99746589999998,
                        "unit": "µg"
                    },
                    "FOLAC": {
                        "label": "Folic acid",
                        "quantity": 416.384,
                        "unit": "µg"
                    },
                    "VITB12": {
                        "label": "Vitamin B12",
                        "quantity": 10.949876718000002,
                        "unit": "µg"
                    },
                    "VITD": {
                        "label": "Vitamin D",
                        "quantity": 1.1315923700000001,
                        "unit": "µg"
                    },
                    "TOCPHA": {
                        "label": "Vitamin E",
                        "quantity": 5.714747029,
                        "unit": "mg"
                    },
                    "VITK1": {
                        "label": "Vitamin K",
                        "quantity": 84.17826266,
                        "unit": "µg"
                    },
                    "WATER": {
                        "label": "Water",
                        "quantity": 656.5098647818066,
                        "unit": "g"
                    }
                },
                "totalDaily": {
                    "ENERC_KCAL": {
                        "label": "Energy",
                        "quantity": 178.1197823536208,
                        "unit": "%"
                    },
                    "FAT": {
                        "label": "Fat",
                        "quantity": 277.5244215384615,
                        "unit": "%"
                    },
                    "FASAT": {
                        "label": "Saturated",
                        "quantity": 338.85215823000004,
                        "unit": "%"
                    },
                    "CHOCDF": {
                        "label": "Carbs",
                        "quantity": 106.69329646150341,
                        "unit": "%"
                    },
                    "FIBTG": {
                        "label": "Fiber",
                        "quantity": 113.004152331875,
                        "unit": "%"
                    },
                    "PROCNT": {
                        "label": "Protein",
                        "quantity": 292.66600225343757,
                        "unit": "%"
                    },
                    "CHOLE": {
                        "label": "Cholesterol",
                        "quantity": 144.64019423333337,
                        "unit": "%"
                    },
                    "NA": {
                        "label": "Sodium",
                        "quantity": 445.5687726234803,
                        "unit": "%"
                    },
                    "CA": {
                        "label": "Calcium",
                        "quantity": 164.92166266,
                        "unit": "%"
                    },
                    "MG": {
                        "label": "Magnesium",
                        "quantity": 67.82111973809523,
                        "unit": "%"
                    },
                    "K": {
                        "label": "Potassium",
                        "quantity": 64.2710060625,
                        "unit": "%"
                    },
                    "FE": {
                        "label": "Iron",
                        "quantity": 165.5090975375,
                        "unit": "%"
                    },
                    "ZN": {
                        "label": "Zinc",
                        "quantity": 246.54200969090914,
                        "unit": "%"
                    },
                    "P": {
                        "label": "Phosphorus",
                        "quantity": 332.6019920857143,
                        "unit": "%"
                    },
                    "VITA_RAE": {
                        "label": "Vitamin A",
                        "quantity": 67.2099660888889,
                        "unit": "%"
                    },
                    "VITC": {
                        "label": "Vitamin C",
                        "quantity": 5.377777777777778,
                        "unit": "%"
                    },
                    "THIA": {
                        "label": "Thiamin (B1)",
                        "quantity": 200.71255992500005,
                        "unit": "%"
                    },
                    "RIBF": {
                        "label": "Riboflavin (B2)",
                        "quantity": 136.78572913076923,
                        "unit": "%"
                    },
                    "NIA": {
                        "label": "Niacin (B3)",
                        "quantity": 236.07410781875,
                        "unit": "%"
                    },
                    "VITB6A": {
                        "label": "Vitamin B6",
                        "quantity": 149.11318116153848,
                        "unit": "%"
                    },
                    "FOLDFE": {
                        "label": "Folate equivalent (total)",
                        "quantity": 239.275366475,
                        "unit": "%"
                    },
                    "VITB12": {
                        "label": "Vitamin B12",
                        "quantity": 456.24486325000015,
                        "unit": "%"
                    },
                    "VITD": {
                        "label": "Vitamin D",
                        "quantity": 7.543949133333334,
                        "unit": "%"
                    },
                    "TOCPHA": {
                        "label": "Vitamin E",
                        "quantity": 38.098313526666665,
                        "unit": "%"
                    },
                    "VITK1": {
                        "label": "Vitamin K",
                        "quantity": 70.14855221666667,
                        "unit": "%"
                    }
                },
                "digest": [
                    {
                        "label": "Fat",
                        "tag": "FAT",
                        "schemaOrgTag": "fatContent",
                        "total": 180.390874,
                        "hasRDI": True,
                        "daily": 277.5244215384615,
                        "unit": "g",
                        "sub": [
                            {
                                "label": "Saturated",
                                "tag": "FASAT",
                                "schemaOrgTag": "saturatedFatContent",
                                "total": 67.770431646,
                                "hasRDI": True,
                                "daily": 338.85215823000004,
                                "unit": "g"
                            },
                            {
                                "label": "Trans",
                                "tag": "FATRN",
                                "schemaOrgTag": "transFatContent",
                                "total": 5.582021966,
                                "hasRDI": False,
                                "daily": 0.0,
                                "unit": "g"
                            },
                            {
                                "label": "Monounsaturated",
                                "tag": "FAMS",
                                "schemaOrgTag": '',
                                "total": 72.71150474500001,
                                "hasRDI": False,
                                "daily": 0.0,
                                "unit": "g"
                            },
                            {
                                "label": "Polyunsaturated",
                                "tag": "FAPU",
                                "schemaOrgTag": '',
                                "total": 17.525676247699995,
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
                        "total": 320.07988938451024,
                        "hasRDI": True,
                        "daily": 106.69329646150341,
                        "unit": "g",
                        "sub": [
                            {
                                "label": "Carbs (net)",
                                "tag": "CHOCDF.net",
                                "schemaOrgTag": '',
                                "total": 291.8288513015415,
                                "hasRDI": False,
                                "daily": 0.0,
                                "unit": "g"
                            },
                            {
                                "label": "Fiber",
                                "tag": "FIBTG",
                                "schemaOrgTag": "fiberContent",
                                "total": 28.251038082968755,
                                "hasRDI": True,
                                "daily": 113.004152331875,
                                "unit": "g"
                            },
                            {
                                "label": "Sugars",
                                "tag": "SUGAR",
                                "schemaOrgTag": "sugarContent",
                                "total": 31.168708368260262,
                                "hasRDI": False,
                                "daily": 0.0,
                                "unit": "g"
                            },
                            {
                                "label": "Sugars, added",
                                "tag": "SUGAR.added",
                                "schemaOrgTag": '',
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
                        "total": 146.33300112671878,
                        "hasRDI": True,
                        "daily": 292.66600225343757,
                        "unit": "g"
                    },
                    {
                        "label": "Cholesterol",
                        "tag": "CHOLE",
                        "schemaOrgTag": "cholesterolContent",
                        "total": 433.92058270000007,
                        "hasRDI": True,
                        "daily": 144.64019423333337,
                        "unit": "mg"
                    },
                    {
                        "label": "Sodium",
                        "tag": "NA",
                        "schemaOrgTag": "sodiumContent",
                        "total": 10693.650542963527,
                        "hasRDI": True,
                        "daily": 445.5687726234803,
                        "unit": "mg"
                    },
                    {
                        "label": "Calcium",
                        "tag": "CA",
                        "schemaOrgTag": '',
                        "total": 1649.2166266000002,
                        "hasRDI": True,
                        "daily": 164.92166266,
                        "unit": "mg"
                    },
                    {
                        "label": "Magnesium",
                        "tag": "MG",
                        "schemaOrgTag": '',
                        "total": 284.8487029,
                        "hasRDI": True,
                        "daily": 67.82111973809523,
                        "unit": "mg"
                    },
                    {
                        "label": "Potassium",
                        "tag": "K",
                        "schemaOrgTag": '',
                        "total": 3020.7372849375006,
                        "hasRDI": True,
                        "daily": 64.2710060625,
                        "unit": "mg"
                    },
                    {
                        "label": "Iron",
                        "tag": "FE",
                        "schemaOrgTag": '',
                        "total": 29.79163755675,
                        "hasRDI": True,
                        "daily": 165.5090975375,
                        "unit": "mg"
                    },
                    {
                        "label": "Zinc",
                        "tag": "ZN",
                        "schemaOrgTag": '',
                        "total": 27.119621066000004,
                        "hasRDI": True,
                        "daily": 246.54200969090914,
                        "unit": "mg"
                    },
                    {
                        "label": "Phosphorus",
                        "tag": "P",
                        "schemaOrgTag": '',
                        "total": 2328.2139446,
                        "hasRDI": True,
                        "daily": 332.6019920857143,
                        "unit": "mg"
                    },
                    {
                        "label": "Vitamin A",
                        "tag": "VITA_RAE",
                        "schemaOrgTag": '',
                        "total": 604.8896948000001,
                        "hasRDI": True,
                        "daily": 67.2099660888889,
                        "unit": "µg"
                    },
                    {
                        "label": "Vitamin C",
                        "tag": "VITC",
                        "schemaOrgTag": '',
                        "total": 4.840000000000001,
                        "hasRDI": True,
                        "daily": 5.377777777777778,
                        "unit": "mg"
                    },
                    {
                        "label": "Thiamin (B1)",
                        "tag": "THIA",
                        "schemaOrgTag": '',
                        "total": 2.4085507191000004,
                        "hasRDI": True,
                        "daily": 200.71255992500005,
                        "unit": "mg"
                    },
                    {
                        "label": "Riboflavin (B2)",
                        "tag": "RIBF",
                        "schemaOrgTag": '',
                        "total": 1.7782144786999998,
                        "hasRDI": True,
                        "daily": 136.78572913076923,
                        "unit": "mg"
                    },
                    {
                        "label": "Niacin (B3)",
                        "tag": "NIA",
                        "schemaOrgTag": '',
                        "total": 37.771857251,
                        "hasRDI": True,
                        "daily": 236.07410781875,
                        "unit": "mg"
                    },
                    {
                        "label": "Vitamin B6",
                        "tag": "VITB6A",
                        "schemaOrgTag": '',
                        "total": 1.9384713551000003,
                        "hasRDI": True,
                        "daily": 149.11318116153848,
                        "unit": "mg"
                    },
                    {
                        "label": "Folate equivalent (total)",
                        "tag": "FOLDFE",
                        "schemaOrgTag": '',
                        "total": 957.1014659,
                        "hasRDI": True,
                        "daily": 239.275366475,
                        "unit": "µg"
                    },
                    {
                        "label": "Folate (food)",
                        "tag": "FOLFD",
                        "schemaOrgTag": '',
                        "total": 254.99746589999998,
                        "hasRDI": False,
                        "daily": 0.0,
                        "unit": "µg"
                    },
                    {
                        "label": "Folic acid",
                        "tag": "FOLAC",
                        "schemaOrgTag": '',
                        "total": 416.384,
                        "hasRDI": False,
                        "daily": 0.0,
                        "unit": "µg"
                    },
                    {
                        "label": "Vitamin B12",
                        "tag": "VITB12",
                        "schemaOrgTag": '',
                        "total": 10.949876718000002,
                        "hasRDI": True,
                        "daily": 456.24486325000015,
                        "unit": "µg"
                    },
                    {
                        "label": "Vitamin D",
                        "tag": "VITD",
                        "schemaOrgTag": '',
                        "total": 1.1315923700000001,
                        "hasRDI": True,
                        "daily": 7.543949133333334,
                        "unit": "µg"
                    },
                    {
                        "label": "Vitamin E",
                        "tag": "TOCPHA",
                        "schemaOrgTag": '',
                        "total": 5.714747029,
                        "hasRDI": True,
                        "daily": 38.098313526666665,
                        "unit": "mg"
                    },
                    {
                        "label": "Vitamin K",
                        "tag": "VITK1",
                        "schemaOrgTag": '',
                        "total": 84.17826266,
                        "hasRDI": True,
                        "daily": 70.14855221666667,
                        "unit": "µg"
                    },
                    {
                        "label": "Sugar alcohols",
                        "tag": "Sugar.alcohol",
                        "schemaOrgTag": '',
                        "total": 0.0,
                        "hasRDI": False,
                        "daily": 0.0,
                        "unit": "g"
                    },
                    {
                        "label": "Water",
                        "tag": "WATER",
                        "schemaOrgTag": '',
                        "total": 656.5098647818066,
                        "hasRDI": False,
                        "daily": 0.0,
                        "unit": "g"
                    }
                ]
            },
            "_links": {
                "self": {
                    "title": "Self",
                    "href": "https://api.edamam.com/api/recipes/v2/6b11398feaa404a407ae7de9f2a08905?type=public&app_id=e909afd5&app_key=34e59dda7e1bffb92e49c416e9449e1d"
                }
            }
        },
        {
            "recipe": {
                "uri": "http://www.edamam.com/ontologies/edamam.owl#recipe_48c40a74e2a865a849dde855bcf9fe17",
                "label": "Tasty Tacos - Kapha",
                "image": "https://edamam-product-images.s3.amazonaws.com/web-img/ee3/ee3f77f4e3f80ac79f297ca4fbc8d47b.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLWVhc3QtMSJIMEYCIQCP2Gbt%2ByPQIVKV%2FafgML7WXbkOusL9fCs6d1le6dFKYAIhAJcnuEh%2B1NzOso38QgGaVBwaVQAMxyMJATg%2FR%2Fl0jl96KsEFCJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMMTg3MDE3MTUwOTg2IgydADkJdybnmhdEGwQqlQUNCCJJEzulouVCRRPPDPN9Ik9nmgPZk%2Fam6u04CTug5FWfzto4W1y6mlAuXr3EHPB%2FvTcZ%2BmAkgcS5%2FRfKsviGgYg1PBDbKvJFWJigqXNb6jHaHO3eyZnXpof0Qk2PachTFyGGF7upzvEiKr6BGB6DtCoEGe3wCd0iFSMS%2Ft8LIlICGGYaaCvWq9TXeaXkel5jju8XxawzfW0OY8ad1NODjiJJ%2FJ02goRzRa3HwZdXj0P4%2FwwiBHg8BMnsBu5XvhNCt9Gz%2Bxp9cZIC8TMv%2FY8rOvepaH28zVl5BjLGle3tn5syTeLiH6OS68I4OndB2qqeqZqdi9cu6zb1H0y8aKh8r8IIaHqXhP6jBXwOxUN8uimNrMJnaDPxNdvFPuR5yx8UApiuserTd1b1ZIBFiBJ6lavYUBrkLW%2B7bZIJltsNTSxF2GTKFWoXHKGf3%2FXYj%2FniRUh%2BB3xUXrXh8PzVKChkdfuCxirnj5UG2XCrj22%2BBJG8S8UHiExHaIwt01Nel6V7Y0IlXWvwqK8YEx%2FHOI%2FewXERfrnIQDCsrQyC7qTLL3HndUW2Ke8ib2iC%2BPgaP6xDqkqdlhOSojQHG4rfwcyVOFOzeauzAO7Rc77mb0rCUJdMckP6nKiD7nrtjlZXznFmYhCvjmWQF2l06Jl7xQsr%2BjkGAeoXo9X%2FiC11ZTNfxOVIe3LWWkRvMwGWvgvtgF4ZEDGaLXgsbO4I8%2FpSmGD4ox9ZWDfX%2BtTURCyBYVXqYpQ4TpgMhHqAtTUr4TNc7GRLVbfi1xqZNQDt1Sfdzh3Xq88dOJyKsyUs7rcFuuxoNyxvqstWVaAyRglOH1n%2BpV0xA7%2FKEHa%2F8%2FzH6uaXeIp3eLJN1%2BGlAQc1sP2jehPHqGi5Lc7YMOKk8akGOrABqEMeyIMA72vRUvaZqcs7N77uX3kDw2%2BTfyF8pS8HYdR1%2BEU1ekEPGlPPLyTo0NFmbmMa4urw%2B19eIvlGSnFjiSeee%2F%2BeotdKLVnDgZ5aNxOYivkgUqjazWNTWX1qdv7Jq7GWrNDLwjZiU5zLvpcjSyzLyGAVIo8pW14m4aC3jppuzjKpasygGK2%2Bf%2BmxisMAkIdRRS5aXW9PY%2FuwiBnL3qiZT5RtAdamISZZM9jUAWY%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231028T003610Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFPXEGMX3T%2F20231028%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=63ab695bddee41eb63a8c9a7c4754745ffd62ff7383d166dc10f2ad96894ebc9",
                "images": {
                    "THUMBNAIL": {
                        "url": "https://edamam-product-images.s3.amazonaws.com/web-img/ee3/ee3f77f4e3f80ac79f297ca4fbc8d47b-s.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLWVhc3QtMSJIMEYCIQCP2Gbt%2ByPQIVKV%2FafgML7WXbkOusL9fCs6d1le6dFKYAIhAJcnuEh%2B1NzOso38QgGaVBwaVQAMxyMJATg%2FR%2Fl0jl96KsEFCJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMMTg3MDE3MTUwOTg2IgydADkJdybnmhdEGwQqlQUNCCJJEzulouVCRRPPDPN9Ik9nmgPZk%2Fam6u04CTug5FWfzto4W1y6mlAuXr3EHPB%2FvTcZ%2BmAkgcS5%2FRfKsviGgYg1PBDbKvJFWJigqXNb6jHaHO3eyZnXpof0Qk2PachTFyGGF7upzvEiKr6BGB6DtCoEGe3wCd0iFSMS%2Ft8LIlICGGYaaCvWq9TXeaXkel5jju8XxawzfW0OY8ad1NODjiJJ%2FJ02goRzRa3HwZdXj0P4%2FwwiBHg8BMnsBu5XvhNCt9Gz%2Bxp9cZIC8TMv%2FY8rOvepaH28zVl5BjLGle3tn5syTeLiH6OS68I4OndB2qqeqZqdi9cu6zb1H0y8aKh8r8IIaHqXhP6jBXwOxUN8uimNrMJnaDPxNdvFPuR5yx8UApiuserTd1b1ZIBFiBJ6lavYUBrkLW%2B7bZIJltsNTSxF2GTKFWoXHKGf3%2FXYj%2FniRUh%2BB3xUXrXh8PzVKChkdfuCxirnj5UG2XCrj22%2BBJG8S8UHiExHaIwt01Nel6V7Y0IlXWvwqK8YEx%2FHOI%2FewXERfrnIQDCsrQyC7qTLL3HndUW2Ke8ib2iC%2BPgaP6xDqkqdlhOSojQHG4rfwcyVOFOzeauzAO7Rc77mb0rCUJdMckP6nKiD7nrtjlZXznFmYhCvjmWQF2l06Jl7xQsr%2BjkGAeoXo9X%2FiC11ZTNfxOVIe3LWWkRvMwGWvgvtgF4ZEDGaLXgsbO4I8%2FpSmGD4ox9ZWDfX%2BtTURCyBYVXqYpQ4TpgMhHqAtTUr4TNc7GRLVbfi1xqZNQDt1Sfdzh3Xq88dOJyKsyUs7rcFuuxoNyxvqstWVaAyRglOH1n%2BpV0xA7%2FKEHa%2F8%2FzH6uaXeIp3eLJN1%2BGlAQc1sP2jehPHqGi5Lc7YMOKk8akGOrABqEMeyIMA72vRUvaZqcs7N77uX3kDw2%2BTfyF8pS8HYdR1%2BEU1ekEPGlPPLyTo0NFmbmMa4urw%2B19eIvlGSnFjiSeee%2F%2BeotdKLVnDgZ5aNxOYivkgUqjazWNTWX1qdv7Jq7GWrNDLwjZiU5zLvpcjSyzLyGAVIo8pW14m4aC3jppuzjKpasygGK2%2Bf%2BmxisMAkIdRRS5aXW9PY%2FuwiBnL3qiZT5RtAdamISZZM9jUAWY%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231028T003610Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFPXEGMX3T%2F20231028%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=b99b4806a27e54dd640d62ccfbbc7b8d8307ac787a7faec21d9b483373700344",
                        "width": 100,
                        "height": 100
                    },
                    "SMALL": {
                        "url": "https://edamam-product-images.s3.amazonaws.com/web-img/ee3/ee3f77f4e3f80ac79f297ca4fbc8d47b-m.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLWVhc3QtMSJIMEYCIQCP2Gbt%2ByPQIVKV%2FafgML7WXbkOusL9fCs6d1le6dFKYAIhAJcnuEh%2B1NzOso38QgGaVBwaVQAMxyMJATg%2FR%2Fl0jl96KsEFCJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMMTg3MDE3MTUwOTg2IgydADkJdybnmhdEGwQqlQUNCCJJEzulouVCRRPPDPN9Ik9nmgPZk%2Fam6u04CTug5FWfzto4W1y6mlAuXr3EHPB%2FvTcZ%2BmAkgcS5%2FRfKsviGgYg1PBDbKvJFWJigqXNb6jHaHO3eyZnXpof0Qk2PachTFyGGF7upzvEiKr6BGB6DtCoEGe3wCd0iFSMS%2Ft8LIlICGGYaaCvWq9TXeaXkel5jju8XxawzfW0OY8ad1NODjiJJ%2FJ02goRzRa3HwZdXj0P4%2FwwiBHg8BMnsBu5XvhNCt9Gz%2Bxp9cZIC8TMv%2FY8rOvepaH28zVl5BjLGle3tn5syTeLiH6OS68I4OndB2qqeqZqdi9cu6zb1H0y8aKh8r8IIaHqXhP6jBXwOxUN8uimNrMJnaDPxNdvFPuR5yx8UApiuserTd1b1ZIBFiBJ6lavYUBrkLW%2B7bZIJltsNTSxF2GTKFWoXHKGf3%2FXYj%2FniRUh%2BB3xUXrXh8PzVKChkdfuCxirnj5UG2XCrj22%2BBJG8S8UHiExHaIwt01Nel6V7Y0IlXWvwqK8YEx%2FHOI%2FewXERfrnIQDCsrQyC7qTLL3HndUW2Ke8ib2iC%2BPgaP6xDqkqdlhOSojQHG4rfwcyVOFOzeauzAO7Rc77mb0rCUJdMckP6nKiD7nrtjlZXznFmYhCvjmWQF2l06Jl7xQsr%2BjkGAeoXo9X%2FiC11ZTNfxOVIe3LWWkRvMwGWvgvtgF4ZEDGaLXgsbO4I8%2FpSmGD4ox9ZWDfX%2BtTURCyBYVXqYpQ4TpgMhHqAtTUr4TNc7GRLVbfi1xqZNQDt1Sfdzh3Xq88dOJyKsyUs7rcFuuxoNyxvqstWVaAyRglOH1n%2BpV0xA7%2FKEHa%2F8%2FzH6uaXeIp3eLJN1%2BGlAQc1sP2jehPHqGi5Lc7YMOKk8akGOrABqEMeyIMA72vRUvaZqcs7N77uX3kDw2%2BTfyF8pS8HYdR1%2BEU1ekEPGlPPLyTo0NFmbmMa4urw%2B19eIvlGSnFjiSeee%2F%2BeotdKLVnDgZ5aNxOYivkgUqjazWNTWX1qdv7Jq7GWrNDLwjZiU5zLvpcjSyzLyGAVIo8pW14m4aC3jppuzjKpasygGK2%2Bf%2BmxisMAkIdRRS5aXW9PY%2FuwiBnL3qiZT5RtAdamISZZM9jUAWY%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231028T003610Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFPXEGMX3T%2F20231028%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=6cf34577136064ad5ff617382426452193bb109bde8d32f7ebabc8273cab58d6",
                        "width": 200,
                        "height": 200
                    },
                    "REGULAR": {
                        "url": "https://edamam-product-images.s3.amazonaws.com/web-img/ee3/ee3f77f4e3f80ac79f297ca4fbc8d47b.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLWVhc3QtMSJIMEYCIQCP2Gbt%2ByPQIVKV%2FafgML7WXbkOusL9fCs6d1le6dFKYAIhAJcnuEh%2B1NzOso38QgGaVBwaVQAMxyMJATg%2FR%2Fl0jl96KsEFCJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMMTg3MDE3MTUwOTg2IgydADkJdybnmhdEGwQqlQUNCCJJEzulouVCRRPPDPN9Ik9nmgPZk%2Fam6u04CTug5FWfzto4W1y6mlAuXr3EHPB%2FvTcZ%2BmAkgcS5%2FRfKsviGgYg1PBDbKvJFWJigqXNb6jHaHO3eyZnXpof0Qk2PachTFyGGF7upzvEiKr6BGB6DtCoEGe3wCd0iFSMS%2Ft8LIlICGGYaaCvWq9TXeaXkel5jju8XxawzfW0OY8ad1NODjiJJ%2FJ02goRzRa3HwZdXj0P4%2FwwiBHg8BMnsBu5XvhNCt9Gz%2Bxp9cZIC8TMv%2FY8rOvepaH28zVl5BjLGle3tn5syTeLiH6OS68I4OndB2qqeqZqdi9cu6zb1H0y8aKh8r8IIaHqXhP6jBXwOxUN8uimNrMJnaDPxNdvFPuR5yx8UApiuserTd1b1ZIBFiBJ6lavYUBrkLW%2B7bZIJltsNTSxF2GTKFWoXHKGf3%2FXYj%2FniRUh%2BB3xUXrXh8PzVKChkdfuCxirnj5UG2XCrj22%2BBJG8S8UHiExHaIwt01Nel6V7Y0IlXWvwqK8YEx%2FHOI%2FewXERfrnIQDCsrQyC7qTLL3HndUW2Ke8ib2iC%2BPgaP6xDqkqdlhOSojQHG4rfwcyVOFOzeauzAO7Rc77mb0rCUJdMckP6nKiD7nrtjlZXznFmYhCvjmWQF2l06Jl7xQsr%2BjkGAeoXo9X%2FiC11ZTNfxOVIe3LWWkRvMwGWvgvtgF4ZEDGaLXgsbO4I8%2FpSmGD4ox9ZWDfX%2BtTURCyBYVXqYpQ4TpgMhHqAtTUr4TNc7GRLVbfi1xqZNQDt1Sfdzh3Xq88dOJyKsyUs7rcFuuxoNyxvqstWVaAyRglOH1n%2BpV0xA7%2FKEHa%2F8%2FzH6uaXeIp3eLJN1%2BGlAQc1sP2jehPHqGi5Lc7YMOKk8akGOrABqEMeyIMA72vRUvaZqcs7N77uX3kDw2%2BTfyF8pS8HYdR1%2BEU1ekEPGlPPLyTo0NFmbmMa4urw%2B19eIvlGSnFjiSeee%2F%2BeotdKLVnDgZ5aNxOYivkgUqjazWNTWX1qdv7Jq7GWrNDLwjZiU5zLvpcjSyzLyGAVIo8pW14m4aC3jppuzjKpasygGK2%2Bf%2BmxisMAkIdRRS5aXW9PY%2FuwiBnL3qiZT5RtAdamISZZM9jUAWY%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231028T003610Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFPXEGMX3T%2F20231028%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=63ab695bddee41eb63a8c9a7c4754745ffd62ff7383d166dc10f2ad96894ebc9",
                        "width": 300,
                        "height": 300
                    }
                },
                "source": "Men's Health",
                "url": "https://www.menshealth.com/recipes/tasty-tacos-kapha",
                "shareAs": "http://www.edamam.com/recipe/tasty-tacos-kapha-48c40a74e2a865a849dde855bcf9fe17/tacos",
                "yield": 6.0,
                "dietLabels": [],
                "healthLabels": [
                    "Sugar-Conscious",
                    "Pescatarian",
                    "Dairy-Free",
                    "Egg-Free",
                    "Peanut-Free",
                    "Tree-Nut-Free",
                    "Soy-Free",
                    "Shellfish-Free",
                    "Pork-Free",
                    "Red-Meat-Free",
                    "Crustacean-Free",
                    "Celery-Free",
                    "Mustard-Free",
                    "Sesame-Free",
                    "Lupine-Free",
                    "Mollusk-Free",
                    "Alcohol-Free",
                    "Sulfite-Free",
                    "Kosher"
                ],
                "cautions": [
                    "Eggs",
                    "Milk",
                    "Sulfites"
                ],
                "ingredientLines": [
                    "CHIPOTLE SALSA:",
                    "1 pint cherry or grape tomatoes",
                    "3 cloves garlic, skins intact",
                    "1/2 small red or yellow onion",
                    "1 chipotle chili pepper in adobo sauce",
                    "1 tablespoon adobo sauce from jar of chipotle chile peppers",
                    "2 teaspoons fresh lime juice",
                    "1/4 cup cilantro, chopped",
                    "1/4 teaspoon salt",
                    "TACOS:",
                    "12 ounces tilapia fillets",
                    "1/2 teaspoon salt",
                    "1 tablespoon extra-virgin olive oil",
                    "1/2 red or green cabbage, thinly sliced",
                    "8 corn tortillas, warmed",
                    "4 radishes, thinly sliced",
                    "1 cup sprouts, such as alfalfa or broccoli"
                ],
                "ingredients": [
                    {
                        "text": "1 pint cherry or grape tomatoes",
                        "quantity": 1.0,
                        "measure": "pint",
                        "food": "cherry or grape tomatoes",
                        "weight": 349.99999999999994,
                        "foodCategory": "vegetables",
                        "foodId": "food_a30b0hpbvavginafe0tocbf6ymje",
                        "image": "https://www.edamam.com/food-img/23e/23e727a14f1035bdc2733bb0477efbd2.jpg"
                    },
                    {
                        "text": "3 cloves garlic, skins intact",
                        "quantity": 3.0,
                        "measure": "clove",
                        "food": "garlic",
                        "weight": 9.0,
                        "foodCategory": "vegetables",
                        "foodId": "food_avtcmx6bgjv1jvay6s6stan8dnyp",
                        "image": "https://www.edamam.com/food-img/6ee/6ee142951f48aaf94f4312409f8d133d.jpg"
                    },
                    {
                        "text": "1/2 small red or yellow onion",
                        "quantity": 0.5,
                        "measure": "<unit>",
                        "food": "yellow onion",
                        "weight": 62.5,
                        "foodCategory": "vegetables",
                        "foodId": "food_bmrvi4ob4binw9a5m7l07amlfcoy",
                        "image": "https://www.edamam.com/food-img/205/205e6bf2399b85d34741892ef91cc603.jpg"
                    },
                    {
                        "text": "1 chipotle chili pepper in adobo sauce",
                        "quantity": 1.0,
                        "measure": "pepper",
                        "food": "chipotle chili",
                        "weight": 73.0,
                        "foodCategory": "canned vegetables",
                        "foodId": "food_bumzpysb5k05cibmscqp2a0fwgpa",
                        "image": "https://www.edamam.com/food-img/c34/c343c40fbfe50bd72bbb3890c83a4315.jpeg"
                    },
                    {
                        "text": "1 tablespoon adobo sauce from jar of chipotle chile peppers",
                        "quantity": 1.0,
                        "measure": "tablespoon",
                        "food": "chipotle chile",
                        "weight": 8.49999999985629,
                        "foodCategory": "canned vegetables",
                        "foodId": "food_bumzpysb5k05cibmscqp2a0fwgpa",
                        "image": "https://www.edamam.com/food-img/c34/c343c40fbfe50bd72bbb3890c83a4315.jpeg"
                    },
                    {
                        "text": "2 teaspoons fresh lime juice",
                        "quantity": 2.0,
                        "measure": "teaspoon",
                        "food": "lime juice",
                        "weight": 10.266666667187403,
                        "foodCategory": "fruit",
                        "foodId": "food_b0iywbmaujvd4eblrooo9bsvn7e6",
                        "image": "https://www.edamam.com/food-img/8f0/8f0c10eb3dbf476a05e61018e76ea220.jpg"
                    },
                    {
                        "text": "1/4 cup cilantro, chopped",
                        "quantity": 0.25,
                        "measure": "cup",
                        "food": "cilantro",
                        "weight": 4.0,
                        "foodCategory": "vegetables",
                        "foodId": "food_alhzhuwb4lc7jnb5s6f02by60bzp",
                        "image": "https://www.edamam.com/food-img/d57/d57e375b6ff99a90c7ee2b1990a1af36.jpg"
                    },
                    {
                        "text": "1/4 teaspoon salt",
                        "quantity": 0.25,
                        "measure": "teaspoon",
                        "food": "salt",
                        "weight": 1.5,
                        "foodCategory": "Condiments and sauces",
                        "foodId": "food_btxz81db72hwbra2pncvebzzzum9",
                        "image": "https://www.edamam.com/food-img/694/6943ea510918c6025795e8dc6e6eaaeb.jpg"
                    },
                    {
                        "text": "12 ounces tilapia fillets",
                        "quantity": 12.0,
                        "measure": "ounce",
                        "food": "tilapia",
                        "weight": 340.1942775,
                        "foodCategory": "seafood",
                        "foodId": "food_ar6pjbvaxqtlqia7jewa4brld7p9",
                        "image": "https://www.edamam.com/food-img/717/717cb400eb49626bb7c95cd29292cef4.jpg"
                    },
                    {
                        "text": "1/2 teaspoon salt",
                        "quantity": 0.5,
                        "measure": "teaspoon",
                        "food": "salt",
                        "weight": 3.0,
                        "foodCategory": "Condiments and sauces",
                        "foodId": "food_btxz81db72hwbra2pncvebzzzum9",
                        "image": "https://www.edamam.com/food-img/694/6943ea510918c6025795e8dc6e6eaaeb.jpg"
                    },
                    {
                        "text": "1 tablespoon extra-virgin olive oil",
                        "quantity": 1.0,
                        "measure": "tablespoon",
                        "food": "extra-virgin olive oil",
                        "weight": 13.5,
                        "foodCategory": "Oils",
                        "foodId": "food_b1d1icuad3iktrbqby0hiagafaz7",
                        "image": "https://www.edamam.com/food-img/4d6/4d651eaa8a353647746290c7a9b29d84.jpg"
                    },
                    {
                        "text": "1/2 red or green cabbage, thinly sliced",
                        "quantity": 0.5,
                        "measure": "<unit>",
                        "food": "green cabbage",
                        "weight": 7.5,
                        "foodCategory": "vegetables",
                        "foodId": "food_afb4o8kb767k0iapchxupaifxk1z",
                        "image": "https://www.edamam.com/food-img/cb1/cb1411c925c19de26620e63cb90d0e14.jpg"
                    },
                    {
                        "text": "8 corn tortillas, warmed",
                        "quantity": 8.0,
                        "measure": "<unit>",
                        "food": "corn tortillas",
                        "weight": 192.0,
                        "foodCategory": "quick breads and pastries",
                        "foodId": "food_bhw0b95agm97s0abfignnb8fsvb3",
                        "image": "https://www.edamam.com/food-img/b8a/b8ad23dcc06f2324f944e47eb579d644.jpg"
                    },
                    {
                        "text": "4 radishes, thinly sliced",
                        "quantity": 4.0,
                        "measure": "<unit>",
                        "food": "radishes",
                        "weight": 48.0,
                        "foodCategory": "vegetables",
                        "foodId": "food_bs6xkukbtd85e7b2lh5zfazpe45y",
                        "image": "https://www.edamam.com/food-img/ad7/ad78f4315cdba1dc26ccef0d7dba464b.jpg"
                    },
                    {
                        "text": "1 cup sprouts, such as alfalfa or broccoli",
                        "quantity": 1.0,
                        "measure": "cup",
                        "food": "broccoli",
                        "weight": 91.0,
                        "foodCategory": "vegetables",
                        "foodId": "food_aahw0jha9f8337ajbopx9aec6z7i",
                        "image": "https://www.edamam.com/food-img/3e4/3e47317a3dd54dc911b9c44122285df1.jpg"
                    }
                ],
                "calories": 1026.9931730667665,
                "totalCO2Emissions": 6040.383595730902,
                "co2EmissionsClass": "E",
                "totalWeight": 1213.3830598340796,
                "totalTime": 30.0,
                "cuisineType": [
                    "mexican"
                ],
                "mealType": [
                    "lunch/dinner"
                ],
                "dishType": [
                    "sandwiches"
                ],
                "totalNutrients": {
                    "ENERC_KCAL": {
                        "label": "Energy",
                        "quantity": 1026.9931730667665,
                        "unit": "kcal"
                    },
                    "FAT": {
                        "label": "Fat",
                        "quantity": 26.06448938416689,
                        "unit": "g"
                    },
                    "FASAT": {
                        "label": "Saturated",
                        "quantity": 4.986337856708361,
                        "unit": "g"
                    },
                    "FATRN": {
                        "label": "Trans",
                        "quantity": 0.0,
                        "unit": "g"
                    },
                    "FAMS": {
                        "label": "Monounsaturated",
                        "quantity": 13.049778835283366,
                        "unit": "g"
                    },
                    "FAPU": {
                        "label": "Polyunsaturated",
                        "quantity": 5.877361560658374,
                        "unit": "g"
                    },
                    "CHOCDF": {
                        "label": "Carbs",
                        "quantity": 121.34065333336986,
                        "unit": "g"
                    },
                    "CHOCDF.net": {
                        "label": "Carbohydrates (net)",
                        "quantity": 99.25908666670298,
                        "unit": "g"
                    },
                    "FIBTG": {
                        "label": "Fiber",
                        "quantity": 22.08156666666688,
                        "unit": "g"
                    },
                    "SUGAR": {
                        "label": "Sugars",
                        "quantity": 19.228506666670697,
                        "unit": "g"
                    },
                    "PROCNT": {
                        "label": "Protein",
                        "quantity": 87.51336977750091,
                        "unit": "g"
                    },
                    "CHOLE": {
                        "label": "Cholesterol",
                        "quantity": 170.09713875,
                        "unit": "mg"
                    },
                    "NA": {
                        "label": "Sodium",
                        "quantity": 2812.577236441577,
                        "unit": "mg"
                    },
                    "CA": {
                        "label": "Calcium",
                        "quantity": 323.87306884348476,
                        "unit": "mg"
                    },
                    "MG": {
                        "label": "Magnesium",
                        "quantity": 315.2130094150253,
                        "unit": "mg"
                    },
                    "K": {
                        "label": "Potassium",
                        "quantity": 2939.2024873037035,
                        "unit": "mg"
                    },
                    "FE": {
                        "label": "Iron",
                        "quantity": 6.934770935700968,
                        "unit": "mg"
                    },
                    "ZN": {
                        "label": "Zinc",
                        "quantity": 5.135176564750542,
                        "unit": "mg"
                    },
                    "P": {
                        "label": "Phosphorus",
                        "quantity": 1385.9276050833819,
                        "unit": "mg"
                    },
                    "VITA_RAE": {
                        "label": "Vitamin A",
                        "quantity": 674.1953333324886,
                        "unit": "µg"
                    },
                    "VITC": {
                        "label": "Vitamin C",
                        "quantity": 205.98400000005847,
                        "unit": "mg"
                    },
                    "THIA": {
                        "label": "Thiamin (B1)",
                        "quantity": 0.5927013204417682,
                        "unit": "mg"
                    },
                    "RIBF": {
                        "label": "Riboflavin (B2)",
                        "quantity": 0.6093573948250062,
                        "unit": "mg"
                    },
                    "NIA": {
                        "label": "Niacin (B3)",
                        "quantity": 19.794015489166252,
                        "unit": "mg"
                    },
                    "VITB6A": {
                        "label": "Vitamin B6",
                        "quantity": 1.7753810628833113,
                        "unit": "mg"
                    },
                    "FOLDFE": {
                        "label": "Folate equivalent (total)",
                        "quantity": 240.10329326670438,
                        "unit": "µg"
                    },
                    "FOLFD": {
                        "label": "Folate (food)",
                        "quantity": 240.10329326670438,
                        "unit": "µg"
                    },
                    "FOLAC": {
                        "label": "Folic acid",
                        "quantity": 0.0,
                        "unit": "µg"
                    },
                    "VITB12": {
                        "label": "Vitamin B12",
                        "quantity": 5.3750695845,
                        "unit": "µg"
                    },
                    "VITD": {
                        "label": "Vitamin D",
                        "quantity": 10.5460226025,
                        "unit": "µg"
                    },
                    "TOCPHA": {
                        "label": "Vitamin E",
                        "quantity": 7.158063776666822,
                        "unit": "mg"
                    },
                    "VITK1": {
                        "label": "Vitamin K",
                        "quantity": 159.63881988499062,
                        "unit": "µg"
                    },
                    "WATER": {
                        "label": "Water",
                        "quantity": 967.8587082925071,
                        "unit": "g"
                    }
                },
                "totalDaily": {
                    "ENERC_KCAL": {
                        "label": "Energy",
                        "quantity": 51.349658653338324,
                        "unit": "%"
                    },
                    "FAT": {
                        "label": "Fat",
                        "quantity": 40.09921443717983,
                        "unit": "%"
                    },
                    "FASAT": {
                        "label": "Saturated",
                        "quantity": 24.931689283541807,
                        "unit": "%"
                    },
                    "CHOCDF": {
                        "label": "Carbs",
                        "quantity": 40.44688444445662,
                        "unit": "%"
                    },
                    "FIBTG": {
                        "label": "Fiber",
                        "quantity": 88.32626666666752,
                        "unit": "%"
                    },
                    "PROCNT": {
                        "label": "Protein",
                        "quantity": 175.02673955500185,
                        "unit": "%"
                    },
                    "CHOLE": {
                        "label": "Cholesterol",
                        "quantity": 56.69904625,
                        "unit": "%"
                    },
                    "NA": {
                        "label": "Sodium",
                        "quantity": 117.1907181850657,
                        "unit": "%"
                    },
                    "CA": {
                        "label": "Calcium",
                        "quantity": 32.387306884348476,
                        "unit": "%"
                    },
                    "MG": {
                        "label": "Magnesium",
                        "quantity": 75.05071652738698,
                        "unit": "%"
                    },
                    "K": {
                        "label": "Potassium",
                        "quantity": 62.53622313412136,
                        "unit": "%"
                    },
                    "FE": {
                        "label": "Iron",
                        "quantity": 38.526505198338704,
                        "unit": "%"
                    },
                    "ZN": {
                        "label": "Zinc",
                        "quantity": 46.68342331591402,
                        "unit": "%"
                    },
                    "P": {
                        "label": "Phosphorus",
                        "quantity": 197.98965786905455,
                        "unit": "%"
                    },
                    "VITA_RAE": {
                        "label": "Vitamin A",
                        "quantity": 74.91059259249874,
                        "unit": "%"
                    },
                    "VITC": {
                        "label": "Vitamin C",
                        "quantity": 228.87111111117608,
                        "unit": "%"
                    },
                    "THIA": {
                        "label": "Thiamin (B1)",
                        "quantity": 49.39177670348069,
                        "unit": "%"
                    },
                    "RIBF": {
                        "label": "Riboflavin (B2)",
                        "quantity": 46.8736457557697,
                        "unit": "%"
                    },
                    "NIA": {
                        "label": "Niacin (B3)",
                        "quantity": 123.71259680728907,
                        "unit": "%"
                    },
                    "VITB6A": {
                        "label": "Vitamin B6",
                        "quantity": 136.56777406794703,
                        "unit": "%"
                    },
                    "FOLDFE": {
                        "label": "Folate equivalent (total)",
                        "quantity": 60.025823316676096,
                        "unit": "%"
                    },
                    "VITB12": {
                        "label": "Vitamin B12",
                        "quantity": 223.96123268750003,
                        "unit": "%"
                    },
                    "VITD": {
                        "label": "Vitamin D",
                        "quantity": 70.30681735,
                        "unit": "%"
                    },
                    "TOCPHA": {
                        "label": "Vitamin E",
                        "quantity": 47.720425177778814,
                        "unit": "%"
                    },
                    "VITK1": {
                        "label": "Vitamin K",
                        "quantity": 133.03234990415885,
                        "unit": "%"
                    }
                },
                "digest": [
                    {
                        "label": "Fat",
                        "tag": "FAT",
                        "schemaOrgTag": "fatContent",
                        "total": 26.06448938416689,
                        "hasRDI": True,
                        "daily": 40.09921443717983,
                        "unit": "g",
                        "sub": [
                            {
                                "label": "Saturated",
                                "tag": "FASAT",
                                "schemaOrgTag": "saturatedFatContent",
                                "total": 4.986337856708361,
                                "hasRDI": True,
                                "daily": 24.931689283541807,
                                "unit": "g"
                            },
                            {
                                "label": "Trans",
                                "tag": "FATRN",
                                "schemaOrgTag": "transFatContent",
                                "total": 0.0,
                                "hasRDI": False,
                                "daily": 0.0,
                                "unit": "g"
                            },
                            {
                                "label": "Monounsaturated",
                                "tag": "FAMS",
                                "schemaOrgTag": '',
                                "total": 13.049778835283366,
                                "hasRDI": False,
                                "daily": 0.0,
                                "unit": "g"
                            },
                            {
                                "label": "Polyunsaturated",
                                "tag": "FAPU",
                                "schemaOrgTag": '',
                                "total": 5.877361560658374,
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
                        "total": 121.34065333336986,
                        "hasRDI": True,
                        "daily": 40.44688444445662,
                        "unit": "g",
                        "sub": [
                            {
                                "label": "Carbs (net)",
                                "tag": "CHOCDF.net",
                                "schemaOrgTag": '',
                                "total": 99.25908666670298,
                                "hasRDI": False,
                                "daily": 0.0,
                                "unit": "g"
                            },
                            {
                                "label": "Fiber",
                                "tag": "FIBTG",
                                "schemaOrgTag": "fiberContent",
                                "total": 22.08156666666688,
                                "hasRDI": True,
                                "daily": 88.32626666666752,
                                "unit": "g"
                            },
                            {
                                "label": "Sugars",
                                "tag": "SUGAR",
                                "schemaOrgTag": "sugarContent",
                                "total": 19.228506666670697,
                                "hasRDI": False,
                                "daily": 0.0,
                                "unit": "g"
                            },
                            {
                                "label": "Sugars, added",
                                "tag": "SUGAR.added",
                                "schemaOrgTag": '',
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
                        "total": 87.51336977750091,
                        "hasRDI": True,
                        "daily": 175.02673955500185,
                        "unit": "g"
                    },
                    {
                        "label": "Cholesterol",
                        "tag": "CHOLE",
                        "schemaOrgTag": "cholesterolContent",
                        "total": 170.09713875,
                        "hasRDI": True,
                        "daily": 56.69904625,
                        "unit": "mg"
                    },
                    {
                        "label": "Sodium",
                        "tag": "NA",
                        "schemaOrgTag": "sodiumContent",
                        "total": 2812.577236441577,
                        "hasRDI": True,
                        "daily": 117.1907181850657,
                        "unit": "mg"
                    },
                    {
                        "label": "Calcium",
                        "tag": "CA",
                        "schemaOrgTag": '',
                        "total": 323.87306884348476,
                        "hasRDI": True,
                        "daily": 32.387306884348476,
                        "unit": "mg"
                    },
                    {
                        "label": "Magnesium",
                        "tag": "MG",
                        "schemaOrgTag": '',
                        "total": 315.2130094150253,
                        "hasRDI": True,
                        "daily": 75.05071652738698,
                        "unit": "mg"
                    },
                    {
                        "label": "Potassium",
                        "tag": "K",
                        "schemaOrgTag": '',
                        "total": 2939.2024873037035,
                        "hasRDI": True,
                        "daily": 62.53622313412136,
                        "unit": "mg"
                    },
                    {
                        "label": "Iron",
                        "tag": "FE",
                        "schemaOrgTag": '',
                        "total": 6.934770935700968,
                        "hasRDI": True,
                        "daily": 38.526505198338704,
                        "unit": "mg"
                    },
                    {
                        "label": "Zinc",
                        "tag": "ZN",
                        "schemaOrgTag": '',
                        "total": 5.135176564750542,
                        "hasRDI": True,
                        "daily": 46.68342331591402,
                        "unit": "mg"
                    },
                    {
                        "label": "Phosphorus",
                        "tag": "P",
                        "schemaOrgTag": '',
                        "total": 1385.9276050833819,
                        "hasRDI": True,
                        "daily": 197.98965786905455,
                        "unit": "mg"
                    },
                    {
                        "label": "Vitamin A",
                        "tag": "VITA_RAE",
                        "schemaOrgTag": '',
                        "total": 674.1953333324886,
                        "hasRDI": True,
                        "daily": 74.91059259249874,
                        "unit": "µg"
                    },
                    {
                        "label": "Vitamin C",
                        "tag": "VITC",
                        "schemaOrgTag": '',
                        "total": 205.98400000005847,
                        "hasRDI": True,
                        "daily": 228.87111111117608,
                        "unit": "mg"
                    },
                    {
                        "label": "Thiamin (B1)",
                        "tag": "THIA",
                        "schemaOrgTag": '',
                        "total": 0.5927013204417682,
                        "hasRDI": True,
                        "daily": 49.39177670348069,
                        "unit": "mg"
                    },
                    {
                        "label": "Riboflavin (B2)",
                        "tag": "RIBF",
                        "schemaOrgTag": '',
                        "total": 0.6093573948250062,
                        "hasRDI": True,
                        "daily": 46.8736457557697,
                        "unit": "mg"
                    },
                    {
                        "label": "Niacin (B3)",
                        "tag": "NIA",
                        "schemaOrgTag": '',
                        "total": 19.794015489166252,
                        "hasRDI": True,
                        "daily": 123.71259680728907,
                        "unit": "mg"
                    },
                    {
                        "label": "Vitamin B6",
                        "tag": "VITB6A",
                        "schemaOrgTag": '',
                        "total": 1.7753810628833113,
                        "hasRDI": True,
                        "daily": 136.56777406794703,
                        "unit": "mg"
                    },
                    {
                        "label": "Folate equivalent (total)",
                        "tag": "FOLDFE",
                        "schemaOrgTag": '',
                        "total": 240.10329326670438,
                        "hasRDI": True,
                        "daily": 60.025823316676096,
                        "unit": "µg"
                    },
                    {
                        "label": "Folate (food)",
                        "tag": "FOLFD",
                        "schemaOrgTag": '',
                        "total": 240.10329326670438,
                        "hasRDI": False,
                        "daily": 0.0,
                        "unit": "µg"
                    },
                    {
                        "label": "Folic acid",
                        "tag": "FOLAC",
                        "schemaOrgTag": '',
                        "total": 0.0,
                        "hasRDI": False,
                        "daily": 0.0,
                        "unit": "µg"
                    },
                    {
                        "label": "Vitamin B12",
                        "tag": "VITB12",
                        "schemaOrgTag": '',
                        "total": 5.3750695845,
                        "hasRDI": True,
                        "daily": 223.96123268750003,
                        "unit": "µg"
                    },
                    {
                        "label": "Vitamin D",
                        "tag": "VITD",
                        "schemaOrgTag": '',
                        "total": 10.5460226025,
                        "hasRDI": True,
                        "daily": 70.30681735,
                        "unit": "µg"
                    },
                    {
                        "label": "Vitamin E",
                        "tag": "TOCPHA",
                        "schemaOrgTag": '',
                        "total": 7.158063776666822,
                        "hasRDI": True,
                        "daily": 47.720425177778814,
                        "unit": "mg"
                    },
                    {
                        "label": "Vitamin K",
                        "tag": "VITK1",
                        "schemaOrgTag": '',
                        "total": 159.63881988499062,
                        "hasRDI": True,
                        "daily": 133.03234990415885,
                        "unit": "µg"
                    },
                    {
                        "label": "Sugar alcohols",
                        "tag": "Sugar.alcohol",
                        "schemaOrgTag": '',
                        "total": 0.0,
                        "hasRDI": False,
                        "daily": 0.0,
                        "unit": "g"
                    },
                    {
                        "label": "Water",
                        "tag": "WATER",
                        "schemaOrgTag": '',
                        "total": 967.8587082925071,
                        "hasRDI": False,
                        "daily": 0.0,
                        "unit": "g"
                    }
                ]
            },
            "_links": {
                "self": {
                    "title": "Self",
                    "href": "https://api.edamam.com/api/recipes/v2/48c40a74e2a865a849dde855bcf9fe17?type=public&app_id=e909afd5&app_key=34e59dda7e1bffb92e49c416e9449e1d"
                }
            }
        },
        {
            "recipe": {
                "uri": "http://www.edamam.com/ontologies/edamam.owl#recipe_f2c95859e5746e05a6f0f3b87aa44827",
                "label": "Picadillo Tacos",
                "image": "https://edamam-product-images.s3.amazonaws.com/web-img/1ec/1ec7eb6bbc3f403cbf13e0559e16eac8.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLWVhc3QtMSJIMEYCIQCP2Gbt%2ByPQIVKV%2FafgML7WXbkOusL9fCs6d1le6dFKYAIhAJcnuEh%2B1NzOso38QgGaVBwaVQAMxyMJATg%2FR%2Fl0jl96KsEFCJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMMTg3MDE3MTUwOTg2IgydADkJdybnmhdEGwQqlQUNCCJJEzulouVCRRPPDPN9Ik9nmgPZk%2Fam6u04CTug5FWfzto4W1y6mlAuXr3EHPB%2FvTcZ%2BmAkgcS5%2FRfKsviGgYg1PBDbKvJFWJigqXNb6jHaHO3eyZnXpof0Qk2PachTFyGGF7upzvEiKr6BGB6DtCoEGe3wCd0iFSMS%2Ft8LIlICGGYaaCvWq9TXeaXkel5jju8XxawzfW0OY8ad1NODjiJJ%2FJ02goRzRa3HwZdXj0P4%2FwwiBHg8BMnsBu5XvhNCt9Gz%2Bxp9cZIC8TMv%2FY8rOvepaH28zVl5BjLGle3tn5syTeLiH6OS68I4OndB2qqeqZqdi9cu6zb1H0y8aKh8r8IIaHqXhP6jBXwOxUN8uimNrMJnaDPxNdvFPuR5yx8UApiuserTd1b1ZIBFiBJ6lavYUBrkLW%2B7bZIJltsNTSxF2GTKFWoXHKGf3%2FXYj%2FniRUh%2BB3xUXrXh8PzVKChkdfuCxirnj5UG2XCrj22%2BBJG8S8UHiExHaIwt01Nel6V7Y0IlXWvwqK8YEx%2FHOI%2FewXERfrnIQDCsrQyC7qTLL3HndUW2Ke8ib2iC%2BPgaP6xDqkqdlhOSojQHG4rfwcyVOFOzeauzAO7Rc77mb0rCUJdMckP6nKiD7nrtjlZXznFmYhCvjmWQF2l06Jl7xQsr%2BjkGAeoXo9X%2FiC11ZTNfxOVIe3LWWkRvMwGWvgvtgF4ZEDGaLXgsbO4I8%2FpSmGD4ox9ZWDfX%2BtTURCyBYVXqYpQ4TpgMhHqAtTUr4TNc7GRLVbfi1xqZNQDt1Sfdzh3Xq88dOJyKsyUs7rcFuuxoNyxvqstWVaAyRglOH1n%2BpV0xA7%2FKEHa%2F8%2FzH6uaXeIp3eLJN1%2BGlAQc1sP2jehPHqGi5Lc7YMOKk8akGOrABqEMeyIMA72vRUvaZqcs7N77uX3kDw2%2BTfyF8pS8HYdR1%2BEU1ekEPGlPPLyTo0NFmbmMa4urw%2B19eIvlGSnFjiSeee%2F%2BeotdKLVnDgZ5aNxOYivkgUqjazWNTWX1qdv7Jq7GWrNDLwjZiU5zLvpcjSyzLyGAVIo8pW14m4aC3jppuzjKpasygGK2%2Bf%2BmxisMAkIdRRS5aXW9PY%2FuwiBnL3qiZT5RtAdamISZZM9jUAWY%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231028T003610Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFPXEGMX3T%2F20231028%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=718c64502b5660e69be6e079452e5060c3518eb7833a6b155b13fa5f90fd6d90",
                "images": {
                    "THUMBNAIL": {
                        "url": "https://edamam-product-images.s3.amazonaws.com/web-img/1ec/1ec7eb6bbc3f403cbf13e0559e16eac8-s.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLWVhc3QtMSJIMEYCIQCP2Gbt%2ByPQIVKV%2FafgML7WXbkOusL9fCs6d1le6dFKYAIhAJcnuEh%2B1NzOso38QgGaVBwaVQAMxyMJATg%2FR%2Fl0jl96KsEFCJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMMTg3MDE3MTUwOTg2IgydADkJdybnmhdEGwQqlQUNCCJJEzulouVCRRPPDPN9Ik9nmgPZk%2Fam6u04CTug5FWfzto4W1y6mlAuXr3EHPB%2FvTcZ%2BmAkgcS5%2FRfKsviGgYg1PBDbKvJFWJigqXNb6jHaHO3eyZnXpof0Qk2PachTFyGGF7upzvEiKr6BGB6DtCoEGe3wCd0iFSMS%2Ft8LIlICGGYaaCvWq9TXeaXkel5jju8XxawzfW0OY8ad1NODjiJJ%2FJ02goRzRa3HwZdXj0P4%2FwwiBHg8BMnsBu5XvhNCt9Gz%2Bxp9cZIC8TMv%2FY8rOvepaH28zVl5BjLGle3tn5syTeLiH6OS68I4OndB2qqeqZqdi9cu6zb1H0y8aKh8r8IIaHqXhP6jBXwOxUN8uimNrMJnaDPxNdvFPuR5yx8UApiuserTd1b1ZIBFiBJ6lavYUBrkLW%2B7bZIJltsNTSxF2GTKFWoXHKGf3%2FXYj%2FniRUh%2BB3xUXrXh8PzVKChkdfuCxirnj5UG2XCrj22%2BBJG8S8UHiExHaIwt01Nel6V7Y0IlXWvwqK8YEx%2FHOI%2FewXERfrnIQDCsrQyC7qTLL3HndUW2Ke8ib2iC%2BPgaP6xDqkqdlhOSojQHG4rfwcyVOFOzeauzAO7Rc77mb0rCUJdMckP6nKiD7nrtjlZXznFmYhCvjmWQF2l06Jl7xQsr%2BjkGAeoXo9X%2FiC11ZTNfxOVIe3LWWkRvMwGWvgvtgF4ZEDGaLXgsbO4I8%2FpSmGD4ox9ZWDfX%2BtTURCyBYVXqYpQ4TpgMhHqAtTUr4TNc7GRLVbfi1xqZNQDt1Sfdzh3Xq88dOJyKsyUs7rcFuuxoNyxvqstWVaAyRglOH1n%2BpV0xA7%2FKEHa%2F8%2FzH6uaXeIp3eLJN1%2BGlAQc1sP2jehPHqGi5Lc7YMOKk8akGOrABqEMeyIMA72vRUvaZqcs7N77uX3kDw2%2BTfyF8pS8HYdR1%2BEU1ekEPGlPPLyTo0NFmbmMa4urw%2B19eIvlGSnFjiSeee%2F%2BeotdKLVnDgZ5aNxOYivkgUqjazWNTWX1qdv7Jq7GWrNDLwjZiU5zLvpcjSyzLyGAVIo8pW14m4aC3jppuzjKpasygGK2%2Bf%2BmxisMAkIdRRS5aXW9PY%2FuwiBnL3qiZT5RtAdamISZZM9jUAWY%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231028T003610Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFPXEGMX3T%2F20231028%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=2a8e320aaa3265065b5b8094171389f23d1ffe82167a3e57372f93d0bced1620",
                        "width": 100,
                        "height": 100
                    },
                    "SMALL": {
                        "url": "https://edamam-product-images.s3.amazonaws.com/web-img/1ec/1ec7eb6bbc3f403cbf13e0559e16eac8-m.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLWVhc3QtMSJIMEYCIQCP2Gbt%2ByPQIVKV%2FafgML7WXbkOusL9fCs6d1le6dFKYAIhAJcnuEh%2B1NzOso38QgGaVBwaVQAMxyMJATg%2FR%2Fl0jl96KsEFCJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMMTg3MDE3MTUwOTg2IgydADkJdybnmhdEGwQqlQUNCCJJEzulouVCRRPPDPN9Ik9nmgPZk%2Fam6u04CTug5FWfzto4W1y6mlAuXr3EHPB%2FvTcZ%2BmAkgcS5%2FRfKsviGgYg1PBDbKvJFWJigqXNb6jHaHO3eyZnXpof0Qk2PachTFyGGF7upzvEiKr6BGB6DtCoEGe3wCd0iFSMS%2Ft8LIlICGGYaaCvWq9TXeaXkel5jju8XxawzfW0OY8ad1NODjiJJ%2FJ02goRzRa3HwZdXj0P4%2FwwiBHg8BMnsBu5XvhNCt9Gz%2Bxp9cZIC8TMv%2FY8rOvepaH28zVl5BjLGle3tn5syTeLiH6OS68I4OndB2qqeqZqdi9cu6zb1H0y8aKh8r8IIaHqXhP6jBXwOxUN8uimNrMJnaDPxNdvFPuR5yx8UApiuserTd1b1ZIBFiBJ6lavYUBrkLW%2B7bZIJltsNTSxF2GTKFWoXHKGf3%2FXYj%2FniRUh%2BB3xUXrXh8PzVKChkdfuCxirnj5UG2XCrj22%2BBJG8S8UHiExHaIwt01Nel6V7Y0IlXWvwqK8YEx%2FHOI%2FewXERfrnIQDCsrQyC7qTLL3HndUW2Ke8ib2iC%2BPgaP6xDqkqdlhOSojQHG4rfwcyVOFOzeauzAO7Rc77mb0rCUJdMckP6nKiD7nrtjlZXznFmYhCvjmWQF2l06Jl7xQsr%2BjkGAeoXo9X%2FiC11ZTNfxOVIe3LWWkRvMwGWvgvtgF4ZEDGaLXgsbO4I8%2FpSmGD4ox9ZWDfX%2BtTURCyBYVXqYpQ4TpgMhHqAtTUr4TNc7GRLVbfi1xqZNQDt1Sfdzh3Xq88dOJyKsyUs7rcFuuxoNyxvqstWVaAyRglOH1n%2BpV0xA7%2FKEHa%2F8%2FzH6uaXeIp3eLJN1%2BGlAQc1sP2jehPHqGi5Lc7YMOKk8akGOrABqEMeyIMA72vRUvaZqcs7N77uX3kDw2%2BTfyF8pS8HYdR1%2BEU1ekEPGlPPLyTo0NFmbmMa4urw%2B19eIvlGSnFjiSeee%2F%2BeotdKLVnDgZ5aNxOYivkgUqjazWNTWX1qdv7Jq7GWrNDLwjZiU5zLvpcjSyzLyGAVIo8pW14m4aC3jppuzjKpasygGK2%2Bf%2BmxisMAkIdRRS5aXW9PY%2FuwiBnL3qiZT5RtAdamISZZM9jUAWY%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231028T003610Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFPXEGMX3T%2F20231028%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=7f83d8cd075afa6dfdaa15526b2942141a62f156f0e503b61013d7165deb23de",
                        "width": 200,
                        "height": 200
                    },
                    "REGULAR": {
                        "url": "https://edamam-product-images.s3.amazonaws.com/web-img/1ec/1ec7eb6bbc3f403cbf13e0559e16eac8.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLWVhc3QtMSJIMEYCIQCP2Gbt%2ByPQIVKV%2FafgML7WXbkOusL9fCs6d1le6dFKYAIhAJcnuEh%2B1NzOso38QgGaVBwaVQAMxyMJATg%2FR%2Fl0jl96KsEFCJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMMTg3MDE3MTUwOTg2IgydADkJdybnmhdEGwQqlQUNCCJJEzulouVCRRPPDPN9Ik9nmgPZk%2Fam6u04CTug5FWfzto4W1y6mlAuXr3EHPB%2FvTcZ%2BmAkgcS5%2FRfKsviGgYg1PBDbKvJFWJigqXNb6jHaHO3eyZnXpof0Qk2PachTFyGGF7upzvEiKr6BGB6DtCoEGe3wCd0iFSMS%2Ft8LIlICGGYaaCvWq9TXeaXkel5jju8XxawzfW0OY8ad1NODjiJJ%2FJ02goRzRa3HwZdXj0P4%2FwwiBHg8BMnsBu5XvhNCt9Gz%2Bxp9cZIC8TMv%2FY8rOvepaH28zVl5BjLGle3tn5syTeLiH6OS68I4OndB2qqeqZqdi9cu6zb1H0y8aKh8r8IIaHqXhP6jBXwOxUN8uimNrMJnaDPxNdvFPuR5yx8UApiuserTd1b1ZIBFiBJ6lavYUBrkLW%2B7bZIJltsNTSxF2GTKFWoXHKGf3%2FXYj%2FniRUh%2BB3xUXrXh8PzVKChkdfuCxirnj5UG2XCrj22%2BBJG8S8UHiExHaIwt01Nel6V7Y0IlXWvwqK8YEx%2FHOI%2FewXERfrnIQDCsrQyC7qTLL3HndUW2Ke8ib2iC%2BPgaP6xDqkqdlhOSojQHG4rfwcyVOFOzeauzAO7Rc77mb0rCUJdMckP6nKiD7nrtjlZXznFmYhCvjmWQF2l06Jl7xQsr%2BjkGAeoXo9X%2FiC11ZTNfxOVIe3LWWkRvMwGWvgvtgF4ZEDGaLXgsbO4I8%2FpSmGD4ox9ZWDfX%2BtTURCyBYVXqYpQ4TpgMhHqAtTUr4TNc7GRLVbfi1xqZNQDt1Sfdzh3Xq88dOJyKsyUs7rcFuuxoNyxvqstWVaAyRglOH1n%2BpV0xA7%2FKEHa%2F8%2FzH6uaXeIp3eLJN1%2BGlAQc1sP2jehPHqGi5Lc7YMOKk8akGOrABqEMeyIMA72vRUvaZqcs7N77uX3kDw2%2BTfyF8pS8HYdR1%2BEU1ekEPGlPPLyTo0NFmbmMa4urw%2B19eIvlGSnFjiSeee%2F%2BeotdKLVnDgZ5aNxOYivkgUqjazWNTWX1qdv7Jq7GWrNDLwjZiU5zLvpcjSyzLyGAVIo8pW14m4aC3jppuzjKpasygGK2%2Bf%2BmxisMAkIdRRS5aXW9PY%2FuwiBnL3qiZT5RtAdamISZZM9jUAWY%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231028T003610Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFPXEGMX3T%2F20231028%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=718c64502b5660e69be6e079452e5060c3518eb7833a6b155b13fa5f90fd6d90",
                        "width": 300,
                        "height": 300
                    }
                },
                "source": "My Recipes",
                "url": "http://www.myrecipes.com/recipe/picadillo-tacos",
                "shareAs": "http://www.edamam.com/recipe/picadillo-tacos-f2c95859e5746e05a6f0f3b87aa44827/tacos",
                "yield": 8.0,
                "dietLabels": [],
                "healthLabels": [
                    "Sugar-Conscious",
                    "Dairy-Free",
                    "Egg-Free",
                    "Peanut-Free",
                    "Tree-Nut-Free",
                    "Soy-Free",
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
                    "Sulfite-Free",
                    "Kosher"
                ],
                "cautions": [
                    "Eggs",
                    "Milk"
                ],
                "ingredientLines": [
                    "1 pound ground round",
                    "1 tablespoon vegetable oil",
                    "2 carrots, diced",
                    "1 small onion, diced",
                    "1/2 teaspoon salt",
                    "2 plum tomatoes, diced",
                    "1 to 2 canned chipotle peppers in adobo sauce, minced",
                    "8 (8-inch) soft taco-size corn or flour tortillas, warmed",
                    "Garnish: fresh cilantro sprigs"
                ],
                "ingredients": [
                    {
                        "text": "1 pound ground round",
                        "quantity": 1.0,
                        "measure": "pound",
                        "food": "ground round",
                        "weight": 453.59237,
                        "foodCategory": "meats",
                        "foodId": "food_boq91pbbhklr6sb0d9sbybzgklkm",
                        "image": "https://www.edamam.com/food-img/cfa/cfae8f9276eaf8f0d9349ba662744a0c.jpg"
                    },
                    {
                        "text": "1 tablespoon vegetable oil",
                        "quantity": 1.0,
                        "measure": "tablespoon",
                        "food": "vegetable oil",
                        "weight": 14.0,
                        "foodCategory": "Oils",
                        "foodId": "food_bt1mzi2ah2sfg8bv7no1qai83w8s",
                        "image": "https://www.edamam.com/food-img/6e5/6e51a63a6300a8ea1b4c4cc68dfaba33.jpg"
                    },
                    {
                        "text": "2 carrots, diced",
                        "quantity": 2.0,
                        "measure": "<unit>",
                        "food": "carrots",
                        "weight": 122.0,
                        "foodCategory": "vegetables",
                        "foodId": "food_ai215e5b85pdh5ajd4aafa3w2zm8",
                        "image": "https://www.edamam.com/food-img/121/121e33fce0bb9546ed7d060b6c114e29.jpg"
                    },
                    {
                        "text": "1 small onion, diced",
                        "quantity": 1.0,
                        "measure": "<unit>",
                        "food": "onion",
                        "weight": 70.0,
                        "foodCategory": "vegetables",
                        "foodId": "food_bmrvi4ob4binw9a5m7l07amlfcoy",
                        "image": "https://www.edamam.com/food-img/205/205e6bf2399b85d34741892ef91cc603.jpg"
                    },
                    {
                        "text": "1/2 teaspoon salt",
                        "quantity": 0.5,
                        "measure": "teaspoon",
                        "food": "salt",
                        "weight": 3.0,
                        "foodCategory": "Condiments and sauces",
                        "foodId": "food_btxz81db72hwbra2pncvebzzzum9",
                        "image": "https://www.edamam.com/food-img/694/6943ea510918c6025795e8dc6e6eaaeb.jpg"
                    },
                    {
                        "text": "2 plum tomatoes, diced",
                        "quantity": 2.0,
                        "measure": "<unit>",
                        "food": "plum tomatoes",
                        "weight": 124.0,
                        "foodCategory": "vegetables",
                        "foodId": "food_ab8jymba5i5xv3apgymg7a90bxb5",
                        "image": "https://www.edamam.com/food-img/23e/23e727a14f1035bdc2733bb0477efbd2.jpg"
                    },
                    {
                        "text": "1 to 2 canned chipotle peppers in adobo sauce, minced",
                        "quantity": 1.5,
                        "measure": "<unit>",
                        "food": "chipotle peppers in adobo",
                        "weight": 109.5,
                        "foodCategory": "canned vegetables",
                        "foodId": "food_bumzpysb5k05cibmscqp2a0fwgpa",
                        "image": "https://www.edamam.com/food-img/c34/c343c40fbfe50bd72bbb3890c83a4315.jpeg"
                    },
                    {
                        "text": "8 (8-inch) soft taco-size corn or flour tortillas, warmed",
                        "quantity": 8.0,
                        "measure": "<unit>",
                        "food": "corn or flour tortillas",
                        "weight": 192.0,
                        "foodCategory": "quick breads and pastries",
                        "foodId": "food_bhw0b95agm97s0abfignnb8fsvb3",
                        "image": "https://www.edamam.com/food-img/b8a/b8ad23dcc06f2324f944e47eb579d644.jpg"
                    },
                    {
                        "text": "Garnish: fresh cilantro sprigs",
                        "quantity": 1.0,
                        "measure": "sprig",
                        "food": "cilantro",
                        "weight": 2.2222222222222223,
                        "foodCategory": "vegetables",
                        "foodId": "food_alhzhuwb4lc7jnb5s6f02by60bzp",
                        "image": "https://www.edamam.com/food-img/d57/d57e375b6ff99a90c7ee2b1990a1af36.jpg"
                    }
                ],
                "calories": 1818.290730911111,
                "totalCO2Emissions": 46060.376866151346,
                "co2EmissionsClass": "G",
                "totalWeight": 1089.2924405508272,
                "totalTime": 0.0,
                "cuisineType": [
                    "mexican"
                ],
                "mealType": [
                    "lunch/dinner"
                ],
                "dishType": [
                    "sandwiches"
                ],
                "totalNutrients": {
                    "ENERC_KCAL": {
                        "label": "Energy",
                        "quantity": 1818.290730911111,
                        "unit": "kcal"
                    },
                    "FAT": {
                        "label": "Fat",
                        "quantity": 110.92232955555556,
                        "unit": "g"
                    },
                    "FASAT": {
                        "label": "Saturated",
                        "quantity": 36.277882757111115,
                        "unit": "g"
                    },
                    "FATRN": {
                        "label": "Trans",
                        "quantity": 5.4597699660000005,
                        "unit": "g"
                    },
                    "FAMS": {
                        "label": "Monounsaturated",
                        "quantity": 51.62642585611111,
                        "unit": "g"
                    },
                    "FAPU": {
                        "label": "Polyunsaturated",
                        "quantity": 7.783990136588889,
                        "unit": "g"
                    },
                    "CHOCDF": {
                        "label": "Carbs",
                        "quantity": 114.34725555555556,
                        "unit": "g"
                    },
                    "CHOCDF.net": {
                        "label": "Carbohydrates (net)",
                        "quantity": 94.67153333333334,
                        "unit": "g"
                    },
                    "FIBTG": {
                        "label": "Fiber",
                        "quantity": 19.67572222222222,
                        "unit": "g"
                    },
                    "SUGAR": {
                        "label": "Sugars",
                        "quantity": 17.356333333333332,
                        "unit": "g"
                    },
                    "PROCNT": {
                        "label": "Protein",
                        "quantity": 92.99052097333335,
                        "unit": "g"
                    },
                    "CHOLE": {
                        "label": "Cholesterol",
                        "quantity": 322.05058270000006,
                        "unit": "mg"
                    },
                    "NA": {
                        "label": "Sodium",
                        "quantity": 2528.528337920934,
                        "unit": "mg"
                    },
                    "CA": {
                        "label": "Calcium",
                        "quantity": 315.55519908775403,
                        "unit": "mg"
                    },
                    "MG": {
                        "label": "Magnesium",
                        "quantity": 266.55825916106386,
                        "unit": "mg"
                    },
                    "K": {
                        "label": "Potassium",
                        "quantity": 2584.800404644066,
                        "unit": "mg"
                    },
                    "FE": {
                        "label": "Iron",
                        "quantity": 12.602452210817727,
                        "unit": "mg"
                    },
                    "ZN": {
                        "label": "Zinc",
                        "quantity": 22.297200025439718,
                        "unit": "mg"
                    },
                    "P": {
                        "label": "Phosphorus",
                        "quantity": 1431.9976112666668,
                        "unit": "mg"
                    },
                    "VITA_RAE": {
                        "label": "Vitamin A",
                        "quantity": 1747.9375836888887,
                        "unit": "µg"
                    },
                    "VITC": {
                        "label": "Vitamin C",
                        "quantity": 104.42599999999999,
                        "unit": "mg"
                    },
                    "THIA": {
                        "label": "Thiamin (B1)",
                        "quantity": 0.5575136079888888,
                        "unit": "mg"
                    },
                    "RIBF": {
                        "label": "Riboflavin (B2)",
                        "quantity": 0.9812944787000002,
                        "unit": "mg"
                    },
                    "NIA": {
                        "label": "Niacin (B3)",
                        "quantity": 24.98464391766667,
                        "unit": "mg"
                    },
                    "VITB6A": {
                        "label": "Vitamin B6",
                        "quantity": 2.407989466211111,
                        "unit": "mg"
                    },
                    "FOLDFE": {
                        "label": "Folate equivalent (total)",
                        "quantity": 108.75924367777779,
                        "unit": "µg"
                    },
                    "FOLFD": {
                        "label": "Folate (food)",
                        "quantity": 108.75924367777779,
                        "unit": "µg"
                    },
                    "FOLAC": {
                        "label": "Folic acid",
                        "quantity": 0.0,
                        "unit": "µg"
                    },
                    "VITB12": {
                        "label": "Vitamin B12",
                        "quantity": 9.706876718000002,
                        "unit": "µg"
                    },
                    "VITD": {
                        "label": "Vitamin D",
                        "quantity": 0.4535923700000001,
                        "unit": "µg"
                    },
                    "TOCPHA": {
                        "label": "Vitamin E",
                        "quantity": 6.660612584555557,
                        "unit": "mg"
                    },
                    "VITK1": {
                        "label": "Vitamin K",
                        "quantity": 50.760051548888896,
                        "unit": "µg"
                    },
                    "WATER": {
                        "label": "Water",
                        "quantity": 759.5180216155462,
                        "unit": "g"
                    }
                },
                "totalDaily": {
                    "ENERC_KCAL": {
                        "label": "Energy",
                        "quantity": 90.91453654555556,
                        "unit": "%"
                    },
                    "FAT": {
                        "label": "Fat",
                        "quantity": 170.6497377777778,
                        "unit": "%"
                    },
                    "FASAT": {
                        "label": "Saturated",
                        "quantity": 181.38941378555558,
                        "unit": "%"
                    },
                    "CHOCDF": {
                        "label": "Carbs",
                        "quantity": 38.115751851851854,
                        "unit": "%"
                    },
                    "FIBTG": {
                        "label": "Fiber",
                        "quantity": 78.70288888888888,
                        "unit": "%"
                    },
                    "PROCNT": {
                        "label": "Protein",
                        "quantity": 185.9810419466667,
                        "unit": "%"
                    },
                    "CHOLE": {
                        "label": "Cholesterol",
                        "quantity": 107.35019423333335,
                        "unit": "%"
                    },
                    "NA": {
                        "label": "Sodium",
                        "quantity": 105.35534741337226,
                        "unit": "%"
                    },
                    "CA": {
                        "label": "Calcium",
                        "quantity": 31.555519908775405,
                        "unit": "%"
                    },
                    "MG": {
                        "label": "Magnesium",
                        "quantity": 63.46625218120568,
                        "unit": "%"
                    },
                    "K": {
                        "label": "Potassium",
                        "quantity": 54.99575329029928,
                        "unit": "%"
                    },
                    "FE": {
                        "label": "Iron",
                        "quantity": 70.01362339343183,
                        "unit": "%"
                    },
                    "ZN": {
                        "label": "Zinc",
                        "quantity": 202.70181841308838,
                        "unit": "%"
                    },
                    "P": {
                        "label": "Phosphorus",
                        "quantity": 204.57108732380954,
                        "unit": "%"
                    },
                    "VITA_RAE": {
                        "label": "Vitamin A",
                        "quantity": 194.21528707654318,
                        "unit": "%"
                    },
                    "VITC": {
                        "label": "Vitamin C",
                        "quantity": 116.02888888888887,
                        "unit": "%"
                    },
                    "THIA": {
                        "label": "Thiamin (B1)",
                        "quantity": 46.45946733240741,
                        "unit": "%"
                    },
                    "RIBF": {
                        "label": "Riboflavin (B2)",
                        "quantity": 75.48419066923078,
                        "unit": "%"
                    },
                    "NIA": {
                        "label": "Niacin (B3)",
                        "quantity": 156.1540244854167,
                        "unit": "%"
                    },
                    "VITB6A": {
                        "label": "Vitamin B6",
                        "quantity": 185.22995893931625,
                        "unit": "%"
                    },
                    "FOLDFE": {
                        "label": "Folate equivalent (total)",
                        "quantity": 27.189810919444447,
                        "unit": "%"
                    },
                    "VITB12": {
                        "label": "Vitamin B12",
                        "quantity": 404.4531965833334,
                        "unit": "%"
                    },
                    "VITD": {
                        "label": "Vitamin D",
                        "quantity": 3.0239491333333337,
                        "unit": "%"
                    },
                    "TOCPHA": {
                        "label": "Vitamin E",
                        "quantity": 44.40408389703705,
                        "unit": "%"
                    },
                    "VITK1": {
                        "label": "Vitamin K",
                        "quantity": 42.30004295740741,
                        "unit": "%"
                    }
                },
                "digest": [
                    {
                        "label": "Fat",
                        "tag": "FAT",
                        "schemaOrgTag": "fatContent",
                        "total": 110.92232955555556,
                        "hasRDI": True,
                        "daily": 170.6497377777778,
                        "unit": "g",
                        "sub": [
                            {
                                "label": "Saturated",
                                "tag": "FASAT",
                                "schemaOrgTag": "saturatedFatContent",
                                "total": 36.277882757111115,
                                "hasRDI": True,
                                "daily": 181.38941378555558,
                                "unit": "g"
                            },
                            {
                                "label": "Trans",
                                "tag": "FATRN",
                                "schemaOrgTag": "transFatContent",
                                "total": 5.4597699660000005,
                                "hasRDI": False,
                                "daily": 0.0,
                                "unit": "g"
                            },
                            {
                                "label": "Monounsaturated",
                                "tag": "FAMS",
                                "schemaOrgTag": '',
                                "total": 51.62642585611111,
                                "hasRDI": False,
                                "daily": 0.0,
                                "unit": "g"
                            },
                            {
                                "label": "Polyunsaturated",
                                "tag": "FAPU",
                                "schemaOrgTag": '',
                                "total": 7.783990136588889,
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
                        "total": 114.34725555555556,
                        "hasRDI": True,
                        "daily": 38.115751851851854,
                        "unit": "g",
                        "sub": [
                            {
                                "label": "Carbs (net)",
                                "tag": "CHOCDF.net",
                                "schemaOrgTag": '',
                                "total": 94.67153333333334,
                                "hasRDI": False,
                                "daily": 0.0,
                                "unit": "g"
                            },
                            {
                                "label": "Fiber",
                                "tag": "FIBTG",
                                "schemaOrgTag": "fiberContent",
                                "total": 19.67572222222222,
                                "hasRDI": True,
                                "daily": 78.70288888888888,
                                "unit": "g"
                            },
                            {
                                "label": "Sugars",
                                "tag": "SUGAR",
                                "schemaOrgTag": "sugarContent",
                                "total": 17.356333333333332,
                                "hasRDI": False,
                                "daily": 0.0,
                                "unit": "g"
                            },
                            {
                                "label": "Sugars, added",
                                "tag": "SUGAR.added",
                                "schemaOrgTag": '',
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
                        "total": 92.99052097333335,
                        "hasRDI": True,
                        "daily": 185.9810419466667,
                        "unit": "g"
                    },
                    {
                        "label": "Cholesterol",
                        "tag": "CHOLE",
                        "schemaOrgTag": "cholesterolContent",
                        "total": 322.05058270000006,
                        "hasRDI": True,
                        "daily": 107.35019423333335,
                        "unit": "mg"
                    },
                    {
                        "label": "Sodium",
                        "tag": "NA",
                        "schemaOrgTag": "sodiumContent",
                        "total": 2528.528337920934,
                        "hasRDI": True,
                        "daily": 105.35534741337226,
                        "unit": "mg"
                    },
                    {
                        "label": "Calcium",
                        "tag": "CA",
                        "schemaOrgTag": '',
                        "total": 315.55519908775403,
                        "hasRDI": True,
                        "daily": 31.555519908775405,
                        "unit": "mg"
                    },
                    {
                        "label": "Magnesium",
                        "tag": "MG",
                        "schemaOrgTag": '',
                        "total": 266.55825916106386,
                        "hasRDI": True,
                        "daily": 63.46625218120568,
                        "unit": "mg"
                    },
                    {
                        "label": "Potassium",
                        "tag": "K",
                        "schemaOrgTag": '',
                        "total": 2584.800404644066,
                        "hasRDI": True,
                        "daily": 54.99575329029928,
                        "unit": "mg"
                    },
                    {
                        "label": "Iron",
                        "tag": "FE",
                        "schemaOrgTag": '',
                        "total": 12.602452210817727,
                        "hasRDI": True,
                        "daily": 70.01362339343183,
                        "unit": "mg"
                    },
                    {
                        "label": "Zinc",
                        "tag": "ZN",
                        "schemaOrgTag": '',
                        "total": 22.297200025439718,
                        "hasRDI": True,
                        "daily": 202.70181841308838,
                        "unit": "mg"
                    },
                    {
                        "label": "Phosphorus",
                        "tag": "P",
                        "schemaOrgTag": '',
                        "total": 1431.9976112666668,
                        "hasRDI": True,
                        "daily": 204.57108732380954,
                        "unit": "mg"
                    },
                    {
                        "label": "Vitamin A",
                        "tag": "VITA_RAE",
                        "schemaOrgTag": '',
                        "total": 1747.9375836888887,
                        "hasRDI": True,
                        "daily": 194.21528707654318,
                        "unit": "µg"
                    },
                    {
                        "label": "Vitamin C",
                        "tag": "VITC",
                        "schemaOrgTag": '',
                        "total": 104.42599999999999,
                        "hasRDI": True,
                        "daily": 116.02888888888887,
                        "unit": "mg"
                    },
                    {
                        "label": "Thiamin (B1)",
                        "tag": "THIA",
                        "schemaOrgTag": '',
                        "total": 0.5575136079888888,
                        "hasRDI": True,
                        "daily": 46.45946733240741,
                        "unit": "mg"
                    },
                    {
                        "label": "Riboflavin (B2)",
                        "tag": "RIBF",
                        "schemaOrgTag": '',
                        "total": 0.9812944787000002,
                        "hasRDI": True,
                        "daily": 75.48419066923078,
                        "unit": "mg"
                    },
                    {
                        "label": "Niacin (B3)",
                        "tag": "NIA",
                        "schemaOrgTag": '',
                        "total": 24.98464391766667,
                        "hasRDI": True,
                        "daily": 156.1540244854167,
                        "unit": "mg"
                    },
                    {
                        "label": "Vitamin B6",
                        "tag": "VITB6A",
                        "schemaOrgTag": '',
                        "total": 2.407989466211111,
                        "hasRDI": True,
                        "daily": 185.22995893931625,
                        "unit": "mg"
                    },
                    {
                        "label": "Folate equivalent (total)",
                        "tag": "FOLDFE",
                        "schemaOrgTag": '',
                        "total": 108.75924367777779,
                        "hasRDI": True,
                        "daily": 27.189810919444447,
                        "unit": "µg"
                    },
                    {
                        "label": "Folate (food)",
                        "tag": "FOLFD",
                        "schemaOrgTag": '',
                        "total": 108.75924367777779,
                        "hasRDI": False,
                        "daily": 0.0,
                        "unit": "µg"
                    },
                    {
                        "label": "Folic acid",
                        "tag": "FOLAC",
                        "schemaOrgTag": '',
                        "total": 0.0,
                        "hasRDI": False,
                        "daily": 0.0,
                        "unit": "µg"
                    },
                    {
                        "label": "Vitamin B12",
                        "tag": "VITB12",
                        "schemaOrgTag": '',
                        "total": 9.706876718000002,
                        "hasRDI": True,
                        "daily": 404.4531965833334,
                        "unit": "µg"
                    },
                    {
                        "label": "Vitamin D",
                        "tag": "VITD",
                        "schemaOrgTag": '',
                        "total": 0.4535923700000001,
                        "hasRDI": True,
                        "daily": 3.0239491333333337,
                        "unit": "µg"
                    },
                    {
                        "label": "Vitamin E",
                        "tag": "TOCPHA",
                        "schemaOrgTag": '',
                        "total": 6.660612584555557,
                        "hasRDI": True,
                        "daily": 44.40408389703705,
                        "unit": "mg"
                    },
                    {
                        "label": "Vitamin K",
                        "tag": "VITK1",
                        "schemaOrgTag": '',
                        "total": 50.760051548888896,
                        "hasRDI": True,
                        "daily": 42.30004295740741,
                        "unit": "µg"
                    },
                    {
                        "label": "Sugar alcohols",
                        "tag": "Sugar.alcohol",
                        "schemaOrgTag": '',
                        "total": 0.0,
                        "hasRDI": False,
                        "daily": 0.0,
                        "unit": "g"
                    },
                    {
                        "label": "Water",
                        "tag": "WATER",
                        "schemaOrgTag": '',
                        "total": 759.5180216155462,
                        "hasRDI": False,
                        "daily": 0.0,
                        "unit": "g"
                    }
                ]
            },
            "_links": {
                "self": {
                    "title": "Self",
                    "href": "https://api.edamam.com/api/recipes/v2/f2c95859e5746e05a6f0f3b87aa44827?type=public&app_id=e909afd5&app_key=34e59dda7e1bffb92e49c416e9449e1d"
                }
            }
        },
        {
            "recipe": {
                "uri": "http://www.edamam.com/ontologies/edamam.owl#recipe_d6d4673c3d725197da7ef0ece3993daf",
                "label": "Quick Beef Tacos",
                "image": "https://edamam-product-images.s3.amazonaws.com/web-img/0dd/0dd087a50dcc84d9b5abb3e66f6c2d29.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLWVhc3QtMSJIMEYCIQCP2Gbt%2ByPQIVKV%2FafgML7WXbkOusL9fCs6d1le6dFKYAIhAJcnuEh%2B1NzOso38QgGaVBwaVQAMxyMJATg%2FR%2Fl0jl96KsEFCJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMMTg3MDE3MTUwOTg2IgydADkJdybnmhdEGwQqlQUNCCJJEzulouVCRRPPDPN9Ik9nmgPZk%2Fam6u04CTug5FWfzto4W1y6mlAuXr3EHPB%2FvTcZ%2BmAkgcS5%2FRfKsviGgYg1PBDbKvJFWJigqXNb6jHaHO3eyZnXpof0Qk2PachTFyGGF7upzvEiKr6BGB6DtCoEGe3wCd0iFSMS%2Ft8LIlICGGYaaCvWq9TXeaXkel5jju8XxawzfW0OY8ad1NODjiJJ%2FJ02goRzRa3HwZdXj0P4%2FwwiBHg8BMnsBu5XvhNCt9Gz%2Bxp9cZIC8TMv%2FY8rOvepaH28zVl5BjLGle3tn5syTeLiH6OS68I4OndB2qqeqZqdi9cu6zb1H0y8aKh8r8IIaHqXhP6jBXwOxUN8uimNrMJnaDPxNdvFPuR5yx8UApiuserTd1b1ZIBFiBJ6lavYUBrkLW%2B7bZIJltsNTSxF2GTKFWoXHKGf3%2FXYj%2FniRUh%2BB3xUXrXh8PzVKChkdfuCxirnj5UG2XCrj22%2BBJG8S8UHiExHaIwt01Nel6V7Y0IlXWvwqK8YEx%2FHOI%2FewXERfrnIQDCsrQyC7qTLL3HndUW2Ke8ib2iC%2BPgaP6xDqkqdlhOSojQHG4rfwcyVOFOzeauzAO7Rc77mb0rCUJdMckP6nKiD7nrtjlZXznFmYhCvjmWQF2l06Jl7xQsr%2BjkGAeoXo9X%2FiC11ZTNfxOVIe3LWWkRvMwGWvgvtgF4ZEDGaLXgsbO4I8%2FpSmGD4ox9ZWDfX%2BtTURCyBYVXqYpQ4TpgMhHqAtTUr4TNc7GRLVbfi1xqZNQDt1Sfdzh3Xq88dOJyKsyUs7rcFuuxoNyxvqstWVaAyRglOH1n%2BpV0xA7%2FKEHa%2F8%2FzH6uaXeIp3eLJN1%2BGlAQc1sP2jehPHqGi5Lc7YMOKk8akGOrABqEMeyIMA72vRUvaZqcs7N77uX3kDw2%2BTfyF8pS8HYdR1%2BEU1ekEPGlPPLyTo0NFmbmMa4urw%2B19eIvlGSnFjiSeee%2F%2BeotdKLVnDgZ5aNxOYivkgUqjazWNTWX1qdv7Jq7GWrNDLwjZiU5zLvpcjSyzLyGAVIo8pW14m4aC3jppuzjKpasygGK2%2Bf%2BmxisMAkIdRRS5aXW9PY%2FuwiBnL3qiZT5RtAdamISZZM9jUAWY%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231028T003610Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFPXEGMX3T%2F20231028%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=cbe499cd048a72453361a9d697f7df91e13c2ffe83ac48de3646e240b6e28968",
                "images": {
                    "THUMBNAIL": {
                        "url": "https://edamam-product-images.s3.amazonaws.com/web-img/0dd/0dd087a50dcc84d9b5abb3e66f6c2d29-s.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLWVhc3QtMSJIMEYCIQCP2Gbt%2ByPQIVKV%2FafgML7WXbkOusL9fCs6d1le6dFKYAIhAJcnuEh%2B1NzOso38QgGaVBwaVQAMxyMJATg%2FR%2Fl0jl96KsEFCJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMMTg3MDE3MTUwOTg2IgydADkJdybnmhdEGwQqlQUNCCJJEzulouVCRRPPDPN9Ik9nmgPZk%2Fam6u04CTug5FWfzto4W1y6mlAuXr3EHPB%2FvTcZ%2BmAkgcS5%2FRfKsviGgYg1PBDbKvJFWJigqXNb6jHaHO3eyZnXpof0Qk2PachTFyGGF7upzvEiKr6BGB6DtCoEGe3wCd0iFSMS%2Ft8LIlICGGYaaCvWq9TXeaXkel5jju8XxawzfW0OY8ad1NODjiJJ%2FJ02goRzRa3HwZdXj0P4%2FwwiBHg8BMnsBu5XvhNCt9Gz%2Bxp9cZIC8TMv%2FY8rOvepaH28zVl5BjLGle3tn5syTeLiH6OS68I4OndB2qqeqZqdi9cu6zb1H0y8aKh8r8IIaHqXhP6jBXwOxUN8uimNrMJnaDPxNdvFPuR5yx8UApiuserTd1b1ZIBFiBJ6lavYUBrkLW%2B7bZIJltsNTSxF2GTKFWoXHKGf3%2FXYj%2FniRUh%2BB3xUXrXh8PzVKChkdfuCxirnj5UG2XCrj22%2BBJG8S8UHiExHaIwt01Nel6V7Y0IlXWvwqK8YEx%2FHOI%2FewXERfrnIQDCsrQyC7qTLL3HndUW2Ke8ib2iC%2BPgaP6xDqkqdlhOSojQHG4rfwcyVOFOzeauzAO7Rc77mb0rCUJdMckP6nKiD7nrtjlZXznFmYhCvjmWQF2l06Jl7xQsr%2BjkGAeoXo9X%2FiC11ZTNfxOVIe3LWWkRvMwGWvgvtgF4ZEDGaLXgsbO4I8%2FpSmGD4ox9ZWDfX%2BtTURCyBYVXqYpQ4TpgMhHqAtTUr4TNc7GRLVbfi1xqZNQDt1Sfdzh3Xq88dOJyKsyUs7rcFuuxoNyxvqstWVaAyRglOH1n%2BpV0xA7%2FKEHa%2F8%2FzH6uaXeIp3eLJN1%2BGlAQc1sP2jehPHqGi5Lc7YMOKk8akGOrABqEMeyIMA72vRUvaZqcs7N77uX3kDw2%2BTfyF8pS8HYdR1%2BEU1ekEPGlPPLyTo0NFmbmMa4urw%2B19eIvlGSnFjiSeee%2F%2BeotdKLVnDgZ5aNxOYivkgUqjazWNTWX1qdv7Jq7GWrNDLwjZiU5zLvpcjSyzLyGAVIo8pW14m4aC3jppuzjKpasygGK2%2Bf%2BmxisMAkIdRRS5aXW9PY%2FuwiBnL3qiZT5RtAdamISZZM9jUAWY%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231028T003610Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFPXEGMX3T%2F20231028%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=7f8a1cab9ad865dd97edc49ff5395ebb6fc29adbd7fa25fd78c7b4a4ba3c307e",
                        "width": 100,
                        "height": 100
                    },
                    "SMALL": {
                        "url": "https://edamam-product-images.s3.amazonaws.com/web-img/0dd/0dd087a50dcc84d9b5abb3e66f6c2d29-m.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLWVhc3QtMSJIMEYCIQCP2Gbt%2ByPQIVKV%2FafgML7WXbkOusL9fCs6d1le6dFKYAIhAJcnuEh%2B1NzOso38QgGaVBwaVQAMxyMJATg%2FR%2Fl0jl96KsEFCJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMMTg3MDE3MTUwOTg2IgydADkJdybnmhdEGwQqlQUNCCJJEzulouVCRRPPDPN9Ik9nmgPZk%2Fam6u04CTug5FWfzto4W1y6mlAuXr3EHPB%2FvTcZ%2BmAkgcS5%2FRfKsviGgYg1PBDbKvJFWJigqXNb6jHaHO3eyZnXpof0Qk2PachTFyGGF7upzvEiKr6BGB6DtCoEGe3wCd0iFSMS%2Ft8LIlICGGYaaCvWq9TXeaXkel5jju8XxawzfW0OY8ad1NODjiJJ%2FJ02goRzRa3HwZdXj0P4%2FwwiBHg8BMnsBu5XvhNCt9Gz%2Bxp9cZIC8TMv%2FY8rOvepaH28zVl5BjLGle3tn5syTeLiH6OS68I4OndB2qqeqZqdi9cu6zb1H0y8aKh8r8IIaHqXhP6jBXwOxUN8uimNrMJnaDPxNdvFPuR5yx8UApiuserTd1b1ZIBFiBJ6lavYUBrkLW%2B7bZIJltsNTSxF2GTKFWoXHKGf3%2FXYj%2FniRUh%2BB3xUXrXh8PzVKChkdfuCxirnj5UG2XCrj22%2BBJG8S8UHiExHaIwt01Nel6V7Y0IlXWvwqK8YEx%2FHOI%2FewXERfrnIQDCsrQyC7qTLL3HndUW2Ke8ib2iC%2BPgaP6xDqkqdlhOSojQHG4rfwcyVOFOzeauzAO7Rc77mb0rCUJdMckP6nKiD7nrtjlZXznFmYhCvjmWQF2l06Jl7xQsr%2BjkGAeoXo9X%2FiC11ZTNfxOVIe3LWWkRvMwGWvgvtgF4ZEDGaLXgsbO4I8%2FpSmGD4ox9ZWDfX%2BtTURCyBYVXqYpQ4TpgMhHqAtTUr4TNc7GRLVbfi1xqZNQDt1Sfdzh3Xq88dOJyKsyUs7rcFuuxoNyxvqstWVaAyRglOH1n%2BpV0xA7%2FKEHa%2F8%2FzH6uaXeIp3eLJN1%2BGlAQc1sP2jehPHqGi5Lc7YMOKk8akGOrABqEMeyIMA72vRUvaZqcs7N77uX3kDw2%2BTfyF8pS8HYdR1%2BEU1ekEPGlPPLyTo0NFmbmMa4urw%2B19eIvlGSnFjiSeee%2F%2BeotdKLVnDgZ5aNxOYivkgUqjazWNTWX1qdv7Jq7GWrNDLwjZiU5zLvpcjSyzLyGAVIo8pW14m4aC3jppuzjKpasygGK2%2Bf%2BmxisMAkIdRRS5aXW9PY%2FuwiBnL3qiZT5RtAdamISZZM9jUAWY%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231028T003610Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFPXEGMX3T%2F20231028%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=403444b159d15daa02ecb8fd21eb66c69ad6b324d24b23c115fbb48590f856fb",
                        "width": 200,
                        "height": 200
                    },
                    "REGULAR": {
                        "url": "https://edamam-product-images.s3.amazonaws.com/web-img/0dd/0dd087a50dcc84d9b5abb3e66f6c2d29.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLWVhc3QtMSJIMEYCIQCP2Gbt%2ByPQIVKV%2FafgML7WXbkOusL9fCs6d1le6dFKYAIhAJcnuEh%2B1NzOso38QgGaVBwaVQAMxyMJATg%2FR%2Fl0jl96KsEFCJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMMTg3MDE3MTUwOTg2IgydADkJdybnmhdEGwQqlQUNCCJJEzulouVCRRPPDPN9Ik9nmgPZk%2Fam6u04CTug5FWfzto4W1y6mlAuXr3EHPB%2FvTcZ%2BmAkgcS5%2FRfKsviGgYg1PBDbKvJFWJigqXNb6jHaHO3eyZnXpof0Qk2PachTFyGGF7upzvEiKr6BGB6DtCoEGe3wCd0iFSMS%2Ft8LIlICGGYaaCvWq9TXeaXkel5jju8XxawzfW0OY8ad1NODjiJJ%2FJ02goRzRa3HwZdXj0P4%2FwwiBHg8BMnsBu5XvhNCt9Gz%2Bxp9cZIC8TMv%2FY8rOvepaH28zVl5BjLGle3tn5syTeLiH6OS68I4OndB2qqeqZqdi9cu6zb1H0y8aKh8r8IIaHqXhP6jBXwOxUN8uimNrMJnaDPxNdvFPuR5yx8UApiuserTd1b1ZIBFiBJ6lavYUBrkLW%2B7bZIJltsNTSxF2GTKFWoXHKGf3%2FXYj%2FniRUh%2BB3xUXrXh8PzVKChkdfuCxirnj5UG2XCrj22%2BBJG8S8UHiExHaIwt01Nel6V7Y0IlXWvwqK8YEx%2FHOI%2FewXERfrnIQDCsrQyC7qTLL3HndUW2Ke8ib2iC%2BPgaP6xDqkqdlhOSojQHG4rfwcyVOFOzeauzAO7Rc77mb0rCUJdMckP6nKiD7nrtjlZXznFmYhCvjmWQF2l06Jl7xQsr%2BjkGAeoXo9X%2FiC11ZTNfxOVIe3LWWkRvMwGWvgvtgF4ZEDGaLXgsbO4I8%2FpSmGD4ox9ZWDfX%2BtTURCyBYVXqYpQ4TpgMhHqAtTUr4TNc7GRLVbfi1xqZNQDt1Sfdzh3Xq88dOJyKsyUs7rcFuuxoNyxvqstWVaAyRglOH1n%2BpV0xA7%2FKEHa%2F8%2FzH6uaXeIp3eLJN1%2BGlAQc1sP2jehPHqGi5Lc7YMOKk8akGOrABqEMeyIMA72vRUvaZqcs7N77uX3kDw2%2BTfyF8pS8HYdR1%2BEU1ekEPGlPPLyTo0NFmbmMa4urw%2B19eIvlGSnFjiSeee%2F%2BeotdKLVnDgZ5aNxOYivkgUqjazWNTWX1qdv7Jq7GWrNDLwjZiU5zLvpcjSyzLyGAVIo8pW14m4aC3jppuzjKpasygGK2%2Bf%2BmxisMAkIdRRS5aXW9PY%2FuwiBnL3qiZT5RtAdamISZZM9jUAWY%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231028T003610Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFPXEGMX3T%2F20231028%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=cbe499cd048a72453361a9d697f7df91e13c2ffe83ac48de3646e240b6e28968",
                        "width": 300,
                        "height": 300
                    },
                    "LARGE": {
                        "url": "https://edamam-product-images.s3.amazonaws.com/web-img/0dd/0dd087a50dcc84d9b5abb3e66f6c2d29-l.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLWVhc3QtMSJIMEYCIQCP2Gbt%2ByPQIVKV%2FafgML7WXbkOusL9fCs6d1le6dFKYAIhAJcnuEh%2B1NzOso38QgGaVBwaVQAMxyMJATg%2FR%2Fl0jl96KsEFCJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMMTg3MDE3MTUwOTg2IgydADkJdybnmhdEGwQqlQUNCCJJEzulouVCRRPPDPN9Ik9nmgPZk%2Fam6u04CTug5FWfzto4W1y6mlAuXr3EHPB%2FvTcZ%2BmAkgcS5%2FRfKsviGgYg1PBDbKvJFWJigqXNb6jHaHO3eyZnXpof0Qk2PachTFyGGF7upzvEiKr6BGB6DtCoEGe3wCd0iFSMS%2Ft8LIlICGGYaaCvWq9TXeaXkel5jju8XxawzfW0OY8ad1NODjiJJ%2FJ02goRzRa3HwZdXj0P4%2FwwiBHg8BMnsBu5XvhNCt9Gz%2Bxp9cZIC8TMv%2FY8rOvepaH28zVl5BjLGle3tn5syTeLiH6OS68I4OndB2qqeqZqdi9cu6zb1H0y8aKh8r8IIaHqXhP6jBXwOxUN8uimNrMJnaDPxNdvFPuR5yx8UApiuserTd1b1ZIBFiBJ6lavYUBrkLW%2B7bZIJltsNTSxF2GTKFWoXHKGf3%2FXYj%2FniRUh%2BB3xUXrXh8PzVKChkdfuCxirnj5UG2XCrj22%2BBJG8S8UHiExHaIwt01Nel6V7Y0IlXWvwqK8YEx%2FHOI%2FewXERfrnIQDCsrQyC7qTLL3HndUW2Ke8ib2iC%2BPgaP6xDqkqdlhOSojQHG4rfwcyVOFOzeauzAO7Rc77mb0rCUJdMckP6nKiD7nrtjlZXznFmYhCvjmWQF2l06Jl7xQsr%2BjkGAeoXo9X%2FiC11ZTNfxOVIe3LWWkRvMwGWvgvtgF4ZEDGaLXgsbO4I8%2FpSmGD4ox9ZWDfX%2BtTURCyBYVXqYpQ4TpgMhHqAtTUr4TNc7GRLVbfi1xqZNQDt1Sfdzh3Xq88dOJyKsyUs7rcFuuxoNyxvqstWVaAyRglOH1n%2BpV0xA7%2FKEHa%2F8%2FzH6uaXeIp3eLJN1%2BGlAQc1sP2jehPHqGi5Lc7YMOKk8akGOrABqEMeyIMA72vRUvaZqcs7N77uX3kDw2%2BTfyF8pS8HYdR1%2BEU1ekEPGlPPLyTo0NFmbmMa4urw%2B19eIvlGSnFjiSeee%2F%2BeotdKLVnDgZ5aNxOYivkgUqjazWNTWX1qdv7Jq7GWrNDLwjZiU5zLvpcjSyzLyGAVIo8pW14m4aC3jppuzjKpasygGK2%2Bf%2BmxisMAkIdRRS5aXW9PY%2FuwiBnL3qiZT5RtAdamISZZM9jUAWY%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231028T003610Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFPXEGMX3T%2F20231028%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=1a6e7c3fd7b4043eb819ed1e83fcb5a6556bde2aaa205a15ac2c622ebcc0f83e",
                        "width": 600,
                        "height": 600
                    }
                },
                "source": "Martha Stewart",
                "url": "http://www.marthastewart.com/338579/beef-tacos",
                "shareAs": "http://www.edamam.com/recipe/quick-beef-tacos-d6d4673c3d725197da7ef0ece3993daf/tacos",
                "yield": 4.0,
                "dietLabels": [],
                "healthLabels": [
                    "Vegetarian",
                    "Pescatarian",
                    "Egg-Free",
                    "Peanut-Free",
                    "Tree-Nut-Free",
                    "Soy-Free",
                    "Fish-Free",
                    "Shellfish-Free",
                    "Pork-Free",
                    "Red-Meat-Free",
                    "Crustacean-Free",
                    "Celery-Free",
                    "Mustard-Free",
                    "Sesame-Free",
                    "Lupine-Free",
                    "Mollusk-Free",
                    "Alcohol-Free",
                    "Sulfite-Free",
                    "Kosher"
                ],
                "cautions": [
                    "Eggs",
                    "Milk",
                    "Sulfites"
                ],
                "ingredientLines": [
                    "3 cups Taco Filling, thawed",
                    "12 corn tortillas (6-inch)",
                    "2 cups shredded iceberg lettuce",
                    "1/2 cup thinly sliced radishes",
                    "1/2 cup shredded Monterey Jack cheese",
                    "1/3 chopped fresh cilantro",
                    "1/2 cup prepared salsa",
                    "1/4 cup reduced-fat sour cream",
                    "Diced jalapeno (optional)"
                ],
                "ingredients": [
                    {
                        "text": "3 cups Taco Filling, thawed",
                        "quantity": 3.0,
                        "measure": "<unit>",
                        "food": "Taco",
                        "weight": 38.099999999999994,
                        "foodCategory": "quick breads and pastries",
                        "foodId": "food_amx6njaaa4q9lsaz4k98faejx12a",
                        "image": "https://www.edamam.com/food-img/def/def506222dc404affdfbf7b7133a34c6.jpg"
                    },
                    {
                        "text": "12 corn tortillas (6-inch)",
                        "quantity": 12.0,
                        "measure": "<unit>",
                        "food": "corn tortillas",
                        "weight": 288.0,
                        "foodCategory": "quick breads and pastries",
                        "foodId": "food_bhw0b95agm97s0abfignnb8fsvb3",
                        "image": "https://www.edamam.com/food-img/b8a/b8ad23dcc06f2324f944e47eb579d644.jpg"
                    },
                    {
                        "text": "2 cups shredded iceberg lettuce",
                        "quantity": 2.0,
                        "measure": "cup",
                        "food": "iceberg lettuce",
                        "weight": 144.0,
                        "foodCategory": "vegetables",
                        "foodId": "food_advhqk1a09o2noblosrg6a4z10xv",
                        "image": "https://www.edamam.com/food-img/3c0/3c00c5ba27678b2f8e1c58b342bd98c7.jpg"
                    },
                    {
                        "text": "1/2 cup thinly sliced radishes",
                        "quantity": 0.5,
                        "measure": "cup",
                        "food": "radishes",
                        "weight": 58.0,
                        "foodCategory": "vegetables",
                        "foodId": "food_bs6xkukbtd85e7b2lh5zfazpe45y",
                        "image": "https://www.edamam.com/food-img/ad7/ad78f4315cdba1dc26ccef0d7dba464b.jpg"
                    },
                    {
                        "text": "1/2 cup shredded Monterey Jack cheese",
                        "quantity": 0.5,
                        "measure": "cup",
                        "food": "Jack cheese",
                        "weight": 66.0,
                        "foodCategory": "Cheese",
                        "foodId": "food_atp17pta7d5it2a80ct13ard6aj3",
                        "image": "https://www.edamam.com/food-img/590/59062b9f8d57ebc7d831b7b7c231f726.jpg"
                    },
                    {
                        "text": "1/3 chopped fresh cilantro",
                        "quantity": 0.3333333333333333,
                        "measure": "<unit>",
                        "food": "cilantro",
                        "weight": 2.333333333333333,
                        "foodCategory": "vegetables",
                        "foodId": "food_alhzhuwb4lc7jnb5s6f02by60bzp",
                        "image": "https://www.edamam.com/food-img/d57/d57e375b6ff99a90c7ee2b1990a1af36.jpg"
                    },
                    {
                        "text": "1/2 cup prepared salsa",
                        "quantity": 0.5,
                        "measure": "cup",
                        "food": "salsa",
                        "weight": 129.5,
                        "foodCategory": "canned soup",
                        "foodId": "food_b0t3obfawlm5k2b6erxscacez35u",
                        "image": "https://www.edamam.com/food-img/995/995d0f166754a0475c181b9c156fec43.jpg"
                    },
                    {
                        "text": "1/4 cup reduced-fat sour cream",
                        "quantity": 0.25,
                        "measure": "cup",
                        "food": "reduced-fat sour cream",
                        "weight": 57.5,
                        "foodCategory": "Dairy",
                        "foodId": "food_ab2gbg1a463bhca1y3gqybp17eqm",
                        "image": "https://www.edamam.com/food-img/0f5/0f5af0f498975dc7beaa817ffb500d51.jpg"
                    },
                    {
                        "text": "Diced jalapeno (optional)",
                        "quantity": 0.0,
                        "measure": '',
                        "food": "jalapeno",
                        "weight": 0.0,
                        "foodCategory": "vegetables",
                        "foodId": "food_b7txsnbadj6plsbq27zvwah80r6y",
                        "image": "https://www.edamam.com/food-img/0df/0df9aa459870a6d477b0925c1fdb6d4c.jpg"
                    }
                ],
                "calories": 1226.9826666666668,
                "totalCO2Emissions": 3840.0620000000004,
                "co2EmissionsClass": "E",
                "totalWeight": 783.4333333333334,
                "totalTime": 15.0,
                "cuisineType": [
                    "mexican"
                ],
                "mealType": [
                    "lunch/dinner"
                ],
                "dishType": [
                    "sandwiches"
                ],
                "totalNutrients": {
                    "ENERC_KCAL": {
                        "label": "Energy",
                        "quantity": 1226.9826666666668,
                        "unit": "kcal"
                    },
                    "FAT": {
                        "label": "Fat",
                        "quantity": 45.11118333333333,
                        "unit": "g"
                    },
                    "FASAT": {
                        "label": "Saturated",
                        "quantity": 21.69024166666667,
                        "unit": "g"
                    },
                    "FATRN": {
                        "label": "Trans",
                        "quantity": 0.06553199999999999,
                        "unit": "g"
                    },
                    "FAMS": {
                        "label": "Monounsaturated",
                        "quantity": 12.817826666666665,
                        "unit": "g"
                    },
                    "FAPU": {
                        "label": "Polyunsaturated",
                        "quantity": 7.3022833333333335,
                        "unit": "g"
                    },
                    "CHOCDF": {
                        "label": "Carbs",
                        "quantity": 172.04853333333338,
                        "unit": "g"
                    },
                    "CHOCDF.net": {
                        "label": "Carbohydrates (net)",
                        "quantity": 146.17000000000004,
                        "unit": "g"
                    },
                    "FIBTG": {
                        "label": "Fiber",
                        "quantity": 25.878533333333337,
                        "unit": "g"
                    },
                    "SUGAR": {
                        "label": "Sugars",
                        "quantity": 12.73725,
                        "unit": "g"
                    },
                    "PROCNT": {
                        "label": "Protein",
                        "quantity": 42.76171,
                        "unit": "g"
                    },
                    "CHOLE": {
                        "label": "Cholesterol",
                        "quantity": 78.86500000000001,
                        "unit": "mg"
                    },
                    "NA": {
                        "label": "Sodium",
                        "quantity": 1648.1323333333335,
                        "unit": "mg"
                    },
                    "CA": {
                        "label": "Calcium",
                        "quantity": 925.6483333333335,
                        "unit": "mg"
                    },
                    "MG": {
                        "label": "Magnesium",
                        "quantity": 299.0396666666667,
                        "unit": "mg"
                    },
                    "K": {
                        "label": "Potassium",
                        "quantity": 1504.9376666666667,
                        "unit": "mg"
                    },
                    "FE": {
                        "label": "Iron",
                        "quantity": 6.049739999999999,
                        "unit": "mg"
                    },
                    "ZN": {
                        "label": "Zinc",
                        "quantity": 7.1446266666666665,
                        "unit": "mg"
                    },
                    "P": {
                        "label": "Phosphorus",
                        "quantity": 1419.2629999999997,
                        "unit": "mg"
                    },
                    "VITA_RAE": {
                        "label": "Vitamin A",
                        "quantity": 273.13433333333336,
                        "unit": "µg"
                    },
                    "VITC": {
                        "label": "Vitamin C",
                        "quantity": 16.223999999999997,
                        "unit": "mg"
                    },
                    "THIA": {
                        "label": "Thiamin (B1)",
                        "quantity": 0.49621433333333337,
                        "unit": "mg"
                    },
                    "RIBF": {
                        "label": "Riboflavin (B2)",
                        "quantity": 0.7169200000000001,
                        "unit": "mg"
                    },
                    "NIA": {
                        "label": "Niacin (B3)",
                        "quantity": 6.89599,
                        "unit": "mg"
                    },
                    "VITB6A": {
                        "label": "Vitamin B6",
                        "quantity": 1.0995796666666666,
                        "unit": "mg"
                    },
                    "FOLDFE": {
                        "label": "Folate equivalent (total)",
                        "quantity": 127.87666666666665,
                        "unit": "µg"
                    },
                    "FOLFD": {
                        "label": "Folate (food)",
                        "quantity": 113.01766666666667,
                        "unit": "µg"
                    },
                    "FOLAC": {
                        "label": "Folic acid",
                        "quantity": 9.143999999999998,
                        "unit": "µg"
                    },
                    "VITB12": {
                        "label": "Vitamin B12",
                        "quantity": 0.7202999999999999,
                        "unit": "µg"
                    },
                    "VITD": {
                        "label": "Vitamin D",
                        "quantity": 0.5685,
                        "unit": "µg"
                    },
                    "TOCPHA": {
                        "label": "Vitamin E",
                        "quantity": 3.446023333333333,
                        "unit": "mg"
                    },
                    "VITK1": {
                        "label": "Vitamin K",
                        "quantity": 53.58893333333334,
                        "unit": "µg"
                    },
                    "WATER": {
                        "label": "Water",
                        "quantity": 513.2482333333334,
                        "unit": "g"
                    }
                },
                "totalDaily": {
                    "ENERC_KCAL": {
                        "label": "Energy",
                        "quantity": 61.34913333333334,
                        "unit": "%"
                    },
                    "FAT": {
                        "label": "Fat",
                        "quantity": 69.4018205128205,
                        "unit": "%"
                    },
                    "FASAT": {
                        "label": "Saturated",
                        "quantity": 108.45120833333335,
                        "unit": "%"
                    },
                    "CHOCDF": {
                        "label": "Carbs",
                        "quantity": 57.349511111111134,
                        "unit": "%"
                    },
                    "FIBTG": {
                        "label": "Fiber",
                        "quantity": 103.51413333333333,
                        "unit": "%"
                    },
                    "PROCNT": {
                        "label": "Protein",
                        "quantity": 85.52342,
                        "unit": "%"
                    },
                    "CHOLE": {
                        "label": "Cholesterol",
                        "quantity": 26.288333333333338,
                        "unit": "%"
                    },
                    "NA": {
                        "label": "Sodium",
                        "quantity": 68.67218055555556,
                        "unit": "%"
                    },
                    "CA": {
                        "label": "Calcium",
                        "quantity": 92.56483333333335,
                        "unit": "%"
                    },
                    "MG": {
                        "label": "Magnesium",
                        "quantity": 71.19992063492063,
                        "unit": "%"
                    },
                    "K": {
                        "label": "Potassium",
                        "quantity": 32.019950354609925,
                        "unit": "%"
                    },
                    "FE": {
                        "label": "Iron",
                        "quantity": 33.60966666666666,
                        "unit": "%"
                    },
                    "ZN": {
                        "label": "Zinc",
                        "quantity": 64.95115151515152,
                        "unit": "%"
                    },
                    "P": {
                        "label": "Phosphorus",
                        "quantity": 202.7518571428571,
                        "unit": "%"
                    },
                    "VITA_RAE": {
                        "label": "Vitamin A",
                        "quantity": 30.34825925925926,
                        "unit": "%"
                    },
                    "VITC": {
                        "label": "Vitamin C",
                        "quantity": 18.026666666666664,
                        "unit": "%"
                    },
                    "THIA": {
                        "label": "Thiamin (B1)",
                        "quantity": 41.351194444444445,
                        "unit": "%"
                    },
                    "RIBF": {
                        "label": "Riboflavin (B2)",
                        "quantity": 55.14769230769231,
                        "unit": "%"
                    },
                    "NIA": {
                        "label": "Niacin (B3)",
                        "quantity": 43.0999375,
                        "unit": "%"
                    },
                    "VITB6A": {
                        "label": "Vitamin B6",
                        "quantity": 84.58305128205127,
                        "unit": "%"
                    },
                    "FOLDFE": {
                        "label": "Folate equivalent (total)",
                        "quantity": 31.96916666666666,
                        "unit": "%"
                    },
                    "VITB12": {
                        "label": "Vitamin B12",
                        "quantity": 30.012500000000003,
                        "unit": "%"
                    },
                    "VITD": {
                        "label": "Vitamin D",
                        "quantity": 3.79,
                        "unit": "%"
                    },
                    "TOCPHA": {
                        "label": "Vitamin E",
                        "quantity": 22.973488888888888,
                        "unit": "%"
                    },
                    "VITK1": {
                        "label": "Vitamin K",
                        "quantity": 44.657444444444444,
                        "unit": "%"
                    }
                },
                "digest": [
                    {
                        "label": "Fat",
                        "tag": "FAT",
                        "schemaOrgTag": "fatContent",
                        "total": 45.11118333333333,
                        "hasRDI": True,
                        "daily": 69.4018205128205,
                        "unit": "g",
                        "sub": [
                            {
                                "label": "Saturated",
                                "tag": "FASAT",
                                "schemaOrgTag": "saturatedFatContent",
                                "total": 21.69024166666667,
                                "hasRDI": True,
                                "daily": 108.45120833333335,
                                "unit": "g"
                            },
                            {
                                "label": "Trans",
                                "tag": "FATRN",
                                "schemaOrgTag": "transFatContent",
                                "total": 0.06553199999999999,
                                "hasRDI": False,
                                "daily": 0.0,
                                "unit": "g"
                            },
                            {
                                "label": "Monounsaturated",
                                "tag": "FAMS",
                                "schemaOrgTag": '',
                                "total": 12.817826666666665,
                                "hasRDI": False,
                                "daily": 0.0,
                                "unit": "g"
                            },
                            {
                                "label": "Polyunsaturated",
                                "tag": "FAPU",
                                "schemaOrgTag": '',
                                "total": 7.3022833333333335,
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
                        "total": 172.04853333333338,
                        "hasRDI": True,
                        "daily": 57.349511111111134,
                        "unit": "g",
                        "sub": [
                            {
                                "label": "Carbs (net)",
                                "tag": "CHOCDF.net",
                                "schemaOrgTag": '',
                                "total": 146.17000000000004,
                                "hasRDI": False,
                                "daily": 0.0,
                                "unit": "g"
                            },
                            {
                                "label": "Fiber",
                                "tag": "FIBTG",
                                "schemaOrgTag": "fiberContent",
                                "total": 25.878533333333337,
                                "hasRDI": True,
                                "daily": 103.51413333333333,
                                "unit": "g"
                            },
                            {
                                "label": "Sugars",
                                "tag": "SUGAR",
                                "schemaOrgTag": "sugarContent",
                                "total": 12.73725,
                                "hasRDI": False,
                                "daily": 0.0,
                                "unit": "g"
                            },
                            {
                                "label": "Sugars, added",
                                "tag": "SUGAR.added",
                                "schemaOrgTag": '',
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
                        "total": 42.76171,
                        "hasRDI": True,
                        "daily": 85.52342,
                        "unit": "g"
                    },
                    {
                        "label": "Cholesterol",
                        "tag": "CHOLE",
                        "schemaOrgTag": "cholesterolContent",
                        "total": 78.86500000000001,
                        "hasRDI": True,
                        "daily": 26.288333333333338,
                        "unit": "mg"
                    },
                    {
                        "label": "Sodium",
                        "tag": "NA",
                        "schemaOrgTag": "sodiumContent",
                        "total": 1648.1323333333335,
                        "hasRDI": True,
                        "daily": 68.67218055555556,
                        "unit": "mg"
                    },
                    {
                        "label": "Calcium",
                        "tag": "CA",
                        "schemaOrgTag": '',
                        "total": 925.6483333333335,
                        "hasRDI": True,
                        "daily": 92.56483333333335,
                        "unit": "mg"
                    },
                    {
                        "label": "Magnesium",
                        "tag": "MG",
                        "schemaOrgTag": '',
                        "total": 299.0396666666667,
                        "hasRDI": True,
                        "daily": 71.19992063492063,
                        "unit": "mg"
                    },
                    {
                        "label": "Potassium",
                        "tag": "K",
                        "schemaOrgTag": '',
                        "total": 1504.9376666666667,
                        "hasRDI": True,
                        "daily": 32.019950354609925,
                        "unit": "mg"
                    },
                    {
                        "label": "Iron",
                        "tag": "FE",
                        "schemaOrgTag": '',
                        "total": 6.049739999999999,
                        "hasRDI": True,
                        "daily": 33.60966666666666,
                        "unit": "mg"
                    },
                    {
                        "label": "Zinc",
                        "tag": "ZN",
                        "schemaOrgTag": '',
                        "total": 7.1446266666666665,
                        "hasRDI": True,
                        "daily": 64.95115151515152,
                        "unit": "mg"
                    },
                    {
                        "label": "Phosphorus",
                        "tag": "P",
                        "schemaOrgTag": '',
                        "total": 1419.2629999999997,
                        "hasRDI": True,
                        "daily": 202.7518571428571,
                        "unit": "mg"
                    },
                    {
                        "label": "Vitamin A",
                        "tag": "VITA_RAE",
                        "schemaOrgTag": '',
                        "total": 273.13433333333336,
                        "hasRDI": True,
                        "daily": 30.34825925925926,
                        "unit": "µg"
                    },
                    {
                        "label": "Vitamin C",
                        "tag": "VITC",
                        "schemaOrgTag": '',
                        "total": 16.223999999999997,
                        "hasRDI": True,
                        "daily": 18.026666666666664,
                        "unit": "mg"
                    },
                    {
                        "label": "Thiamin (B1)",
                        "tag": "THIA",
                        "schemaOrgTag": '',
                        "total": 0.49621433333333337,
                        "hasRDI": True,
                        "daily": 41.351194444444445,
                        "unit": "mg"
                    },
                    {
                        "label": "Riboflavin (B2)",
                        "tag": "RIBF",
                        "schemaOrgTag": '',
                        "total": 0.7169200000000001,
                        "hasRDI": True,
                        "daily": 55.14769230769231,
                        "unit": "mg"
                    },
                    {
                        "label": "Niacin (B3)",
                        "tag": "NIA",
                        "schemaOrgTag": '',
                        "total": 6.89599,
                        "hasRDI": True,
                        "daily": 43.0999375,
                        "unit": "mg"
                    },
                    {
                        "label": "Vitamin B6",
                        "tag": "VITB6A",
                        "schemaOrgTag": '',
                        "total": 1.0995796666666666,
                        "hasRDI": True,
                        "daily": 84.58305128205127,
                        "unit": "mg"
                    },
                    {
                        "label": "Folate equivalent (total)",
                        "tag": "FOLDFE",
                        "schemaOrgTag": '',
                        "total": 127.87666666666665,
                        "hasRDI": True,
                        "daily": 31.96916666666666,
                        "unit": "µg"
                    },
                    {
                        "label": "Folate (food)",
                        "tag": "FOLFD",
                        "schemaOrgTag": '',
                        "total": 113.01766666666667,
                        "hasRDI": False,
                        "daily": 0.0,
                        "unit": "µg"
                    },
                    {
                        "label": "Folic acid",
                        "tag": "FOLAC",
                        "schemaOrgTag": '',
                        "total": 9.143999999999998,
                        "hasRDI": False,
                        "daily": 0.0,
                        "unit": "µg"
                    },
                    {
                        "label": "Vitamin B12",
                        "tag": "VITB12",
                        "schemaOrgTag": '',
                        "total": 0.7202999999999999,
                        "hasRDI": True,
                        "daily": 30.012500000000003,
                        "unit": "µg"
                    },
                    {
                        "label": "Vitamin D",
                        "tag": "VITD",
                        "schemaOrgTag": '',
                        "total": 0.5685,
                        "hasRDI": True,
                        "daily": 3.79,
                        "unit": "µg"
                    },
                    {
                        "label": "Vitamin E",
                        "tag": "TOCPHA",
                        "schemaOrgTag": '',
                        "total": 3.446023333333333,
                        "hasRDI": True,
                        "daily": 22.973488888888888,
                        "unit": "mg"
                    },
                    {
                        "label": "Vitamin K",
                        "tag": "VITK1",
                        "schemaOrgTag": '',
                        "total": 53.58893333333334,
                        "hasRDI": True,
                        "daily": 44.657444444444444,
                        "unit": "µg"
                    },
                    {
                        "label": "Sugar alcohols",
                        "tag": "Sugar.alcohol",
                        "schemaOrgTag": '',
                        "total": 0.0,
                        "hasRDI": False,
                        "daily": 0.0,
                        "unit": "g"
                    },
                    {
                        "label": "Water",
                        "tag": "WATER",
                        "schemaOrgTag": '',
                        "total": 513.2482333333334,
                        "hasRDI": False,
                        "daily": 0.0,
                        "unit": "g"
                    }
                ]
            },
            "_links": {
                "self": {
                    "title": "Self",
                    "href": "https://api.edamam.com/api/recipes/v2/d6d4673c3d725197da7ef0ece3993daf?type=public&app_id=e909afd5&app_key=34e59dda7e1bffb92e49c416e9449e1d"
                }
            }
        }
    ]
}
        

        # return Response(responseJSON)
        return Response(dummy_data)
       
       
        