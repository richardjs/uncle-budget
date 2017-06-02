from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView

import unclebudget.views

urlpatterns = [
	url(r'^$', unclebudget.views.ActiveBudgetList.as_view(), name='budget_list'),
	url(r'^all$', unclebudget.views.AllBudgetList.as_view(), name='all_budget_list'),

	url('^budget_create$', unclebudget.views.BudgetCreate.as_view(), name='budget_create'),
	url(r'^budget/(?P<pk>\d+)$', unclebudget.views.BudgetDetail.as_view(), name='budget_detail'),
	url(r'^budget/(?P<pk>\d+)/update$', unclebudget.views.BudgetUpdate.as_view(), name='budget_update'),

	url(r'^budget/(?P<budget_pk>\d+)/income_create$', unclebudget.views.IncomeCreate.as_view(), name='income_create'),
	url(r'^budget/(?P<budget_pk>\d+)/income_update/(?P<pk>\d+)$', unclebudget.views.IncomeUpdate.as_view(), name='income_update'),
	url(r'^budget/(?P<budget_pk>\d+)/expense_create$', unclebudget.views.ExpenseCreate.as_view(), name='expense_create'),
	url(r'^budget/(?P<budget_pk>\d+)/expense_update/(?P<pk>\d+)$', unclebudget.views.ExpenseUpdate.as_view(), name='expense_update'),

	url(r'^item/(?P<pk>\d+)$', unclebudget.views.ItemDetail.as_view(), name='item_detail'),

	url(r'^templates$', unclebudget.views.TemplateList.as_view(), name='template_list'),
	url(r'^template_create$', unclebudget.views.TemplateCreate.as_view(), name='template_create'),

	# POST endpoints
	url(r'^budget_copy$', unclebudget.views.budget_copy, name='budget_copy'),
	url(r'^budget_delete$', unclebudget.views.budget_delete, name='budget_delete'),
	url(r'^item_delete$', unclebudget.views.item_delete, name='item_delete'),
	url(r'^transaction_create$', unclebudget.views.transaction_create, name='transaction_create'),
	url(r'^transaction_delete$', unclebudget.views.transaction_delete, name='transaction_delete'),
	url(r'^singleton_pay$', unclebudget.views.singleton_pay, name='singleton_pay'),
]
