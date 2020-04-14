# Generated by Django 3.0.5 on 2020-04-15 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('match', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Human',
            fields=[
                ('match_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='match.Match')),
                ('avatar', models.ImageField(null=True, upload_to='', verbose_name='Avatar')),
            ],
            options={
                'verbose_name': 'Human',
                'verbose_name_plural': 'Humans',
                'db_table': 'human',
            },
            bases=('match.match',),
        ),
    ]
