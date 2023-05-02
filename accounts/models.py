from django.db import models
from django.contrib.auth.models import User


from .EnumUserType import ProfileType


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class customerProfile(TimeStampedModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=False)
    base_role =models.CharField(max_length=50, default=ProfileType.CUSTOMER)
    customer_id = models.IntegerField(null=True, blank=True)
    is_verified = models.BooleanField(default=True)

    def __str__(self):
        return self.base_role

