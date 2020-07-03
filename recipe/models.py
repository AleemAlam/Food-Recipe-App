from django.db import models

# Create your models here.
CATEGORY = (
    ('veg', 'VEGETARIAN'),
    ('nveg','NON-VEGETARIAN')
)

CATEGORY_FOR_MAKING = (
    ('beg', 'BEGGINER'),
    ('inter','INTERMEDIATE')
)

class Recipe(models.Model):
    title = models.CharField(max_length = 100)
    category = models.CharField(choices = CATEGORY, max_length = 20)
    description = models.CharField(max_length = 200)
    ingredients = models.TextField()
    prepare_time = models.CharField(max_length = 3)
    cook_time = models.CharField(max_length = 3)
    recipe_details = models.TextField()
    added_date = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to = 'food_pics/%Y/%m/%d/')
    video_link = models.CharField(max_length = 500)
    who_can_make = models.CharField(choices = CATEGORY_FOR_MAKING, max_length = 20)
    best_recipe = models.BooleanField(default = False)
    best_recipe = models.BooleanField(default = False)
    gluten_free = models.BooleanField(default = False)
    show_home = models.BooleanField(default = False)


    def __str__(self):
        return self.title
