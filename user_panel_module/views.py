from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView


# Create your views here.

class UserPanelDashboardPage(TemplateView):
    template_name = "user_panel_module/user_panel_page.html"


class EditUserProfilePage(View):
    def get(self, request: HttpRequest):
        return render(request, '', {})

    def post(self, request: HttpRequest):
        pass


def user_panel_menu_component(request: HttpRequest):
    return render(request, "components/user_panel_menu_component.html")
