# Generated by Django 2.2.3 on 2019-07-02 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.CharField(default='English', max_length=250),
        ),
    ]