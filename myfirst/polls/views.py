from django.shortcuts import render
from django.http import HttpResponse
import requests
# Create your views here.
def index(request):
    #return HttpResponse("Hello, world. You're at the poll index.")
    r = requests.get('https://api.vk.com/method/users.get?user_id=113852454&v=5.74&access_token=2154d0feb75374b36ad24420b1a243917477353266f32c9304894d4bafaa8a8e7ff625b05d8c0cddaa547', params={'user_ids':189330747, 'fields':'followers_count, military, blacklisted, can_post, common_count, photo_200'})
    user =  r.json()
    html = "<html><body>It is  %s.</body></html>" % user
    return HttpResponse(html)


#r = requests.get('https://api.vk.com/method/users.get', params={'user_ids':1})  
#a =  r.json()
#print(HttpResponse(a))
