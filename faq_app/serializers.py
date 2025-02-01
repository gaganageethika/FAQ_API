from rest_framework import serializers
from .models import FAQ

class FAQSerializer(serializers.ModelSerializer):
    question = serializers.CharField(
        label="Question (English)",
        help_text="Enter the question in English."
    )
    answer = serializers.CharField(
        label="Answer (English)",
        help_text="Enter the answer in English."
    )
    question_hi = serializers.CharField(
        label="Question (Hindi)",
        help_text="Automatically translated into Hindi.",
        required=False
    )
    question_bn = serializers.CharField(
        label="Question (Bengali)",
        help_text="Automatically translated into Bengali.",
        required=False
    )
    answer_hi = serializers.CharField(
        label="Answer (Hindi)",
        help_text="Automatically translated into Hindi.",
        required=False
    )
    answer_bn = serializers.CharField(
        label="Answer (Bengali)",
        help_text="Automatically translated into Bengali.",
        required=False
    )

    class Meta:
        model = FAQ
        fields = ['id', 'question', 'answer', 'question_hi', 'question_bn', 'answer_hi', 'answer_bn']