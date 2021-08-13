from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
types=(
    ('student','student'),
    ('teacher','teacher')
)
depart=(
    ('Computer Engineering','Computer Engineering'),
    ('Information Technology','Information Technology'),
    ('Civil Engineering','Civil Engineering'),
    ('Mechanical Engineering','Mechanical Engineering'),
    ('Chemical Engineering','Chemical Engineering'),
    ('Electronics and Telecommunication Engineering','Electronics and Telecommunication Engineering'),
    ('Instrumentation and Control Engineering','Instrumentation and Control Engineering'),
    ('Automation and Robotics','Automation and Robotics'),
    ('Applied Science','Applied Science')
)
year=(
    (2018,2018),
    (2019,2019),
    (2020,2020),
    (2021,2021),
    (2022,2022),
    (2023,2023),
    (2024,2024)
)
std=(
    ('FE','FE'),
    ('SE','SE'),
    ('TE','TE'),
    ('BE','BE'),

)
class Userform(User):
    select_type= models.CharField (choices=types, max_length=80)
    institute=models.CharField(max_length=100)
    department=models.CharField(choices=depart,max_length=80)
    Class=models.CharField(choices=std,max_length=100)
    passout_year=models.IntegerField(choices=year)
    phonenumber=models.CharField(max_length=100)
    
class Blogpost(models.Model):
    views=models.IntegerField(default=0)

class Notification(models.Model):
    title=models.CharField(max_length=100)
    date=models.DateTimeField()
    def __str__(self):
        return self.title

class Event(models.Model):
    event_title=models.CharField(max_length=100)
    program_name=models.CharField(max_length=100)
    program_date=models.DateTimeField()
    program_venue=models.CharField(max_length=100)
    program_audience=models.CharField(max_length=100)
    program_details=models.TextField()
    program_image=models.ImageField( upload_to="upload/images", blank=True )

    def __str__(self):
        return self.event_title




class blogcomment(models.Model):
    comment=models.TextField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    parent=models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    image=models.ImageField(upload_to="upload/images", blank=True )
    timestamp=models.DateTimeField()
    
    def __str__(self):
        return self.comment
  
    

