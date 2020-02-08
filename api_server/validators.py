from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.core.validators import URLValidator

def validate_rating(value):
    if value != -1 and value != 0 and value != 1 and value != 2:
        raise ValidationError(
            _('%(value)s is not -1, 0, 1 or 2!'),
            params={'value': value},
        )

def validate_url(value):
    try:
        validate = URLValidator()
        validate(value)
    except (ValueError, ValidationError):
        raise ValidationError(
            _('%(value)s is not url!'),
            params={'value': value},
        )

def validate_longitude(value):
    if value < -180 or value > 180:
        raise ValidationError(
            _('%(value)s is out of the range from -180 to 180'),
            params={'value': value},
        )
    
def validate_latitude(value):
    if value < -90 or value > 90:
        raise ValidationError(
            _('%(value)s is out of the range from -90 to 90'),
            params={'value': value},
        )

