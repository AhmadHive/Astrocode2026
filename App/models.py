from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.conf import settings

class TeamManager(BaseUserManager):
    def create_user(self, team_name, password=None, **extra_fields):
        if not team_name: raise ValueError('يجب تحديد اسم الفريق')
        user = self.model(team_name=team_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, team_name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(team_name, password, **extra_fields)

class Track(models.Model):
    name = models.CharField(max_length=200)
    logo = models.URLField()
    description = models.TextField()
    definition = models.TextField()
    def __str__(self): return self.name

class Challenge(models.Model):
    track = models.ForeignKey(Track, on_delete=models.CASCADE, related_name='challenges')
    logo = models.URLField(default='https://res.cloudinary.com/diadkkzve/image/upload/v1778875753/Screenshot_2026-05-15_230827_jdc4yb.png')
    name = models.CharField(max_length=200)
    details = models.TextField()
    requirements = models.TextField()
    def __str__(self): return f"{self.track.name} - {self.name}"

class Team(AbstractBaseUser, PermissionsMixin):
    team_name = models.CharField(max_length=100, unique=True)
    university = models.CharField(max_length=150)
    challenge = models.ForeignKey(Challenge, on_delete=models.PROTECT, related_name='teams', null=True)
    
    leader_name = models.CharField(max_length=100)
    member2_name = models.CharField(max_length=100)
    member3_name = models.CharField(max_length=100, blank=True, null=True)
    member4_name = models.CharField(max_length=100, blank=True, null=True)

    email_1 = models.EmailField(unique=True)
    email_2 = models.EmailField(blank=True, null=True)
    phone_1 = models.CharField(max_length=20)
    phone_2 = models.CharField(max_length=20, blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = TeamManager()
    USERNAME_FIELD = 'team_name'
    REQUIRED_FIELDS = ['leader_name', 'university', 'email_1']

class Submission(models.Model):
    team = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='submission')
    description = models.TextField(max_length=1000)
    drive_link = models.URLField()
    submitted_at = models.DateTimeField(auto_now_add=True)