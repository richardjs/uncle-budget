from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView

import unclebudget.views

urlpatterns = [
	url(r'^$', unclebudget.views.BudgetList.as_view(), name='budget_list'),
	url('^budget_create$', unclebudget.views.BudgetCreate.as_view(), name='budget_create'),
	url(r'^budget/(?P<pk>\d+)$', unclebudget.views.BudgetDetail.as_view(), name='budget_detail'),
	url(r'^budget/(?P<budget_pk>\d+)/income_create$', unclebudget.views.IncomeCreate.as_view(), name='income_create'),
	url(r'^budget/(?P<budget_pk>\d+)/income_update/(?P<pk>\d+)$', unclebudget.views.IncomeUpdate.as_view(), name='income_update'),
	url(r'^budget/(?P<budget_pk>\d+)/expense_create$', unclebudget.views.ExpenseCreate.as_view(), name='expense_create'),
	url(r'^budget/(?P<budget_pk>\d+)/expense_update/(?P<pk>\d+)$', unclebudget.views.ExpenseUpdate.as_view(), name='expense_update'),

	url(r'^item/(?P<pk>\d+)$', unclebudget.views.ItemDetail.as_view(), name='item_detail'),

	# POST endpoints
	url(r'^item_delete$', unclebudget.views.item_delete, name='item_delete'),
	url(r'^transaction_create$', unclebudget.views.transaction_create, name='transaction_create'),
	url(r'^transaction_delete$', unclebudget.views.transaction_delete, name='transaction_delete'),
]
