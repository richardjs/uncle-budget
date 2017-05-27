from django.contrib.auth.models import User
from django.db import models

class Budget(models.Model):
	name = models.CharField(max_length=200)
	last_modified = models.DateTimeField(auto_now=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	template = models.BooleanField(default=False)

	@property
	def surplus(self):
		balance = 0
		for item in self.income:
			balance += item.budgeted
		for item in self.item_set.filter(income=False):
			balance -= item.budgeted
		return balance

	@property
	def balance(self):
		balance = 0
		for item in self.income:
			balance += item.total
		for item in self.item_set.filter(income=False):
			balance -= item.total
		return balance
	
	@property
	def income(self):
		return self.item_set.filter(income=True).union(self.transfer_set.all()).order_by('-budgeted')

	@property
	def income_budgeted(self):
		return sum(item.budgeted for item in self.income)

	@property
	def income_total(self):
		return sum(item.total for item in self.income)

	@property
	def expenses(self):
		return self.item_set.filter(income=False).order_by('singleton', '-budgeted')

	@property
	def expenses_budgeted(self):
		return sum(item.budgeted for item in self.item_set.filter(income=False))

	@property
	def expenses_total(self):
		return sum(item.total for item in self.item_set.filter(income=False))

	def expenses_remaining(self):
		return self.expenses_budgeted - self.expenses_total
	
	def copy(self):
		copy = Budget.objects.get(id=self.id)
		copy.pk = None
		copy.name = 'Copy of ' + copy.name
		copy.save()
		for item in self.item_set.all():
			transactions = item.transaction_set.all()
			item.pk = None
			item.budget = copy
			item.save()
			for transaction in transactions:
				transaction.pk = None
				transaction.item = item
				transaction.save()
		return copy

	def __str__(self):
		return self.name

class Item(models.Model):
	budget = models.ForeignKey('Budget', on_delete=models.CASCADE)

	name = models.CharField(max_length=200)
	budgeted = models.DecimalField(max_digits=9, decimal_places=2, blank=True)#, null=True)
	income = models.BooleanField(default=False)
	singleton = models.BooleanField(default=False)

	transfer_to = models.ForeignKey('Budget', related_name='transfer_set', blank=True, null=True)
	
	@property
	def remaining(self):
		return self.budgeted - self.total
	
	def save(self):
		if self.income:
			self.singleton = True
		if self.transfer_to:
			self.singleton = True
		super().save()

	@property
	def total(self):
		if self.singleton or self.income:
			return self.budgeted
		total = 0
		for transaction in self.transaction_set.all():
			total += transaction.amount
		return total
	
	def __str__(self):
		return '%s - %s' % (self.name, self.budget.name)
	
class Transaction(models.Model):
	item = models.ForeignKey('Item', on_delete=models.CASCADE)
	amount = models.DecimalField(max_digits=9, decimal_places=2)
	comment = models.CharField(max_length=200)

	def __str__(self):
		return '%s - $%.2f' % (self.comment, self.amount)
