from django.shortcuts import render
from django.http import HttpResponse
import requests
import json

# Create your views here.

def Country(request):
    re = requests.get("https://corona.azure-api.net/summary")
    js=json.loads(re.text)
    return render(request,"corona/country.html",{"globalData":js["globalData"],"countries":js["countries"]})


def state(request,slug):
    re=requests.get(f"https://corona.azure-api.net/country/{slug}")
    js=json.loads(re.text)
    summary=js["Summary"]
    state=js["State"]
    return render(request,"corona/state.html",{"state":state,"summary":summary})

def news(request,slug,slug1):
    if(slug1=="NULL"):
        slug1=""
    re=requests.get(f"https://newsapi.org/v2/top-headlines?language=en&q=corona&country={slug1}&apiKey=b8bfef2ab9be4231b76c6938a6b87e17")
    js=json.loads(re.text)
    news=js["articles"]
    return render(request,"corona/news.html",{"news":news,"country":slug})

def search(request):
    query = request.POST.get("search")
    re=requests.get(f"https://corona.azure-api.net/country/{query}")
    if(re.status_code == 404):
        print("if not")
        return render(request,"corona/search.html",{"search":1})
    js=json.loads(re.text)
    summary=js["Summary"]
    state=js["State"]
    return render(request,"corona/state.html",{"state":state,"summary":summary})