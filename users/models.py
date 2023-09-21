from django.db import models
# from django.contrib.auth.models import User
from PIL import Image, ImageOps
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.contrib.auth.hashers import make_password


class CustomUserManager(UserManager):
    def _create_user(self, student_id, password, **extra_fields):
        student_id = self.normalize_email(student_id)
        user = CustomUser(student_id=student_id, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, student_id, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(student_id, password, **extra_fields)

    def create_superuser(self, student_id, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("last_name", "System")
        extra_fields.setdefault("first_name", "Administrator")

        assert extra_fields["is_staff"]
        assert extra_fields["is_superuser"]
        return self._create_user(student_id, password, **extra_fields)
 

class CustomUser(AbstractUser):

    username = None  # Removed username, using email instead
    email = models.EmailField(unique=True, null=True, blank=True)
    student_id = models.CharField(max_length=15, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    USERNAME_FIELD = "student_id"
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return str(self.student_id)





# class Profile(models.Model):
#     user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
#     image = models.ImageField(default='default.jpg', upload_to='profile_pics')
#     is_employee = models.BooleanField(default=False)
#     def save(self, *args, **kwargs):
#         super().save(*args, **kwargs)
#         image = Image.open(self.image.path)
#         # ImageOps compatible mode
#         if image.mode not in ("L", "RGB"):
#             image = image.convert("RGB")

#         imagefit = ImageOps.fit(image, (200, 200), Image.Resampling.LANCZOS)
#         imagefit.save(self.image.path)

#     def __str__(self):
#         return f'{self.user.username} Profile'



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

