from celery import shared_task
from .selenium import SeleniumData
from .models import Stats

@shared_task
def instStat():
    username = "obberecht"
    password = "dagestanec12345"   
    [followers, name, followings] = SeleniumData(username, password)
    stats = Stats.objects.all()
    if len(stats) > 0:
       Stats.objects.filter(id = 1).update(followers = followers, name = name, followings = followings)
       return("Succes")
    else:  
       stats = Stats(followers = followers, name = name, followings = followings)
       stats.save()
       return("Succes")

def test():
    return "Hello"