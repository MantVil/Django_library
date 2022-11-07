# Generated by Django 4.1.3 on 2022-11-07 09:48

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('labrary', '0003_bookinstance'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinstance',
            options={'ordering': ['due_back']},
        ),
        migrations.AlterField(
            model_name='bookinstance',
            name='unique_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='unique ID'),
        ),
    ]