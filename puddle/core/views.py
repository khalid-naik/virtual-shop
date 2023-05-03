from django.shortcuts import render,redirect
from item.models import category,Item
from .forms import SignuupForm

# Create your views here.
def index(request):
    items = Item.objects.filter(is_sold = False)[0:6]
    categories = category.objects.all()

    # contex = {
    #     'catogories' : categories,
    #     'items' : items,
    # }

    return render(request,'core/index.html',{
        'categories' : categories,
        'items' : items,
    })

def contact(request):
    return render(request,'core/contact.html')

def signup(request):

    if request.method == 'POST':
        form = SignuupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignuupForm()

    return render(request,'core/signup.html',{
        'form' : form
    })