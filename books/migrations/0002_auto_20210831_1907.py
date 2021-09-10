# Generated by Django 3.2.5 on 2021-08-31 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='longDescription',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='pageCount',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='book',
            name='shortDescription',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='thumbnailUrl',
            field=models.CharField(max_length=256, null=True),
        ),
    ]
