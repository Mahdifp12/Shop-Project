from django.shortcuts import render
from django.views import View

from .forms import RegisterForm


# Create your views here.

class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        context = {
            "register_form": register_form
        }

        return render(request, 'account_app/register.html', context)

    def post(self, request):
        register_form = RegisterForm(request.POST or None)

        if register_form.is_valid():
            print(register_form.cleaned_data)

        context = {
            "register_form": register_form
        }

        return render(request, 'account_app/register.html', context)
