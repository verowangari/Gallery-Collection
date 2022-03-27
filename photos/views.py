from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
import datetime as dt
from .models import Category,Photo

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def photos_of_day(request):
    date = dt.date.today()

    
    return render(request, 'all-photos/today-photos.html', {"date": date,})

def convert_dates(dates):

    # Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    # Returning the actual day of the week
    day = days[day_number]
    return day

# View Function to present news from past days
def past_days_photos(request, past_date):

    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(photos_of_day)

    return render(request, 'all-photos/past-photos.html', {"date": date})

def gallery(request):
    categories=Category.objects.all()
    photos=Photo.objects.all()
    context = {'categories': categories, 'photos': photos}
    return render(request,'all-photos/gallery.html', context)

def viewPhoto(request,pk):
    photo=Photo.objects.get(id=pk)
    return render(request,'all-photos/photo.html',{'photo':photo})

def addPhoto(request):
    categories=Category.objects.all()
    
    if request.method== 'POST':
        data=request.POST
        image=request.FILES.get('image')
        print('data:', data)
        print('image:', image)
    context = {'categories': categories}
    return render(request,'all-photos/add.html',context)