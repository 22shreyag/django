from django.shortcuts import render
from django.http import HttpResponse
from firstapp.models import Topic,Webpage,Accessrecord

def index(request):
     Webpages_list = Accessrecord.objects.order_by('date')
     date_dict ={'Access_record':Webpages_list}
     return render(request,'firstapp/index.html',context=date_dict)

# Create your views here.
