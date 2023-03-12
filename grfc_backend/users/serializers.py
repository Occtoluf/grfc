from .models import Subdivision
from rest_framework import serializers


class SubfivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subdivision
        fields = '__all__'
        # Если нужны определенные поля, то берите те, что снизу
        # fields = ('title', 'full_title', 'full_title_r', 'full_title_d', 'full_title_t')  # noqa 501
