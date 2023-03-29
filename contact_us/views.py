from django.views.generic import ListView
from django.views.generic.edit import CreateView

from site_settings_module.models import SiteSettings
from .forms import ContactUsModelForm
from .models import UserProfile


class ContactUsView(CreateView):
    form_class = ContactUsModelForm
    template_name = "contact_us/contact_us_page.html"
    success_url = "/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["settings"]: SiteSettings = SiteSettings.objects.filter(is_main_setting=True).first()
        return context


class CreateProfileView(CreateView):
    template_name = "contact_us/create_profile.html"
    model = UserProfile
    fields = "__all__"
    success_url = "/contact-us/profile/"


class ProfilesView(ListView):
    model = UserProfile
    template_name = "contact_us/profile_list.html"
    context_object_name = "profiles"
