# Generated by Django 3.1.2 on 2022-07-28 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0003_blogs_links'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='video',
            field=models.CharField(max_length=1200, null=True),
        ),
    ]
