# -*- coding: utf-8 -*-

import logging

from django.conf import settings
from django.core.mail import send_mail

from todos.models import Todo

logger = logging.getLogger(__name__)


def send_todo_notification_email(subject, message_body, mail_to):
    """
        - Used to send Notification Email on Create, Update or Delete any ToDos Action by the User
    """
    logger.info("==============================================================")
    logger.info("                                                              ")
    logger.info("          ToDos Notification Email method calling...          ")
    logger.info("                                                              ")
    logger.info("==============================================================")
    mail_from = settings.DEFAULT_FROM_EMAIL

    try:
        logger.info(message_body)
        logger.info(subject)

        send_mail(subject, '', mail_from, mail_to, html_message=message_body, fail_silently=False)
        logger.info("{subject} Notification Email has been sent successfully to User: {user_email}".format(subject=subject, user_email=mail_to))

    except Exception as error:
        logger.info("Error while sending ToDo:- {} Notification Email. {error}".format(error=str(error)))
