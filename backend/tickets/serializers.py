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
        

    def validate_content(self, value):
        if not value:
            raise serializers.ValidationError("Content cannot be empty")
        return value

class TicketSerializer(serializers.ModelSerializer):
    job_position = JobPositionSerializer()
    tech_stacks = TechStackSerializer(many=True)
    ticket_comments = CommentSerializer(many=True, read_only=True)

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
            'ticket_comments'
        ]
    
    def create(self, validated_data):
        """
        Create the Ticket object and its related JobPosition and TechStack objects
        """

        job_position_data = validated_data.pop('job_position')
        tech_stacks_data = validated_data.pop('tech_stacks')
        
        # Create and save the JobPosition object before creating the Ticket
        job_position = JobPosition.objects.create(**job_position_data)
        
        # Assign the JobPosition object when creating the Ticket
        ticket = Ticket.objects.create(job_position=job_position, **validated_data)

        for tech_stack_data in tech_stacks_data:
            tech_stack = TechStack.objects.create(**tech_stack_data)
            ticket.tech_stacks.add(tech_stack)
            
        return ticket
    
    def update(self, instance, validated_data):
        """
        Update the Ticket object and its related JobPosition and TechStack objects
        """

        job_position_data = validated_data.pop('job_position')
        tech_stacks_data = validated_data.pop('tech_stacks')
        
        # Update the JobPosition object before updating the Ticket
        job_position = instance.job_position
        job_position.position = job_position_data.get('position', job_position.position)
        job_position.save()
        
        # Update the Ticket object
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.middle_initial = validated_data.get('middle_initial', instance.middle_initial)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email_address = validated_data.get('email_address', instance.email_address)
        instance.resume_url = validated_data.get('resume_url', instance.resume_url)
        instance.progress = validated_data.get('progress', instance.progress)
        instance.assignees = validated_data.get('assignees', instance.assignees)
        instance.save()
        
        # Update the TechStack objects before updating the Ticket
        instance.tech_stacks.clear()
        for tech_stack_data in tech_stacks_data:
            tech_stack = TechStack.objects.create(**tech_stack_data)
            instance.tech_stacks.add(tech_stack)
            
        return instance

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id', 
            'email', 
            'role', 
            
        ]