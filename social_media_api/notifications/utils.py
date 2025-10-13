from .models import Notification
from django.contrib.contenttypes.models import ContentType

def create_notification(actor, recipient, verb, target=None):
    """
    Helper function to create a notification instance.
    """
    if actor == recipient:
        return  # Prevent self-notifications
    content_type = None
    object_id = None
    if target:
        content_type = ContentType.objects.get_for_model(target.__class__)
        object_id = target.id
    Notification.objects.create(
        actor=actor,
        recipient=recipient,
        verb=verb,
        target_content_type=content_type,
        target_object_id=object_id,
    )
