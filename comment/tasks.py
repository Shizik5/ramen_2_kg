from django.core.mail import send_mail
from project.celery import app
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken, BlacklistedToken
from datetime import datetime
from drf_api_logger.models import APILogsModel
from comment.models import Comment


@app.task(bind=True)
def send_new_comment_email(self, comment_id):
    comment = Comment.objects.get(pk=comment_id)

    subject = 'New Comment on Your Post'
    message = f'Hi \n\nYou have a new comment on your post: "{comment.body}"\n\nBest regards,\nYour Website Team'
    from_email = 'sadyr.top@gmail.com'
    recipient_list = ['dastan12151@gmail.com']

    send_mail(subject, message, from_email, recipient_list, fail_silently=False)
