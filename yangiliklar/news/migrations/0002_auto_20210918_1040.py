# Generated by Django 3.2.7 on 2021-09-18 05:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Yangilik turi')),
            ],
            options={
                'verbose_name': 'Yangilik turi',
                'verbose_name_plural': 'Yangilik turlari',
            },
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'Yangilik', 'verbose_name_plural': 'Yangiliklar'},
        ),
        migrations.AlterField(
            model_name='news',
            name='content',
            field=models.TextField(blank=True, verbose_name='Yangilik matni'),
        ),
        migrations.AlterField(
            model_name='news',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan vaqti'),
        ),
        migrations.AlterField(
            model_name='news',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Chop qilinganligi'),
        ),
        migrations.AlterField(
            model_name='news',
            name='photo',
            field=models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Rasm'),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=150, verbose_name='Sarlavhasi'),
        ),
        migrations.AlterField(
            model_name='news',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name="O'zgartirilgan vaqti"),
        ),
        migrations.AddField(
            model_name='news',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='news.category'),
        ),
    ]
