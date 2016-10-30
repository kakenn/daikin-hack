from django.db import models


class Answer(models.Model):
    parent = models.ForeignKey(
        "cms.Answer",
        models.SET_NULL,
        null=True,
        blank=True
    )
    text = models.CharField(max_length=255)
    keyword = models.CharField(max_length=255)
