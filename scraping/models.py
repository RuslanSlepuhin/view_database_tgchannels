from django.db import models


class Telegramchannels(models.Model):
    chat_name = models.CharField(max_length=150, blank=True, null=True)
    title = models.CharField(max_length=1000, blank=True, null=True)
    body = models.CharField(max_length=6000, blank=True, null=True)
    time_of_public = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'telegramchannels'
        verbose_name = 'telegram message'
        verbose_name_plural = 'telegram messages'


    def ___str___(self):
        return self.title
