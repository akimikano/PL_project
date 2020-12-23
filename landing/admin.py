from django.contrib import admin
from modeltranslation.admin import TranslationTabularInline, TabbedTranslationAdmin

from .models import MainPage, MainPageFeature, MainPageAdvantage, Delivery, Service, \
    TextService, AboutCompany, Property, Feedback, Contacts, AdvantagesSection, AdvantageItem


#  -------------------Главная страница----------------
class MainPageFeatureTabularInline(TranslationTabularInline):
    model = MainPageFeature
    extra = 0


class MainPageAdvantageTabularInline(TranslationTabularInline):
    model = MainPageAdvantage
    extra = 0


class MainPageAdmin(TabbedTranslationAdmin):
    inlines = [MainPageFeatureTabularInline, MainPageAdvantageTabularInline]

    class Meta:
        model = MainPage

    def has_add_permission(self, request):
        if self.model.objects.count() > 0:
            return False
        else:
            return True


#  -------------------О компании----------------
class PropertyTabularInline(TranslationTabularInline):
    model = Property
    extra = 0


class AboutCompanyAdmin(TabbedTranslationAdmin):
    inlines = [PropertyTabularInline]

    class Meta:
        model = AboutCompany

    def has_add_permission(self, request):
        if self.model.objects.count() > 0:
            return False
        else:
            return True


#  -------------------Услуги----------------
class TextTabularInline(TranslationTabularInline):
    model = TextService
    extra = 0


class ServiceTabularInline(TranslationTabularInline):
    model = Service
    extra = 0


class DeliveryAdmin(TabbedTranslationAdmin):
    inlines = [ServiceTabularInline, TextTabularInline]

    class Meta:
        model = Delivery

    def has_add_permission(self, request):
        if self.model.objects.count() > 0:
            return False
        else:
            return True


#  -------------------Преимущества----------------
class AdvantageItemTabularInline(TranslationTabularInline):
    model = AdvantageItem
    extra = 0


class AdvantagesSectionAdmin(TabbedTranslationAdmin):
    inlines = [AdvantageItemTabularInline]

    class Meta:
        model = AdvantagesSection

    def has_add_permission(self, request):
        if self.model.objects.count() > 0:
            return False
        else:
            return True


#  -------------------Контакты----------------
class ContactsAdmin(TabbedTranslationAdmin):
    class Meta:
        model = Contacts

    def has_add_permission(self, request):
        if self.model.objects.count() > 0:
            return False
        else:
            return True


admin.site.register(Feedback)
admin.site.register(MainPage, MainPageAdmin)
admin.site.register(Contacts, ContactsAdmin)
admin.site.register(AdvantagesSection, AdvantagesSectionAdmin)
admin.site.register(Delivery, DeliveryAdmin)
admin.site.register(AboutCompany, AboutCompanyAdmin)
