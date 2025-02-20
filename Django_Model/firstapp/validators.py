from django.core.exceptions import ValidationError
def comma_separated_validator(value):
    if not all(item.strip().isalpha() for item in value.split(',')):  
        raise ValidationError("Only letters and commas are allowed.")