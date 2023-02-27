from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home_module/index_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['text'] = ""
        return context


def site_header_component(request):
    return render(
        request,
        template_name="shared/site_header_component.html",
        context={}
    )


def site_footer_component(request):
    return render(
        request,
        template_name="shared/site_footer_component.html",
        context={}
    )
