from django.db import models

class Budget(models.Model):
	name = models.CharField(max_length=200)
	last_modified = models.DateTimeField(auto_now=True)

	def balance(self):
		balance = 0
		for item in self.item_set.all():
			total = item.total
			if(item.income):
				balance += total
			else:
				balance -= total
		return balance

	def __str__(self):
		return self.name

class Item(models.Model):
	budget = models.ForeignKey('Budget')
	budgeted = models.DecimalField(max_digits=9, decimal_places=2)
	income = models.BooleanField(default=False)

	def total(self):
		total = 0
		for transaction in self.transaction_set.all():
			total += transaction.amount
		return total

class Transaction(models.Model):
	item = models.ForeignKey('Item')
	amount = models.DecimalField(max_digits=9, decimal_places=2)
	comment = models.CharField(max_length=200)
