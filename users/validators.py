import datetime

from dateutil.relativedelta import relativedelta
from rest_framework.exceptions import ValidationError


def check_birth_date(value):
    age = relativedelta(datetime.data.today(), value).year
    if age < 9:
        raise ValidationError(f"Возраст {age} лет слишком мал!")