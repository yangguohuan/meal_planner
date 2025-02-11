from django.urls import path
from . import views

app_name = 'meal_plans'
urlpatterns = [
    path('',views.index,name='index'),
    path('plans', views.plans, name='plans'),
    path('plans/<int:plan_id>', views.plan, name='plan'),
]