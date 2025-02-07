from django.db import models


class FileAttachment(models.Model):
  name = models.CharField(max_length=90)
  extension = models.CharField(max_length=15)
  size = models.FloatField()
  src = models.TextField()
  content_type = models.CharField(max_length=45)

  class Meta:
    db_table = 'file_attachments'


class AudioAttachment(models.Model):
  src = models.TextField()

  class Meta:
    db_table = 'audio_attachments'