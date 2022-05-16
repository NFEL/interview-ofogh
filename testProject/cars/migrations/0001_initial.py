# Generated by Django 4.0.4 on 2022-05-15 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('type', models.CharField(choices=[('small', 'small'), ('big', 'big')], max_length=150)),
                ('color', models.CharField(max_length=255)),
                ('length', models.FloatField()),
                ('load_valume', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Color-Name')),
            ],
        ),
    ]