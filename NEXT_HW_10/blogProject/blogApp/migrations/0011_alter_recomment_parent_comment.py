# Generated by Django 5.0.3 on 2024-04-10 12:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0010_remove_comment_parent_comment_recomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recomment',
            name='parent_comment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='blogApp.comment'),
        ),
    ]
