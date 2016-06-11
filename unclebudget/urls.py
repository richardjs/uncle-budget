from django.conf.urls import url

import unclebudget.views

urlpatterns = [
	url('^$', unclebudget.views.budget_list, name='budget_list'),
	url('^budget/(\d+)$', unclebudget.views.budget_detail, name='budget_detail'),
	url('^item/(\d+)$', unclebudget.views.item_detail, name='item_detail'),

	# POST endpoints
	url('^transaction_create$', unclebudget.views.transaction_create, name='transaction_create'),
	url('^transaction_delete$', unclebudget.views.transaction_delete, name='transaction_delete'),
]
