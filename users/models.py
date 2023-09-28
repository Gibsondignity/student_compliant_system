from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone


class CustomUserManager(BaseUserManager):
    def create_user(self, student_id, password=None, **extra_fields):
        if not student_id:
            raise ValueError('The Student ID field must be set')
        user = self.model(student_id=student_id, **extra_fields)
        # if password == confirm_password:
        #     user.set_password(password)
        # else:
        #     raise ValueError('The password fields didn’t match.')
        
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, student_id, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(student_id, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    student_id = models.CharField(unique=True, max_length=10)
    first_name = models.CharField(max_length=24, null=True)
    last_name = models.CharField(max_length=24, null=True)
    email = models.EmailField(null=True)
    confirm_password = models.CharField(max_length=24, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = 'student_id'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

    def save(self, *args, **kwargs):
        if self.password == self.confirm_password:
            self.set_password(self.password)
            self.confirm_password = None
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.student_id





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
    
    employee = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    department = models.CharField(max_length=124, choices=department_choices, blank=True, null=True)

    def __str__(self):
        return f'{self.employee.student_id}'

