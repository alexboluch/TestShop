# Generated by Django 3.2 on 2021-09-23 14:26

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewPrice',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('new_price', models.IntegerField()),
                ('changes_date', models.DateTimeField(auto_now_add=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.item')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.employee')),
            ],
            options={
                'ordering': ['-changes_date'],
            },
        ),
    ]
