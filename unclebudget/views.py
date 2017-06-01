from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from unclebudget.models import Budget, Item, Transaction

class ActiveBudgetList(LoginRequiredMixin, ListView):
	def get_queryset(self):
		return Budget.objects.filter(user=self.request.user, template=False).order_by('-last_modified')

class AllBudgetList(LoginRequiredMixin, ListView):
	def get_context_data(self):
		context = super().get_context_data()
		context['all'] = True
		return context 

	def get_queryset(self):
		return Budget.objects.filter(user=self.request.user, template=False).order_by('-last_modified')

class TemplateList(LoginRequiredMixin, ListView):
	template_name = 'unclebudget/template_list.html'

	def get_queryset(self):
		return Budget.objects.filter(user=self.request.user, template=True).order_by('-last_modified')

class BudgetCreate(LoginRequiredMixin, CreateView):
	model = Budget
	fields = ['name']
	success_url = reverse_lazy('budget_list')

	def get_context_data(self):
		context = super().get_context_data()
		context['budgets'] = Budget.objects.filter(user=self.request.user, template=False)
		context['templates'] = Budget.objects.filter(user=self.request.user, template=True)
		return context

	def form_valid(self, form):
		name = form.instance.name
		template = form.instance.template
		form.instance.user = self.request.user
		copy_id = None
		if self.request.POST['copy'] == 'template':
			copy_id = int(self.request.POST['copy_from_template'])
		if self.request.POST['copy'] == 'budget':
			copy_id = int(self.request.POST['copy_from_budget'])
		form.instance = Budget.objects.get(id=copy_id).copy()
		form.instance.name = name
		form.instance.template = template
		return super().form_valid(form) 

class TemplateCreate(BudgetCreate):
	success_url = reverse_lazy('template_list')

	def form_valid(self, form):
		form.instance.template = True
		return super().form_valid(form) 

class BudgetUpdate(LoginRequiredMixin, UpdateView):
	model = Budget
	fields = ['name']
	success_url = reverse_lazy('budget_list')

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form) 

	def get_object(self):
		budget = super().get_object()
		if budget.user != self.request.user:
			raise PermissionDenied
		return budget

class BudgetDetail(LoginRequiredMixin, DetailView):
	model = Budget

	def get_object(self):
		budget = super().get_object()
		if budget.user != self.request.user:
			raise PermissionDenied
		return budget

class ExpenseCreate(LoginRequiredMixin, CreateView):
	model = Item
	fields = ['name', 'budgeted', 'singleton', 'transfer_to']

	def form_valid(self, form):
		budget = Budget.objects.get(id=self.kwargs['budget_pk'])
		if budget.user != self.request.user:
			raise PermissionDenied
		form.instance.budget = budget
		if self.request.POST['type'] == 'single':
			form.instance.singleton = True
		elif self.request.POST['type'] == 'transfer':
			transfer_id = int(self.request.POST['transfer_to'])
			if transfer_id != budget.id:
				transfer_to = Budget.objects.get(id=transfer_id)
				form.instance.transfer_to = transfer_to
		return super().form_valid(form) 
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Add Expense Item'
		context['budget'] = Budget.objects.get(id=self.kwargs['budget_pk'])
		context['budgets'] = Budget.objects.filter(user=self.request.user, template=False)
		context['expense_create'] = True
		return context

	def get_success_url(self):
		return reverse('budget_detail', kwargs={'pk': self.kwargs['budget_pk']})

class ExpenseUpdate(LoginRequiredMixin, UpdateView):
	model = Item
	fields = ['name', 'budgeted']

	def form_valid(self, form):
		budget = Budget.objects.get(id=self.kwargs['budget_pk'])
		if budget.user != self.request.user:
			raise PermissionDenied
		form.instance.budget = budget
		return super().form_valid(form) 
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Add Expense Item'
		context['budget'] = Budget.objects.get(id=self.kwargs['budget_pk'])
		return context

	def get_object(self):
		item = super().get_object()
		if item.budget.user != self.request.user:
			raise PermissionDenied
		return item

	def get_success_url(self):
		return reverse('budget_detail', kwargs={'pk': self.kwargs['budget_pk']})

class IncomeCreate(LoginRequiredMixin, CreateView):
	model = Item
	fields = ['name', 'budgeted']

	def form_valid(self, form):
		budget = Budget.objects.get(id=self.kwargs['budget_pk'])
		if budget.user != self.request.user:
			raise PermissionDenied
		form.instance.budget = budget
		form.instance.income = True
		return super().form_valid(form) 

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Add Income Item'
		context['budget'] = Budget.objects.get(id=self.kwargs['budget_pk'])
		return context

	def get_success_url(self):
		return reverse('budget_detail', kwargs={'pk': self.kwargs['budget_pk']})

class IncomeUpdate(LoginRequiredMixin, UpdateView):
	model = Item
	fields = ['name', 'budgeted']

	def form_valid(self, form):
		budget = Budget.objects.get(id=self.kwargs['budget_pk'])
		if budget.user != self.request.user:
			raise PermissionDenied
		form.instance.budget = budget
		form.instance.income = True
		return super().form_valid(form) 

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Add Income Item'
		context['budget'] = Budget.objects.get(id=self.kwargs['budget_pk'])
		return context

	def get_object(self):
		item = super().get_object()
		if item.budget.user != self.request.user:
			raise PermissionDenied
		return item

	def get_success_url(self):
		return reverse('budget_detail', kwargs={'pk': self.kwargs['budget_pk']})

class ItemDetail(LoginRequiredMixin, DetailView):
	model = Item

	def get_object(self):
		item = super().get_object()
		if item.budget.user != self.request.user:
			raise PermissionDenied
		return item

def budget_copy(request):
	budget = Budget.objects.get(id=request.POST['budgetID'])
	if budget.user != request.user:
		raise PermissionDenied

	budget.copy()
	return redirect('budget_list')

def budget_delete(request):
	budget = Budget.objects.get(id=request.POST['budgetID'])
	if budget.user != request.user:
		raise PermissionDenied

	budget.delete()
	return redirect('budget_list')

def item_delete(request):
	item = Item.objects.get(id=request.POST['itemID'])
	if item.budget.user != request.user:
		raise PermissionDenied

	budgetID = item.budget.id
	item.delete()
	return redirect('budget_detail', budgetID)

def transaction_create(request):
	item = Item.objects.get(id=request.POST['itemID'])
	if item.budget.user != request.user:
		raise PermissionDenied

	Transaction(
		item=item,
		amount=request.POST['amount'],
		comment=request.POST['comment']
	).save()
	return redirect('item_detail', request.POST['itemID'])

def transaction_delete(request):
	transaction = Transaction.objects.get(id=request.POST['transactionID'])
	if transaction.item.budget.user != request.user:
		raise PermissionDenied

	itemID = transaction.item.id
	transaction.delete()
	return redirect('item_detail', itemID)
