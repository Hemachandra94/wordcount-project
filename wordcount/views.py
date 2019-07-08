from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse('Hello!! Welcome to home page')
def homeHTML(request):
    return render(request, 'home.html')
def count(request):

    data = request.GET['fulltext']

    wordList = data.split()

    wordDictionary = {}

    for word in wordList:
        if word in wordDictionary:
            wordDictionary[word] += 1
        else:
            wordDictionary[word] = 1

    return render(request, 'countView.html', {"dataEntered" : data, "NumOfWords" : len(wordList), "wordDictionary": wordDictionary.items()})

def about(request):
    return HttpResponse("This page will return the number of words and the frequency of words entered in the text box")
