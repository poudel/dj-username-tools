# Generated by Django 2.0.2 on 2018-02-23 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UsernameBlacklist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(help_text='Username to black list', max_length=250, unique=True, verbose_name='username')),
                ('is_blocked', models.BooleanField(default=True, help_text="Set this to False if you need to whitelist this username but don't want to delete it. This also ensures that a whitelisted username will stay whitelisted when re-populating using the `populate` manager method.", verbose_name='is blocked')),
            ],
        ),
    ]
