# Generated by Django 4.1b1 on 2024-07-29 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('subtitle', models.CharField(blank=True, max_length=300, null=True)),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='cover_images/')),
                ('key_points', models.JSONField(blank=True, null=True)),
                ('body', models.TextField()),
            ],
        ),
    ]
