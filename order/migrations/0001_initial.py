# Generated by Django 3.2.7 on 2022-01-17 11:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0002_productreview_author'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('total_sum', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('order_status', model_utils.fields.StatusField(choices=[('In progress', 'In progress'), ('Canceled', 'Canceled'), ('Finished', 'Finished')], default='In progress', max_length=100, no_check_for_status=True)),
                ('products', models.ManyToManyField(to='product.Product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='orders', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'order',
                'ordering': ['created_at'],
            },
        ),
    ]