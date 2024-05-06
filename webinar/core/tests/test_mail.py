from unittest.mock import mock_open, patch

from django.core import mail
from django.test import TestCase

from webinar.core.mail import send_email

template = "test_template.txt"
content = "Hello {{ name }},\n\nHere is the content of my email."


class SendEmailTestCase(TestCase):
    @patch(
        "builtins.open",
        new_callable=mock_open,
        read_data=content,
    )
    def test_send_email(self, mock_file):
        subject = "Test email subject"
        to_email_list = ["foo@example.co.zm", "bar@example.co.zm"]
        context = {"name": "John Doe"}

        assert open(template).read() == content
        mock_file.assert_called_with(template)

        send_email(subject, to_email_list, template, context=context)

        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, subject)
        self.assertEqual(mail.outbox[0].to, to_email_list)
        self.assertIn("Hello John Doe,", mail.outbox[0].body)
        self.assertIn("content of my email", mail.outbox[0].body)

    @patch(
        "builtins.open",
        new_callable=mock_open,
        read_data=content,
    )
    def test_send_email_no_context(self, mock_file):
        subject = "Test email subject"
        to_email_list = ["somebody@example.co.zm"]

        assert open(template).read() == content
        mock_file.assert_called_with(template)

        send_email(subject, to_email_list, template)

        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, subject)
        self.assertEqual(mail.outbox[0].to, to_email_list)
        self.assertIn("Hello ,", mail.outbox[0].body)
        self.assertIn("content of my email", mail.outbox[0].body)
