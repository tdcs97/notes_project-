from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


# Create you
# r models here.
class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, default=None, null=True)
    note = models.CharField(max_length=500, default=None, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=50, default=None, null=True)
    email = models.EmailField(max_length=50, default=None, null=True)
    subject = models.CharField(max_length=50, default=None, null=True)
    msg = models.CharField(max_length=500, default=None, null=True)

    def __str__(self):
        return self.name

# class Register(models.Model):
#     name = models.CharField(max_length=50, default=None, null=True)
#     email = models.EmailField(max_length=50, default=None, null=True)
#     num = models.IntegerField(default=None, null=True)
#     passwd = models.IntegerField(default=None, null=True)

#     def __str__(self):
#         return self.name

# class Login(models.Model):
#     username = models.CharField(max_length=50, default=None, null=True)
#     password = models.IntegerField(default=None, null=True)

#     def __str__(self):
#         return self.username