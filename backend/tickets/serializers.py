from rest_framework import serializers
from .models import Ticket, TicketProgress, JobPosition, Comment, TechStack, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class JobPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPosition
        fields = '__all__'

class TechStackSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechStack
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'

class TicketSerializer(serializers.ModelSerializer):
    job_position = JobPositionSerializer(read_only=True)
    assignees = UserSerializer(read_only=True)
    tech_stacks = TechStackSerializer(many=True, read_only=True)

    class Meta:
        model = Ticket
        fields = '__all__'

class TicketProgressSerializer(serializers.ModelSerializer):
    ticket = TicketSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = TicketProgress
        fields = '__all__'