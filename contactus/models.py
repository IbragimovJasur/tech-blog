from django.db import models
from django.contrib.auth import get_user_model

class Message(models.Model):
    sentby= models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank= True)
    name= models.CharField(max_length=50, null=True, blank=True)
    email= models.EmailField(null=False, blank=False)
    sent_in= models.DateTimeField(auto_now_add= True)
    phone= models.CharField(max_length=13, null=True, blank=True) #try to add government code and models.PhoneNumField
    subject_of_message= models.CharField(max_length=50, null=False, blank=False)
    content_of_message= models.TextField(null=False, blank=False)
    
    def __str__(self):
        return self.subject_of_message