from django.views.generic.edit import CreateView

from .forms import ContactUsModelForm, ProfileForm
from .models import UserProfile


class ContactUsView(CreateView):
    form_class = ContactUsModelForm
    template_name = "contact_us/contact_us_page.html"
    success_url = "/"


class CreateProfileView(CreateView):
    template_name = "contact_us/create_profile.html"
    model = UserProfile
    fields = "__all__"
    success_url = "/contact-us/profile/"
