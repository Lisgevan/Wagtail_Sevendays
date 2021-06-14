from django.db import models

from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core import blocks
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.images.blocks import ImageChooserBlock

class Carousel(blocks.StructBlock):
    image = ImageChooserBlock()
    text = blocks.RichTextBlock()
class HomePage(Page):
    banner_title = models.CharField(max_length=100, default='Welcome to my Homepage!')

    body = StreamField([
        #('name', blocks.SomethingBlock()),
        ('heading', blocks.CharBlock(template='blocks/heading_block.html')),
        ('image', ImageChooserBlock(template='blocks/image_block.html')),
        ('paragraph', blocks.RichTextBlock()),
        ('carousel', Carousel()),
    ], null=True)

    content_panels = Page.content_panels + [
        FieldPanel("banner_title"),
        StreamFieldPanel("body"),
    ]
