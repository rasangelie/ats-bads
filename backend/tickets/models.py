import uuid
from django.db import models
from authentication.models import User
from auditlog.registry import auditlog


# Create your models here.

class JobPosition(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    position = models.CharField(max_length=100)

    def __str__(self):
        return self.position

class Ticket(models.Model):
    class TicketProgressChoices(models.IntegerChoices):
        APPLICATION = 1, 'Application'
        SCREENING = 2, 'Screening'
        FOR_REVIEW = 3, 'For Review'
        INTERVIEWING = 4, 'Interviewing'
        TRIAL_TEST = 5, 'Trial Test'
        PASSED = 6, 'Passed'
        POOLED = 7, 'Pooled'
        WITHDREW = 8, 'Withdrew'
        REJECTED = 9, 'Rejected'
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=100)
    middle_initial = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField()
    job_position = models.ForeignKey(JobPosition, on_delete=models.CASCADE, related_name='tickets')
    resume_url = models.URLField()
    tech_stacks = models.ManyToManyField('TechStack', related_name='tickets')
    progress = models.IntegerField(choices=TicketProgressChoices.choices, default=TicketProgressChoices.APPLICATION)
    assignees = models.ForeignKey(User, on_delete=models.CASCADE) 
    created_at = models.DateTimeField(auto_now_add=True)
    #last_moved = models.CharField(max_length=100)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.last_name.__str__() + ", " + self.first_name.__str__()


auditlog.register(Ticket, include_fields=['progress', 'updated_at'])


class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comments')
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='ticket_comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content

class TechStack(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tech_stack = models.CharField(max_length=100)

    def __str__(self):
        return self.tech_stack
    


    