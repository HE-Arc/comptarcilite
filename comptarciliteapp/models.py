from django.db import models

# Account
class Account(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    members = models.ManyToManyField('auth_user', through='Membership')

# Transactions
class Transaction(models.Model):
    timestamp = models.DateTimeField()
    amount = models.DecimalField(max_digits=16, decimal_places=2)
    description = models.TextField()
    id_account = models.ForeignKey(Account, on_delete=models.CASCADE)
    id_user = models.ForeignKey('auth_user', on_delete=models.SET_NULL, null=True)
    #id_cat = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

#class Category(models.Model):
    #name = models.CharField(max_length=30)
    #description = models.TextField()

class Membership(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    user = models.ForeignKey('auth_user', on_delete=models.CASCADE)
    is_owner = models.BooleanField()

