from django.utils.text import slugify
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "home/home_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        page_title = "Home"
        context["page_title"] = page_title
        context["slug"] = slugify(page_title)

        return context
