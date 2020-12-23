from modeltranslation.translator import TranslationOptions, register

from .models import MainPage, MainPageFeature, MainPageAdvantage, AboutCompany, Property, Delivery, Service,TextService, \
                    AdvantagesSection, AdvantageItem, Contacts


@register(MainPage)
class MainPageTO(TranslationOptions):
    fields = ('first_title', 'first_description', 'second_title', 'second_description')\



@register(MainPageFeature)
class MainPageFeatureTO(TranslationOptions):
    fields = ('title',)


@register(MainPageAdvantage)
class MainPageAdvantageTO(TranslationOptions):
    fields = ('title', 'description')


@register(AboutCompany)
class AboutCompanyTO(TranslationOptions):
    fields = ('heading', 'text',)


@register(Property)
class PropertyTO(TranslationOptions):
    fields = ('description',)


@register(Delivery)
class DeliveryTO(TranslationOptions):
    fields = ('title',)


@register(Service)
class ServiceTO(TranslationOptions):
    fields = ('title',)


@register(TextService)
class TextServiceTO(TranslationOptions):
    fields = ('title',)


@register(AdvantagesSection)
class AdvantagesSectionTO(TranslationOptions):
    fields = ('title',)


@register(AdvantageItem)
class AdvantageItemTO(TranslationOptions):
    fields = ('title', 'description')


@register(Contacts)
class ContactsTO(TranslationOptions):
    fields = ('address', 'policy', 'personal_data', 'index',)