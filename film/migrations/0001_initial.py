# Generated by Django 4.0.2 on 2022-02-19 13:17

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('slug', models.SlugField(max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, unique=True)),
                ('rating', models.PositiveSmallIntegerField()),
                ('img', models.ImageField(null=True, upload_to='images')),
                ('description', models.TextField()),
                ('body', models.CharField(max_length=140)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='films', to='film.category')),
            ],
        ),
        migrations.CreateModel(
            name='VideoReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('rating', models.PositiveIntegerField(default=1)),
                ('like', models.PositiveSmallIntegerField(default=0)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to=settings.AUTH_USER_MODEL)),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='film.video')),
            ],
        ),
        migrations.CreateModel(
            name='VideoPlay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('film', models.FileField(blank=True, null=True, upload_to='videos', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4'])])),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='film.video')),
            ],
        ),
    ]
