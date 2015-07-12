from django.http import HttpResponse
from django.shortcuts import render

from .models import Budget

def budget_list(request):
	budgets = Budget.objects.all().order_by('-last_modified')
	return render(request, 'unclebudget/budget_list.html', locals())

def budget_detail(request, budget_id):
	budget = Budget.objects.get(id=budget_id)
	return render(request, 'unclebudget/budget_detail.html', locals())
