from django.http.response import Http404, HttpResponse
from django.shortcuts import render

# Create your views here.
def view(request):
    return render(request,'single.html')

texts=["Lorem ipsum dolor sit, amet consectetur adipisicing elit. Iure, recusandae animi aliquid non ab minima hic numquam commodi ex maiores, voluptate, magnam ad molestiae officia?","Empower your teams. Take your project management skills to the next level. Concept to launch in record time. Starting at only $7. Trusted by 65k+ Teams. Integrates w/ Other Tools. For Teams of All Sizes. Agile Functionality. Services: Agile Workflow, Fast Issue Tracking.","Find Speech Text Converter. Search Faster, Better & Smarter at ZapMeta Now! The Complete Overview. Wiki, News & More. Trusted by Millions. 100+ Million Visitors. Web, Images & Video. Information 24/7. Types: pdf, doc, ppt, xls, txt."]

def section(request,num):
    if 1<=num<=3:
        return HttpResponse(texts[num-1])
    else:
        raise Http404("No such sextion")