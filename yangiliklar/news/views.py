from django.shortcuts import render

from .models import News

def index(request):
    news = News.objects.all()
    context = {
        'news': news,
        'title': "Yangiliklar",
    }
    return render(request, 'news/index.html', context)

# Create your views here.
