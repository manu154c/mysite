# Generated by Django 3.0.3 on 2020-06-14 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='tagline',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=255)),
                ('body_text', models.TextField()),
                ('pub_date', models.DateField()),
                ('mod_date', models.DateField()),
                ('number_of_comments', models.IntegerField()),
                ('number_of_pingbacks', models.IntegerField()),
                ('rating', models.IntegerField()),
                ('authors', models.ManyToManyField(to='blog.Author')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Blog')),
            ],
        ),
    ]