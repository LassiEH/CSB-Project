# Generated by Django 4.2.4 on 2023-12-05 18:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='question',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='polls.question'),
        ),
    ]
