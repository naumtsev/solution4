import requests
from requests import get, post, put
import sys
import os
def size(response_my):
    resp = response_my['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['boundedBy']['Envelope']
    lx, ly = map(float, resp['lowerCorner'].split())
    rx, ry = map(float, resp['upperCorner'].split())
    w = abs(rx - lx)
    h = abs(ry - ly)
    return (w, h)

def scope(response_my):
    w, h = size(response_my)
    return w / 3 , h / 3

def position(response_my):
    return response_my['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']


def search(place):
    geocoder_request = "http://geocode-maps.yandex.ru/1.x/?geocode={}&format=json".format(place)
    response = get(geocoder_request)
    json_response = response.json()['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
    x, y = json_response.split()
    return (str(x) + ',' + str(y), (float(x), float(y)))


toponym_to_find = " ".join(sys.argv[1:])
me = toponym_to_find

my_adress = search(me)[0]

map_request = 'https://geocode-maps.yandex.ru/1.x/?geocode={}&kind=district&format=json'.format(my_adress, my_adress)
request = get(map_request).json()['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['metaDataProperty']['GeocoderMetaData']['text']
print(request)

# D:\Python\python.exe main.py

