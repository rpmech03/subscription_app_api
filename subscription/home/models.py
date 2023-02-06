from django.db import models
from django.contrib.auth.models import User
import uuid


class BaseModel(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True

class Blog(BaseModel):
    blog_title = models.CharField(max_length=100)
    blog_description = models.TextField()
    is_paid = models.BooleanField(default=False)
    blog_owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

class Subscription(BaseModel):
    subscription_name = models.CharField(max_length=100)
    subscription_days = models.TextField(default=30)
    subscription_price = models.IntegerField()

class SubscriptionOrder(BaseModel):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    subscription = models.ForeignKey(Subscription, on_delete= models.CASCADE, null=True, blank=True)
    subscription_end_date = models.DateField()
    is_paid = models.BooleanField(default=False)