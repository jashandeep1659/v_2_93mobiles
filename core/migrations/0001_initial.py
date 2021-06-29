# Generated by Django 3.2.4 on 2021-06-27 10:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='iPhone_Name',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('slug', models.SlugField(max_length=200)),
                ('iPhone_name', models.CharField(max_length=25)),
                ('processor', models.CharField(max_length=110)),
                ('camera', models.CharField(max_length=100)),
                ('display', models.CharField(max_length=100)),
                ('display_panel_type', models.CharField(max_length=100)),
                ('ratings_ips', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Produts_Offers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('i_product', models.IntegerField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-updated_at'],
            },
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('series_name', models.CharField(max_length=25)),
                ('slug', models.SlugField(max_length=200)),
                ('starting_from', models.IntegerField()),
                ('logo_serie', models.ImageField(upload_to='serie/images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('slug', models.SlugField(max_length=200)),
                ('older_price', models.IntegerField()),
                ('new_price', models.IntegerField()),
                ('battery_health', models.IntegerField()),
                ('condition', models.CharField(choices=[('new', 'New'), ('best', ' Best'), ('good', ' Good')], default='best', max_length=100)),
                ('color', models.CharField(max_length=40)),
                ('storage', models.CharField(max_length=100)),
                ('face_id', models.BooleanField(default=True)),
                ('special_note', models.CharField(max_length=1000)),
                ('main_image', models.ImageField(upload_to='main_images/')),
                ('status', models.BooleanField(default='True')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('uploaded_at', models.DateField(auto_now_add=True)),
                ('warranty', models.IntegerField()),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.iphone_name')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='other_product_images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_image', models.ImageField(upload_to='product/images/')),
                ('proudct_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.product')),
            ],
        ),
        migrations.AddField(
            model_name='iphone_name',
            name='of_series',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.series'),
        ),
    ]