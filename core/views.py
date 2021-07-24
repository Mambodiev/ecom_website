
from django.utils.translation import gettext as _
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import reverse
from django.views import generic
from django.views.generic.edit import FormView
from django.shortcuts import render

from django.core import paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .forms import ContactForm
from cart.models import Product
from core.models import (                      
                        About,
                        Faq,
                        Terms_of_use,
                        Privacy_policy,
                        Shipping_returns,
                        Carousel,
                        )

def home(request):

    product = Product.objects.all()
    carousel = Carousel.objects.all()

    paginator = Paginator(product, per_page=4)
    page_number = request.GET.get('page',1)
    page_obj = paginator.get_page(page_number)

    products_latest = Product.objects.all().order_by('id')[:4]
    products_picked = Product.objects.all().order_by('?')[:4]


    context = {
        'page': 'page',
        'product': page_obj.object_list,
        'carousel': carousel,
        'paginator': paginator,
        'page_number': int(page_number),
        'products_latest':products_latest,
        'products_picked':products_picked,
    }

    return render(request, 'index.html',context)

    


class ContactView(generic.FormView):
    form_class=ContactForm
    template_name = "contact.html"

    def get_success_url(self):
        return reverse("contact")

    def form_valid(self, form):
        messages.info(
            self.request, "Thanks for getting in touch. We have received your message.")
        name = form.cleaned_data.get(_('name'))
        email = form.cleaned_data.get(_('email'))
        message = form.cleaned_data.get(_('message'))

        full_message = f"""
            Received message below from {name}, {email}
            ________________________


            {message}
            """
        send_mail(
            subject="Received contact form submission",
            message=full_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.NOTIFY_EMAIL]
        )
        return super(ContactView, self).form_valid(form)


class AboutView(generic.TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context['about'] = About.objects.all()
        return context

class FaqView(generic.TemplateView):
    template_name = "faq.html"

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context['faq'] = Faq.objects.all()
        return context


class Terms_of_useView(generic.TemplateView):
    template_name = "terms_of_use.html"

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context['terms_of_use'] = Terms_of_use.objects.all()
        return context

        
class Privacy_policyView(generic.TemplateView):
    template_name = "privacy_policy.html"

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context['privacy_policy'] = Privacy_policy.objects.all()
        return context


class Shipping_returnsView(generic.TemplateView):
    template_name = "shipping_returns.html"


    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context['shipping_returns'] = Shipping_returns.objects.all()
        return context