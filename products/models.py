from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#product class
#title -char
#pub_date-datetime
#body- text
#url text
#image- image
#icon-image
#votes_total-integer
#hunter-foreignkey
class Product(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    url=models.TextField()
    
    votes_total=models.IntegerField(default = 1)
    hunter = models.ForeignKey(User , on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %y')
    



