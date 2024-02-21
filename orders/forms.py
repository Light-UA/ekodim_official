import re
from django import forms


class CreateOrderForm( forms.Form ):
    first_name = forms.CharField()
    last_name = forms.CharField()
    phone_number = forms.CharField()

    def clean_phone_number(self):
        data = self.cleaned_data['phone_number']

        if not data.isdigit():
            raise forms.ValidationError( "Номер телефону повинен містити лише цифри" )

        pattern = re.compile( r'^\d{10}$' )
        if not pattern.match( data ):
            raise forms.ValidationError( "Невірний формат номера" )

        return data
