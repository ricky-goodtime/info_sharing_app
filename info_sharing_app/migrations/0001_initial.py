# Generated by Django 3.1.2 on 2020-10-27 13:07

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=100)),
                ('info_about', models.IntegerField(choices=[(1, '業務連絡'), (2, '日程調整'), (3, '人事異動'), (4, 'その他')])),
                ('text', models.TextField()),
                ('shared_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person', models.CharField(max_length=20)),
                ('comment_about', models.IntegerField(choices=[(1, '補足'), (2, '意見'), (3, 'その他')])),
                ('text', models.TextField()),
                ('info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='info_sharing_app.info')),
            ],
        ),
    ]
