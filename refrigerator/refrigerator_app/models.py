from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser


class FoodCategory(models.Model):
    """カテゴリー"""
    name = models.CharField(
        max_length=20,
        help_text="食品のカテゴリー。「野菜」など"
    )


class Food(models.Model):
    """食品"""
    category = models.ForeignKey(
        FoodCategory,
        help_text="食品のカテゴリー",
        on_delete=models.CASCADE
    )

    name = models.CharField(
        max_length=50,
        help_text="食品の名前"
    )


class User(models.Model):
    """ユーザー"""
    name = models.CharField(
        max_length=50,
        help_text="ユーザーの名前"
    )


class Stock(models.Model):
    """在庫"""
    food = models.ForeignKey(
        Food,
        help_text="どの食品の在庫なのか",
        on_delete=models.CASCADE
    )

    put_by = models.ForeignKey(
        User,
        help_text="在庫を入れた人",
        on_delete=models.CASCADE
    )

    amount = models.PositiveSmallIntegerField(
        help_text="在庫の個数"
    )

    expiration_date = models.DateField(
        help_text="消費期限"
    )
