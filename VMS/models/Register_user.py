from django.contrib.auth.models import AbstractUser
from django.db import models


role_choices = (
    ('admin', 'admin'),
    ('buyer', 'buyer'),
    ('vendor', 'vendor'),
)


class CustomUser(AbstractUser):

    user_role= models.CharField(choices= role_choices, max_length=100,default='customes')

    # Provide unique related_name for groups and user_permissions
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="customuser_set",
        related_query_name="user",
        blank=True,
        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="customuser_set",
        related_query_name="user",
        blank=True,
        help_text="Specific permissions for this user.",
    )

    def __str__(self):
        return self.username