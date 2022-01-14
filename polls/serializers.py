from rest_framework import serializers
from polls.models import Choice, Poll, Question, Vote

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True)
    class Meta:
        model = Question
        fields = '__all__'


class PollSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)
    class Meta:
        model = Poll
        fields = '__all__'

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = '__all__'