from django.shortcuts import render
import pandas as pd
from .models import Customer


posts = [
    {
        'author':'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First Post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author':'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second Post content',
        'date_posted': 'August 28, 2018'
    }

]


# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

def table(request):
    filepath = 'C:/Users/bhoof001/Documents/YT-Django-Webapp/django_project/blog/test_data.csv'
    data = pd.read_csv(filepath)
    data_html = data.to_html()
    context = {'loaded_data': data_html}
    return render(request, "blog/table.html", context)

def data(request):
    
    data = Customer.objects.all()
    for item in data:
        print('#################################################################')
        print(item)
    cust = {
        "customer_data": data
    }


    return render(request, "blog/data.html", context=cust)
    

