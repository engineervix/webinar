import os
from typing import List, Optional

import pycmarkgfm
from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from premailer import transform


def send_email(
    subject: str,
    to_email_list: List[str],
    template: str,
    context: Optional[dict] = None,
    md_to_html: Optional[bool] = False,
) -> None:
    """
    Sends an email with the specified subject,
    to the specified list of email recipients,
    using the supplied text template with optional context.

    Args:
        subject: The subject line of the email.
        to_email_list: A list of email addresses to send the email to.
        template: The path to the text template to use.
        context: A dictionary containing values to pass to the template (optional).
        md_to_html: Whether the template content is written in Markdown format and
        should be rendered as HTML.

    Returns:
        None
    """

    # If context is None, set it to an empty dictionary
    if context is None:
        context = {}

    # Render the text template using the provided context
    text_content = render_to_string(template, context)

    if md_to_html:
        html = pycmarkgfm.gfm_to_html(text_content)
        with open(
            os.path.join(settings.APPS_DIR, "assets/css/gfm.min.css"),
            "r",
            encoding="utf-8",
        ) as f:
            github_markdown_css = f.read()
        # see https://github.com/sindresorhus/github-markdown-css?tab=readme-ov-file#usage
        formatted_content = f"""
        <!DOCTYPE html>
        <html lang="en">
            <head>
                <meta name="viewport" content="width=device-width, initial-scale=1">
                <style>{github_markdown_css}</style>
                <style>
                    html {{
                        box-sizing: border-box;
                    }}
                    *,
                    *::before,
                    *::after {{
                        box-sizing: inherit;
                    }}
                    .markdown-body {{
                        margin: 0 auto;
                        max-width: 980px;
                        padding: 45px;
                    }}
                    @media (max-width: 767px) {{
                        .markdown-body {{
                            padding: 15px;
                        }}
                    }}
                </style>
            </head>
            <body class="markdown-body">{html}</body>
        </html>
        """
        text_content = transform(formatted_content)

    # Create the email message object
    email = EmailMessage(
        subject=subject,
        body=text_content,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=to_email_list,
    )

    # If markdown to html is enabled, set the content type to HTML
    if md_to_html:
        email.content_subtype = "html"

    # Send the email
    email.send()
