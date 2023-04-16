from celery import shared_task
from .selenium import SeleniumData
from .models import Stats, Rekvizit

@shared_task
def instStat():
   data = Rekvizit.objects.all()
   username = ""
   password = ""

   for d in data:
      password = d.password 
      username = d.login 

   [followers, name, followings] = SeleniumData(username, password)
   
   stats = Stats.objects.all()
   if followers == "" and name == "" and followings == "":
      return("failed")
   if len(stats) > 0:
      Stats.objects.filter(id = 1).update(followers = followers, name = name, followings = followings)
      return("Succes")
   else:  
      stats = Stats(followers = followers, name = name, followings = followings)
      stats.save()
      return("Succes")

