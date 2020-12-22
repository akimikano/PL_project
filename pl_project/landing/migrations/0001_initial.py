# Generated by Django 3.1.4 on 2020-12-22 17:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutCompany',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(blank=True, max_length=64, null=True, verbose_name='Заголовок')),
                ('photo', models.FileField(blank=True, null=True, upload_to='', verbose_name='Фотография')),
                ('text', models.TextField(blank=True, null=True, verbose_name='Текст')),
            ],
            options={
                'verbose_name': 'О компании',
                'verbose_name_plural': 'О компании',
            },
        ),
        migrations.CreateModel(
            name='AdvantagesSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Преимущества')),
            ],
            options={
                'verbose_name': 'Раздел преимуществ',
                'verbose_name_plural': 'Раздел преимуществ',
            },
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='E-mail')),
                ('phone_number', models.CharField(blank=True, max_length=13, null=True, unique=True, verbose_name='Телефон')),
                ('address', models.CharField(blank=True, max_length=128, null=True, verbose_name='Адрес')),
                ('play_market', models.URLField(blank=True, null=True, verbose_name='Ссылка на Play Market')),
                ('app_store', models.URLField(blank=True, null=True, verbose_name='Ссылка на App Store')),
                ('facebook', models.URLField(blank=True, null=True, verbose_name='Ссылка на Facebook')),
                ('instagram', models.URLField(blank=True, null=True, verbose_name='Ссылка Instagram')),
                ('telegram', models.URLField(blank=True, null=True, verbose_name='Ссылка на Telegram')),
                ('whatsapp', models.URLField(blank=True, null=True, verbose_name='Ссылка на WhatsApp')),
                ('vk', models.URLField(blank=True, null=True, verbose_name='Ссылка на VK')),
                ('policy', models.URLField(blank=True, null=True, verbose_name='Политика конфиденциальности')),
                ('personal_data', models.URLField(blank=True, null=True, verbose_name='Передача персональных данных')),
                ('index', models.CharField(blank=True, max_length=255, null=True, verbose_name='Копирайт')),
            ],
            options={
                'verbose_name': 'Контакт',
                'verbose_name_plural': 'Контакты',
            },
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=32, null=True, verbose_name='Заголовок')),
            ],
            options={
                'verbose_name': 'Услуги(Раздел)',
                'verbose_name_plural': 'Услуги(Раздел)',
            },
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=64, null=True, verbose_name='Имя')),
                ('phone_number', models.CharField(blank=True, max_length=13, null=True, unique=True, verbose_name='Телефон')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
                ('is_confirmed', models.BooleanField(blank=True, null=True, verbose_name='Согласен на обработку персональных данных')),
            ],
            options={
                'verbose_name': 'Обратная связь',
                'verbose_name_plural': 'Обратная связь',
            },
        ),
        migrations.CreateModel(
            name='MainPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seo_title', models.CharField(blank=True, max_length=255, null=True, verbose_name='seo_title')),
                ('seo_description', models.CharField(blank=True, max_length=255, null=True, verbose_name='seo_description')),
                ('seo_keywords', models.CharField(blank=True, max_length=255, null=True, verbose_name='seo_keywords')),
                ('og_title', models.CharField(blank=True, max_length=64, null=True, verbose_name='seo og:title')),
                ('og_image', models.ImageField(blank=True, help_text='изображение, характеризующее страницу', null=True, upload_to='seo', verbose_name='seo og:image')),
                ('og_description', models.TextField(blank=True, help_text='краткое описание страницы длиной не более 300 символов', max_length=300, null=True, verbose_name='seo og:description')),
                ('first_title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок(1)')),
                ('first_description', models.TextField(blank=True, null=True, verbose_name='Описание(1)')),
                ('image', models.FileField(blank=True, null=True, upload_to='')),
                ('second_title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок(2)')),
                ('second_description', models.TextField(blank=True, null=True, verbose_name='Описание(2)')),
                ('play_market', models.URLField(blank=True, null=True, verbose_name='Ссылка на Play Market')),
                ('app_store', models.URLField(blank=True, null=True, verbose_name='Ссылка на App Store')),
                ('facebook', models.URLField(blank=True, null=True, verbose_name='Ссылка на Facebook')),
                ('instagram', models.URLField(blank=True, null=True, verbose_name='Ссылка Instagram')),
                ('telegram', models.URLField(blank=True, null=True, verbose_name='Ссылка на Telegram')),
                ('whatsapp', models.URLField(blank=True, null=True, verbose_name='Ссылка на WhatsApp')),
            ],
            options={
                'verbose_name': 'Главная страница',
                'verbose_name_plural': 'Главная страница',
            },
        ),
        migrations.CreateModel(
            name='TextService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=32, null=True, verbose_name='Название')),
                ('delivery', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='services_text', to='landing.delivery', verbose_name='Доставка')),
            ],
            options={
                'verbose_name_plural': 'Услуги(Текст)',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.FileField(blank=True, null=True, upload_to='', verbose_name='Фотография')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок')),
                ('delivery', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='services_service_item', to='landing.delivery', verbose_name='Доставка')),
                ('texts', models.ManyToManyField(blank=True, null=True, related_name='texts', to='landing.TextService', verbose_name='Строки')),
            ],
            options={
                'verbose_name': 'Услуга',
                'verbose_name_plural': 'Услуги',
            },
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(blank=True, max_length=16, null=True, verbose_name='Цифра')),
                ('description', models.CharField(blank=True, max_length=128, null=True, verbose_name='Описание')),
                ('about_company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='properties', to='landing.aboutcompany', verbose_name='О компании')),
            ],
            options={
                'verbose_name_plural': 'По свойства',
            },
        ),
        migrations.CreateModel(
            name='MainPageFeature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок')),
                ('image', models.FileField(blank=True, null=True, upload_to='', verbose_name='Иконка')),
                ('fk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='features', to='landing.mainpage', verbose_name='Главная')),
            ],
            options={
                'verbose_name': 'Возможность',
                'verbose_name_plural': 'Возможности',
            },
        ),
        migrations.CreateModel(
            name='MainPageAdvantage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('image', models.FileField(blank=True, null=True, upload_to='', verbose_name='Иконка')),
                ('fk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='advantages', to='landing.mainpage', verbose_name='Главная страница')),
            ],
            options={
                'verbose_name': 'Главная страница(Преимущество)',
                'verbose_name_plural': 'Главная страница(Преимущества)',
            },
        ),
        migrations.CreateModel(
            name='AdvantageItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Заглавие')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('image', models.FileField(blank=True, null=True, upload_to='', verbose_name='Иконка')),
                ('fk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='advantages', to='landing.advantagessection', verbose_name='Раздел')),
            ],
            options={
                'verbose_name': 'Преимущество',
                'verbose_name_plural': 'Преимущества',
            },
        ),
    ]
