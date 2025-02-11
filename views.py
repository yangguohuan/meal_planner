from django.shortcuts import render
from .models import Plan

# Create your views here.
def index(request):
    return render(request, 'meal_plans/index.html')
def plans(request):
    plans = Plan.objects.order_by('date_added')
    context = { 'plans':plans }
    return render(request, 'meal_plans/plans.html', context)
def plan(request, plan_id):
    plan = Plan.objects.get(id=plan_id)
    text = plan.detail_set.order_by('-date_added')
    context = {'plan':plan, 'text':text }
    return render(request, 'meal_plans/plan.html', context)