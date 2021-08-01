from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse, JsonResponse
from bs4 import BeautifulSoup
import requests


class JSONResponseMixin:
    """
    A mixin that can be used to render a JSON response.
    """

    def render_to_json_response(self, context, **response_kwargs):
        """
        Returns a JSON response, transforming 'context' to make the payload.
        """
        return JsonResponse(
            self.get_data(context),
            **response_kwargs
        )

    def get_data(self, context):
        """
        Returns an object that will be serialized as JSON by json.dumps().
        """
        # Note: This is *EXTREMELY* naive; in reality, you'll need
        # to do much more complex handling to ensure that arbitrary
        # objects -- such as Django model instances or querysets
        # -- can be serialized as JSON.
        return context


class KFoodReportViews(TemplateView):
    template_name = "at_project/gy/k-food-report.html"


def recipe_ajax(request):
    if request.is_ajax():
        test = request.GET
        _url = ''.join([f'{value}={test[value]}' if  idx == 0 else f'&{value}={test[value]}' for idx, value in enumerate(test)])
        url = f'http://api.nongsaro.go.kr/service/{_url}'
        res = requests.get(url)
        soup = BeautifulSoup(res.content, 'html.parser')
        return HttpResponse(soup,
                            content_type='application/json')
    return render(request, 'at_project/gy/repice.html')


class KFoodIdolViews(TemplateView):
    template_name = "at_project/gy/k-food-idol.html"


class FoodRecipe2Views(TemplateView):
    template_name = "at_project/gy/food-recipe-2.html"

class TableauTestViews(TemplateView):
    template_name = "at_project/gy/tableau_test.html"