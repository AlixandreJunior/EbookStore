import string
import phonenumbers
from django.core.exceptions import ValidationError
from validate_docbr import CPF

def validate_cpf(value: string) -> None:
    cpf = CPF()
    if not cpf.validate(value):
        raise ValidationError("CPF inválido.")
    
def validate_br_phone(value):
    try:
        phone = phonenumbers.parse(value, "BR")
        if not phonenumbers.is_valid_number(phone):
            raise ValidationError("Número de telefone brasileiro inválido.")
    except phonenumbers.NumberParseException:
        raise ValidationError("Número de telefone brasileiro inválido.")