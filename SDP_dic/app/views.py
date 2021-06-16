from django.shortcuts import render
from .models import Word
from django.http import JsonResponse
from django.db.models import Q
def home(request):
    if request.method=='POST':
        word=request.POST['word']
        print(word)
        find=Word.objects.filter(Q(Word=word) or Q(Bangli_word=word))
        return render(request,'result.html',{'word':find})
    return render(request,'index.html')


