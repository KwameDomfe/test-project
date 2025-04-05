from django.core.exceptions import ValidationError

from pint.errors import UndefinedUnitError
import pint

valid_unit_of_measurement = ['pound', 'lbs', 'oz', 'gram']

def validate_unit_of_measure(value):
    unit_reg = pint.UnitRegistry()
    try:
        single_unit = unit_reg [value]
    except UndefinedUnitError as error:
        raise ValidationError(f'"{value}" is not a valid unit of measurement.')
    except:
        raise ValidationError(f'{value} is invalid. Unknown Error.')