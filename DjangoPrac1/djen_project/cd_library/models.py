from django.db import models

# Create your models here.
GENRE_CHOICES=(
    ('R','ROCK')
    ('B', 'Blues'),
    ('J', 'Jazz'),
    ('P', 'Pop'),
    
)
#To make the description field optional, we pass the null and blank arguments as True
#A TextField can contain any number of characters and is suitable for fields such as description, summary, content

class CD(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField(null=True,blank=True)
    artist=models.CharField(max_length=40)
    date=models.DateField()
    genre=models.CharField(max_length=1,choices=GENRE_CHOICES)

def __unicode__(self):
    return "%s by %s, %s" %(self.title, self.artist, self.date.year)