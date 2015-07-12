from django.db import models

class Budget(models.Model):
	name = models.CharField(max_length=200)
	last_modified = models.DateTimeField(auto_now=True)

	def balance(self):
		balance = 0
		for item in self.item_set.all():
			total = item.total()
			if(item.income):
				balance += total
			else:
				balance -= total
		return balance
	
	def income(self):
		return self.item_set.filter(income=True)

	def expenses(self):
		return self.item_set.filter(income=False)
	
	def __str__(self):
		return self.name

class Item(models.Model):
	budget = models.ForeignKey('Budget')
	name = models.CharField(max_length=200)
	budgeted = models.DecimalField(max_digits=9, decimal_places=2, blank=True)#, null=True)
	income = models.BooleanField(default=False)

	def total(self):
		total = 0
		for transaction in self.transaction_set.all():
			total += transaction.amount
		return total
	
	def __str__(self):
		return '%s - %s' % (self.name, self.budget.name)

class Transaction(models.Model):
	item = models.ForeignKey('Item')
	amount = models.DecimalField(max_digits=9, decimal_places=2)
	comment = models.CharField(max_length=200)

	def __str__(self):
		return '%s - $%.2f' % (self.comment, self.amount)
