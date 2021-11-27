from django.contrib.auth.models import User
from django.db import models

# Create your models here.

MEAMORY = (('n', '  '),
              ("4GB", "4GB"),
              ("16GB", "16GB")
              )

class Device(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    uptime=models.CharField(max_length=25,null=True,blank=True)
    memory_usage=models.CharField(choices=MEAMORY,default='n',max_length=25,null=True, blank=True)
    cpu_usage=models.CharField(max_length=25,null=True,blank=True)
    is_active=models.BooleanField(default=True,)

    def __str__(self):
        return str(self.uptime)

class Diskpartitioninfo(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    info=models.CharField(max_length=25,null=True,blank=True)

    def __str__(self):
        return f'{self.device.id}{self.info}'


