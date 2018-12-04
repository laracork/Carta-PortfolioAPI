from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator

class Investments(models.Model):
    '''
    Model containing investment information.
    Cost of shares is in cents to reduce floating-point errors and because JSON
        doesn't properly support decimal values.
    Buy date stamp is auto filled upon object creation but the sell
        date stamp is nullified upon object creation and updated upon
        selling via the admin panel.
    MinValueValidator has been included because this validation is turned off
        for SQLite. Inclusion will prevent negative integers.
    '''

    company_name = models.CharField(max_length=50)
    share_quantity = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])
    cost_cents = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])
    buy_date = models.DateField(auto_now_add=True)
    sell_date = models.DateField(blank=True, null=True, default=None)
    updated_date = models.DateField(auto_now=True, null=True)

    class Meta:
        db_table = 'Investments'

    def __str__(self):
        cost = int(self.cost_cents / 100)
        return f'Investment for {self.company_name} bought on {self.buy_date} for ${cost}'
