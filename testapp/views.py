from django.shortcuts import render

# Create your views here.

def home_page_view(request):
    return render(request, 'testapp/home.html')


def movie_view(request):
    news1 = "Sara Ali Khan is too hot."
    news2 = "Ranbir dating to Alia"
    news3  = "Ranbeer and Dipika is going to marry soon in Italy"

    my_dict = {'news1': news1, 'news2': news2, 'news3': news3}

    return render(request, 'testapp/movienews.html', my_dict)

def rss_view(request):
    return render(request, 'testapp/rss.xml')
