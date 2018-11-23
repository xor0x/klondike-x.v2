from modeltranslation.translator import register, TranslationOptions
from .models import Post
from django.utils.translation import gettext_lazy as _

@register(Post)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'body',)
