import logging

import django_rq
from django import forms
from django.db import transaction
from django.utils.http import urlencode
from hcaptcha.fields import hCaptchaField

from webinar.core.mail import send_email
from webinar.core.models import Registration, Webinar
from webinar.core.notifications import send_notification

logger = logging.getLogger(__name__)


class RegistrationForm(forms.ModelForm):
    hcaptcha = hCaptchaField(theme="dark", label="Verification")

    class Meta:
        model = Registration
        fields = [
            "name",
            "email",
            "company",
            "role",
        ]

    def save(self, commit=True):
        instance = super().save(commit=False)

        if commit:
            instance.save()

        @transaction.on_commit
        def send_confirmation_email():
            # NOTE: ideally, we want to ensure that every registration is
            # associated with a webinar object. However, I kept things
            # simple as I wanted to quickly get this up & running.
            wagtail_webinar = Webinar.objects.filter(title__icontains="wagtail").first()
            if wagtail_webinar:
                title = wagtail_webinar.title
                datetime = wagtail_webinar.datetime
                url = wagtail_webinar.url

                company = instance.company or "Not specified"
                role = instance.role or "Not specified"

                queue = django_rq.get_queue("default")
                queue.enqueue(
                    send_email,
                    subject=f"🎉 Webinar » {title}",
                    to_email_list=[instance.email],
                    template="core/webinar_registration_notification_email.txt",
                    context={
                        "name": instance.name,
                        "event": title,
                        "datetime": datetime,
                        "url": url,
                        "generic_encoded_location": urlencode({"location": url}),
                        "yahoo_encoded_location": urlencode({"in_loc": url}),
                        "contact": wagtail_webinar.organizer,
                    },
                    md_to_html=True,
                )
                queue.enqueue(
                    send_notification,
                    heading=f"🎉 New Registration » {title} Webinar",
                    content=f"{instance.name} <{instance.email}> has just registered to attend the webinar.\n\nCompany: {company}\nRole: {role}",
                )

            else:
                logger.error("No Webinar object found!")

        return instance
