from django.db import models


class SEO(models.Model):
    class Meta:
        abstract = True

    seo_title = models.CharField('seo_title', max_length=255, null=True, blank=True)
    seo_description = models.CharField('seo_description', max_length=255, null=True, blank=True)
    seo_keywords = models.CharField('seo_keywords', max_length=255, null=True, blank=True)
    og_title = models.CharField('seo og:title', max_length=64, null=True, blank=True)
    og_image = models.ImageField('seo og:image', upload_to='seo', null=True, blank=True,
                                 help_text='изображение, характеризующее страницу')
    og_description = models.TextField('seo og:description', max_length=300, null=True, blank=True,
                                      help_text='краткое описание страницы длиной не более 300 символов')


class MainPage(SEO):
    class Meta:
        verbose_name = 'Главная страница'
        verbose_name_plural = 'Главная страница'

    first_title = models.CharField(max_length=255, verbose_name='Заголовок(1)', blank=True, null=True)
    first_description = models.TextField(verbose_name='Описание(1)', blank=True, null=True)
    image = models.FileField(blank=True, null=True)
    second_title = models.CharField(max_length=255, verbose_name='Заголовок(2)', blank=True, null=True)
    second_description = models.TextField(verbose_name='Описание(2)', blank=True, null=True)
    play_market = models.URLField(verbose_name='Ссылка на Play Market', blank=True, null=True)
    app_store = models.URLField(verbose_name='Ссылка на App Store', blank=True, null=True)
    facebook = models.URLField(verbose_name='Ссылка на Facebook', blank=True, null=True)
    instagram = models.URLField(verbose_name='Ссылка Instagram', blank=True, null=True)
    telegram = models.URLField(verbose_name='Ссылка на Telegram', blank=True, null=True)
    whatsapp = models.URLField(verbose_name='Ссылка на WhatsApp', blank=True, null=True)

    def __str__(self):
        return self.first_title


class MainPageFeature(models.Model):
    class Meta:
        verbose_name = 'Возможность'
        verbose_name_plural = 'Возможности'

    title = models.CharField(max_length=255, verbose_name='Заголовок', blank=True, null=True)
    image = models.FileField(verbose_name='Иконка', blank=True, null=True)
    fk = models.ForeignKey(MainPage, on_delete=models.CASCADE, verbose_name='Главная', related_name='features',
                           blank=True, null=True)

    def __str__(self):
        return self.title


class MainPageAdvantage(models.Model):
    class Meta:
        verbose_name = 'Главная страница(Преимущество)'
        verbose_name_plural = 'Главная страница(Преимущества)'

    title = models.CharField(max_length=255, verbose_name='Заголовок', blank=True, null=True)
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    image = models.FileField(verbose_name='Иконка', blank=True, null=True)
    fk = models.ForeignKey(MainPage, on_delete=models.CASCADE, verbose_name='Главная страница',
                           related_name='advantages', blank=True, null=True)

    def __str__(self):
        return self.title


class Delivery(models.Model):
    title = models.CharField('Заголовок', max_length=32, null=True, blank=True)

    class Meta:
        verbose_name = 'Услуги(Раздел)'
        verbose_name_plural = 'Услуги(Раздел)'

    def __str__(self):
        return self.title


class TextService(models.Model):
    title = models.CharField(verbose_name='Название', max_length=32, blank=True, null=True)
    delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE, verbose_name='Доставка',
                                 related_name='services_text', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Услуги(Текст)'

    def __str__(self):
        return self.title


class Service(models.Model):
    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    photo = models.FileField(verbose_name='Фотография', blank=True, null=True)
    title = models.CharField(verbose_name='Заголовок', max_length=255, blank=True, null=True)
    delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE, verbose_name='Доставка',
                                 related_name='services_service_item', blank=True, null=True)
    texts = models.ManyToManyField(TextService, related_name='texts', verbose_name='Строки', blank=True, null=True)

    def __str__(self):
        return self.title


class AboutCompany(models.Model):
    class Meta:
        verbose_name = 'О компании'
        verbose_name_plural = 'О компании'

    heading = models.CharField('Заголовок', max_length=64, blank=True, null=True)
    photo = models.FileField('Фотография', blank=True, null=True)
    text = models.TextField('Текст', blank=True, null=True)

    def __str__(self):
        return str(self.heading)


class Property(models.Model):
    class Meta:
        verbose_name_plural = 'По свойства'

    number = models.CharField('Цифра', max_length=16, blank=True, null=True)
    description = models.CharField('Описание', max_length=128, blank=True, null=True)
    about_company = models.ForeignKey('AboutCompany', on_delete=models.CASCADE, verbose_name='О компании',
                                      related_name='properties', blank=True, null=True)

    def __str__(self):
        return str(self.number)


class Feedback(models.Model):
    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'

    name = models.CharField('Имя', max_length=64, blank=True, null=True)
    phone_number = models.CharField('Телефон', max_length=13, unique=True, blank=True, null=True)
    comment = models.TextField('Комментарий', blank=True, null=True)
    is_confirmed = models.BooleanField('Согласен на обработку персональных данных', blank=True, null=True)

    def __str__(self):
        return self.name


class Contacts(models.Model):
    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    email = models.EmailField('E-mail', blank=True, null=True)
    phone_number = models.CharField('Телефон', max_length=13, unique=True, blank=True, null=True)
    address = models.CharField('Адрес', max_length=128, blank=True, null=True)
    play_market = models.URLField(verbose_name='Ссылка на Play Market', blank=True, null=True)
    app_store = models.URLField(verbose_name='Ссылка на App Store', blank=True, null=True)
    facebook = models.URLField(verbose_name='Ссылка на Facebook', blank=True, null=True)
    instagram = models.URLField(verbose_name='Ссылка Instagram', blank=True, null=True)
    telegram = models.URLField(verbose_name='Ссылка на Telegram', blank=True, null=True)
    whatsapp = models.URLField(verbose_name='Ссылка на WhatsApp', blank=True, null=True)
    vk = models.URLField(verbose_name='Ссылка на VK', blank=True, null=True)
    policy = models.URLField(verbose_name='Политика конфиденциальности', blank=True, null=True)
    personal_data = models.URLField(verbose_name='Передача персональных данных', blank=True, null=True)
    index = models.CharField(verbose_name='Копирайт', max_length=255, blank=True, null=True)


class AdvantagesSection(models.Model):
    class Meta:
        verbose_name = 'Раздел преимуществ'
        verbose_name_plural = 'Раздел преимуществ'

    title = models.CharField(max_length=255, verbose_name='Преимущества', blank=True, null=True)

    def __str__(self):
        return self.title


class AdvantageItem(models.Model):
    class Meta:
        verbose_name = 'Преимущество'
        verbose_name_plural = 'Преимущества'

    title = models.CharField(max_length=255, verbose_name='Заглавие', blank=True, null=True)
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    image = models.FileField(verbose_name='Иконка', blank=True, null=True)
    fk = models.ForeignKey(AdvantagesSection, on_delete=models.CASCADE, related_name='advantages',
                           verbose_name='Раздел', blank=True, null=True)

    def __str__(self):
        return self.title
