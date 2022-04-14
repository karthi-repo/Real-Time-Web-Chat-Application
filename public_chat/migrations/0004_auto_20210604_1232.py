# Generated by Django 2.2.19 on 2021-06-04 12:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('public_chat', '0003_publicchatroom_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicchatroom',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL),
        ),
    ]