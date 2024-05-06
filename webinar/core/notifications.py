import apprise
from django.conf import settings


def send_notification(heading, content):
    """
    Example

    heading = "🎉 New Registration » Introduction to Wagtail Webinar"
    content = "Someone has just registered to attend the webinar"
    """
    # Create an Apprise instance
    apprise_obj = apprise.Apprise()

    ntfy = settings.APPRISE_NTFY_URL
    apprise_obj.add(ntfy)

    apprise_obj.notify(
        body=content,
        title=heading,
    )
