# Generated by Django 3.0.5 on 2020-04-14 06:05

from django.db import migrations, models
import human.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Human',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(upload_to='', verbose_name='Avatar')),
            ],
            options={
                'verbose_name': 'Human',
                'verbose_name_plural': 'Humans',
            },
            bases=(human.models.HumanMixin, models.Model),
        ),
    ]
