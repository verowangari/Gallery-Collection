from unicodedata import name
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
    # user = request.user
    category = request.GET.get('category')
    
    
    if category == None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(
            category__name=category)
    
  
    categories=Category.objects.all()
    # photos=Photo.objects.all()
    context = {'categories': categories, 'photos': photos}
    return render(request,'all-photos/gallery.html', context)

def viewPhoto(request,pk):
    photo=Photo.objects.get(id=pk)
    return render(request,'all-photos/photo.html',{'photo':photo})

# def addPhoto(request):
#     categories=Category.objects.all()
    
#     if request.method== 'POST':
#         data=request.POST
#         image=request.FILES.get('image')
        
#         if data['category'] !='none':
#             category=Category.objects.get(id=data['category'])
#         elif data['category_new'] !='':
#             category,created=Category.objects.get_or_create(name=data['category_new'])
            
#         else:
#             category=None
#             photo=Photo.objects.create(
                
#                 category=category,
#                 description=data['description'],
#                 image=image,
#             )
            
#             return redirect('gallery')
#     context = {'categories': categories}
#     return render(request,'all-photos/add.html',context)

def addPhoto(request):
    # user = request.user

    # categories = user.category_set.all()
    categories=Category.objects.all()

    if request.method == 'POST':
        data = request.POST
        images = request.FILES.getlist('images')

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(
                # user=user,
                name=data['category_new'])
        else:
            category = None

        for image in images:
            photo = Photo.objects.create(
                category=category,
                description=data['description'],
                image=image,
            )

        return redirect('gallery')

    context = {'categories': categories}
    return render(request, 'all-photos/add.html', context)

def search_results(request):

    if 'photo' in request.GET and request.GET["photo"]:
        category = request.GET.get("photo")
        searched_photos = Photo.search_by_category(category)
        message = f"{category}"

        return render(request, 'all-photos/search.html',{"message":message,"photos": searched_photos})

    else:
        message = "You haven't searched for any category"
        return render(request, 'all-photos/search.html',{"message":message})