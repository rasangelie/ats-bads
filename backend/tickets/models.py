from django.db import models
# from django.contrib.auth.models import User
from authentication.models import User
import uuid

# Create your models here.
class Ticket(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=100)
    middle_initial = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField()
    job_position = models.OneToOneField('JobPosition', on_delete=models.CASCADE)
    resume_url = models.URLField()
    tech_stacks = models.ManyToManyField('TechStack')
    assignees = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.TimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name  

    
class TicketProgress(models.Model):
    class TicketProgressChoices(models.IntegerChoices):
        APPLICATION = 1, 'Application'
        SCREENING = 2, 'Screening'
        FOR_REVIEW = 3, 'For Review'
        INTERVIEWING = 4, 'Interviewing'
        TRIAL_TEST = 5, 'Trial Test'
    
    progress = models.IntegerField(choices=TicketProgressChoices.choices, default=TicketProgressChoices.APPLICATION)

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.TimeField(auto_now_add=True)


class JobPosition(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    position = models.CharField(max_length=100)

class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.TimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class TechStack(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tech_stack = models.CharField(max_length=100)
    

    