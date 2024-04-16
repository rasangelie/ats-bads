# Generated by Django 5.0.4 on 2024-04-16 15:32

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobPosition',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('position', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TechStack',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('tech_stack', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('content', models.TextField()),
                ('created_at', models.TimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.user')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('middle_initial', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email_address', models.EmailField(max_length=254)),
                ('resume_url', models.URLField()),
                ('assignees', models.CharField(max_length=100)),
                ('created_at', models.TimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('comments', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.comment')),
                ('job_position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.jobposition')),
                ('tech_stacks', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.techstack')),
            ],
        ),
        migrations.CreateModel(
            name='TicketProgress',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('progress', models.IntegerField(choices=[(1, 'Application'), (2, 'Screening'), (3, 'For Review'), (4, 'Interviewing'), (5, 'Trial Test')], default=1)),
                ('created_at', models.TimeField(auto_now_add=True)),
                ('ticket_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.ticket')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.user')),
            ],
        ),
    ]
