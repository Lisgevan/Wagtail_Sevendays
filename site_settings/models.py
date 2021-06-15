from django.db import models

from wagtail.admin.edit_handlers import FieldPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting

@register_setting
class SocialMediaSettings(BaseSetting):
    facebook = models.URLField(max_length=100, blank=True)
    instagram = models.URLField(max_length=100, blank=True)
    twitter = models.URLField(max_length=100, blank=True)
    pinterest = models.URLField(max_length=100, blank=True)
    youtube = models.URLField(max_length=100, blank=True)
    github = models.URLField(max_length=100, blank=True)

    panels = [
        FieldPanel("facebook"),
        FieldPanel("instagram"),
        FieldPanel("twitter"),
        FieldPanel("pinterest"),
        FieldPanel("youtube"),
        FieldPanel("github"),
    ]