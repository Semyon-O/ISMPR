from rest_framework import serializers

from ismpr_orders.models import Feedback


class FeedbackSerializer(serializers.ModelSerializer):

    class Meta:
        model = Feedback
        fields = ['id','FeedbackDescription', 'order', 'Score']
        read_only_fields = ['id']