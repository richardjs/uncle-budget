from django.contrib import admin

from unclebudget.models import Budget, Item, Transaction

admin.site.register(Budget)
admin.site.register(Item)
admin.site.register(Transaction)
