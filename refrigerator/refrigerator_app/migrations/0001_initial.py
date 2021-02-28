# Generated by Django 3.1.6 on 2021-02-28 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='食品の名前', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='FoodCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='食品のカテゴリー。「野菜」など', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='ユーザーの名前', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveSmallIntegerField(help_text='在庫の個数')),
                ('expiration_date', models.DateField(help_text='消費期限')),
                ('food', models.ForeignKey(help_text='どの食品の在庫なのか', on_delete=django.db.models.deletion.CASCADE, to='refrigerator_app.food')),
                ('put_by', models.ForeignKey(help_text='在庫を入れた人', on_delete=django.db.models.deletion.CASCADE, to='refrigerator_app.user')),
            ],
        ),
        migrations.AddField(
            model_name='food',
            name='category',
            field=models.ForeignKey(help_text='食品のカテゴリー', on_delete=django.db.models.deletion.CASCADE, to='refrigerator_app.foodcategory'),
        ),
    ]