from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.views import View
from .forms import ContactUsModelForm


class ContactUsView(CreateView):
    form_class = ContactUsModelForm
    template_name = "contact_us/contact_us_page.html"
    success_url = "/"


def get_file(file):
    with open("temp/image.jpg", "wb+") as dest:
        for ch in file.chunks():
            dest.write(ch)


class CreateProfileView(View):
    def get(self, request):
        return render(request, 'contact_us/create_profile.html', context={})

    def post(self, request):
        get_file(request.FILES['profile'])
        return redirect('/contact-us/profile')
