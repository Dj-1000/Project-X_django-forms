from django.contrib import auth
from django.contrib.auth import authenticate
from .forms import LoginForm, CreateRecordForm, CreateUserForm, UpdateRecordForm
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Record
from django.http import Http404, HttpResponseBadRequest

def home(request):
    return render(request, "webapp/index.html")


def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect("login")

    return render(request, "webapp/register.html", context={"form": form})


def login(request):
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect("dashboard")

    return render(request, "webapp/login.html", context={"form2": form})


@login_required
def dashboard(request):
    records = Record.objects.all()

    return render(
        request,
        "webapp/dashboard.html",
        context={
            "records": records,
        },
    )


@login_required
def create_record(request):
    form = CreateRecordForm()
    if request.method == "POST":
        form = CreateRecordForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("dashboard")

    return render(request, "webapp/create-record.html", context={"form": form})


@login_required
def update_record(request, pk):
    record = Record.objects.filter(id=pk).first()
    if not record:
        return render(request,'webapp/404.html',context={'message':'Sorry! record not found'})
    form = UpdateRecordForm(instance=record)
    if request.method == "POST":
        form = UpdateRecordForm(instance=record, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")

    return render(request, "webapp/update-record.html", context={"form": form})


@login_required
def view_record(request, pk):
    record = Record.objects.filter(id=pk).first()
    return render(request, "webapp/view-record.html", context={"record": record})

@login_required
def delete_record(request,pk):
    record = Record.objects.filter(id=pk).first()
    if record is None:
        message = "Sorry! This objects doesn't exist"
        return redirect("webapp/404.html",context = {'message':message})
    
    record.delete()
    return redirect("dashboard")

@login_required
def logout(request):
    auth.logout(request)
    return redirect("login")
