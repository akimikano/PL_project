from django.shortcuts import redirect
from django.views.generic import TemplateView, CreateView

from .forms import FeedbackForm
from .models import MainPage, AdvantagesSection, AboutCompany, Contacts, Delivery, Service, Feedback


class MainPageView(TemplateView):
    template_name = 'landing/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        main_object = MainPage.objects.prefetch_related('features', 'advantages').first()
        advantages_section = AdvantagesSection.objects.prefetch_related('advantages').first()
        about_company = AboutCompany.objects.first()
        delivery = Delivery.objects.prefetch_related('services_service_item').first()
        services = Service.objects.prefetch_related('texts').all()
        # services = Service.objects.prefetch_related('texts').all()
        context['main_page'] = main_object
        context['advantages_section'] = advantages_section
        context['company'] = about_company
        context['delivery'] = delivery
        context['services'] = services
        context['contacts'] = Contacts.objects.first()
        context['form'] = FeedbackForm()

        return context


class FeedbackView(CreateView):
    template_name = 'landing/index.html'
    form_class = FeedbackForm
    model = Feedback
    success_url = '/'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            self.object = form.save(commit=False)
            self.object.save()
            return redirect('index')
        else:
            return redirect('index')
