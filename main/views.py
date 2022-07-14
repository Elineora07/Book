from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Ism
from .form import IsmForm
from account.form import LoginForm
from django.contrib.auth.decorators import login_required
from .models import Carousel


def main_index(request):
    sarlavha = "Bosh sahifa"
    
    
    return render(request, "main/index.html", context={
        "page_title": sarlavha,
        "ismlar": Ism.objects.all(),
        'carousel': Carousel.objects.all()
        
    })
    
    
def main_about(request):
    sarlavha = "Biz haqimizda"
    return render(request, "main/about.html", context={
        "page_title": sarlavha,
        
    })
    

def main_virtual(request):
    sarlavha = "Virtual kutubxona"
    return render(request, "main/virtual.html", context={
        "page_title": sarlavha
    })
@login_required
def main_contacts(request):
    sarlavha = "Bog'lanish uchun ma'lumot"
    return render(request, "main/contacts.html", context={
        "page_title": sarlavha
    })

def main_help(request):
    sarlavha = "Yordam"
    return render(request, "main/help.html", context={
        "page_title": sarlavha
    })

def main_support(request):
    sarlavha = "Fan darsliklari"
    return render(request, "main/support.html", context={
        "page_title": sarlavha
    })

def main_add(request):
    form = IsmForm()
    if request.method == "POST":
        form = IsmForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            Ism(ism=form.cleaned_data['ism'],
                familiya=form.cleaned_data['fam'],
                ty=form.cleaned_data['ty']).save()
        
            messages.success(request, "Ism muvaffaqiyatli qo'shildi")
            
            return redirect("main:index")
    
    return render(request, "main/add.html", {
        "page_title": "Add",
        "form": form
        
    })
def  main_delete(request):
    id = request.GET.get("id")
    
    Ism.objects.filter(id=id).delete()
    messages.info(request, "Muvaffaqiyatli o'chirildi!")
    return redirect("main:index")
