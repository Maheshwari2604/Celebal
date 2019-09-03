from django.db import models

# Create your models here.

class profile(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class subprofile(models.Model):
    name = models.CharField(max_length=100)
    notes = models.TextField()
    profile = models.ForeignKey(profile, related_name='subprofile', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
