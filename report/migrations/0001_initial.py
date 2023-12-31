# Generated by Django 4.2.5 on 2023-09-24 01:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diagnosed_with', models.CharField(choices=[('nothing', 'nothing'), ('covid', 'covid'), ('common cold', 'common cold'), ('stomach bug', 'stomach bug')], max_length=20)),
                ('lives_at', models.CharField(choices=[('kardon', 'kardon'), ('atlantic', 'atlantic'), ('university', 'university'), ('james_s_white', 'james_s_white'), ('j_h', 'j_h'), ('nineteen_forty', 'nineteen_forty'), ('conwell', 'conwell'), ('edge', 'edge'), ('morgan_hall', 'morgan_hall'), ('oxford_village', 'oxford_village'), ('thirteen', 'thirteen'), ('temple_towers', 'temple_towers'), ('beech', 'beech')], max_length=20)),
                ('symptoms', models.JSONField(default=dict)),
                ('smoked', models.BooleanField()),
                ('drank', models.BooleanField()),
                ('around_sick', models.BooleanField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
