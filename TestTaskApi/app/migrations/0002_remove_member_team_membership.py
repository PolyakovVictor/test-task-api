# Generated by Django 5.0.1 on 2024-01-15 17:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='team',
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='memberships', to='app.member')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='memberships', to='app.team')),
            ],
        ),
    ]