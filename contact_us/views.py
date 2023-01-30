from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic.edit import FormView

from .forms import ContactUsModelForm


class ContactUsView(FormView):
    template_name = "contact_us/contact_us_page.html"
    form_class = ContactUsModelForm

    # def post(self, request):
    #     data = request.POST
    #     form = ContactUsModelForm(data=data)
    #
    #     if form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect(reverse('home_page'))
    #
    #     return render(request, "contact_us/contact_us_page.html", context={
    #         'form': form
    #     })
