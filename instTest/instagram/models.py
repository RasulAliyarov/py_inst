from django.db import models

class Stats(models.Model):
    name = models.CharField("Username", max_length=255)
    followers = models.CharField("Followers", max_length=255)
    followings = models.CharField("Following",max_length=255)

    def __str__(self) :
        return self.name
# class Users 