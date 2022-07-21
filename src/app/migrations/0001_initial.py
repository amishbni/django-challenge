# Generated by Django 4.0.6 on 2022-07-21 09:46

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=150, verbose_name='First name')),
                ('last_name', models.CharField(max_length=150, verbose_name='Last name')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=150, verbose_name='Title')),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=8)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('user_type', models.CharField(choices=[('user', 'user'), ('admin', 'admin')], default='user', max_length=5)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.user')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
