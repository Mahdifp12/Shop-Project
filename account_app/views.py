from django.shortcuts import render
from django.views import View
from .models import User
from .forms import RegisterForm
from django.utils.crypto import get_random_string


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
            user_email = register_form.cleaned_data.get("email")
            user_password = register_form.cleaned_data.get("password")
            user: bool = User.objects.filter(email__iexact=user_email).exists()
            if user:
                register_form.add_error('email', 'ایمیل وارد شده تکراری میباشد')

            else:
                new_user = User(email=user_email, email_active_code=get_random_string(72))
                new_user.set_password(user_password)
                new_user.save()
                # todo: send email active code
        context = {
            "register_form": register_form
        }

        return render(request, 'account_app/register.html', context)
