from django.shortcuts import render, get_object_or_404
from .models import Recipe
from django.views.generic import TemplateView

# Create your views here.
def index(request):
    home_recipe= Recipe.objects.all().filter(show_home = True)
    best_recipe= Recipe.objects.all().filter(best_recipe = True)
    latest_recipe = Recipe.objects.all().filter(show_home = False)[:6]
    return render(request,'recipe/index.html',{'home_recipe':home_recipe,'best_recipe':best_recipe,'latest_recipe':latest_recipe})

class AboutTemplateView(TemplateView):
    template_name = 'recipe/about.html'

def all_recipe(request):
    all_recipe = Recipe.objects.all().order_by('-added_date')
    return render(request, 'recipe/all_recipe.html',{'all_recipe':all_recipe})

def single_recipe(request, pk):
    recipe = get_object_or_404(Recipe,pk=pk)
    recipe_ingredients = recipe.ingredients.split('\n')
    recipe_details = recipe.recipe_details.split('\n')
    return render(request,'recipe/recipe.html',{'recipe':recipe,'recipe_ingredients':recipe_ingredients,'recipe_details':recipe_details})

def contact(request):
    return render(request,'recipe/contact.html')

def vegans(request):
    all_recipe = Recipe.objects.all().filter(category = 'veg').order_by('-added_date')
    return render(request,'recipe/all_recipe.html',{'all_recipe':all_recipe})

def non_vegans(request):
    all_recipe = Recipe.objects.all().filter(category = 'nveg').order_by('-added_date')
    return render(request,'recipe/all_recipe.html',{'all_recipe':all_recipe})
