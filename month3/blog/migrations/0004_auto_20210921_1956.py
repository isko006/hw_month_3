# Generated by Django 3.2.6 on 2021-09-21 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('university', models.CharField(max_length=100)),
                ('faculty', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=1)),
            ],
        ),
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='hashtags',
            new_name='hashtag',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='blog',
            new_name='blog',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='datetime',
            new_name='date',
        ),
        migrations.AddField(
            model_name='blog',
            name='date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(upload_to='blog_pics'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(default=''),
        ),
    ]