from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, AccessRecord, Webpage
from first_app.forms import UserForm, UserProfileInfoForm

# Create your views here.
def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}
    return render(request, 'first_app/index.html', context=date_dict)

def register(request):

    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password()
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profil_pic = request.FILES['profile']

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'first_app/registration.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})


