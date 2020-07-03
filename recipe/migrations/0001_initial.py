# Generated by Django 3.0.6 on 2020-05-15 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('veg', 'VEGETARIAN'), ('nveg', 'NON-VEGETARIAN')], max_length=20)),
                ('description', models.CharField(max_length=200)),
                ('ingredients', models.TextField()),
                ('prepare_time', models.CharField(max_length=3)),
                ('cook_time', models.CharField(max_length=3)),
                ('recipe_details', models.TextField()),
                ('added_date', models.DateTimeField(auto_now_add=True)),
                ('photo', models.ImageField(upload_to='food_pics/%Y/%m/%d/')),
                ('video_link', models.CharField(max_length=500)),
                ('who_can_make', models.CharField(choices=[('beg', 'BEGGINER'), ('inter', 'INTERMEDIATE')], max_length=20)),
                ('best_recipe', models.BooleanField(default=False)),
                ('gluten_free', models.BooleanField(default=False)),
                ('show_home', models.BooleanField(default=False)),
            ],
        ),
    ]
