from rest_framework import serializers

from .models import Comment, JobPosition, TechStack, Ticket
from authentication.models import User
                     


class JobPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPosition
        fields = [
            'id', 
            'position'
        ]

class TechStackSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechStack
        fields = [
            'id', 
            'tech_stack'
        ]

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'id', 
            'user', 
            'ticket', 
            'content', 
            'created_at', 
            'updated_at'
        ]

class TicketSerializer(serializers.ModelSerializer):
    job_position = JobPositionSerializer()
    tech_stacks = TechStackSerializer(many=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Ticket
        fields = [
            'id', 
            'first_name', 
            'middle_initial', 
            'last_name', 
            'email_address', 
            'job_position', 
            'resume_url', 
            'tech_stacks', 
            'progress', 
            'assignees', 
            'created_at', 
            'updated_at', 
            'comments'
        ]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id', 
            'email', 
            'role', 
            
        ]