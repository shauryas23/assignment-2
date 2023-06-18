from django.db import models
from django.contrib.auth.hashers import make_password

class UserProfile(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=128)
    email = models.CharField(max_length=50)
    balance = models.FloatField(default=0)
    
    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super(UserProfile, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.username
 
class Transaction(models.Model):
        from_user = models.ForeignKey(UserProfile, related_name='from_user', on_delete=models.DO_NOTHING)
        to_user = models.ForeignKey(UserProfile, related_name='to_user', on_delete=models.DO_NOTHING)
        amount = models.FloatField(default=0)
        
        def __str__(self):
            return str(self.from_user.id) + + ' sending ' + str(self.amount)  + + ' to ' + str(self.to_user.id)  