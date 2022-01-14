from rest_framework import viewsets
from polls.models import Poll, Vote
from polls.serializers import PollSerializer, VoteSerializer
from rest_framework.response import Response
from rest_framework.decorators import action

class PollView(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    
    @action(methods=['get'], detail=False, url_path='active', url_name='active')
    def active_polls(self, request):
        active_polls = Poll.objects.filter(active=True)
        serializer = self.get_serializer(active_polls, many=True)
        return Response(serializer.data)

class VoteView(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    
    @action(methods=['get'], detail=False, url_path='user-votes', url_name='user_votes')
    def user_votes(self, request):
        user_votes = Vote.objects.filter(user_id=request.query_params["user_id"])
        serializer = self.get_serializer(user_votes, many=True)
        return Response(serializer.data)