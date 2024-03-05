from django.contrib.auth.models import  User
from django.db import models
from django.utils import timezone

class Staff(models.Model):
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
    
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=124, choices=department_choices, blank=True, null=True)

    def __str__(self):
        return f'{self.employee.student_id}'

