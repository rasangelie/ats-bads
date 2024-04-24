import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    class UserRoleChoices(models.IntegerChoices):
        ADMIN = 1, 'Admin'
        MANAGER = 2, 'Manager'
        CONTRIBUTOR = 3, 'Contributor'
    
    role = models.IntegerField(choices=UserRoleChoices.choices, default=UserRoleChoices.MANAGER)
    # role = models.IntegerField(
    #     choices=[(choice.value, choice.name) for choice in UserRoleChoices],
    #     default=UserRoleChoices.MANAGER,
    # )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    

    def __str__(self):
        return self.first_name