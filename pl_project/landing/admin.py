from django.contrib import admin

from .models import MainPage, MainPageFeature, MainPageAdvantage, Delivery, Service, \
    TextService, AboutCompany, Property, Feedback, Contacts, AdvantagesSection, AdvantageItem


#  -------------------Главная страница----------------
class MainPageFeatureTabularInline(admin.TabularInline):
    model = MainPageFeature
    extra = 0


class MainPageAdvantageTabularInline(admin.TabularInline):
    model = MainPageAdvantage
    extra = 0


class MainPageAdmin(admin.ModelAdmin):
    inlines = [MainPageFeatureTabularInline, MainPageAdvantageTabularInline]

    class Meta:
        model = MainPage

    def has_add_permission(self, request):
        if self.model.objects.count() > 0:
            return False
        else:
            return True


#  -------------------О компании----------------
class PropertyTabularInline(admin.TabularInline):
    model = Property
    extra = 0


class AboutCompanyAdmin(admin.ModelAdmin):
    inlines = [PropertyTabularInline]

    class Meta:
        model = AboutCompany

    def has_add_permission(self, request):
        if self.model.objects.count() > 0:
            return False
        else:
            return True


#  -------------------Услуги----------------
class TextTabularInline(admin.TabularInline):
    model = TextService
    extra = 0


class ServiceTabularInline(admin.TabularInline):
    model = Service
    extra = 0


class DeliveryAdmin(admin.ModelAdmin):
    inlines = [ServiceTabularInline, TextTabularInline]

    class Meta:
        model = Delivery

    def has_add_permission(self, request):
        if self.model.objects.count() > 0:
            return False
        else:
            return True


#  -------------------Преимущества----------------
class AdvantageItemTabularInline(admin.TabularInline):
    model = AdvantageItem
    extra = 0


class AdvantagesSectionAdmin(admin.ModelAdmin):
    inlines = [AdvantageItemTabularInline]

    class Meta:
        model = AdvantagesSection

    def has_add_permission(self, request):
        if self.model.objects.count() > 0:
            return False
        else:
            return True


#  -------------------Контакты----------------
class ContactsAdmin(admin.ModelAdmin):
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
