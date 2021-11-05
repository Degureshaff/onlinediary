from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render,HttpResponseRedirect,get_object_or_404
from django.views.generic import TemplateView, CreateView, DeleteView, UpdateView
from django.contrib.auth.models import User
from .models import mgBCOsh,mgFronOsh,mgFullOsh,mgUIOsh,mgBCBi,mgFronBi,mgFullBi,mgUIBi,mgBCUz,mgFronUz,mgFullUz,mgUIUz,evBCOsh,evFronOsh,evFullOsh,evUIOsh,evBCBi,evFronBi,evFullBi,evUIBi,evBCUz,evFronUz,evFullUz,evUIUz
from .forms import mgBCOshform,mgFronOshform,mgFullOshform,mgUIOshform,mgBCBiform,mgFronBiform,mgFullBiform,mgUIBiform,mgBCUzform,mgFronUzform,mgFullUzform,mgUIUzform,evBCOshform,evFronOshform,evFullOshform,evUIOshform,evBCBiform,evFronBiform,evFullBiform,evUIBiform,evBCUzform,evFronUzform,evFullUzform,evUIUzform
from django.contrib.auth.decorators import user_passes_test


def Vu(request):
    return render(request, 'PP/day.html')

def VU(request):
    return render(request,"PP/ni.html")

def time(request):
    return render(request,"tim/1.html")



def email_check(user):
    return user.email.endswith('bootcampOsh@gmail.com')
@user_passes_test(email_check, login_url='/accounts/login/')
def aS(request):
    mgBcOsh = mgBCOsh.objects.all()
    mgfronOsh = mgFronOsh.objects.all()
    mgfullOsh = mgFullOsh.objects.all()
    mguiOsh = mgUIOsh.objects.all()
    return render(request,"mor/aS.html",{"mgBcOsh":mgBcOsh,"mgfronOsh":mgfronOsh,"mgfullOsh":mgfullOsh,"mguiOsh":mguiOsh,})

def email_check(user):
    return user.email.endswith('bootcampBi@gmail.com')
@user_passes_test(email_check, login_url='/accounts/login/')
def AS(request):
    mgBcBi = mgBCBi.objects.all()
    mgfronBi = mgFronBi.objects.all()
    mgfullBi = mgFullBi.objects.all()
    mguiBi = mgUIBi.objects.all()
    return render(request,"mor/AS.html",{"mgBcBi":mgBcBi,"mgfronBi":mgfronBi,"mgfullBi":mgfullBi,"mguiBi":mguiBi,})



def email_check(user):
    return user.email.endswith('bootcampUz@gmail.com')
@user_passes_test(email_check, login_url='/accounts/login/')
def As(request):
    mgBcUz = mgBCUz.objects.all()
    mgfronUz = mgFronUz.objects.all()
    mgfullUz = mgFullUz.objects.all()
    mguiUz = mgUIUz.objects.all()
    return render(request,"mor/As.html",{"mgBcUz":mgBcUz,"mgfronUz":mgfronUz,"mgfullUz":mgfullUz,"mguiUz":mguiUz,})


def email_check(user):
    return user.email.endswith('bootcampOsh@gmail.com')
@user_passes_test(email_check, login_url='/accounts/login/')
def aSd(request):
    evBcOsh = evBCOsh.objects.all()
    evfronOsh = evFronOsh.objects.all()
    evfullOsh = evFullOsh.objects.all()
    evuiOsh = evUIOsh.objects.all()
    return render(request,"eve/aSd.html",{"evBcOsh":evBcOsh,"evfronOsh":evfronOsh,"evfullOsh":evfullOsh,"evuiOsh":evuiOsh,})


def email_check(user):
    return user.email.endswith('bootcampBi@gmail.com')
@user_passes_test(email_check, login_url='/accounts/login/')
def ASD(request):
    evBcBi = evBCBi.objects.all()
    evfronBi = evFronBi.objects.all()
    evfullBi = evFullBi.objects.all()
    evuiBi = evUIBi.objects.all()
    return render(request,"eve/ASD.html",{"evBcBi":evBcBi,"evfronBi":evfronBi,"evfullBi":evfullBi,"evuiBi":evuiBi,})

def email_check(user):
    return user.email.endswith('bootcampUz@gmail.com')
@user_passes_test(email_check, login_url='/accounts/login/')
def AsD(request):
    evBcUz = evBCUz.objects.all()
    evfronUz = evFronUz.objects.all()
    evfullUz = evFullUz.objects.all()
    evuiUz = evUIUz.objects.all()
    return render(request,"eve/AsD.html",{"evBcUz":evBcUz,"evfronUz":evfronUz,"evfullUz":evfullUz,"evuiUz":evuiUz,})




class LoginView(TemplateView):
    template_name = "registration/login.html"

    def dispatch(self, request, *args, **kwargs):
        context = {}
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse("profile"))
            else:
                context['error'] = "Логин или пароль неправильные"
        return render(request, self.template_name, context)

class ProfilePage(TemplateView):
    template_name = "registration/profile.html"

class RegisterView(TemplateView):
    template_name = "registration/register.html"

    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            password2 = request.POST.get('password2')

            if password == password2:
                User.objects.create_user(username, email, password)
                return redirect(reverse("login"))

        return render(request, self.template_name)

# ------------------------------^--------------------

def email_check(user):
    return user.email.endswith('q@gmail.com')
@user_passes_test(email_check, login_url='/accounts/login/')
def adminperson(request):
    mgBcOsh = mgBCOsh.objects.all()
    mgfronOsh = mgFronOsh.objects.all()
    mgfullOsh = mgFullOsh.objects.all()
    mguiOsh = mgUIOsh.objects.all()
    mgBcBi = mgBCBi.objects.all()
    mgfronBi = mgFronBi.objects.all()
    mgfullBi = mgFullBi.objects.all()
    mguiBi = mgUIBi.objects.all()
    mgBcUz = mgBCUz.objects.all()
    mgfronUz = mgFronUz.objects.all()
    mgfullUz = mgFullUz.objects.all()
    mguiUz = mgUIUz.objects.all()
# 
    evBcOsh = evBCOsh.objects.all()
    evfronOsh = evFronOsh.objects.all()
    evfullOsh = evFullOsh.objects.all()
    evuiOsh = evUIOsh.objects.all()
    evBcBi = evBCBi.objects.all()
    evfronBi = evFronBi.objects.all()
    evfullBi = evFullBi.objects.all()
    evuiBi = evUIBi.objects.all()
    evBcUz = evBCUz.objects.all()
    evfronUz = evFronUz.objects.all()
    evfullUz = evFullUz.objects.all()
    evuiUz = evUIUz.objects.all()

    return render(request, 'adper.html',{
        'mgBcOsh':mgBcOsh,
        'mgfronOsh':mgfronOsh,
        'mgfullOsh':mgfullOsh,
        'mguiOsh':mguiOsh,
        'mgBcBi':mgBcBi,
        'mgfronBi':mgfronBi,
        'mgfullBi':mgfullBi,
        'mguiBi':mguiBi,
        'mgBcUz':mgBcUz,
        'mgfronUz':mgfronUz,
        'mgfullUz':mgfullUz,
        'mguiUz':mguiUz,
        'evBcOsh':evBcOsh,
        'evfronOsh':evfronOsh,
        'evfullOsh':evfullOsh,
        'evuiOsh':evuiOsh,
        'evBcBi':evBcBi,
        'evfronBi':evfronBi,
        'evfullBi':evfullBi,
        'evuiBi':evuiBi,
        'evBcUz':evBcUz,
        'evfronUz':evfronUz,
        'evfullUz':evfullUz,
        'evuiUz':evuiUz,
    })
# -------------------------------^----------------
def mgPersonBCOsh(request):
    mgBcOsh = mgBCOsh.objects.all()
    return render(request, 'ad.html',{
        'mgBCOsh':mgBcOsh
    })

def mgcreateBcOsh(request):
    context ={}
 
    form = mgBCOshform(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
         
    context['form']= form
    return render(request, "func/create.html", context)


def mgdeleteBcOsh(request, id):
    context ={}
 
    obj = get_object_or_404(mgBCOsh, id = id)
 
 
    if request.method =="POST":
    
        obj.delete()
        return HttpResponseRedirect("/")
 
    return render(request, "func/delete.html", context)

def mgupdateBcOsh(request, id):

    context ={}
 
    obj = get_object_or_404(mgBCOsh, id = id)

    form = mgBCOshform(request.POST or None, instance = obj)
 

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
 
    context["form"] = form
 
    return render(request, "func/update.html", context)

def mgPersonFronOsh(request):
    mgfronOsh = mgFronOsh.objects.all()
    return render(request, 'table/perO.html',{
        'mgfronOsh':mgfronOsh
    })

def mgcreateFronOsh(request):
    context ={}
 
    form = mgFronOshform(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
         
    context['form']= form
    return render(request, "func/create.html", context)


def mgdeleteFronOsh(request, id):
    context ={}
 
    obj = get_object_or_404(mgFronOsh, id = id)
 
 
    if request.method =="POST":
    
        obj.delete()
        return HttpResponseRedirect("/")
 
    return render(request, "func/delete.html", context)

def mgupdateFronOsh(request, id):

    context ={}
 
    obj = get_object_or_404(mgFronOsh, id = id)

    form = mgFronOshform(request.POST or None, instance = obj)
 

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
 
    context["form"] = form
 
    return render(request, "func/update.html", context)

def mgPersonFullOsh(request):
    mgfullosh = mgFullOsh.objects.all()
    return render(request, 'table/perO.html',{
        'mgfullosh':mgfullosh
    })

def mgcreateFullOsh(request):
    context ={}
 
    form = mgFullOshform(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
         
    context['form']= form
    return render(request, "func/create.html", context)


def mgdeleteFullOsh(request, id):
    context ={}
 
    obj = get_object_or_404(mgFullOsh, id = id)
 
 
    if request.method =="POST":
    
        obj.delete()
        return HttpResponseRedirect("/")
 
    return render(request, "func/delete.html", context)

def mgupdateFullOsh(request, id):

    context ={}
 
    obj = get_object_or_404(mgFullOsh, id = id)

    form = mgFullOshform(request.POST or None, instance = obj)
 

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
 
    context["form"] = form
 
    return render(request, "func/update.html", context)

def mgPersonUIOsh(request):
    mgUiOsh = mgUIOsh.objects.all()
    return render(request, 'table/perO.html',{
        'mgUiOsh':mgUiOsh
    })

def mgcreateUiOsh(request):
    context ={}
 
    form = mgUIOshform(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
         
    context['form']= form
    return render(request, "func/create.html", context)


def mgdeleteUIOsh(request, id):
    context ={}
 
    obj = get_object_or_404(mgUIOsh, id = id)
 
 
    if request.method =="POST":
    
        obj.delete()
        return HttpResponseRedirect("/")
 
    return render(request, "func/delete.html", context)

def mgupdateUIOsh(request, id):

    context ={}
 
    obj = get_object_or_404(mgUIOsh, id = id)

    form = mgUIOshform(request.POST or None, instance = obj)
 

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
 
    context["form"] = form
 
    return render(request, "func/update.html", context)

# ---------------------------+-------------
def mgPersonBCBi(request):
    mgBcbi = mgBCBi.objects.all()
    return render(request, 'table/perO.html',{
        'mgBcbi':mgBcbi
    })

def mgcreateBcBi(request):
    context ={}
 
    form = mgBCBiform(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
         
    context['form']= form
    return render(request, "func/create.html", context)


def mgdeleteBcBi(request, id):
    context ={}
 
    obj = get_object_or_404(mgBCBi, id = id)
 
 
    if request.method =="POST":
    
        obj.delete()
        return HttpResponseRedirect("/")
 
    return render(request, "func/delete.html", context)

def mgupdateBcBi(request, id):

    context ={}
 
    obj = get_object_or_404(mgBCBi, id = id)

    form = mgBCBiform(request.POST or None, instance = obj)
 

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
 
    context["form"] = form
 
    return render(request, "func/update.html", context)

def mgPersonFronBi(request):
    mgfronBi = mgFronBi.objects.all()
    return render(request, 'table/perO.html',{
        'mgfronBi':mgfronBi
    })

def mgcreateFronBi(request):
    context ={}
 
    form = mgFronBiform(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
         
    context['form']= form
    return render(request, "func/create.html", context)


def mgdeleteFronBi(request, id):
    context ={}
 
    obj = get_object_or_404(mgFronBi, id = id)
 
 
    if request.method =="POST":
    
        obj.delete()
        return HttpResponseRedirect("/")
 
    return render(request, "func/delete.html", context)

def mgupdateFronBi(request, id):

    context ={}
 
    obj = get_object_or_404(mgFronBi, id = id)

    form = mgFronBiform(request.POST or None, instance = obj)
 

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
 
    context["form"] = form
 
    return render(request, "func/update.html", context)

def mgPersonFullBi(request):
    mgfullbi = mgFullBi.objects.all()
    return render(request, 'table/perO.html',{
        'mgfullbi':mgfullbi
    })

def mgcreateFullBi(request):
    context ={}
 
    form = mgFullBiform(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
         
    context['form']= form
    return render(request, "func/create.html", context)


def mgdeleteFullBi(request, id):
    context ={}
 
    obj = get_object_or_404(mgFullBi, id = id)
 
 
    if request.method =="POST":
    
        obj.delete()
        return HttpResponseRedirect("/")
 
    return render(request, "func/delete.html", context)

def mgupdateFullBi(request, id):

    context ={}
 
    obj = get_object_or_404(mgFullBi, id = id)

    form = mgFullBiform(request.POST or None, instance = obj)
 

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
 
    context["form"] = form
 
    return render(request, "func/update.html", context)

def mgPersonUIBi(request):
    mgUibi = mgUIBi.objects.all()
    return render(request, 'table/perO.html',{
        'mgUibi':mgUibi
    })

def mgcreateUIBi(request):
    context ={}
 
    form = mgUIBiform(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
         
    context['form']= form
    return render(request, "func/create.html", context)


def mgdeleteUIBi(request, id):
    context ={}
 
    obj = get_object_or_404(mgUIBi, id = id)
 
 
    if request.method =="POST":
    
        obj.delete()
        return HttpResponseRedirect("/")
 
    return render(request, "func/delete.html", context)

def mgupdateUIBi(request, id):

    context ={}
 
    obj = get_object_or_404(mgUIBi, id = id)

    form = mgUIBiform(request.POST or None, instance = obj)
 

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
 
    context["form"] = form
 
    return render(request, "func/update.html", context)

# ----------------------0----------------------------

def mgPersonBCUz(request):
    mgBcuz = mgBCUz.objects.all()
    return render(request, 'table/perO.html',{
        'mgBcuz':mgBcuz
    })

def mgcreateBcUz(request):
    context ={}
 
    form = mgBCUzform(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
         
    context['form']= form
    return render(request, "func/create.html", context)


def mgdeleteBcUz(request, id):
    context ={}
 
    obj = get_object_or_404(mgBCUz, id = id)
 
 
    if request.method =="POST":
    
        obj.delete()
        return HttpResponseRedirect("/")
 
    return render(request, "func/delete.html", context)

def mgupdateBcUz(request, id):

    context ={}
 
    obj = get_object_or_404(mgBCUz, id = id)

    form = mgBCUzform(request.POST or None, instance = obj)
 

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
 
    context["form"] = form
 
    return render(request, "func/update.html", context)

def mgPersonFronUz(request):
    mgfronuz = mgFronUz.objects.all()
    return render(request, 'table/perO.html',{
        'mgfronuz':mgfronuz
    })

def mgcreateFronUz(request):
    context ={}
 
    form = mgFronUzform(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
         
    context['form']= form
    return render(request, "func/create.html", context)


def mgdeleteFronUz(request, id):
    context ={}
 
    obj = get_object_or_404(mgFronUz, id = id)
 
 
    if request.method =="POST":
    
        obj.delete()
        return HttpResponseRedirect("/")
 
    return render(request, "func/delete.html", context)

def mgupdateFronUz(request, id):

    context ={}
 
    obj = get_object_or_404(mgFronUz, id = id)

    form = mgFronUzform(request.POST or None, instance = obj)
 

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
 
    context["form"] = form
 
    return render(request, "func/update.html", context)
def mgPersonFullUz(request):
    mgfulluz = mgFullUz.objects.all()
    return render(request, 'table/perO.html',{
        'mgfulluz':mgfulluz
    })

def mgcreateFullUz(request):
    context ={}
 
    form = mgFullUzform(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
         
    context['form']= form
    return render(request, "func/create.html", context)


def mgdeleteFullUz(request, id):
    context ={}
 
    obj = get_object_or_404(mgFullUz, id = id)
 
 
    if request.method =="POST":
    
        obj.delete()
        return HttpResponseRedirect("/")
 
    return render(request, "func/delete.html", context)

def mgupdateFullUz(request, id):

    context ={}
 
    obj = get_object_or_404(mgFullOsh, id = id)

    form = mgFullOshform(request.POST or None, instance = obj)
 

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
 
    context["form"] = form
 
    return render(request, "func/update.html", context)

def mgPersonUIUz(request):
    mgUiuz = mgUIUz.objects.all()
    return render(request, 'table/perO.html',{
        'mgUiuz':mgUiuz
    })

def mgcreateUIUz(request):
    context ={}
 
    form = mgUIUzform(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
         
    context['form']= form
    return render(request, "func/create.html", context)


def mgdeleteUIUz(request, id):
    context ={}
 
    obj = get_object_or_404(mgUIUz, id = id)
 
 
    if request.method =="POST":
    
        obj.delete()
        return HttpResponseRedirect("/")
 
    return render(request, "func/delete.html", context)

def mgupdateUIUz(request, id):

    context ={}
 
    obj = get_object_or_404(mgUIUz, id = id)

    form = mgUIUzform(request.POST or None, instance = obj)
 

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
    context["form"] = form
    return render(request, "func/update.html", context)


# ----------ev---------

def evPersonBCOsh(request):
    evBcOsh = evBCOsh.objects.all()
    return render(request, 'table/perO.html',{
        'evBCOsh':evBcOsh
    })

def evcreateBcOsh(request):
    context ={}
 
    form = evBCOshform(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
         
    context['form']= form
    return render(request, "func/create.html", context)


def evdeleteBcOsh(request, id):
    context ={}
 
    obj = get_object_or_404(evBCOsh, id = id)
 
 
    if request.method =="POST":
    
        obj.delete()
        return HttpResponseRedirect("/")
 
    return render(request, "func/delete.html", context)

def evupdateBcOsh(request, id):

    context ={}
 
    obj = get_object_or_404(evBCOsh, id = id)

    form = evBCOshform(request.POST or None, instance = obj)
 

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
 
    context["form"] = form
 
    return render(request, "func/update.html", context)

def evPersonFronOsh(request):
    fronOsh = evFronOsh.objects.all()
    return render(request, 'table/perO.html',{
        'fronOsh':fronOsh
    })

def evcreateFronOsh(request):
    context ={}
 
    form = evFronOshform(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
         
    context['form']= form
    return render(request, "func/create.html", context)


def evdeleteFronOsh(request, id):
    context ={}
 
    obj = get_object_or_404(evFronOsh, id = id)
 
 
    if request.method =="POST":
    
        obj.delete()
        return HttpResponseRedirect("/")
 
    return render(request, "func/delete.html", context)

def evupdateFronOsh(request, id):

    context ={}
 
    obj = get_object_or_404(evFronOsh, id = id)

    form = evFronOshform(request.POST or None, instance = obj)
 

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
 
    context["form"] = form
 
    return render(request, "func/update.html", context)

def evPersonFullOsh(request):
    evfullosh = evFullOsh.objects.all()
    return render(request, 'table/perO.html',{
        'evfullosh':evfullosh
    })

def evcreateFullOsh(request):
    context ={}
 
    form = evFullOshform(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
         
    context['form']= form
    return render(request, "func/create.html", context)


def evdeleteFullOsh(request, id):
    context ={}
 
    obj = get_object_or_404(evFullOsh, id = id)
 
 
    if request.method =="POST":
    
        obj.delete()
        return HttpResponseRedirect("/")
 
    return render(request, "func/delete.html", context)

def evupdateFullOsh(request, id):

    context ={}
 
    obj = get_object_or_404(evFullOsh, id = id)

    form = evFullOshform(request.POST or None, instance = obj)
 

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
 
    context["form"] = form
 
    return render(request, "func/update.html", context)

def evPersonUIOsh(request):
    evUiOsh = evUIOsh.objects.all()
    return render(request, 'table/perO.html',{
        'evUiOsh':evUiOsh
    })

def evcreateUIOsh(request):
    context ={}
 
    form = evUIOshform(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
         
    context['form']= form
    return render(request, "func/create.html", context)


def evdeleteUIOsh(request, id):
    context ={}
 
    obj = get_object_or_404(evUIOsh, id = id)
 
 
    if request.method =="POST":
    
        obj.delete()
        return HttpResponseRedirect("/")
 
    return render(request, "func/delete.html", context)

def evupdateUIOsh(request, id):

    context ={}
 
    obj = get_object_or_404(evUIOsh, id = id)

    form = evUIOshform(request.POST or None, instance = obj)
 

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
 
    context["form"] = form
 
    return render(request, "func/update.html", context)

# ---------------------------+-------------
def evPersonBCBi(request):
    evBcbi = evBCBi.objects.all()
    return render(request, 'table/perO.html',{
        'evBcbi':evBcbi
    })

def evcreateBcBi(request):
    context ={}
 
    form = evBCBiform(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
         
    context['form']= form
    return render(request, "func/create.html", context)


def evdeleteBcBi(request, id):
    context ={}
 
    obj = get_object_or_404(evBCBi, id = id)
 
 
    if request.method =="POST":
    
        obj.delete()
        return HttpResponseRedirect("/")
 
    return render(request, "func/delete.html", context)

def evupdateBcBi(request, id):

    context ={}
 
    obj = get_object_or_404(evBCBi, id = id)

    form = evBCBiform(request.POST or None, instance = obj)
 

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
 
    context["form"] = form
 
    return render(request, "func/update.html", context)

def evPersonFronBi(request):
    evfronBi = evFronBi.objects.all()
    return render(request, 'table/perO.html',{
        'evFronBi':evfronBi
    })

def evcreateFronBi(request):
    context ={}
 
    form = evFronBiform(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
         
    context['form']= form
    return render(request, "func/create.html", context)


def evdeleteFronBi(request, id):
    context ={}
 
    obj = get_object_or_404(evFronBi, id = id)
 
 
    if request.method =="POST":
    
        obj.delete()
        return HttpResponseRedirect("/")
 
    return render(request, "func/delete.html", context)

def evupdateFronBi(request, id):

    context ={}
 
    obj = get_object_or_404(evFronBi, id = id)

    form = evFronBiform(request.POST or None, instance = obj)
 

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
 
    context["form"] = form
 
    return render(request, "func/update.html", context)

def evPersonFullBi(request):
    evfullbi = evFullBi.objects.all()
    return render(request, 'table/perO.html',{
        'evfullbi':evfullbi
    })

def evcreateFullBi(request):
    context ={}
 
    form = evFullBiform(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
         
    context['form']= form
    return render(request, "func/create.html", context)


def evdeleteFullBi(request, id):
    context ={}
 
    obj = get_object_or_404(evFullBi, id = id)
 
 
    if request.method =="POST":
    
        obj.delete()
        return HttpResponseRedirect("/")
 
    return render(request, "func/delete.html", context)

def evupdateFullBi(request, id):

    context ={}
 
    obj = get_object_or_404(evFullBi, id = id)

    form = evFullBiform(request.POST or None, instance = obj)
 

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
 
    context["form"] = form
 
    return render(request, "func/update.html", context)

def evPersonUIBi(request):
    evUibi = evUIBi.objects.all()
    return render(request, 'table/perO.html',{
        'evUibi':evUibi
    })

def evcreateUIBi(request):
    context ={}
 
    form = evUIBiform(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
         
    context['form']= form
    return render(request, "func/create.html", context)


def evdeleteUIBi(request, id):
    context ={}
 
    obj = get_object_or_404(evUIBi, id = id)
 
 
    if request.method =="POST":
    
        obj.delete()
        return HttpResponseRedirect("/")
 
    return render(request, "func/delete.html", context)

def evupdateUIBi(request, id):

    context ={}
 
    obj = get_object_or_404(evUIBi, id = id)

    form = evUIBiform(request.POST or None, instance = obj)
 

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
 
    context["form"] = form
 
    return render(request, "func/update.html", context)

# ----------------------0----------------------------

def evPersonBCUz(request):
    evBcuz = evBCUz.objects.all()
    return render(request, 'table/perO.html',{
        'evBcuz':evBcuz
    })

def evcreateBcUz(request):
    context ={}
 
    form = evBCUzform(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
         
    context['form']= form
    return render(request, "func/create.html", context)


def evdeleteBcUz(request, id):
    context ={}
 
    obj = get_object_or_404(evBCUz, id = id)
 
 
    if request.method =="POST":
    
        obj.delete()
        return HttpResponseRedirect("/")
 
    return render(request, "func/delete.html", context)

def evupdateBcUz(request, id):

    context ={}
 
    obj = get_object_or_404(evBCUz, id = id)

    form = evBCUzform(request.POST or None, instance = obj)
 

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
 
    context["form"] = form
 
    return render(request, "func/update.html", context)

def evPersonFronUz(request):
    evfronuz = evFronUz.objects.all()
    return render(request, 'table/perO.html',{
        'evfronuz':evfronuz
    })

def evcreateFronUz(request):
    context ={}
 
    form = evFronUzform(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
         
    context['form']= form
    return render(request, "func/create.html", context)


def evdeleteFronUz(request, id):
    context ={}
 
    obj = get_object_or_404(evFronUz, id = id)
 
 
    if request.method =="POST":
    
        obj.delete()
        return HttpResponseRedirect("/")
 
    return render(request, "func/delete.html", context)

def evupdateFronUz(request, id):

    context ={}
 
    obj = get_object_or_404(evFronUz, id = id)

    form = evFronUzform(request.POST or None, instance = obj)
 

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
 
    context["form"] = form
 
    return render(request, "func/update.html", context)
def evPersonFullUz(request):
    evfulluz = evFullUz.objects.all()
    return render(request, 'table/perO.html',{
        'evfulluz':evfulluz
    })

def evcreateFullUz(request):
    context ={}
 
    form = evFullUzform(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
         
    context['form']= form
    return render(request, "func/create.html", context)


def evdeleteFullUz(request, id):
    context ={}
 
    obj = get_object_or_404(evFullUz, id = id)
 
 
    if request.method =="POST":
    
        obj.delete()
        return HttpResponseRedirect("/")
 
    return render(request, "func/delete.html", context)

def evupdateFullUz(request, id):

    context ={}
 
    obj = get_object_or_404(evFullUz, id = id)

    form = evFullUzform(request.POST or None, instance = obj)
 

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
 
    context["form"] = form
 
    return render(request, "func/update.html", context)

def evPersonUIUz(request):
    evUiuz = evUIUz.objects.all()
    return render(request, 'table/perO.html',{
        'evUiuz':evUiuz
    })

def evcreateUIUz(request):
    context ={}
 
    form = evUIUzform(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
         
    context['form']= form
    return render(request, "func/create.html", context)


def evdeleteUIUz(request, id):
    context ={}
 
    obj = get_object_or_404(evUIUz, id = id)
 
 
    if request.method =="POST":
    
        obj.delete()
        return HttpResponseRedirect("/")
 
    return render(request, "func/delete.html", context)

def evupdateUIUz(request, id):

    context ={}
 
    obj = get_object_or_404(evUIUz, id = id)

    form = evUIUzform(request.POST or None, instance = obj)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
    context["form"] = form
    return render(request, "func/update.html", context)