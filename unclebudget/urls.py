from django.conf.urls import url

import unclebudget.views

urlpatterns = [
	url('^$', unclebudget.views.budget_list, name='budget_list'),
	url('^budget/(\d+)$', unclebudget.views.budget_detail, name='budget_detail'),
]
