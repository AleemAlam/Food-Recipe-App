from django.urls import path,include
from recipe import views

urlpatterns = [
    path('', views.index , name= 'index'),
    path('about/', views.AboutTemplateView.as_view(), name = 'about'),
    path('all_recipe/', views.all_recipe , name = 'all_recipe'),
    path('vegans/', views.vegans , name = 'vegans'),
    path('non-vegans/', views.non_vegans , name = 'non-vegans'),
    path('<int:pk>/recipe', views.single_recipe , name = 'single_recipe'),
    path('contact/', views.contact , name = 'contact'),
]
