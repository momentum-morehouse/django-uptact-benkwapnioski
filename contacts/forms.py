from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'name',
            'address_1',
            'address_2',
            'city',
            'state',
            'zip_code',
            'phone_number',
            'email',
            'birthday',
        ]
# class NoteForm(forms.Form):
#     class Meta:
#         model = Note
#         fields = [
#           'description',
#         ]
