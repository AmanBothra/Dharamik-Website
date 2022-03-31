# import base64
# import threading

# from django.conf import settings
# from django.template.loader import render_to_string

# from sendgrid import SendGridAPIClient
# from sendgrid.helpers.mail import (Attachment, Disposition, FileContent,
#                                    FileName, FileType, Mail)


# class MailClient(object):
#     def __init__(self):
#         """
#         Init for mail client.
#         """
#         self.sendgrid = SendGridAPIClient(settings.SEND_GRID_API_KEY)
#         self.mail_content = None

#     def config(self, form_email, to_email, subject, template_full_path, context={}, file=None, file_type=None,file_name=None):
#         """
#         Configation for sending mail  form, to and subject.

#         @parmas : form_email (string) : Email ID for mail sender.
#         @parmas : to_email (string or python list) : Email ID for mail receiver.
#         @parmas : subject (string) : Email subject.
#         """

#         context["mime_type"] = "text/plain"
#         content = render_to_string(template_full_path, context)

#         content.mime_type = "text/html"

#         self.mail_content = Mail(
#             from_email=form_email,
#             to_emails=to_email,
#             subject=subject,
#             html_content=content,
#         )
#         if file:
#             encoded_file = base64.b64encode(file.read()).decode()
#             attached_file = Attachment(
#                 FileContent(encoded_file),
#                 FileName(file_name),
#                 FileType(file_type),
#                 Disposition('attachment')
#             )
#             self.mail_content.attachment = attached_file

#     def send(self):
#         """
#         Send mail as a python threading
#         """
#         thread = threading.Thread(target=self.background_task, args=())
#         thread.daemon = True
#         thread.start()

#     def background_task(self):
#         """
#         Send mail as background process.
#         """
#         self.sendgrid.send(self.mail_content)
