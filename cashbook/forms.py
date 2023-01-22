""" Forms """

from django import forms
from .models import Cashbook


class CashbookForm(forms.ModelForm):
    """ Create cashbook form """
    class Meta:
        """ Sets model and fields for user form """
        model = Cashbook
        fields = ('book_title', 'book_category',
                  'spend_item', 'spend_amount')
