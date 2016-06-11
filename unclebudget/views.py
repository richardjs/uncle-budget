from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import Budget, Item, Transaction

def budget_list(request):
	budgets = Budget.objects.all().order_by('-last_modified')
	return render(request, 'unclebudget/budget_list.html', locals())

def budget_detail(request, budget_id):
	budget = Budget.objects.get(id=budget_id)
	return render(request, 'unclebudget/budget_detail.html', locals())

def item_detail(request, item_id):
	item = Item.objects.get(id=item_id)
	return render(request, 'unclebudget/item_detail.html', locals())

def transaction_create(request):
	Transaction(
		item=Item.objects.get(id=request.POST['itemID']),
		amount=request.POST['amount'],
		comment=request.POST['comment']
	).save()
	return redirect('item_detail', request.POST['itemID'])

def transaction_delete(request):
	transaction = Transaction.objects.get(id=request.POST['transactionID'])
	itemID = transaction.item.id
	transaction.delete()
	return redirect('item_detail', itemID)
