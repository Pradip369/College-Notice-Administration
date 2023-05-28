from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator,RegexValidator

class Branch(models.Model):
    name = models.CharField(max_length=200)
    hod = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


class Notice(models.Model):
    subject = models.CharField(max_length=200)
    msg = models.TextField()
    cr_date = models.DateTimeField(auto_now_add=True)
    branch = models.ForeignKey(to=Branch,on_delete=CASCADE,null=True,blank=True)
    
    def __str__(self):
        return self.subject  


class Profile(models.Model):
    user = models.OneToOneField(to=User,on_delete=CASCADE)
    branch = models.ForeignKey(to=Branch,on_delete=CASCADE,null=True,blank=True)
    sem = models.IntegerField(default=1,choices=((1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8)))
    mark_10 = models.IntegerField(default=0, validators=[MinValueValidator(0),MaxValueValidator(100)])
    mark_11 = models.IntegerField(default=0, validators=[MinValueValidator(0),MaxValueValidator(100)])
    mark_12 = models.IntegerField(default=0, validators=[MinValueValidator(0),MaxValueValidator(100)])
    mark_aggr = models.IntegerField(default=0, validators=[MinValueValidator(0),MaxValueValidator(100)])
    roll_no = models.IntegerField(validators=[MinValueValidator(0)],default=00,unique=True)
    phone_no = models.CharField(validators= [RegexValidator("^0?[5-9]{1}\d{9}$")],max_length=15,null=True,blank=True)
    my_img = models.ImageField(upload_to="images\\",null=True)
    my_resume = models.FileField(upload_to="doc\\",null=True)
    skills = models.TextField(null=True,blank=True)
    
    
    def __str__(self):
        return str(self.user)
    


class Question(models.Model):
    subject = models.CharField(max_length=40)
    question= models.TextField()
    cr_date = models.DateTimeField(auto_now_add=True)
    user =  models.ForeignKey(to=User,on_delete=CASCADE,null=True)
    
    
    def __str__(self):
        return self.subject 