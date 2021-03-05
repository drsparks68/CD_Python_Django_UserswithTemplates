from django.shortcuts import render
from .models import User

# show all of the data from a table
def index(request):
    context = {
    	"all_the_users": User.objects.all()
    }
    return render(request, "index.html", context)

def process_user(request):
    if request.method == 'POST':
        User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], age=request.POST['age'])
    return render(request, "index.html")