import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')
import django
django.setup()
import random
from firstapp.models import Accessrecord,Webpage,Topic
from faker import Faker
fakegen=Faker()
topics=['Search','social','marketplace','new','game']
def add_topic():
    t=Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t
def populate(N=5):
    for entry in range (N):
     top=add_topic()

     fake_url=fakegen.url()
     fake_urls=fakegen.date()
     fake_name=fakegen.name()
     webpd=Webpage.objects.get_or_create(topics=top,url=fake_url,name=fake_name)[0]
     acc=Accessrecord.objects.get_or_create(name=webpd,date=fake_date)[0]
if __name__ == '__main__':
    print("populating script!")
    populate(20)
    print("complete")
