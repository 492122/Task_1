from django.http import HttpResponse
from django.shortcuts import render
import datetime
#from django.template import RequestContext, Template
from django.template import loader
#def index(request):
 #   now = datetime.datetime.now()
#    html = "<html><body>It is now %s.</body></html>" % now
  #  return HttpResponse(html)
import requests
def index(request):
    r = requests.get('https://api.vk.com/method/wall.get?user_id=138524541&v=5.74&access_token=55308fc0ef2409dbcc786c63a683cb619da2d8c98161a96e8e160d4e14ca7202edee8600844d4d95290d7',params={'owner_id':-153484210,'count':4})
    response = r.json()
    b = response['response']['count']
    a = '<html><body>Количество постов на стене =  %s.</body></html>' % b 
    #for i in range(1,2): #Создаём цикл с переменными для каждого поста
    timestamp = response['response']['items'][1]['date'] #дата и время публикации в Unix-формате
    #post_date = datetime.datetime.fromtimestamp(timestamp)
    likes_count = response['response']['items'][1]['likes']['count'] #количество лайков   
    #d = '<html><body>Количество лайков на последнем посте =  %s</body></html>' % likes_count
    d = '%s' % likes_count
    #e = render(request, 'vk_visit/list.html')
    t1 = loader.get_template('vk_visit/list.html')
    like = {"likes_count":d}
    context = {'likes_count': likes_count}

    return HttpResponse(t1.render(like))
    #return render(request, 'vk_visit/list.html', context)

    