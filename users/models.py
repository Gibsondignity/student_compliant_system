from django.contrib.auth.models import  User
from django.db import models
from django.utils import timezone

class Staff(models.Model):
    department_choices = (
        
        ('Finance and Account', 'Finance and Account'), 
        ('Faculty of Engineering ', 'Faculty of Engineering'),
        ('Faculty of Computing and Information System(FoCIS)', 'Faculty of Computing and Information System(FoCIS)'),
        ('Business school ', 'Business school'),
        ('Security', 'Security'),
        ('Library', 'Library'),
        ('Student Affairs', 'Student Affairs'),
                          
    )
    
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=124, choices=department_choices, blank=True, null=True)

    def __str__(self):
        return f'{self.employee.student_id}'

