from django.core.exceptions import ValidationError


def validation_content(value):
    content = value
    if content == 'abc':
        raise ValidationError('Cannot be ABC')
    return value
