from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = (
        ('user', 'User'),
        ('admin', 'Admin'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')

class PeriodLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='period_logs')
    period_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-period_date']

    def __str__(self):
        return f"{self.user.username} - {self.period_date}"
