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
def index(request, group_name):   
    g = requests.get('https://api.vk.com/method/groups.getById?user_id=138524541&v=5.74&access_token=8932da4dfdb25ef2c5a75d6803c4d5b0b13112ab1a0c464c90cc58caf940e1a11069881f197fa43a9e0ab',params={'group_id': group_name, 'fields':'name'} )
    name_dict = g.json()
    group_id = name_dict['response'][0]['id']
    r = requests.get('https://api.vk.com/method/wall.get?user_id=138524541&v=5.74&access_token=8932da4dfdb25ef2c5a75d6803c4d5b0b13112ab1a0c464c90cc58caf940e1a11069881f197fa43a9e0ab',params={'owner_id': -group_id,'count':4}) #-153484210
    response = r.json()
    post = response['response']['count']
    count_r = '<html><body>Количество постов на стене =  %s.</body></html>' % post 
    #for i in range(1,2): #Создаём цикл с переменными для каждого поста
    timestamp = response['response']['items'][1]['date'] #дата и время публикации в Unix-формате
    #post_date = datetime.datetime.fromtimestamp(timestamp)
    likes_count = response['response']['items'][1]['likes']['count'] #количество лайков   
    #d = '<html><body>Количество лайков на последнем посте =  %s</body></html>' % likes_count
    output= '%d' % likes_count
    #e = render(request, 'vk_visit/list.html')
    t1 = loader.get_template('vk_visit/list.html')
    like = {"likes_count":output}
    context = {'likes_count': likes_count}
    return HttpResponse(t1.render(like))
    #return render(request, 'vk_visit/list.html', context)

#def name(request, group_name):
 #   g = requests.get('https://api.vk.com/method/groups.getById?user_id=138524541&v=5.74&access_token=8932da4dfdb25ef2c5a75d6803c4d5b0b13112ab1a0c464c90cc58caf940e1a11069881f197fa43a9e0ab',params={'group_id': 153484210, 'fields':'name'} )
 #   name_dict = g.json()
 #   group = name_dict['response'][0]['screen_name']
 #   return HttpResponse(group_name = group)
 #    dsds