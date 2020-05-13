from django.db import models
class Topic(models.Model):
    topname=models.CharField(max_length=264,unique=True)
    def __str__(self):
        return self.topname
class Webpage(models.Model):
    topic=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=264,unique=True)
    url=models.URLField(unique=True)

    def __str__(self):
        return self.name
class Accessrecord(models.Model):
    name=models.ForeignKey(Webpage,on_delete=models.CASCADE)
    data=models.DateField()
    def __str__(self):
        return str(self.date)
