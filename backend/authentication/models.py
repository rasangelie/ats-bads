from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.
class User(AbstractUser):
    class UserRoleChoices(models.IntegerChoices):
        ADMIN = 1, 'Admin'
        MANAGER = 2, 'Manager'
        CONTRIBUTOR = 3, 'Contributor'
    
    role = models.IntegerField(choices=UserRoleChoices.choices, default=UserRoleChoices.MANAGER)

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=100)
    middle_initial = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField()
    created_at = models.TimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name