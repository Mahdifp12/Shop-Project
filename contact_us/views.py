from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.views import View
from .forms import ContactUsModelForm


class ContactUsView(CreateView):
    form_class = ContactUsModelForm
    template_name = "contact_us/contact_us_page.html"
    success_url = "/"


class CreateProfileView(View):
    def get(self, request):
        return render(request, 'contact_us/create_profile.html', context={})

    def post(self, request):
        print(request.FILES)
        return redirect('/contact-us/profile')
