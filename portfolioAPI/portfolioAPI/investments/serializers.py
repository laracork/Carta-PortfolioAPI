from rest_framework import serializers
from . models import Investments

class InvestmentsSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Investments
        fields=('url', 'company_name', 'share_quantity', 'cost_cents',)
