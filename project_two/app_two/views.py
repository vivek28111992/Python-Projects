from django.shortcuts import render
from django.http import HttpResponse
from app_two.models import User
from app_two.forms import NewUserForm

# Create your views here.
def index(request):
    return HttpResponse('<em>My Second App</em>')

def help(request):
    my_dict = {'page': "Help Page!"}
    return render(request, 'help.html', context=my_dict)

def users(request):
    user_list = User.objects.order_by('first_name')
    user_dict = {'users': user_list}
    return render(request, 'users.html', context=user_dict)

def signup(request):
    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR FORM INVALID')

    return render(request, 'signup.html', {'form': form})
