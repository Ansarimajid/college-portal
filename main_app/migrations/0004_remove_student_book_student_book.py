# Generated by Django 4.0.6 on 2022-08-31 09:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_remove_student_book_student_book'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='book',
        ),
        migrations.AddField(
            model_name='student',
            name='book',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.book'),
        ),
    ]
