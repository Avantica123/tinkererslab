# Generated by Django 3.2.6 on 2021-08-11 04:49

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Userform',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.user')),
                ('select_type', models.CharField(choices=[('student', 'student'), ('teacher', 'teacher')], max_length=80)),
                ('institute', models.CharField(max_length=100)),
                ('department', models.CharField(choices=[('Computer Engineering', 'Computer Engineering'), ('Information Technology', 'Information Technology'), ('Civil Engineering', 'Civil Engineering'), ('Mechanical Engineering', 'Mechanical Engineering'), ('Chemical Engineering', 'Chemical Engineering'), ('Electronics and Telecommunication Engineering', 'Electronics and Telecommunication Engineering'), ('Instrumentation and Control Engineering', 'Instrumentation and Control Engineering'), ('Automation and Robotics', 'Automation and Robotics'), ('Applied Science', 'Applied Science')], max_length=80)),
                ('passout_year', models.IntegerField(choices=[('2018', '2018'), ('2019', '2019'), ('2020', '2020'), ('2021', '2021'), ('2022', '2022'), ('2023', '2023'), ('2024', '2024')])),
                ('number', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]