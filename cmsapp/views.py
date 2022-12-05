from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView, UpdateView
from .models import PageData, UserData
from .forms import PageDataForm


def index(request):
    pageData = PageData.objects.all()[:1].get()
    context = {'pageData': pageData}
    request_obj = UserData(record="request made")
    request_obj.save()
    return render(request, 'index.html', context)


@login_required(login_url='/login')
def home(request):
    return render(request, 'home.html')


@login_required(login_url='/login')
def manage(request):
    pageData = PageData.objects.all()[:1].get()
    context = {'pageData': pageData}
    return render(request, 'manage.html', context)


@method_decorator(login_required(login_url='/login'), name="dispatch")
class createinfo(CreateView):
    model = PageData
    form_class = PageDataForm
    success_url = '/home'
    template_name = 'manage-edit.html'


@method_decorator(login_required(login_url='/login'), name="dispatch")
class editinfo(UpdateView):
    model = PageData
    form_class = PageDataForm
    success_url = '/home'
    template_name = 'manage-edit.html'


@login_required(login_url='/login')
def analytics(request):
    request_data = UserData.objects.all().order_by('-timecreated')[:100]
    context = {'request_data': request_data}
    return render(request, 'analytics.html', context)


#Login & user management
def login(request):
    c = {}
    return render(request, 'signin.html')


def login_auth(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/home')
    else:
        return HttpResponseRedirect('/login')


def logout_view(request):
    logout(request)
    return render(request, 'logout.html')


