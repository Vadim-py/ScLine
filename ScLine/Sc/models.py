from django.db import models

class ScLineUsr(models.Model):
    username = models.CharField(max_length=30)
    vk = models.CharField(max_length=30)
    inst = models.CharField(max_length=30)
    tiktok = models.CharField(max_length=30)
    youtube = models.CharField(max_length=30)
    facebook = models.CharField(max_length=30)
    link1 = models.CharField(max_length=30)
    link2 = models.CharField(max_length=30)
    link3 = models.CharField(max_length=30)
    link4 = models.CharField(max_length=30)
    link5 = models.CharField(max_length=30)

    def __str__(self):
        return self.username
