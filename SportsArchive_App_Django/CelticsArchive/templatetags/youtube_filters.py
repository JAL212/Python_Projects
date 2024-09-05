import re
from django import template

register = template.Library()

@register.filter(name='youtube_id')
def youtube_id(value):
    """
    Extract the YouTube video ID from a URL.
    """
    pattern = (
        r'(?:https?:\/\/)?(?:www\.)?'
        '(?:youtube\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|\S*?[?&]v=)|'
        'youtu\.be\/)([a-zA-Z0-9_-]{11})'
    )
    match = re.search(pattern, value)
    return match.group(1) if match else value