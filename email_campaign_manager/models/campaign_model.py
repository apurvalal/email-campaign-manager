from django.db import models
import uuid

class Campaign(models.Model):
    campaign_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    subject = models.TextField()
    preview_text = models.TextField()
    article_url = models.TextField()
    html_content = models.TextField()
    plain_text_content = models.TextField()
    published_date = models.DateTimeField()

    def __str__(self):
        return self.subject
