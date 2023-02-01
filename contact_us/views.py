from django.views.generic.edit import CreateView
from .forms import ContactUsModelForm
from .models import ContactUs


class ContactUsView(CreateView):
    model = ContactUs
    form_class = ContactUsModelForm
    template_name = "contact_us/contact_us_page.html"
    success_url = "/"
