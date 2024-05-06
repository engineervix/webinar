import pytz
from django.conf import settings
from django.db import models
from django.utils.functional import cached_property
from django.utils.text import slugify


class Webinar(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    title = models.CharField(max_length=255)
    datetime = models.DateTimeField()
    url = models.URLField()
    duration = models.DurationField(blank=True, null=True)
    intro = models.TextField(blank=True)
    description = models.TextField(blank=True)
    organizer = models.EmailField()

    class Meta:
        ordering = ["-datetime"]

    def __str__(self):
        return "{} ({})".format(self.title, self.datetime.astimezone(pytz.timezone("Africa/Lusaka")))

    @cached_property
    def atcb_config(self):
        """
        default add-to-calendar-button configuration

        https://github.com/add2cal/add-to-calendar-button
        """

        intro = f"\n\n{self.intro}" if self.intro else ""
        date_format = "%Y-%m-%d"
        time_format = "%H:%M"
        datetime = self.datetime.astimezone(pytz.timezone("Africa/Lusaka"))
        ends_on = datetime.strftime(date_format)
        starts_at = datetime.strftime(time_format)
        ends_at = (datetime + self.duration).strftime(time_format)
        base_url = getattr(settings, "BASE_URL", "")

        config = {
            "name": self.title,
            # Formatting a URL in the description like [url]https://....[/url] makes it clickable  # noqa: E501
            "description": f"[url]{base_url}[/url]{intro}",
            "startDate": datetime.strftime(date_format),
            "endDate": ends_on,
            "startTime": starts_at,
            "endTime": ends_at,
            "location": self.url,
            "options": [
                "Apple",
                "Google",
                "iCal",
                "Microsoft365",
                "MicrosoftTeams",
                "Outlook.com",
                "Yahoo",
            ],
            "timeZone": getattr(settings, "TIME_ZONE", "Africa/Lusaka"),
            "trigger": "click",
            "iCalFileName": f"webinar_{datetime.strftime(date_format)}_{slugify(self.title)}",  # noqa: E501
        }

        return config


class Registration(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # NOTE: this boolean is currently not used
    # the initial idea was to send emails via management command and cron job
    # but I decided to use django-rq
    notification_sent = models.BooleanField(default=False)

    # NOTE: this FK is also not used at this point, but to be revisited
    # once this is shipped
    webinar = models.ForeignKey(Webinar, blank=True, null=True, on_delete=models.SET_NULL)

    name = models.CharField(max_length=255)
    email = models.EmailField()
    company = models.CharField(max_length=255, blank=True)
    role = models.CharField(max_length=255, blank=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return "{} ({})".format(self.name, self.created)
