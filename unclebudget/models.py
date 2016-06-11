from django.db import models

class Budget(models.Model):
	name = models.CharField(max_length=200)
	last_modified = models.DateTimeField(auto_now=True)

	@property
	def surplus(self):
		balance = 0
		for item in self.item_set.all():
			budgeted = item.budgeted
			if(item.income):
				balance += budgeted
			else:
				balance -= budgeted
		return balance

	@property
	def balance(self):
		balance = 0
		for item in self.item_set.all():
			total = item.total
			if(item.income):
				balance += total
			else:
				balance -= total
		return balance
	
	@property
	def income(self):
		return self.item_set.filter(income=True)

	@property
	def income_budgeted(self):
		return sum(item.budgeted for item in self.item_set.filter(income=True))

	@property
	def income_total(self):
		return sum(item.total for item in self.item_set.filter(income=True))

	@property
	def expenses(self):
		return self.item_set.filter(income=False)

	@property
	def expenses_budgeted(self):
		return sum(item.budgeted for item in self.item_set.filter(income=False))

	@property
	def expenses_total(self):
		return sum(item.total for item in self.item_set.filter(income=False))

	def expenses_remaining(self):
		return self.expenses_budgeted - self.expenses_total

	def __str__(self):
		return self.name

class Item(models.Model):
	budget = models.ForeignKey('Budget')
	name = models.CharField(max_length=200)
	budgeted = models.DecimalField(max_digits=9, decimal_places=2, blank=True)#, null=True)
	income = models.BooleanField(default=False)
	singleton = models.BooleanField(default=False)

	@property
	def total(self):
		if self.singleton:
			return self.budgeted
		total = 0
		for transaction in self.transaction_set.all():
			total += transaction.amount
		return total
	
	@property
	def remaining(self):
		return self.budgeted - self.total
	
	def __str__(self):
		return '%s - %s' % (self.name, self.budget.name)

class Transaction(models.Model):
	item = models.ForeignKey('Item')
	amount = models.DecimalField(max_digits=9, decimal_places=2)
	comment = models.CharField(max_length=200)

	def __str__(self):
		return '%s - $%.2f' % (self.comment, self.amount)
