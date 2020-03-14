from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from preferences.models import Preference


class PreferenceSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.id')

    class Meta:
        model = Preference
        fields = ('name', 'user')


class RecommendationSerializer(serializers.Serializer):

    class FreeHoursSerializer(serializers.Serializer):
        free_hours_start = serializers.TimeField()
        free_hours_end = serializers.TimeField()

    latitude = serializers.FloatField(min_value=-90, max_value=90)
    longitude = serializers.FloatField(min_value=-180, max_value=180)
    type = serializers.CharField()
    free_hours = FreeHoursSerializer()
