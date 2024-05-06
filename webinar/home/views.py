from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import FormView

from webinar.core.forms import RegistrationForm
from webinar.core.models import Webinar


class HomeView(FormView):
    form_class = RegistrationForm
    template_name = "home/home_page.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.save()
        messages.success(
            self.request,
            "Thank you for registering! Please check your mailbox for details. Looking forward to seeing you soon!",
        )

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        wagtail_webinar = Webinar.objects.filter(title__icontains="wagtail").first()

        page_title = "Introduction to Wagtail » Register Now!"
        context["page_title"] = page_title
        context["webinar"] = wagtail_webinar

        return context
