from django.db import models
from twilio.rest import Client

# Create your models here.


class Message(models.Model):
    name = models.CharField(max_length=100)
    Message = models.CharField(max_length=255, default='Type here')

    def __str__(self):
        return self.name
    
    def __str__(self):
        return self.Message

    def save(self, *args, **kwargs):
        
            account_sid = ''
            auth_token = ''
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                body=f"Today's Weather Report Of {self.name} : {self.Message}",
                from_='',
                to=''
            )
            print(message.sid)
       
       

