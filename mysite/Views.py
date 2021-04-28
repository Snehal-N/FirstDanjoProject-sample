# i have created this file-snehal
from django.http import HttpResponse
from django.shortcuts import  render

def index(request):
    #return HttpResponse(''' <h1>Sanket</h1> <a href="https://www.youtube.com/watch?v=e2qSFKCkn_Y">Follow me</a>''')
    #return HttpResponse("Home")
    params={'name':'snehal','place':'pune'}
    return render(request, 'index.html',params)

def about(request):
    return HttpResponse("about snehal")

def analyze(request):

    djtext=request.GET.get('text', 'default')
    chktext = request.GET.get('chk', 'Off')
    fullcap=request.GET.get('fullcap','Off')
    #print(request.GET.get('text','default'))
    #return HttpResponse("remove punc")
    print(djtext)
    print(chktext)
    if chktext=="on":
        analyzed=""
        punc = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''

        for char in djtext:
               if char not in punc:
                   analyzed=analyzed+char

        params={'purpose':'Removed punctuations','analyzed_text':analyzed}
        return render(request,'analyze.html',params)

    elif(fullcap=='on'):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {'purpose': 'Change to Capital', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    else:
        return  HttpResponse("error")

def capfirst(request):
    return HttpResponse("capitalized first")


def newlineremove(request):
    return HttpResponse("newlineremove")


def spaceremove(request):
    return HttpResponse('''spaceremove  <a href="/">Back</a>''')


def charcount(request):
    return HttpResponse("charcount")