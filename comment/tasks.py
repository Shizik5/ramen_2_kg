from celery import shared_task
from django.core.mail import send_mail
from .models import Comment

@shared_task()
def send_new_comment_email(comment_id):
    comment = Comment.objects.get(pk=comment_id)

    subject = 'New Comment on Your Post'
    message = f'Hi {comment.post.owner},\n\nYou have a new comment on your post: "{comment.body}"\n\nBest regards,\nYour Website Team'
    from_email = 'darinaibrag@gmail.com'
    recipient_list = [comment.post.owner.email]

    send_mail(subject, message, from_email, recipient_list)