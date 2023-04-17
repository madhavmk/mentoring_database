# Generated by Django 4.0.3 on 2022-05-17 13:25

from django.db import migrations, models
import django.db.models.deletion
import mentoring.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminEventRegistration',
            fields=[
                ('admin_event_registration_pkey', models.BigAutoField(primary_key=True, serialize=False)),
                ('registration_info', models.JSONField(default=dict)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('event_pkey', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('additional_information', models.JSONField(default=mentoring.models.default_event_additional_info)),
            ],
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('meeting_pkey', models.BigAutoField(primary_key=True, serialize=False)),
                ('additional_info', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('person_pkey', models.BigAutoField(primary_key=True, serialize=False)),
                ('contact_information', models.JSONField(default=mentoring.models.default_person_contact_info)),
                ('personal_information', models.JSONField(default=mentoring.models.default_person_personal_info)),
                ('industry_information', models.JSONField(default=dict)),
                ('educational_information', models.JSONField(default=dict)),
            ],
        ),
        migrations.CreateModel(
            name='MentorEventRegistration',
            fields=[
                ('mentor_event_registration_pkey', models.BigAutoField(primary_key=True, serialize=False)),
                ('registration_info', models.JSONField(default=dict)),
                ('event_pkey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mentoring.event')),
                ('person_pkey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mentoring.person')),
            ],
        ),
        migrations.CreateModel(
            name='MenteeEventRegistration',
            fields=[
                ('mentee_event_registration_pkey', models.BigAutoField(primary_key=True, serialize=False)),
                ('registration_info', models.JSONField(default=dict)),
                ('event_pkey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mentoring.event')),
                ('person_pkey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mentoring.person')),
            ],
        ),
        migrations.CreateModel(
            name='MeetingPersonRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('admin', 'administrator'), ('mentor', 'mentor'), ('mentee', 'mentee')], max_length=13)),
                ('admin_pkey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mentoring.admineventregistration')),
                ('meeting_pkey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mentoring.meeting')),
                ('mentee_pkey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mentoring.menteeeventregistration')),
                ('mentor_pkey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mentoring.mentoreventregistration')),
            ],
        ),
        migrations.AddField(
            model_name='admineventregistration',
            name='event_pkey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mentoring.event'),
        ),
        migrations.AddField(
            model_name='admineventregistration',
            name='person_pkey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mentoring.person'),
        ),
    ]
