# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.contrib.auth.models import User
import constants as const


class Category(models.Model):
    name = models.CharField(max_length=const.category_max_length, null=False)


class Groups(models.Model):
    name = models.CharField(max_length=const.group_max_length, null=False)
    members = models.ManyToManyField(User, related_name='members', blank=True)


class Expenses(models.Model):
    description = models.CharField(max_length=const.expenses_max_length)
    total_amount = models.DecimalField(
        max_digits=const.expenses_max_digit, decimal_places=2)
    group = models.ForeignKey(Groups, null=True, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, default=1, on_delete=models.CASCADE)


class UserExpense(models.Model):
    expense = models.ForeignKey(
        Expenses, default=1, on_delete=models.CASCADE, related_name="users")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="expenses")
    amount_owed = models.DecimalField(
        max_digits=const.user_expenses_max_digit, decimal_places=const.user_expenses_decimal_places)
    amount_lent = models.DecimalField(
        max_digits=const.user_expenses_max_digit, decimal_places=const.user_expenses_decimal_places)

    def __str__(self):
        return f"user: {self.user}, amount_owed: {self.amount_owed} amount_lent: {self.amount_lent}"
