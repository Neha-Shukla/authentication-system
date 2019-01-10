# Generated by Django 2.1.4 on 2018-12-19 04:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.CharField(max_length=250)),
                ('album_title', models.CharField(max_length=500)),
                ('genre', models.CharField(max_length=100)),
                ('album_logo', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_type', models.CharField(max_length=10)),
                ('song_title', models.CharField(max_length=250)),
                ('audio_file', models.FileField(blank=True, max_length=10000, null=True, upload_to='')),
                ('video', models.CharField(blank=True, max_length=100, null=True)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.Album')),
            ],
        ),
    ]