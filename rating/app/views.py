from django.shortcuts import render
from .models import Rating
from django.http import JsonResponse
# Create your views here.
def main_view(request):
    rating=Rating.objects.filter(score=0).order_by("?").first()
    return render(request,'main.html',{'rating':rating})
def rate_view(request):
    if request.method=="POST":
        el_id=request.POST.get('el_id')
        val=request.POST.get('val')
        obj=Rating.objects.get(id=el_id)
        obj.score=val
        obj.save()
        return JsonResponse({'success':'true','score':val},safe=False)
    return JsonResponse({'success':'false'})