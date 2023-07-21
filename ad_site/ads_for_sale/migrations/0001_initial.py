# Generated by Django 4.2 on 2023-05-11 10:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('main_text', models.TextField(verbose_name='Текст объявления')),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('end_up', models.DateTimeField(verbose_name='Окончание срока публикации')),
                ('moderated', models.BooleanField(default=False)),
                ('hidden', models.BooleanField(default=False)),
                ('blocked', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Категория')),
                ('description', models.CharField(max_length=255)),
                ('hidden', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='UsersSubscribed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ads_for_sale.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_rating', models.IntegerField(default=0)),
                ('author', models.BooleanField(default=True)),
                ('subsribed_to_newsletter', models.BooleanField(default=False)),
                ('mail_confirmed', models.BooleanField(default=False)),
                ('banned', models.BooleanField(default=False)),
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Replies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('ad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ads_for_sale.ads')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(default='default_userpic.png', upload_to='images/profile/')),
                ('bio', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='user',
            field=models.ManyToManyField(through='ads_for_sale.UsersSubscribed', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='AdsCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ads_for_sale.ads', verbose_name='Объявление')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ads_for_sale.category', verbose_name='Категория')),
            ],
        ),
        migrations.AddField(
            model_name='ads',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ads_for_sale.users', verbose_name='Автор'),
        ),
        migrations.AddField(
            model_name='ads',
            name='category',
            field=models.ManyToManyField(through='ads_for_sale.AdsCategory', to='ads_for_sale.category', verbose_name='Категория'),
        ),
    ]