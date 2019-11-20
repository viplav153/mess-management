from django.db import models

# Create your models here.
class Menu(models.Model):
    monday_breakfast=models.TextField()
    monday_lunch=models.TextField()
    monday_tiffin=models.TextField()
    monday_dinner=models.TextField()
    tuesday_breakfast=models.TextField()
    tuesday_lunch=models.TextField()
    tuesday_tiffin=models.TextField()
    tuesday_dinner=models.TextField()
    wednesday_breakfast=models.TextField()
    wednesday_lunch=models.TextField()
    wednesday_tiffin=models.TextField()
    wednesday_dinner=models.TextField()
    thrusday_breakfast=models.TextField()
    thrusday_lunch=models.TextField()
    thrusday_tiffin=models.TextField()
    thrusday_dinner=models.TextField()
    friday_breakfast=models.TextField()
    friday_lunch=models.TextField()
    friday_tiffin=models.TextField()
    friday_dinner=models.TextField()
    saturday_breakfast=models.TextField()
    saturday_lunch=models.TextField()
    saturday_tiffin=models.TextField()
    saturday_dinner=models.TextField()
    sunday_breakfast=models.TextField()
    sunday_lunch=models.TextField()
    sunday_tiffin=models.TextField()
    sunday_dinner=models.TextField()

    def save(self,*args,**kwargs):
        if self.__class__.objects.count():
            self.pk=self.__class__.objects.first().pk
        super().save(*args,**kwargs)
    
    
    
    
    
