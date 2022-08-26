from django.db import models

# Create your models here.
class Blogmodel(models.Model):
    AUTHOR=[
        ("Unknown","Unknown"),
        ("Arun","Arun"),
        ("Mari","Mari"),
        ("Pranish","Pranish"),
        ("Naren","Naren"),
        ("Kavin","Kavin"),
    ]
    TYPE=[
        ("Python","Python"),
        ("CSS","CSS"),
        ("HTML","HTML"),
        ("AJAX","AJAX"),
        ("Others","Others"),
    ]
    title=models.CharField(max_length=30)
    post=models.CharField(max_length=200)
    author=models.CharField(max_length=50,choices=AUTHOR,default='Unknown')
    post_regarding=models.CharField(max_length=15,choices=TYPE,default='Python')
    contact=models.PositiveIntegerField(default='0000000000')
    brief_about_post=models.CharField(max_length=1000,default='Nothing defined!!!')
    image=models.ImageField(upload_to='profile_pic',null=True,blank=True)

    def __str__(self):
        return f"{self.title} : {self.post}"

class SearchModel(models.Model):
    employee_name=models.CharField(max_length=30)
    designation=models.CharField(max_length=30)
    address=models.CharField(max_length=100)
