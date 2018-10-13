import json

import requests
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


def  home(request):
    return render(request, 'agcosite/home.html')

def process_raw_data(data):
    i=True
    headerArray=[]
    resultArray=[]
    for elem in data['result']['Rows']:
        if i:
            for header in elem['Data']:
                headerArray.append(header['VarCharValue'])
            i=False
        else:
            itemDict={}
            c=0
            for item in elem['Data']:
                itemDict.update({headerArray[c]:item['VarCharValue']})
                c+=1
            itemDict.update({'name':'Bruce Wayne','city':'Gotham'})
            resultArray.append(itemDict)
    return resultArray

@csrf_exempt
def api(request):
    response = requests.get('https://a9d3013nfg.execute-api.eu-west-1.amazonaws.com/dev/histdata')

    data=json.loads(response.content)
    data=process_raw_data(data)
    return JsonResponse(data, safe=False)
