import json
from django.contrib.messages import error
from django.http import HttpResponse
from django.shortcuts import render
from imdbRatings.settings import movies_json_file
from django.core.paginator import Paginator

def dict_data():
    dict_data = json.loads(open(movies_json_file).read())
    titles = [x['title'][0:len(x['title']) - 1] for x in dict_data if
              x['title'] != '' and x['poster'] != '' and x['trailer']['link'] != '' and x['rating'] != '' and x[
                  'plot'] != '']
    posters = [x['poster'] for x in dict_data if
               x['title'] != '' and x['poster'] != '' and x['trailer']['link'] != '' and x['rating'] != '' and x[
                   'plot'] != '']
    trailer_links = [x['trailer']['link'] for x in dict_data if
                     x['title'] != '' and x['poster'] != '' and x['trailer']['link'] != '' and x['rating'] != '' and x[
                         'plot'] != '']
    ratings = [x['rating'] for x in dict_data if
               x['title'] != '' and x['poster'] != '' and x['trailer']['link'] != '' and x['rating'] != '' and x[
                   'plot'] != '']
    plots = [x['plot'] for x in dict_data if
             x['title'] != '' and x['poster'] != '' and x['trailer']['link'] != '' and x['rating'] != '' and x[
                 'plot'] != '']

    #print(titles)
    #print(len(ratings))
    #print(len(posters))

    context = [{'title': title, 'poster': poster, 'rating': rating, 'plot': plot, 'trailer': trailer} for
               title, poster, rating, plot, trailer in zip(titles, posters, ratings, plots, trailer_links)]
    return context


def showIndex(request):
    data = dict_data()
    pg = Paginator(data,6)
    page_num = request.GET.get("page_no",1)
    page =pg.page(page_num)
    for x in data:
        if(x['rating'])>='9':
            return render(request,'index.html',{'page':page,'max':x})

def searchMovie(request):
    name = request.GET.get('sMovie')
    slink = request.GET.get('sLink')
    context = dict_data()
    for x in context:
        if (x['title'] == name) or (x['title'] == slink):
            return render(request, 'searched_movie.html', {'data':x})
    else:
        error(request, 'enter another movie name')
        return HttpResponse('NOT FOUND')


