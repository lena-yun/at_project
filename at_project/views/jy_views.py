from django.shortcuts import render
from django.views.generic import TemplateView


class IndexMainViews(TemplateView):
    template_name = "at_project/jy/index.html"

<<<<<<< HEAD

class FoodRecipe1Views(TemplateView):
    template_name = "at_project/jy/food-recipe-1.html"


class KFoodReport2Views(TemplateView):
    template_name = "at_project/jy/k-food-report-2.html"
=======
class FoodRecipe1Views(TemplateView):
    template_name = "at_project/jy/food-recipe-1.html"

class KFoodReport2Views(TemplateView):
    template_name = "at_project/jy/k-food-report-2.html"
>>>>>>> 4924ba81d39261b47505f3aeda2f859ea77f8049
