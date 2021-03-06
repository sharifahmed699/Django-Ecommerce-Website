# Generated by Django 3.1.4 on 2020-12-13 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=40)),
                ('subject', models.CharField(blank=True, max_length=200)),
                ('message', models.TextField(blank=True, max_length=1000)),
                ('status', models.CharField(choices=[('New', 'New'), ('Read', 'Read'), ('Closed', 'Closed')], default='New', max_length=40)),
                ('ip', models.CharField(blank=True, max_length=100)),
                ('Note', models.CharField(blank=True, max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('keywords', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('phone', models.IntegerField()),
                ('faxx', models.CharField(blank=True, max_length=50)),
                ('email', models.EmailField(blank=True, max_length=50, null=True)),
                ('smptserver', models.CharField(max_length=100)),
                ('smptemail', models.EmailField(blank=True, max_length=50, null=True)),
                ('smptpassword', models.CharField(blank=True, max_length=50)),
                ('smptport', models.CharField(blank=True, max_length=100)),
                ('icon', models.ImageField(blank=True, null=True, upload_to='icon/')),
                ('facebook', models.CharField(blank=True, max_length=100)),
                ('instagram', models.CharField(blank=True, max_length=100)),
                ('address', models.TextField()),
                ('contact', models.TextField()),
                ('reference', models.TextField()),
                ('status', models.CharField(choices=[('True', 'True'), ('False', 'false')], max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
