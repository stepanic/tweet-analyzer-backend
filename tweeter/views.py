from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json



@csrf_exempt
def analyzer(request):
  response_data = {}

  if request.method == 'GET':
    response_data['status'] = False
    response_data['message'] = 'GET is not allowed, only POST method!'


  elif request.method == 'POST':
    '''
    Primanje podataka (izvora - Twitter usernamei i hashtagovi)
    @dnevnikhr
    #ladygaga
    ...
    njih N komada

    i uz svaki source dolazi i podataka koliko se tvitova zeli za svakog dohvatiti

    npr. na
    sources[1] se nalazi '#ladygaga'
    a na
    how_many[1] se nalazi '12' sto znaci da se za #ladygaga u analizu ubacuje prvih 12 twitova
    '''
    sources =  request.POST.getlist("sources")
    how_many =  request.POST.getlist("how_many")


    '''
    BZIK TODO
    ovdje ubaciti spajanje na skripte za analizu

    zamijeniti response_data['data'] koji su hardkodirani sa dobivenim podacima iz analizatora
    zadrzati strukturu nazivlja atributa u dictionariju !!!

    data je lista dictionarija koji u sebi imaju:
    tweet_id
    tweet_text
    class_id - ovo je lista pri cemu je [SVM, Bayes, NN]

    '''

    response_data['status'] = True
    response_data['message'] = 'Analyer finished successfully!'

    '''
    TODO zamijeniti
    '''
    response_data['data'] = [

        {
            'tweet_id':1,
            'tweet_text': 'Ovo je tweet sa bla bla bla 123',
            'class_id': [2,1,2]
        },
        {
            'tweet_id':2,
            'tweet_text': 'Ovo je tweet sa bla bla bla 123 56546 56',
            'class_id': [1,1,2]
        },
        {
            'tweet_id':3,
            'tweet_text': 'frgtr tyery Ovo je tweet sa bla bla bla 123 98 0 90 89',
            'class_id': [0,1,0]
        },
        {
            'tweet_id':4,
            'tweet_text': 'hki uy iuou iou io Ovo je tweet sa bla bla bla 123 34 2 312 67 87 987',
            'class_id': [0,1,2]
        },
        {
            'tweet_id':5,
            'tweet_text': 'hki uy iuou iou io Oj ghj ghj ghjvo je tweet sa bla bla bla 123 34 2 312 67 87 987',
            'class_id': [3,4,4]
        },
        {
            'tweet_id':6,
            'tweet_text': 'hki uy iuou idf gd fg df gdf gou io Oj ghj ghj ghjvo je tweet sa bla bla bla 123 34 2 312 67 87 987',
            'class_id': [2,4,3]
        }

    ]

  response = HttpResponse(json.dumps(response_data), content_type="application/json")
  response["Access-Control-Allow-Origin"] = "*"
  response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
  response["Access-Control-Max-Age"] = "1000"
  response["Access-Control-Allow-Headers"] = "*"
  return response


