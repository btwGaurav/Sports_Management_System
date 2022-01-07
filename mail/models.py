from django.db import models
from django.core.mail import send_mail
from Home_Page.models import *

# Create your models here.



class MailText(models.Model):
    subject = models.TextField(max_length=500)
    message = models.TextField(max_length=1000)
    event_id = models.IntegerField(default='-1')
    # attachment = models.FileField()
    send_it = models.BooleanField(default=False) #check it if you want to send your email
    temp = RegistrationData.objects.all()
    user_email = []
    
    def save(self, *args, **kwargs):
        if self.send_it:
            #First you create your list of users
            user_email=self.user_email

            for i in self.temp:
                if i.tournamentid == self.event_id:
                    user_email.append(str(i.email))
            
            #Then you can send the message. 
            send_mail(str(self.subject), 
                        str(self.message),
                        'write_your_email_here',
                        user_email, 
                        fail_silently=False)
        super(MailText, self).save(*args, **kwargs)

    def __str__(self):
        return self.subject                    

    class Meta:
        verbose_name = "Email to send"
        verbose_name_plural = "Emails to send"

