from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# from users.models import Employee 
# Create your models here.
class Complaint(models.Model):
    status_choices = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Solved', 'Solved')
    ]
    
    type_choices = (('Class Room', 'Class Room'), ('Campus', 'Campus'), ('Library', 'Library'), ('Administration', 'Administration'),)
    
    department_choices = (
        
        ('Heavy duty and light vehicle ', 'Heavy duty and light vehicle'), 
        ('Plant', 'Plant'), 
        ('Surface mining ', 'Surface mining '), 
        ('Finance (support services)', 'Finance (support services)'), 
        ('Underground', 'Underground'), 
        ('Security and safety department ', 'Security and safety department '), 
        ('Primus(canteen)', 'Primus(canteen)'), 
        ('Environment department', 'Environment department'), 
        
                          
    )
    
    title = models.CharField(max_length=100, verbose_name= 'Enter your complaint', blank=True)
    details = models.TextField(verbose_name= 'Explain in more detail', blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    type = models.CharField(choices=type_choices, max_length=64, default='Campus', blank=True)
    department = models.CharField(choices=department_choices, max_length=124, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    status = models.CharField(choices=status_choices, default='Pending', max_length=24)
    comment = models.CharField(max_length=265, blank=True, default="")
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('complaint-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title


class Feedback(models.Model):
    complaint = models.ForeignKey(Complaint, on_delete=models.CASCADE)
    content = models.TextField(max_length=120)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '{}-{}'.format(self.complaint.title, str(self.user.username))