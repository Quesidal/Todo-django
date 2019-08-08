import uuid

from django.db import models

from django_extensions.db.models import TimeStampedModel


class UUIDTimestampedModel(TimeStampedModel):
    """
    Abstract base model,
    Overrides ID with UUID4, inherits TimeStampedModel
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True
