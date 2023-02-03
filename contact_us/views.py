from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.views import View
from .forms import ContactUsModelForm, ProfileForm
from .models import UserProfile


class ContactUsView(CreateView):
    form_class = ContactUsModelForm
    template_name = "contact_us/contact_us_page.html"
    success_url = "/"


class CreateProfileView(View):
    def get(self, request):
        form = ProfileForm()
        return render(request, 'contact_us/create_profile.html', context={
            'form': form
        })

    def post(self, request):
        form_submited = ProfileForm(request.POST, request.FILES)

        if form_submited.is_valid():
            # get_file(request.FILES['profile'])
            profile = UserProfile(image=request.FILES['user_image'])
            profile.save()
            return redirect('/contact-us/profile')

        return render(request, 'contact_us/create_profile.html', context={
            'form': form_submited
        })
