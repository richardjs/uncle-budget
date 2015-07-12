from django.conf.urls import url

import unclebudget.views

urlpatterns = [
	url('^$', unclebudget.views.budget_list, name='budget_list'),
]
