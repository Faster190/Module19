# Generated by Django 5.1.2 on 2024-10-16 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('balance', models.DecimalField(decimal_places=2, max_digits=8)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=8)),
                ('size', models.DecimalField(decimal_places=2, max_digits=8)),
                ('description', models.TextField()),
                ('age_limited', models.BooleanField(default=True)),
                ('buyer', models.ManyToManyField(related_name='Games', to='task1.buyer')),
            ],
        ),
    ]
